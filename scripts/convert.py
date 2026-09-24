"""Markdown copies of PDFs and arXiv papers, with their figures as separate image files.

A PDF is parsed on this machine by pymupdf4llm with PyMuPDF's layout model,
which recovers headings, tables, and figure regions. An arXiv paper is read
from arXiv's own HTML rendering of its LaTeX, which keeps formulas as LaTeX;
papers without one fall back to their PDF.
"""

from __future__ import annotations

import re
import tempfile
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


def get(url: str, timeout: int = 120) -> tuple[bytes, str, str]:
    """(body, media type, final URL) of a GET request."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        kind = (response.headers.get("Content-Type") or "").split(";")[0].strip().lower()
        return response.read(), kind, response.geturl()


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
    except (urllib.error.URLError, TimeoutError) as error:
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
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise ConvertError(f"arXiv HTML returned HTTP {error.code} for {paper.id}{paper.version}") from error
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
        except (urllib.error.URLError, TimeoutError):
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
