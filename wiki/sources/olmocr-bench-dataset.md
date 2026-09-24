---
title: "olmOCR-Bench dataset and unit-test protocol"
summary: "AI2's PDF-to-Markdown benchmark tests content, order, table relationships, and rendered math, but not all scholarly structure."
url: https://huggingface.co/datasets/allenai/olmOCR-bench
author: "Allen Institute for AI"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:04:20Z
    sha256: "ef0a0aa5df6b765dbeaa0ebbf00905ebefaa1778041489355a2ef9de02cfd060"
    type: text/html
---

## Overview

The Allen Institute for AI's dataset card describes olmOCR-Bench, a research-oriented collection of PDFs and binary tests for judging PDF-to-Markdown conversions. Its source breakdown, test definitions, and historical comparison table make it useful for interpreting published parser scores, not for declaring that every heading, code fence, or figure caption survived. It is a first-party benchmark specification, but its table mixes particular historical tool releases, and the authors also develop olmOCR. The live Hugging Face model leaderboard above the dataset card is a separate, changing interface. Compare this benchmark's test coverage with [OmniDocBench's component-level evaluation](../omnidocbench-study/) and the later [olmOCR 2 evaluation](../olmocr-two-study/), rather than transferring scores between them.

## Key points

- The corpus contains 1,403 PDFs and 7,010 tests: 721 text-presence, 823 text-absence, 1,061 reading-order, 1,020 table, and 3,385 math tests. (Table 1, "Distribution of Test Classes")
- Reading order checks relative positions of selected text spans; table tests check neighboring cell values; formulas are compared by rendered symbol layout. These are not direct heading hierarchy, code-block, or figure-caption association tests. ("Evaluation Criteria")
- The historical dataset-card table reports Marker 1.6.2 at 59.4, MinerU 1.3.10 at 61.5, Mistral OCR at 72.0, and original anchored olmOCR at 77.4 overall, each with reported uncertainty; those versions must not be interchanged with newer releases. ("Benchmark Results by Document Source")
- Its sources include arXiv mathematical pages, old scans, internally assembled tables and layouts, and model-assisted test generation. (Table 2, "Document source category breakdown")
- The dataset's ODC-BY-1.0 license is distinct from the OCR software and model-weight licenses. ("License")
