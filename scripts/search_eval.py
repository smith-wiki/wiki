#!/usr/bin/env python3
"""Measure which chunker and embedding model find the right source for the wiki's own claims.

Usage:
  search_eval.py [--chunkers NAME,...] [--models MODEL,...]

Every Key point on a source page becomes a query whose answer is that page's
current capture; every current capture with a Markdown copy is in the corpus.
For each chunker and model the script ranks captures by their best chunk and
reports hit@1, hit@5, and mean reciprocal rank for dense, BM25, and fused
(reciprocal rank fusion) retrieval. Embeddings are cached under raw/index/.
Run it through `sw search-eval`; rerun it whenever the Markdown copies, the
chunker candidates, or the embedding models change.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sqlite3
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from chonkie import OpenAIGenie, SemanticChunker, SentenceChunker, SlumberChunker, TokenChunker
from chonkie.embeddings import BaseEmbeddings

from fetch import Store, primary_root
from search import CREDENTIALS, embed, embedding_text, first_heading, markdown_chunker, split

DB_LOCK = threading.Lock()  # one sqlite connection serves every worker thread
MODELS = ["qwen/qwen3-embedding-8b", "voyageai/voyage-4-lite", "voyageai/voyage-4"]
SLUMBER_MODEL = "google/gemini-2.5-flash-lite"


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
        with ThreadPoolExecutor(max_workers=6) as pool:
            results = pool.map(lambda batch: embed([text for _, text in batch], model, query), batches)
            for batch, vectors in zip(batches, results):
                for (key, _), vector in zip(batch, vectors):
                    known[key] = np.asarray(vector, dtype=np.float32)
                with DB_LOCK:
                    self.db.executemany("insert or replace into vectors values (?, ?, ?)",
                                        [(model, key, known[key].tobytes()) for key, _ in batch])
                    self.db.commit()
        matrix = np.stack([known[key] for key in keys])
        return matrix / np.linalg.norm(matrix, axis=1, keepdims=True)


class OpenRouterEmbeddings(BaseEmbeddings):
    """Chonkie embeddings backed by the cache, for the semantic chunker."""

    def __init__(self, cache: Cache, model: str) -> None:
        super().__init__()
        self.cache, self.model = cache, model

    def embed(self, text: str) -> np.ndarray:
        return self.cache.vectors(self.model, [text])[0]

    def embed_batch(self, texts: list[str]) -> list[np.ndarray]:
        return list(self.cache.vectors(self.model, texts)) if texts else []

    @property
    def dimension(self) -> int:
        return len(self.embed("dimension"))

    def get_tokenizer(self):
        return "character"


def chunkers(cache: Cache) -> dict:
    genie = lambda: OpenAIGenie(model=SLUMBER_MODEL, base_url="https://openrouter.ai/api/v1",
                                api_key=os.environ["OPENROUTER_API_KEY"])
    return {
        "token-1000": lambda: TokenChunker(tokenizer="character", chunk_size=1000),
        "sentence-1600": lambda: SentenceChunker(tokenizer="character", chunk_size=1600),
        "recursive-md-800": lambda: markdown_chunker(800),
        "recursive-md-1600": lambda: markdown_chunker(1600),
        "recursive-md-3200": lambda: markdown_chunker(3200),
        # 0.3 is the loosest threshold that still splits; higher ones leave chunks of 300 to 500 characters.
        "semantic-1600": lambda: SemanticChunker(embedding_model=OpenRouterEmbeddings(cache, MODELS[0]),
                                                 chunk_size=1600, threshold=0.3),
        "slumber-1600": lambda: SlumberChunker(genie=genie(), tokenizer="character", chunk_size=1600,
                                               candidate_size=256, verbose=False),
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--chunkers", help="comma-separated chunker names")
    parser.add_argument("--models", help="comma-separated OpenRouter embedding models")
    args = parser.parse_args()
    missing = [name for name in CREDENTIALS if not os.environ.get(name)]
    if missing:
        print(f"sw search-eval: missing {', '.join(missing)}", file=sys.stderr)
        return 1

    root = primary_root()
    cache = Cache(root / "raw" / "index" / "eval-embeddings.sqlite")
    available = chunkers(cache)
    names = args.chunkers.split(",") if args.chunkers else list(available)
    models = args.models.split(",") if args.models else MODELS
    worktree = Path(__file__).resolve().parent.parent
    docs, queries = corpus(Store(root), worktree)
    shas = list(docs)
    print(f"{len(docs)} captures, {len(queries)} Key point queries")
    query_texts, gold = [text for text, _ in queries], [sha for _, sha in queries]

    for name in names:
        chunker = CachedChunker(cache.db, name, available[name])
        with ThreadPoolExecutor(max_workers=8) as pool:
            split_docs = list(pool.map(lambda sha: split(docs[sha][1], chunker), shas))
        texts, owners = [], []
        for position, (sha, pieces) in enumerate(zip(shas, split_docs)):
            texts += [embedding_text(docs[sha][0], piece) for piece in pieces]
            owners += [position] * len(pieces)
        owners = np.array(owners)
        lexical = bm25(texts, query_texts)
        print(f"\n{name}: {len(texts)} chunks, {sum(map(len, texts)) / len(texts):.0f} characters on average")
        print(f"  bm25                     {summary(doc_ranks(lexical, owners, gold, shas))}")
        for model in models:
            dense = cache.vectors(model, query_texts, query=True) @ cache.vectors(model, texts).T
            print(f"  {model:24} {summary(doc_ranks(dense, owners, gold, shas))}")
            print(f"  {model + ' + bm25':24} {summary(doc_ranks(fused(dense, lexical), owners, gold, shas))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
