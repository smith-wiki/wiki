#!/usr/bin/env python3
"""Tidy wiki Markdown before a commit and reject broken links between wiki pages.

Usage:
  tidy.py PAGE...      fold typography, strip trailing whitespace, end with one newline,
                       then check each relative link against the pages under wiki/
  tidy.py --text TEXT  print TEXT with typography folded to ASCII
"""

from __future__ import annotations

import posixpath
import re
import sys
from pathlib import Path

# Typographic quotes, dashes, ellipses, and no-break spaces are not a language; fold them to ASCII.
FOLD = str.maketrans({
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "--", "\u2026": "...", "\u00a0": " ",
})

LINK = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def tidy(text: str) -> str:
    lines = [line.rstrip() for line in text.translate(FOLD).split("\n")]
    return "\n".join(lines).rstrip("\n") + "\n"


def page_url(wiki: Path, page: Path, text: str) -> str:
    """The site URL of the page: its permalink, or Eleventy's /a/b/ for wiki/a/b.md and /a/ for wiki/a/index.md."""
    permalink = re.search(r"^permalink:\s*(\S+)", text.split("\n---", 1)[0], re.M)
    if permalink:
        url = permalink.group(1).strip("\"'")
        return url if url.endswith("/") else posixpath.dirname(url).rstrip("/") + "/"
    parts = page.relative_to(wiki).with_suffix("").parts
    if parts[-1] == "index":
        parts = parts[:-1]
    return "/" + "".join(f"{part}/" for part in parts)


def exists(wiki: Path, url_path: str) -> bool:
    relative = url_path.strip("/")
    if not relative:
        return (wiki / "index.md").exists()
    if posixpath.splitext(relative)[1]:
        return (wiki / relative).exists()
    return (wiki / f"{relative}.md").exists() or (wiki / relative / "index.md").exists()


def broken_links(wiki: Path, page: Path, text: str) -> list[str]:
    base = page_url(wiki, page, text)
    found = []
    for target in LINK.findall(CODE.sub("", text)):
        if re.match(r"[a-z][a-z0-9+.-]*:|#|//", target):
            continue
        path = target.split("#", 1)[0].split("?", 1)[0]
        resolved = posixpath.normpath(posixpath.join(base, path))
        if not exists(wiki, resolved):
            found.append(target)
    return found


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[0] == "--text":
        sys.stdout.write(argv[1].translate(FOLD))
        return 0
    if not argv or argv[0].startswith("-"):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    wiki = Path(__file__).resolve().parent.parent / "wiki"
    errors = []
    for name in argv:
        page = Path(name).resolve()
        text = page.read_text(encoding="utf-8")
        tidied = tidy(text)
        if tidied != text:
            page.write_text(tidied, encoding="utf-8")
        errors += [f"{name}: broken link {target}" for target in broken_links(wiki, page, tidied)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
