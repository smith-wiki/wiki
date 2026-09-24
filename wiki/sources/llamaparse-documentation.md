---
title: "LlamaParse parsing configuration"
summary: "Hosted LlamaParse configuration controls OCR, layout, tables, page boundaries, and optional outputs, without a local parser-engine license."
url: https://developers.llamaindex.ai/llamaparse/parse/guides/configuring-parse/
author: "LlamaIndex"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:13:44Z
    sha256: "8f5c7d3b72cd2053ac393c2c37e408bf355e607d741d15bd7d57249ad9c2de92"
    type: text/html
  - retrieved: 2026-09-24T08:17:58Z
    sha256: "c30e7a94f2515c0b4fa8500111c9107881d1787a434b7316a36f144d9fa6bc26"
    type: text/html
    url: https://developers.llamaindex.ai/llamaparse/parse/guides/configuring-parse/
---

## Overview

LlamaIndex's Parse guides document options for a managed document-parsing API, aimed at developers tuning page output and structured extraction. OCR, page selection, table markup, image extraction, header handling, and merging tables across pages all affect the resulting Markdown. The preserved option guides include both a newer configuration page and a v1 options page; parameter availability should therefore be checked for the chosen API version. These are first-party descriptions of controllable behavior, not comparative scores on [olmOCR-Bench](../olmocr-bench-dataset/) or [OmniDocBench](../omnidocbench-repository/). They do not grant rights to run parser model weights on a laptop, nor establish reliable code-fence or figure-caption association for scientific PDFs. The separate [self-hosting guide](../llamaparse-self-hosting/) clarifies enterprise deployment.

## Key points

- Options select parsing quality/modes and output settings; page separator and page numbering preserve attribution in Markdown. ("Configuring Parse"; "Page separator")
- HTML table output can retain row/column spans that pipe Markdown cannot; optional cross-page table merging changes pagination and removes headers/footers. ("Output table as HTML in markdown"; "Merge tables across pages in markdown")
- OCR and image extraction can be configured separately; bounding-box cropping and header/footer filtering alter what content survives. ("Disable OCR"; "Disable image extraction"; "Bounding box"; "Hide headers")
