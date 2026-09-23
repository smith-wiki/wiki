#!/usr/bin/env python3
"""Print a compact Markdown-like reading copy of a preserved HTML capture."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

SKIP = {"script", "style", "svg", "noscript", "template", "iframe", "canvas", "head"}
BLOCK = {
    "p", "div", "section", "article", "header", "footer", "main", "aside", "nav",
    "ul", "ol", "li", "table", "tr", "blockquote", "pre", "dl", "dt", "dd",
    "figure", "figcaption", "br", "hr", "h1", "h2", "h3", "h4", "h5", "h6",
}


class Reader(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.skip_depth = 0
        self.in_title = False
        self.title = ""
        self.lines: list[str] = []
        self.current: list[str] = []
        self.href: str | None = None
        self.link_start = 0

    def flush(self) -> None:
        text = re.sub(r"\s+", " ", "".join(self.current)).strip()
        if text and text not in {"-", "#"}:
            self.lines.append(text)
        self.current = []
        self.href = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self.in_title = True
        if tag in SKIP:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in BLOCK:
            self.flush()
        if re.fullmatch(r"h[1-6]", tag):
            self.current.append("#" * int(tag[1]) + " ")
        elif tag == "li":
            self.current.append("- ")
        elif tag == "a":
            href = dict(attrs).get("href") or ""
            if href and not href.startswith(("#", "javascript:", "data:", "mailto:")):
                self.href = urljoin(self.base_url, href)
                self.link_start = len(self.current)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        if tag in SKIP:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag == "a" and self.href:
            if "".join(self.current[self.link_start:]).strip():
                self.current.insert(self.link_start, "[")
                self.current.append(f"]({self.href})")
            self.href = None
        if tag in BLOCK:
            self.flush()

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
            return
        if not self.skip_depth:
            self.current.append(data)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: extract_text.py HTML_FILE BASE_URL", file=sys.stderr)
        return 2
    raw = Path(sys.argv[1]).read_bytes()
    reader = Reader(sys.argv[2])
    reader.feed(raw.decode("utf-8", errors="replace"))
    reader.close()
    reader.flush()
    title = re.sub(r"\s+", " ", reader.title).strip()
    if title:
        print(f"Title: {title}\n")
    print("\n".join(reader.lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
