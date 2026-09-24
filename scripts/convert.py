"""Markdown copies of PDFs and arXiv papers, with their figures as separate image files.

A PDF is parsed on this machine by pymupdf4llm with PyMuPDF's layout model,
which recovers headings, tables, and figure regions. An arXiv paper is read
from arXiv's own HTML rendering of its LaTeX, which keeps formulas as LaTeX;
papers without one fall back to their PDF. A vision model then describes each
figure in text placed under it and marked as generated, so search finds figures
by what they show.
"""

from __future__ import annotations

import base64
import hashlib
import http.client
import json
import mimetypes
import os
import re
import tempfile
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ElementTree
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse

import pymupdf
import pymupdf.layout  # noqa: F401  (switches pymupdf4llm to the layout model; without it headings are lost)
import pymupdf4llm
from bs4 import BeautifulSoup
from markdownify import markdownify

USER_AGENT = "smith-wiki-fetch/1.0 (+https://github.com/smith-wiki/wiki)"
ARXIV = re.compile(
    r"https?://(?:www\.|export\.)?arxiv\.org/(?:abs|pdf|html)/"
    r"(?P<id>\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})(?P<version>v\d+)?(?:\.pdf)?/?(?:[?#].*)?$"
)
ATOM = {"atom": "http://www.w3.org/2005/Atom"}


class ConvertError(Exception):
    pass


Assets = dict[str, bytes]
SPENT: dict[str, float] = {}  # US dollars per model, as OpenRouter reports them


NETWORK_ERRORS = (urllib.error.URLError, TimeoutError, http.client.HTTPException)


def send(request: urllib.request.Request, timeout: int) -> tuple[bytes, str, str]:
    """(body, media type, final URL) of REQUEST, retrying dropped connections and busy servers."""
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                kind = (response.headers.get("Content-Type") or "").split(";")[0].strip().lower()
                # One read() of a body over 4 MiB stops at 4 MiB here (Python 3.14 over TLS); chunked reads do not.
                body = b"".join(iter(lambda: response.read(1 << 20), b""))
                return body, kind, response.geturl()
        except NETWORK_ERRORS as error:
            transient = not isinstance(error, urllib.error.HTTPError) or error.code in (406, 408, 429) or error.code >= 500
            if attempt == 3 or not transient:
                raise
            time.sleep(2 ** attempt * 2)
    raise AssertionError("unreachable")


def get(url: str, timeout: int = 120) -> tuple[bytes, str, str]:
    return send(urllib.request.Request(url, headers={"User-Agent": USER_AGENT}), timeout)


def chat(model: str, prompt: str, image: tuple[str, bytes] | None = None, max_tokens: int = 400) -> str:
    """One reply from MODEL through OpenRouter, optionally about an image given as (file name, bytes)."""
    content: list[dict] = [{"type": "text", "text": prompt}]
    if image:
        kind = mimetypes.guess_type(image[0])[0] or "image/png"
        data = base64.b64encode(image[1]).decode()
        content.append({"type": "image_url", "image_url": {"url": f"data:{kind};base64,{data}"}})
    # Reasoning models (DeepSeek V4) otherwise spend the whole token budget thinking and return no content.
    body = {"model": model, "temperature": 0, "max_tokens": max_tokens, "usage": {"include": True},
            "reasoning": {"enabled": False}, "messages": [{"role": "user", "content": content}]}
    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions", data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}", "Content-Type": "application/json"})
    reply = json.loads(send(request, 180)[0])
    SPENT[model] = SPENT.get(model, 0.0) + (reply.get("usage") or {}).get("cost", 0.0)
    return (reply["choices"][0]["message"]["content"] or "").strip()


# Figures

