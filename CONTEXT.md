# Smith Wiki

A public research wiki built from captured evidence. Research turns turn captured sources into linked wiki pages; a source captured without a page stays in the store, and a later turn may bring it in.

## Evidence

**Source**:
One URL whose content the wiki relies on, such as a paper, a documentation page, or a repository README. A repository or a book is one Source: its README or its chapter; other files of it are separate Sources, usually without a page.
_Avoid_: Document, reference, work

**Source page**:
The wiki page in `wiki/sources/` that annotates one Source. A Source may have no page yet.
_Avoid_: Source card

**Capture**:
The stored copy of a Source at one moment: its Original and a Markdown version of it. A Source has one current Capture; recapturing replaces it, and the earlier one stays only in the archive.
_Avoid_: Download, snapshot, version

**Original**:
The exact bytes a URL returned when it was captured; never modified.
_Avoid_: Raw file

**Locator**:
The position of a claim inside a Source, written in the wiki: a heading or exact text for a web page, a page or section for a paper, a file and heading for a repository.
_Avoid_: Anchor, pointer

## Search

**Search scope**:
The part of the corpus a search covers: `sources` (the current Captures) or `wiki` (wiki pages, Source pages included).
_Avoid_: Index, collection

**Chunk**:
A piece of a Capture or a wiki page that search stores and returns. Chunks change whenever chunking changes; a Locator does not.
_Avoid_: Passage, snippet
