---
title: "Python usage"
summary: Trafilatura's extractor options and Markdown/structured-output modes, including tables and image controls.
url: https://trafilatura.readthedocs.io/en/latest/usage-python.html
author: Trafilatura project
publisher: "Trafilatura"
kind: webpage
captures:
  - retrieved: 2026-09-24T07:40:51Z
    sha256: "a6d50c80fcaad76263598cad577bd606efb280ca7c7a700fcc4b1fe311972239"
    type: text/html
---

## Overview

Trafilatura's Python guide documents the local extraction interface and its distinct output formats, including Markdown, HTML, JSON, and structured XML. It is first-party API documentation, useful for supported options but not an independent quality test. The standard extractor selects main content and can fall back to readability and jusText; this can improve recall while obscuring which internal extractor selected a particular fragment. Tables are included by default, images require opting in, and richer structural data is available through XML or a Python document object. The guide gives no quantitative assurance about code, formulas, captions, or complex table conversion; [WebMainBench](../webmainbench-structure-study/) supplies a separate check for some of those.

## Key points
- `extract()` selects main content, falling back to readability and jusText if its first result is too short; `html2txt()` instead returns all page text. (Extraction functions)
- Markdown is an output option; tables are included by default, while image inclusion retains alt, src, and title when enabled. (Output; Choice of HTML elements; Important notes)
- XML and `bare_extraction()` expose extra elements more directly, because not every requested element maps into every output format. (Important notes; Python objects as output)
