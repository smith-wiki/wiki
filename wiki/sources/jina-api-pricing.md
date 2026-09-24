---
title: Jina AI API pricing and limits
summary: Jina's public embedding-token purchase tiers and throughput limits for hosted API use.
url: https://jina.ai/contact-sales/
author: Jina AI
kind: webpage
captures:
  - retrieved: 2026-09-24T08:42:06Z
    sha256: "05c95e96a34369c35cdd87189788f8c4aa4eac3cf77593f65c26f797b0362caa"
    type: text/html
---

## Overview

Jina AI's self-serve purchase and limits page prices input tokens used by hosted embedding requests and lists rate tiers. It is first-party evidence for estimating calls to the Jina Embeddings v4 API, but published payment tiers are not an invoice for a particular image: token usage varies with model, preprocessing, and resolution. The page also distinguishes service access from model-weight licensing; this matters if an archive chooses a local rather than hosted index. Read it with [Jina's image-token explanation](../jina-embedding-api-docs/) and the [v4 model study](../jina-embeddings-four-study/). The document neither quotes total vector database costs nor measures figure-level citation quality.


## Key points

- The purchase table offers $50 for 1B tokens ($0.050 per million) and $500 for 11B tokens ($0.045 per million); this is hosted service pricing, not local inference cost (Pricing tiers).
- The embedding endpoint's displayed throughput is 100 RPM/100k TPM free, 500 RPM/2M TPM paid, and 5,000 RPM/50M TPM premium (Service rate limits, Embedding API).
- **Inference:** At $0.05 per million tokens, a 4,840-token example image costs $0.000242 gross, or $24.20 per 100,000 images of that token size, excluding free usage, storage, and query costs ([Jina AI, n.d.](../jina-embedding-api-docs/); Pricing tiers).
