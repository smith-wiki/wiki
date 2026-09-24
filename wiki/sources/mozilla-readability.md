---
title: Mozilla Readability repository
summary: Firefox Reader View extractor returns selected HTML and text from a supplied DOM rather than Markdown.
url: https://raw.githubusercontent.com/mozilla/readability/ab4027a8b37669745016869a37a504727992b2ba/README.md
author: Mozilla
kind: repository
captures:
  - retrieved: 2026-09-24T07:47:34Z
    sha256: "0b9299bbc294dcabca728f5063bb8720f8dcc87b7a498f31b218d7bdafa3fc23"
    type: text/plain
---

## Overview

Mozilla's Readability.js is the standalone article extractor used by Firefox Reader View. The pinned project README defines its local browser and Node interface: a caller passes a DOM, and `parse()` returns processed article HTML, plain text, and metadata. The library does not itself fetch, render JavaScript, or convert HTML to Markdown, so pairing it with a converter changes structural fidelity independently of its content-boundary selection. Relative image and link URLs can be resolved when the supplied DOM has the original URL. Mozilla also warns that Readability output is not sanitized; consumer applications must sanitize untrusted content before displaying it. For numerical comparisons, see the [multi-type benchmark](../wcxb-content-extraction-benchmark/), which scores text extraction rather than downstream formatting.

## Key points
- `parse()` returns HTML in `content` and tags-stripped `textContent`, along with title and metadata; Markdown is not an output. (README, API Reference: parse)
- The library consumes a supplied DOM in the browser or Node via a separate DOM implementation; cloning avoids mutating the original. (README, Basic usage; Node.js usage)
- Node's jsdom script execution is disabled by default and Mozilla strongly recommends leaving it disabled. (README, Node.js usage)
- Readability does not sanitize untrusted content and recommends a separate sanitizer for display. (README, Security)
