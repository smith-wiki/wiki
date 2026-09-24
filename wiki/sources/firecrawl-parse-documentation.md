---
title: "Firecrawl Parse PDF API"
summary: "Hosted PDF parsing exposes Markdown, page markers, ordered typed blocks with provenance, and fast/auto/OCR modes."
url: https://docs.firecrawl.dev/features/parse
author: "Firecrawl"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:14:03Z
    sha256: "aa681b4461f6433fa1f120dd7a6ca5c7b22a9b1927aedf5e144c781ab0b02b90"
    type: text/html
---

## Overview

Firecrawl's Parse documentation specifies a hosted document API that turns PDFs into Markdown and optional per-page content or typed layout blocks. Its block schema includes positions, reading-order indices, provenance, confidence, and links into Markdown, making it more auditable than a bare string when preserving scientific structure. The default auto mode attempts embedded text first and falls back to OCR; fast and forced-OCR modes have different failure and cost profiles. The source is first-party product documentation, not a published score for the managed PDF parser on [olmOCR-Bench](../olmocr-bench-dataset/) or [OmniDocBench](../omnidocbench-repository/). Figure and caption labels do not themselves establish a durable association, and [self-hosting guidance](../firecrawl-deployment-limits/) does not promise out-of-box parity with cloud extraction.

## Key points

- PDFs can return whole-document Markdown, physical-page Markdown, page-break markers, and typed blocks with bounding boxes and Markdown character spans. ("Per-page markdown"; "Page markers"; "Layout blocks")
- Block types include title, section header, table, formula, figure, and caption; `readingOrder`, `source`, and nullable confidence expose extraction provenance. ("Block fields")
- `fast` uses embedded text and fails on image-only pages; `auto` may fall back to OCR; `ocr` forces it. ("PDF options")
- The API bills PDF parsing per page, and the documented block/page options add no additional credits. ("Considerations")
