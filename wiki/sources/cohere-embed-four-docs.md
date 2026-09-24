---
title: Cohere Embed model documentation
summary: Official Embed v4 modality, context, and dense embedding dimension contract; no published ViDoRe score.
url: https://docs.cohere.com/docs/cohere-embed
author: Cohere
publisher: Cohere
kind: documentation
captures:
  - retrieved: 2026-09-24T08:40:27Z
    sha256: "d33c7b4d8818bc92d94cebc3be0b87d400729577a5dad8d60055aca726bc4a6d"
    type: text/html
---

## Overview

Cohere's model-reference page lists the current Embed family and defines the modalities, embedding dimensions, input context, and similarity functions supported by `embed-v4.0`. It is the authoritative product contract for the named model, not an independent retrieval evaluation or a public benchmark report. Mixed text/image inputs allow a figure to retain nearby context in an embedding unit, but the returned vector is not itself a citation to a source region. The source complements the competing-vendor [Voyage 3.5 comparison](../voyage-multimodal-three-five-release/), which includes a Cohere v4 row under Voyage's protocol, and [ViDoRe v3](../vidore-three-study/), which separates page retrieval from evidence boxes. This page supplies no tested figure-localization quality or deployment bill.


## Key points

- `embed-v4.0` accepts text, images, or mixed text/images such as PDF content (model table, Embed v4 row).
- One output vector can have 256, 512, 1024, or default 1536 dimensions; supported similarity metrics are cosine, dot product, and Euclidean distance (model table, Embed v4 row).
- Context length is 128k tokens, not evidence that a long source produces a precise figure-level match (model table, Embed v4 row).
- This model table gives no ViDoRe result, figure benchmark, API per-image charge, or timing guarantee (model table).
