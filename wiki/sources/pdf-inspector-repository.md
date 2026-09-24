---
title: "pdf-inspector local PDF engine and Apple benchmark"
summary: "Firecrawl's MIT Rust parser has native-text structure extraction and an Apple M4 Pro benchmark distinct from hosted Firecrawl Parse."
url: https://raw.githubusercontent.com/firecrawl/pdf-inspector/876fe9ac65c1b05512b9a1a182b5c56bcfdd6c39/README.md
author: "Firecrawl"
kind: repository
captures:
  - retrieved: 2026-09-24T08:21:53Z
    sha256: "412d70d7ee16302a4452eff75f7a985296f271cecf82a5c2a6f6ebbea3134c5d"
    type: text/plain
---

## Overview

The pinned pdf-inspector README describes Firecrawl's MIT-licensed native Rust component for classifying and extracting PDFs into Markdown. It is particularly useful for separating a documented Apple-local CPU path from Firecrawl's managed Parse service: the default path handles embedded text, columns, headings, tables, code, and caption-like prefixes, while optional selective OCR requires additional PDFium, ONNX Runtime, and model assets. Its author-run OpenDataLoader corpus benchmark supplies one measured Apple M4 Pro snapshot for the native parser, not for the hosted service and not on olmOCR-Bench or OmniDocBench. Even this score applies only to an older named parser version and an OCR-disabled configuration. See the [server integration](../firecrawl-server-repository/) and [Parse API contract](../firecrawl-parse-documentation/) before inferring feature or quality parity.

## Key points

- The local Rust parser handles multi-column order, headings, heuristic/rectangle tables, monospace code, and caption prefix detection; optional OCR needs external native libraries and models. ("Features"; "Markdown features"; "Selective OCR")
- On a 200-PDF OCR-disabled corpus, its vendor-reported v0.2.6 result is 0.875 overall, 0.915 order NID, 0.814 table TEDS, and 0.788 heading MHS. The median sequential 200-document run is 0.470 seconds on Apple M4 Pro; the tested PyMuPDF4LLM was 0.2.0. ("Benchmark")
- The benchmark is a native-parser comparison, not a score for Firecrawl Cloud's PDF `/parse` endpoint. ("Benchmark"; "Best fit")
- The library is MIT licensed, distinct from the AGPL Firecrawl server. ("License")
