---
title: "Mistral OCR processor and OCR 4.1 service"
summary: "Hosted OCR returns Markdown and optional ordered typed blocks, tables, images, and confidence; newer fields require newer API models."
url: https://docs.mistral.ai/capabilities/document_ai/basic_ocr
author: "Mistral AI"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:13:26Z
    sha256: "4c9fbe64da52cbe0885b5850100ba64dec843467b878dd971511ef8c19503e58"
    type: text/html
  - retrieved: 2026-09-24T08:17:38Z
    sha256: "fc21f65d57eee4be094a1ff8b12619d63a57459d1facf71ae3a9c7f5b3d4882a"
    type: text/html
    url: https://docs.mistral.ai/models/ocr-4-1
---

## Overview

Mistral AI's OCR processor documentation describes its hosted document OCR API for PDF and image extraction. It defines per-page Markdown, table and image assets, optional reading-order blocks with geometry and confidence, and model-dependent feature availability. The companion OCR 4.1 model page identifies a current service and listed per-page price. This is a product interface specification, not proof that its current model earned the [older Mistral OCR API benchmark row](../olmocr-two-study/): that evaluation does not identify OCR 4.1, and block extraction requires OCR 4 or newer. A Mac can upload or supply a document URL, but no local inference engine or downloadable weights are offered here. Treat code-block and caption labels as observable output fields to validate, not a guarantee that every relationship survives.

## Key points

- The API returns page Markdown and optional image/table assets; `table_format` can request separate Markdown or HTML tables. ("OCR capabilities"; "OCR with images and PDFs")
- `include_blocks` returns reading-order boxes with labels for titles, equations, captions, code, tables, and images, but requires OCR 4 or later; separate table formatting starts at OCR 2512. ("Block extraction"; "OCR capabilities")
- OCR 4.1 is a hosted `/v1/ocr` model listed at USD 4 per 1,000 pages or USD 5 per 1,000 annotated pages; this is not the unnamed historical benchmark model. ("OCR 4.1", "Features"; "Price")
