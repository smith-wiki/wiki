---
title: "Marker repository: PDF-to-Markdown pipeline"
summary: "Marker outputs Markdown or block JSON with code, equations, and tables; Apple inference uses llama.cpp and its model weights have restrictions."
url: https://raw.githubusercontent.com/datalab-to/marker/8a1d2344de25d7ec4c5209133aed7af565874ff0/README.md
author: "Datalab"
kind: repository
captures:
  - retrieved: 2026-09-24T08:11:08Z
    sha256: "1b874b82efc709d55d3a251cc631c13f695ed08935241fb4cce995e964fd00e4"
    type: text/plain
---

## Overview

Datalab's pinned Marker README documents a PDF conversion pipeline with layout detection, selective OCR, table reconstruction, and optional LLM correction. It is addressed to developers choosing Markdown, HTML, chunks, or typed JSON. Its output includes equations, fenced code, image references, and heading/caption block classes, making the structured form preferable when retaining more than linear text. On Apple Silicon the current VLM server uses llama.cpp, while smaller support models can use Torch devices; CPU/MPS defaults to fast rather than highest-quality balanced mode. The README's benchmark and speed claims are vendor-run and use a B200 or other specified configurations, not Mac measurements. Its Apache-2.0 code license does not cover the modified OpenRAIL-M model weights. Compare [READoc](../readoc-study/) and [olmOCR 2's versioned evaluation](../olmocr-two-study/).

## Key points

- Marker advertises formatted tables, equations, inline math, code blocks, images, and multiple output formats; JSON exposes typed `Caption`, `Code`, `Equation`, `SectionHeader`, `Table`, and image blocks. ("Features"; "JSON")
- On CPU/Apple Silicon its VLM server uses llama.cpp; CPU/MPS defaults to fast mode, whereas balanced mode uses more VLM inference. Disabling OCR skips scanned pages and equations. ("Conversion modes"; "Install")
- Code is Apache-2.0, but the model weights have a modified OpenRAIL-M license with commercial-use thresholds. ("Commercial usage")
- Its vendor-run throughput table uses concurrent processing on an NVIDIA B200, so it is not a measured Apple Silicon runtime. ("Benchmarks"; "Throughput")
