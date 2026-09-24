#!/usr/bin/env python3
"""Measure which chunker and embedding model find the right source for the wiki's own claims.

Usage:
  search_eval.py [--chunkers NAME,...] [--models MODEL,...]
  search_eval.py --passages DIR [--per-doc N] [--chunkers NAME,...] [--models MODEL,...]

Every Key point on a source page becomes a query whose answer is that page's
current capture; every current capture with a Markdown copy is in the corpus.
For each chunker and model the script ranks captures by their best chunk and
reports hit@1, hit@5, and mean reciprocal rank for dense, BM25, and fused
(reciprocal rank fusion) retrieval. With --passages, the corpus is the Markdown
files in DIR, an LLM writes one question per sampled paragraph, and a hit is a
chunk that holds at least half of that paragraph: this measures chunking itself,
not just finding the right document. Models run through OpenRouter, except the
local ModernBERT embedder, which late chunking also uses for its pooled vectors.
Embeddings and chunk spans are cached under raw/index/.
Run it through `sw search-eval`; rerun it whenever the Markdown copies, the
chunker candidates, or the embedding models change.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import os
import random
import re
import sqlite3
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from chonkie import LateChunker, NeuralChunker, SemanticChunker, SentenceChunker, TokenChunker

from fetch import Store, primary_root
from convert import FIGURE, SPENT, chat, describe_figures, raster
from search import CREDENTIALS, embed, embedding_text, first_heading, markdown_chunker, split
from search import MODEL as SEARCH_MODEL

DB_LOCK = threading.Lock()  # one sqlite connection serves every worker thread
LOCAL = "local:nomic-ai/modernbert-embed-base"  # also the late-chunking model; 8192-token context
LOCAL_PREFIX = {True: "search_query: ", False: "search_document: "}
MODELS = ["qwen/qwen3-embedding-8b", "voyageai/voyage-4-lite", "voyageai/voyage-4", LOCAL]
SEQUENTIAL = {"semantic-1600", "neural", "late-400"}  # torch models run one text at a time
QUESTION_MODEL = "google/gemini-2.5-flash-lite"
VISION_CANDIDATES = ["google/gemini-2.5-flash-lite", "google/gemini-3.1-flash-lite",
                     "deepseek/deepseek-v4-flash-vision-exp", "deepseek/deepseek-v4.1-flash"]
FIGURE_QUESTION_MODEL = "openai/gpt-4.1-mini"  # another family than the describers, so questions do not echo them
FIGURE_QUESTION_PROMPT = (
    "The image below is a figure from a research document; nearby text is given for context. Write one question a "
    "researcher could ask whose answer is shown in this figure. Ask about what it shows, in your own words; do not "
    "mention figure numbers or copy the caption. If the image is a formula, a logo, or decoration, reply SKIP. "
    "Reply with the question only.\n\nNearby text:\n"
)
QUESTION_PROMPT = (
    "Write one specific question that a researcher could ask and that the passage below answers. "
    "Use your own words: do not copy distinctive phrases, names of sections, or numbers unless the question "
    "cannot be asked without them. Reply with the question only.\n\nPassage:\n"
)


@functools.cache
def local_model():
    from chonkie.embeddings import SentenceTransformerEmbeddings
    return SentenceTransformerEmbeddings(LOCAL.removeprefix("local:"))


class Cache:
    """Embeddings by model and text hash, so candidates that share chunks share vectors."""

    def __init__(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.execute("create table if not exists vectors (model text, key text, vector blob, primary key (model, key))")

    def vectors(self, model: str, texts: list[str], query: bool = False) -> np.ndarray:
        keys = [hashlib.sha256(f"{query}:{text}".encode()).hexdigest() for text in texts]
        known = {}
        for start in range(0, len(keys), 500):
            part = keys[start:start + 500]
            with DB_LOCK:
                rows = self.db.execute(
                    f"select key, vector from vectors where model = ? and key in ({','.join('?' * len(part))})",
                    [model, *part]).fetchall()
            known.update({key: np.frombuffer(blob, dtype=np.float32) for key, blob in rows})
        missing = [(key, text) for key, text in dict(zip(keys, texts)).items() if key not in known]
        batches = [missing[start:start + 32] for start in range(0, len(missing), 32)]
        if model == LOCAL:
            work = lambda batch: local_model().embed_batch([LOCAL_PREFIX[query] + text for _, text in batch])
        else:
            work = lambda batch: embed([text for _, text in batch], model, query)
        with ThreadPoolExecutor(max_workers=1 if model == LOCAL else 6) as pool:
            for batch, vectors in zip(batches, pool.map(work, batches)):
                for (key, _), vector in zip(batch, vectors):
                    known[key] = np.asarray(vector, dtype=np.float32)
                with DB_LOCK:
                    self.db.executemany("insert or replace into vectors values (?, ?, ?)",
                                        [(model, key, known[key].tobytes()) for key, _ in batch])
                    self.db.commit()
        matrix = np.stack([known[key] for key in keys])
        return matrix / np.linalg.norm(matrix, axis=1, keepdims=True)


class Capped:
    """A chunker whose chunks longer than LIMIT characters are split again by the Markdown rules."""

    def __init__(self, inner, limit: int = 3200) -> None:
        self.inner, self.limit, self.splitter = inner, limit, markdown_chunker()

    def chunk(self, text: str) -> list[SimpleNamespace]:
        found = []
        for chunk in self.inner.chunk(text):
            if len(chunk.text) <= self.limit:
                found.append(chunk)
                continue
            for part in self.splitter.chunk(chunk.text):
                found.append(SimpleNamespace(text=part.text, start_index=chunk.start_index + part.start_index,
                                             end_index=chunk.start_index + part.end_index))
        return found


def chunkers() -> dict:
    """Candidate chunkers; all run on this machine, so choosing one costs no model calls."""
    return {
        "token-1000": lambda: TokenChunker(tokenizer="character", chunk_size=1000),
        "sentence-1600": lambda: SentenceChunker(tokenizer="character", chunk_size=1600),
        "recursive-md-400": lambda: markdown_chunker(400),
        "recursive-md-600": lambda: markdown_chunker(600),
        "recursive-md-800": lambda: markdown_chunker(800),
        "recursive-md-1600": lambda: markdown_chunker(1600),
        "recursive-md-3200": lambda: markdown_chunker(3200),
        # 0.3 is the loosest threshold that still splits; higher ones leave chunks of 300 to 500 characters.
        "semantic-1600": functools.cache(lambda: SemanticChunker(embedding_model=local_model(), chunk_size=1600,
                                                                 threshold=0.3)),
        # Torch chunkers load their model once and run one text at a time.
        # The neural chunker sets no maximum; pieces over 3200 characters are split by the recursive rules.
        "neural": functools.cache(lambda: Capped(NeuralChunker(model="mirth/chonky_modernbert_base_1",
                                                               min_characters_per_chunk=24))),
        # About 1600 characters; boundaries follow the Markdown rules, vectors are pooled from the whole text.
        "late-400": functools.cache(lambda: LateChunker(embedding_model=local_model(), chunk_size=400,
                                                        rules=markdown_chunker().rules, min_characters_per_chunk=24)),
    }


def corpus(store: Store, worktree: Path) -> tuple[dict[str, tuple[str, str]], list[tuple[str, str]]]:
    """Current captures with Markdown (sha -> title, text) and Key point queries (text, sha)."""
    docs = {}
    for sha in sorted(set(store.pointers().values())):
        capture, original = store.restore(sha)
        markdown = original.with_name("content.md")
        if markdown.exists():
            text = markdown.read_text()
            docs[sha] = (capture.meta.get("title") or first_heading(text) or capture.url, text)
    queries = []
    for page in sorted((worktree / "wiki" / "sources").glob("*.md")):
        body = page.read_text()
        match = re.search(r'^sha256:\s*"?([0-9a-f]{64})', body, re.M)
        if not match or match.group(1) not in docs or "## Key points" not in body:
            continue
        for line in body.split("## Key points", 1)[1].splitlines():
            if line.startswith("- "):
                claim = re.sub(r"\s*\([^()]*(\([^()]*\)[^()]*)*\)\s*$", "", line[2:]).strip()
                queries.append((re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", claim), match.group(1)))
    return docs, queries


def bm25(chunk_texts: list[str], query_texts: list[str]) -> np.ndarray:
    """Okapi BM25 scores (queries x chunks) with plain lowercase word tokens."""
    tokenize = lambda text: re.findall(r"[a-z0-9]+", text.lower())
    chunk_terms = [Counter(tokenize(text)) for text in chunk_texts]
    lengths = np.array([sum(terms.values()) for terms in chunk_terms], dtype=np.float32)
    average = lengths.mean()
    frequency = Counter(term for terms in chunk_terms for term in terms)
    count = len(chunk_terms)
    scores = np.zeros((len(query_texts), count), dtype=np.float32)
    for row, query in enumerate(query_texts):
        for term in set(tokenize(query)):
            if term not in frequency:
                continue
            idf = math.log(1 + (count - frequency[term] + 0.5) / (frequency[term] + 0.5))
            tf = np.array([terms.get(term, 0) for terms in chunk_terms], dtype=np.float32)
            scores[row] += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * lengths / average))
    return scores


def doc_ranks(scores: np.ndarray, owners: np.ndarray, gold: list[str], shas: list[str]) -> list[int]:
    """Rank of the gold capture for each query when captures are ranked by their best chunk."""
    ranks = []
    index = {sha: position for position, sha in enumerate(shas)}
    for row, answer in enumerate(gold):
        best = np.full(len(shas), -np.inf)
        np.maximum.at(best, owners, scores[row])
        ranks.append(int((best > best[index[answer]]).sum()) + 1)
    return ranks


def passages(text: str) -> list[tuple[int, int]]:
    """Prose paragraphs of 300 to 1500 characters before any References section: the spans questions are asked about."""
    end = re.search(r"^#+\s*(\d+\.?\s*)?(references|bibliography)\b", text, re.I | re.M)
    found = []
    for match in re.finditer(r"[^\n](?:.|\n(?!\s*\n))*", text[:end.start() if end else len(text)]):
        block = match.group(0).strip()
        if 300 <= len(block) <= 1500 and not block.startswith(("|", "```", "![", "#", "<", "$$")):
            found.append((match.start(), match.end()))
    return found


def ask(prompt: str) -> str:
    """One answer from QUESTION_MODEL through OpenRouter."""
    return chat(QUESTION_MODEL, prompt, max_tokens=200)


def passage_queries(db: sqlite3.Connection, docs: dict, per_doc: int) -> list[tuple[str, int, int, int]]:
    """(question, document position, start, end): questions an LLM wrote for sampled paragraphs, cached."""
    with DB_LOCK:
        db.execute("create table if not exists questions (model text, key text, question text, primary key (model, key))")
    wanted = []
    for position, (name, (_, text)) in enumerate(docs.items()):
        spans = passages(text)
        for start, end in random.Random(name).sample(spans, min(per_doc, len(spans))):
            wanted.append((position, start, end, text[start:end]))

    def question(item):
        key = hashlib.sha256(item[3].encode()).hexdigest()
        with DB_LOCK:
            row = db.execute("select question from questions where model = ? and key = ?", (QUESTION_MODEL, key)).fetchone()
        if row:
            return row[0]
        text = ask(QUESTION_PROMPT + item[3])
        with DB_LOCK:
            db.execute("insert or replace into questions values (?, ?, ?)", (QUESTION_MODEL, key, text))
            db.commit()
        return text

    with ThreadPoolExecutor(max_workers=8) as pool:
        return [(text, position, start, end) for text, (position, start, end, _) in zip(pool.map(question, wanted), wanted)]


def passage_ranks(scores: np.ndarray, owners: np.ndarray, spans: np.ndarray, gold: list[tuple[int, int, int]]) -> list[float]:
    """Rank of the first chunk that holds at least half of the gold paragraph (or is half made of it); inf if none."""
    ranks = []
    for row, (position, start, end) in enumerate(gold):
        overlap = np.clip(np.minimum(spans[:, 1], end) - np.maximum(spans[:, 0], start), 0, None)
        smaller = np.minimum(spans[:, 1] - spans[:, 0], end - start)
        hit = (owners == position) & (overlap >= 0.5 * smaller)
        order = np.argsort(-scores[row])
        found = np.nonzero(hit[order])[0]
        ranks.append(float(found[0] + 1) if len(found) else math.inf)
    return ranks


def strip_descriptions(text: str) -> str:
    """TEXT without the generated figure descriptions that describe_figures inserted."""
    return re.sub(r"\n\n> Figure description \(generated by [^\n]*\n", "\n", text)


def figure_spans(text: str) -> dict[str, tuple[int, int]]:
    """Figure file name -> span from its image link to the end of the block after it (caption or description)."""
    spans = {}
    for match in FIGURE.finditer(text):
        after = re.match(r"\s*\n\s*\n?([^\n](?:.|\n(?!\s*\n))*)", text[match.end():])
        spans.setdefault(match.group(1), (match.start(), match.end() + (after.end() if after else 0)))
    return spans


def figure_questions(db: sqlite3.Connection, docs: dict, assets: dict, per_doc: int) -> list[tuple[str, int, str]]:
    """(question, document position, figure name) for sampled figures, written from the image by another model."""
    with DB_LOCK:
        db.execute("create table if not exists questions (model text, key text, question text, primary key (model, key))")
    wanted = []
    for position, (key, (_, text)) in enumerate(docs.items()):
        names = [name for name in figure_spans(text) if raster(name, assets[key].get(name, b""))]
        for name in random.Random(key).sample(names, min(per_doc, len(names))):
            start, end = figure_spans(text)[name]
            wanted.append((position, name, raster(name, assets[key][name]), text[max(0, start - 400):end]))

    def question(item) -> str:
        digest = hashlib.sha256(item[2][1]).hexdigest()
        with DB_LOCK:
            row = db.execute("select question from questions where model = ? and key = ?",
                             (FIGURE_QUESTION_MODEL, digest)).fetchone()
        if row:
            return row[0]
        reply = chat(FIGURE_QUESTION_MODEL, FIGURE_QUESTION_PROMPT + item[3], item[2], max_tokens=200)
        with DB_LOCK:
            db.execute("insert or replace into questions values (?, ?, ?)", (FIGURE_QUESTION_MODEL, digest, reply))
            db.commit()
        return reply

    with ThreadPoolExecutor(max_workers=8) as pool:
        replies = list(pool.map(question, wanted))
    return [(reply, position, name) for reply, (position, name, _, _) in zip(replies, wanted) if reply.strip() != "SKIP"]


def fused(*rankings: np.ndarray, k: int = 60) -> np.ndarray:
    """Reciprocal rank fusion of chunk scores, per query."""
    total = np.zeros_like(rankings[0])
    for scores in rankings:
        order = np.argsort(-scores, axis=1)
        ranks = np.empty_like(order)
        np.put_along_axis(ranks, order, np.arange(scores.shape[1])[None, :], axis=1)
        total += 1.0 / (k + ranks + 1)
    return total


def summary(ranks: list[int]) -> str:
    hits = lambda n: sum(rank <= n for rank in ranks) / len(ranks)
    reciprocal = np.array([1 / rank for rank in ranks])
    margin = 1.96 * reciprocal.std(ddof=1) / math.sqrt(len(ranks))
    return f"hit@1 {hits(1):.3f}  hit@5 {hits(5):.3f}  MRR {reciprocal.mean():.3f} +/- {margin:.3f}"


class CachedChunker:
    """A chunker that remembers the spans it produced, so slow chunkers run once per text."""

    def __init__(self, db: sqlite3.Connection, name: str, make) -> None:
        self.db, self.name, self.make = db, name, make
        with DB_LOCK:
            db.execute("create table if not exists spans (chunker text, key text, spans text, primary key (chunker, key))")

    def chunk(self, text: str) -> list[SimpleNamespace]:
        key = hashlib.sha256(text.encode()).hexdigest()
        with DB_LOCK:
            row = self.db.execute("select spans from spans where chunker = ? and key = ?", (self.name, key)).fetchone()
        if row:
            spans = json.loads(row[0])
        else:
            spans = [(chunk.start_index, chunk.end_index) for chunk in self.make().chunk(text)]
            with DB_LOCK:
                self.db.execute("insert or replace into spans values (?, ?, ?)", (self.name, key, json.dumps(spans)))
                self.db.commit()
        return [SimpleNamespace(text=text[start:end], start_index=start, end_index=end) for start, end in spans]


def figure_eval(store: Store, cache: Cache, vision_models: list[str], per_doc: int) -> int:
    """Rank figures for questions written from their images, without descriptions and with each model's."""
    docs, assets = {}, {}
    for sha in sorted(set(store.pointers().values())):
        capture, original = store.restore(sha)
        markdown, folder = original.with_name("content.md"), original.with_name("assets")
        if markdown.exists() and folder.is_dir() and FIGURE.search(markdown.read_text()):
            text = strip_descriptions(markdown.read_text())
            docs[sha] = (capture.meta.get("title") or first_heading(text) or capture.url, text)
            assets[sha] = {path.name: path.read_bytes() for path in folder.iterdir()}
    queries = figure_questions(cache.db, docs, assets, per_doc)
    print(f"{len(docs)} captures with figures, {len(queries)} questions written from figure images "
          f"({FIGURE_QUESTION_MODEL})")
    variants = {"no descriptions": docs}
    for model in vision_models:
        before = SPENT.get(model, 0.0)
        with ThreadPoolExecutor(max_workers=4) as pool:
            texts = pool.map(lambda key: describe_figures(docs[key][1], assets[key], model)[0], docs)
            variants[model] = {key: (docs[key][0], text) for key, text in zip(docs, texts)}
        described = sum(text.count("> Figure description (") for _, text in variants[model].values())
        cost = SPENT.get(model, 0.0) - before
        print(f"{model}: {described} figures described for ${cost:.4f}, ${cost / len(docs):.4f} per capture")

    query_texts = [text for text, _, _ in queries]
    for variant, texts in variants.items():
        keys = list(texts)
        chunk_texts, owners, spans = [], [], []
        for position, key in enumerate(keys):
            pieces = split(texts[key][1])
            chunk_texts += [embedding_text(texts[key][0], piece) for piece in pieces]
            owners += [position] * len(pieces)
            spans += [(piece.start, piece.end) for piece in pieces]
        owners, spans = np.array(owners), np.array(spans)
        gold = [(position, *figure_spans(texts[keys[position]][1])[name]) for _, position, name in queries]
        lexical = bm25(chunk_texts, query_texts)
        dense = cache.vectors(SEARCH_MODEL, query_texts, query=True) @ cache.vectors(SEARCH_MODEL, chunk_texts).T
        rank = lambda scores: passage_ranks(scores, owners, spans, gold)
        print(f"\n{variant}: {len(chunk_texts)} chunks")
        print(f"  {'bm25':30} {summary(rank(lexical))}")
        print(f"  {SEARCH_MODEL:30} {summary(rank(dense))}")
        print(f"  {SEARCH_MODEL + ' + bm25':30} {summary(rank(fused(dense, lexical)))}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--chunkers", help="comma-separated chunker names")
    parser.add_argument("--models", help=f"comma-separated OpenRouter embedding models, or {LOCAL}")
    parser.add_argument("--passages", type=Path, metavar="DIR",
                        help="score passage retrieval on the Markdown files in DIR with LLM-written questions")
    parser.add_argument("--per-doc", type=int, default=8, help="questions per document with --passages or --figures")
    parser.add_argument("--figures", action="store_true",
                        help="score figure retrieval with no descriptions and with each vision model's descriptions")
    parser.add_argument("--vision-models", default=",".join(VISION_CANDIDATES),
                        help="comma-separated OpenRouter vision models for --figures")
    args = parser.parse_args()
    missing = [name for name in CREDENTIALS if not os.environ.get(name)]
    if missing:
        print(f"sw search-eval: missing {', '.join(missing)}", file=sys.stderr)
        return 1

    root = primary_root()
    cache = Cache(root / "raw" / "index" / "eval-embeddings.sqlite")
    if args.figures:
        return figure_eval(Store(root), cache, args.vision_models.split(","), args.per_doc)
    available = chunkers()
    names = args.chunkers.split(",") if args.chunkers else list(available)
    models = args.models.split(",") if args.models else MODELS
    if args.passages:
        docs = {path.stem: (first_heading(path.read_text()) or path.stem, path.read_text())
                for path in sorted(args.passages.glob("*.md"))}
        queries = passage_queries(cache.db, docs, args.per_doc)
        query_texts, gold = [text for text, *_ in queries], [tuple(where) for _, *where in queries]
        print(f"{len(docs)} documents, {len(queries)} questions about single paragraphs ({QUESTION_MODEL})")
    else:
        docs, queries = corpus(Store(root), Path(__file__).resolve().parent.parent)
        query_texts, gold = [text for text, _ in queries], [sha for _, sha in queries]
        print(f"{len(docs)} captures, {len(queries)} Key point queries")
    keys = list(docs)

    for name in names:
        chunker = CachedChunker(cache.db, name, available[name])
        with ThreadPoolExecutor(max_workers=1 if name in SEQUENTIAL else 8) as pool:
            split_docs = list(pool.map(lambda key: split(docs[key][1], chunker), keys))
        texts, owners, spans = [], [], []
        for position, (key, pieces) in enumerate(zip(keys, split_docs)):
            texts += [embedding_text(docs[key][0], piece) for piece in pieces]
            owners += [position] * len(pieces)
            spans += [(piece.start, piece.end) for piece in pieces]
        owners, spans = np.array(owners), np.array(spans)
        if args.passages:
            rank = lambda scores: passage_ranks(scores, owners, spans, gold)
        else:
            rank = lambda scores: doc_ranks(scores, owners, gold, keys)
        lexical = bm25(texts, query_texts)
        print(f"\n{name}: {len(texts)} chunks, {sum(map(len, texts)) / len(texts):.0f} characters on average")
        print(f"  {'bm25':30} {summary(rank(lexical))}")
        for model in models:
            dense = cache.vectors(model, query_texts, query=True) @ cache.vectors(model, texts).T
            print(f"  {model:30} {summary(rank(dense))}")
            print(f"  {model + ' + bm25':30} {summary(rank(fused(dense, lexical)))}")
        if name.startswith("late"):
            # Late chunking's point is its vectors: chunk embeddings pooled from the whole text in context.
            late = available[name]()
            pooled = np.stack([chunk.embedding for key in keys for chunk in late.chunk(docs[key][1]) if chunk.text.strip()])
            dense = cache.vectors(LOCAL, query_texts, query=True) @ (pooled / np.linalg.norm(pooled, axis=1, keepdims=True)).T
            print(f"  {'late pooled':30} {summary(rank(dense))}")
            print(f"  {'late pooled + bm25':30} {summary(rank(fused(dense, lexical)))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
