---
title: "Embedding API - Jina AI"
summary: Jina's embedding API explains multimodal image token accounting and actual usage reporting.
url: https://jina.ai/embeddings/
author: Jina AI
kind: documentation
captures:
  - retrieved: 2026-09-24T08:41:47Z
    sha256: "de96c8422c8e5feffe3459546142c11b0f35711384e30bd5abb25c3d63b304d6"
    type: text/html
---

## Overview

Jina AI's embedding API guide describes input, modes, and usage accounting for image and text embedding models. Its image-token example makes v4 costs more concrete than a generic per-token tariff: it gives a representative 600-by-600 pixel charge and directs customers to the actual response usage for exact billing. The guide is a first-party operational contract, not a comparative benchmark or a guarantee for PDF pages of another size. Pair it with the [Jina v4 paper](../jina-embeddings-four-study/) for the dense/late architecture and [Jina's pricing page](../jina-api-pricing/) for the published token rate. A model vector has no source-figure provenance by itself.


## Key points

- A 600-by-600 image uses approximately 4,840 tokens in `jina-embeddings-v4`; different encoders and inputs change image tokenization (Image token counting).
- API responses include usage with an image-token breakdown, so invoice estimates should use measured calls rather than a fixed tokens-per-page assumption (Image token counting).
- Embedding image pixels does not extract figure boundaries or authenticate generated descriptions (Embedding API; Image token counting).