# Chosen by `sw search-eval --figures`: on 56 questions written from the figures of 11 papers, descriptions raised
# figure retrieval from MRR 0.52 to 0.74 (+/- 0.09) at about $0.0003 a figure. Within the same margin and at higher
# OpenRouter prices: gemini-3.1-flash-lite 0.72, deepseek-v4-flash-vision-exp 0.69, deepseek-v4.1-flash 0.64.
VISION_MODEL = "google/gemini-2.5-flash-lite"
FIGURE = re.compile(r"!\[[^\]]*\]\(assets/([^)\s]+)\)")
SKIPPED_KINDS = {"formula", "logo", "decoration"}
DESCRIBE_PROMPT = """You describe one image from a research document so that text search can find it later.
The document text around the image is given only as context; describe what the image itself shows.

Reply in exactly this form:
KIND: one of chart, diagram, table, photo, screenshot, formula, logo, decoration, other
DESCRIPTION: two to six sentences on what the image shows: its type, its axes, legend, labels, or components
and how they connect, and the main result or pattern it displays. Use the labels and numbers visible in the
image; do not add anything that is not visible.

If KIND is formula, logo, or decoration, reply with the KIND line only.

Context:
"""


def description_marker(model: str) -> str:
    return f"> Figure description (generated by {model}, not from the source):"


def raster(name: str, data: bytes) -> tuple[str, bytes] | None:
    """The image as PNG (SVG rendered, CMYK converted) for the vision model; None if it is not an image."""
    try:
        if name.lower().endswith(".svg"):
            pixels = pymupdf.open(stream=data, filetype="svg")[0].get_pixmap(dpi=150)
        else:
            pixels = pymupdf.Pixmap(data)
            if pixels.colorspace and pixels.colorspace.n > 3:
                pixels = pymupdf.Pixmap(pymupdf.csRGB, pixels)
        if min(pixels.width, pixels.height) < 48:
            return None
        return Path(name).stem + ".png", pixels.tobytes("png")
    except (RuntimeError, ValueError):
        return None


def describe_figures(markdown: str, assets: Assets, model: str = VISION_MODEL) -> tuple[str, int]:
    """Insert a generated description under each figure worth describing; return the Markdown and the count.

    Formulas, logos, decorations, and images under 48 pixels a side are left undescribed. Figures that
    already carry a description are skipped, so this can run again after a partial failure.
    """
    wanted = {}
    for match in FIGURE.finditer(markdown):
        name = match.group(1)
        following = markdown[match.end():match.end() + 200].lstrip()
        if name in assets and not following.startswith("> Figure description") and name not in wanted:
            image = raster(name, assets[name])
            if image:
                wanted[name] = (markdown[max(0, match.start() - 600):match.end() + 600], image)

    replies: dict[str, str] = {}
    by_bytes: dict[str, str] = {}

    def describe(name: str) -> tuple[str, str]:
        context, image = wanted[name]
        return name, chat(model, DESCRIBE_PROMPT + context, image)

    unique = {}
    for name in wanted:  # identical images (such as light and dark variants) are described once
        digest = hashlib.sha256(assets[name]).hexdigest()
        by_bytes.setdefault(digest, name)
        unique[name] = by_bytes[digest]
    with ThreadPoolExecutor(max_workers=8) as pool:
        replies.update(pool.map(describe, sorted(set(unique.values()))))

    count = 0

    def insert(match: re.Match) -> str:
        nonlocal count
        reply = replies.get(unique.get(match.group(1), ""), "")
        kind = re.search(r"KIND:\s*(\w+)", reply)
        text = re.search(r"DESCRIPTION:\s*(.+)", reply, re.S)
        if not text or (kind and kind.group(1).lower() in SKIPPED_KINDS):
            return match.group(0)
        count += 1
        return f"{match.group(0)}\n\n{description_marker(model)} {' '.join(text.group(1).split())}\n"

    return FIGURE.sub(insert, markdown), count


# PDF

