---
title: "voyage-multimodal-3.5: a new multimodal retrieval frontier with video support"
summary: Voyage's 3.5 announcement compares Cohere Embed v4 on visual-document retrieval and describes dense-index options.
url: https://blog.voyageai.com/2026/01/15/voyage-multimodal-3-5/
author: Voyage AI
publisher: "Voyage AI"
published: 2026-01-15
kind: article
captures:
  - retrieved: 2026-09-24T08:39:24Z
    sha256: "9bbca90928413eea01c118ee784f4186ea07b4fd5b4c2a1730c31697ce57b6b9"
    type: text/html
---

## Overview

Voyage AI's 2026 model announcement describes a multimodal dense embedding service with interleaved text, image, and video inputs. It evaluates the 3.5 release against Cohere Embed v4, Amazon Nova 2, and its earlier 3 release using ViDoRe v1/v2 and MIRACL-VISION datasets. This is the clearest reviewed named Cohere v4 comparison, but it is run by a competing vendor, uses nDCG@10 rather than the original ViDoRe papers' nDCG@5, and the post states inconsistent percentage summaries. Its Matryoshka dimensions and quantization are useful for storage planning, not proof of lower end-to-end costs. Read with [ViDoRe v2's historical evaluation](../vidore-two-study/) and [Voyage's older figure-specific comparison](../voyage-multimodal-three-release/); neither validates figure-level source citations.


## Key points

- `voyage-multimodal-3.5` accepts interleaved text and images and outputs 2048, 1024, 512, or 256 dimensional dense vectors, with float32, int8/uint8, or binary choices (Model architecture; Matryoshka embeddings and quantization).
- Its 15 visual-document retrieval datasets combine ViDoRe v1, ViDoRe v2, and MIRACL-VISION; it also tests three video datasets separately (Evaluation Details, Datasets).
- Cohere Embed v4 is named as a comparator; cosine top-ten retrieval is reported as nDCG@10, not a figure-box score (Evaluation Details, Baselines and Metrics).
- The post's TL;DR reports a 4.56% advantage over Cohere v4, while Results says 2.26%; the discrepancy prevents quoting either percentage without checking the underlying dataset sheet (TL;DR; Results, Visual document retrieval).
- Unlike the older release's extracted figure/table suite, the visual-document comparison is primarily screenshot/page retrieval and does not assess exact source-figure citation (Evaluation Details, Datasets).
