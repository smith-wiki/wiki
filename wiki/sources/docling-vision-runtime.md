---
title: "Docling vision models and model catalog"
summary: "Docling documents model-specific Apple MLX/MPS inference and component-specific accelerator support and limitations."
url: https://docling-project.github.io/docling/usage/vision_models/
author: "Docling project"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:14:31Z
    sha256: "5ea70ff6883452f20f3136f5c203018ab00bb37674355d2e83a7bad46727dc05"
    type: text/html
  - retrieved: 2026-09-24T08:18:18Z
    sha256: "96dec45f6e80b896c84985311c115055e46ff6552edc05fd15e3a2800a869ffa"
    type: text/html
    url: https://docling-project.github.io/docling/usage/model_catalog/
---

## Overview

Docling's vision-model guide describes how to run page conversion locally with a chosen VLM in its `VlmPipeline`, while its companion model catalog maps layout, OCR, table, and specialized stages to devices. This is implementation guidance for practitioners, not a benchmark ranking of all Docling configurations. It makes Apple Silicon support concrete: selected Transformers models use MPS and selected MLX models run on Apple hardware, yet other pipeline components may run on CPU. The published M3 Max measurements are for a single specified PDF page and particular model/backends, not an expected document-wide throughput figure. The guide also describes when picture and caption blocks can be linked in structured output. Read it alongside the [Docling repository](../docling-repository/) and [READoc](../readoc-study/).

## Key points

- Local VLM choices include Transformers/MPS and MLX on Apple; a specified M3 Max one-page comparison reports SmolDocling MLX 6.15453 seconds versus Transformers/MPS 102.212 seconds. ("Available local models")
- The model catalog enumerates separate layout, table-structure, OCR, and vision components and their device support; a complete pipeline is not necessarily all-MPS. ("Model catalog", pipeline model entries)
- The Chandra HTML conversion example preserves headings, tables, math, and code whitespace; nested captions link to their picture/table while separate layout blocks remain unlinked. ("Chandra HTML output")
- JSON retains rich structure that individual Markdown exports may omit. ("Chandra HTML output")
