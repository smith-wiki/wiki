---
title: ColQwen2.5 v0.2 model repository
summary: Pinned model card documents patch cap, example vector count, processor version caveat, MPS example, and backbone license.
url: https://huggingface.co/vidore/colqwen2.5-v0.2/raw/dcbe8d9cede518bce830488364ba0e40c873645b/README.md
author: ViDoRe project
kind: repository
captures:
  - retrieved: 2026-09-24T08:48:43Z
    sha256: "0bb2a7a0939cae5895c6cb89bff2276a6f53a37d3aef794d8c4dc9d392f38c8c"
    type: text/plain
---

## Overview

The ViDoRe project's pinned Hugging Face model card specifies the exact `colqwen2.5-v0.2` checkpoint's visual inputs, multivector output, training processor, and limitations. It gives a concrete page/query embedding shape and warns that recent `colpali-engine` versions changed the query prefix, which matters when reproducing [ViDoRe v2](../vidore-two-study/) comparisons. The card documents an Apple MPS example but not measured Mac throughput or memory. Its licensing section distinguishes the MIT adapters from the Qwen Research-licensed backbone; repository metadata alone is not a commercial license. This is maintainer documentation, not a fresh independent benchmark. Its 768-patch cap and variable-length output help explain the storage tradeoff in [visual evidence retrieval](../../concepts/visual-evidence-retrieval/).


## Key points

- Input resolution is dynamic, bounded by 768 image patches, with more patches reported to improve performance at additional memory cost (Version specificity).
- Example embeddings are `(25, 128)` for a query and `(755, 128)` for a document image; masks can drop 11 non-image tokens per page (Usage, Sentence Transformers).
- The checkpoint used `colpali-engine==0.3.7`; versions 0.3.13+ no longer add its training-time `Query: ` prefix, which can change comparisons (Version specificity; Usage, ColPali Engine warning).
- Example model loading names Apple Silicon `mps`, but no benchmarked Mac pages/second or peak unified memory is supplied (Usage, ColPali Engine).
- Backbone Qwen2.5-VL has the Qwen Research License and attached adapters have MIT terms; both must be considered for deployment (License).