def pdf_markdown(original: bytes) -> tuple[str, Assets]:
    """Markdown of a PDF, with figure regions written as PNG assets linked as assets/NAME."""
    document = pymupdf.open(stream=original, filetype="pdf")
    with tempfile.TemporaryDirectory() as scratch:
        markdown = pymupdf4llm.to_markdown(document, write_images=True, image_path=scratch,
                                           image_format="png", show_progress=False)
        assets = {}
        for path in sorted(Path(scratch).iterdir()):
            name = "figure" + path.name if path.name.startswith("-") else path.name
            assets[name] = path.read_bytes()
            # The link holds the resolved temporary path (/private/var/... on macOS), so match its file name.
            markdown = re.sub(r"\]\([^)\s]*/" + re.escape(path.name) + r"\)", f"](assets/{name})", markdown)
    return markdown.rstrip() + "\n", assets


# arXiv

@dataclass
class Paper:
    id: str
    version: str
    meta: dict[str, str]

    @property
    def pdf(self) -> str:
        return f"https://arxiv.org/pdf/{self.id}{self.version}"

    @property
    def html(self) -> str:
        return f"https://arxiv.org/html/{self.id}{self.version}"


def arxiv_paper(url: str) -> Paper | None:
    """The arXiv paper a link names, at the version it names or the latest; None for other URLs."""
    match = ARXIV.match(url)
    if not match:
        return None
    wanted = match.group("id") + (match.group("version") or "")
    try:
        feed, _, _ = get(f"https://export.arxiv.org/api/query?id_list={wanted}")
    except NETWORK_ERRORS as error:
        raise ConvertError(f"arXiv API unreachable for {wanted}: {error}") from error
    entry = ElementTree.fromstring(feed).find("atom:entry", ATOM)
    found = entry.findtext("atom:id", "", ATOM) if entry is not None else ""
    version = re.search(r"(v\d+)$", found)
    if not version:
        raise ConvertError(f"arXiv has no paper {wanted}")
    names = [name.text.strip() for name in entry.findall("atom:author/atom:name", ATOM)]
    author = " and ".join(names) if len(names) <= 2 else ", ".join(names[:-1]) + ", and " + names[-1]
    meta = {
        "title": re.sub(r"\s+", " ", entry.findtext("atom:title", "", ATOM)).strip(),
        "author": author,
        "publisher": "arXiv",
        "published": entry.findtext("atom:updated", "", ATOM)[:10],  # the date of this version
    }
    return Paper(match.group("id"), version.group(1), meta)


def arxiv_markdown(paper: Paper) -> tuple[str, Assets] | None:
    """Markdown of arXiv's HTML rendering with formulas as LaTeX and figures as assets; None without one."""
    try:
        page, kind, final = get(paper.html)
    except NETWORK_ERRORS as error:
        if isinstance(error, urllib.error.HTTPError) and error.code == 404:
            return None
        raise ConvertError(f"could not read arXiv's HTML rendering of {paper.id}{paper.version}: {error}") from error
    soup = BeautifulSoup(page, "lxml")
    article = soup.select_one("article")
    if kind != "text/html" or article is None:
        return None
    for tag in article.select("script, style, nav"):
        tag.decompose()
    for math in article.find_all("math"):
        latex = (math.get("alttext") or math.get_text(" ", strip=True)).strip()
        block = math.get("display") == "block"
        math.replace_with(soup.new_string(f"\n\n$$\n{latex}\n$$\n\n" if block else f"${latex}$"))
    figures = []
    for number, tag in enumerate(article.find_all(["img", "object"]), 1):
        source = tag.get("src" if tag.name == "img" else "data")
        if source and not source.startswith("data:"):
            remote = urljoin(final, source)
            figures.append((tag, remote, f"{number:03d}-{Path(urlparse(remote).path).name}"))

    def download(figure) -> bytes | None:
        try:
            return get(figure[1])[0]
        except NETWORK_ERRORS:
            return None  # a missing figure must not lose the paper; its alt text stays in the Markdown

    assets: Assets = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for (tag, _, name), data in zip(figures, pool.map(download, figures)):
            if data is not None:
                assets[name] = data
                image = soup.new_tag("img", src=f"assets/{name}", alt=tag.get("alt") or tag.get("aria-label") or "")
                tag.replace_with(image)
    markdown = markdownify(str(article), heading_style="ATX", bullets="-")
    return re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n", assets
