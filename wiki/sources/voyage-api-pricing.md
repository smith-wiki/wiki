---
title: Voyage API pricing
summary: Official multimodal 3.5 per-pixel and per-token charges, image clamps, free allowance, and batch caveat.
url: https://docs.voyageai.com/docs/pricing
author: Voyage AI
publisher: Voyage AI
kind: documentation
captures:
  - retrieved: 2026-09-24T08:41:28Z
    sha256: "dd823a511559ef53a48c96de78d68efe3f5ed71963f46369076c0876063df0bb"
    type: text/html
---

## Overview

Voyage AI's pricing documentation specifies how its multimodal embedding endpoint charges separately for text tokens and processed image/video pixels. Unlike a model-quality announcement, this page gives billable floors, ceilings, free usage, and batch conditions needed to estimate page-image or figure-crop embedding costs. It does not include PDF rasterization, caption generation, a vector database, network traffic, or query latency. The listed charges are provider terms at capture time and can change; usage responses remain decisive for a particular job. Compare with [Jina's token billing](../jina-api-pricing/) and the [Voyage 3.5 release](../voyage-multimodal-three-five-release/). The original figure, not its priced embedding, remains the evidence returned to a reader.


## Key points

- Both multimodal-3.5 and multimodal-3 cost $0.12 per million text tokens and $0.60 per billion image/video pixels, after 200M free text tokens and 150B free pixels per account (Multimodal Embeddings).
- Images under 50,000 pixels are upscaled and billed as 50,000; over 2M are downsampled and billed as 2M. Documented gross image charges range from $0.00003 to $0.0012 (Multimodal Embeddings, image examples).
- A 1000-by-1000 image costs $0.0006 gross; a page billed at 2M pixels costs $0.0012, or $120 gross per 100,000 images before free allowance (Multimodal Embeddings, image examples; arithmetic).
- The batch endpoint offers a 33% discount but consumes no free credits; neither rate includes image description generation (Batch and Files API).
