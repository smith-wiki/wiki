---
title: HTML Standard figure and figcaption elements
summary: HTML's source-level association between self-contained figure content and its authored caption.
url: https://html.spec.whatwg.org/multipage/grouping-content.html#the-figure-element
author: WHATWG
kind: specification
captures:
  - retrieved: 2026-09-24T08:44:45Z
    sha256: "7e5df4fb2d856394a9f042851dbe20249453d1c62714fe52c2ec8ee34229eaac"
    type: text/html
---

## Overview

The WHATWG HTML Standard defines the semantics and content model for `figure` and `figcaption` elements. It establishes a source-level way to group a self-contained visual and its authored caption, including an example with a `figure` ID that can be used as a URL fragment. This specification is more authoritative than a generated web-to-Markdown reading copy when an archive must preserve caption authorship. It does not promise that every web diagram uses semantic HTML or that an element ID remains stable across revisions. Combine it with [web capture fidelity](../../concepts/web-capture-fidelity/) and [visual evidence retrieval](../../concepts/visual-evidence-retrieval/): retain the captured DOM, asset, and URL rather than treating a generated description as the publisher's caption.


## Key points

- `figure` represents self-contained flow content typically referred to as one unit, optionally with a caption (section 4.4.12, The figure element).
- The first child `figcaption` is the figure's caption; with none, the `figure` has no caption in this semantic structure (section 4.4.12, The figure element).
- The standard shows `<figure id="l4">` with a caption and an `<a href="#l4">` reference, establishing a possible author-provided page fragment (section 4.4.12, code-listing example).
- A `figcaption` can include further source attribution, distinct from the image's alternative text (section 4.4.13, The figcaption element).
