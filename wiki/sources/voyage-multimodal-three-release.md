---
title: "voyage-multimodal-3: all-in-one embedding model for interleaved text, images, and screenshots"
summary: Voyage's original multimodal release compares extracted figure/table image retrieval with page screenshots and text.
url: https://blog.voyageai.com/2024/11/12/voyage-multimodal-3/
author: Voyage AI
publisher: "Voyage AI"
published: 2024-11-12
kind: article
captures:
  - retrieved: 2026-09-24T08:39:07Z
    sha256: "8c5d027bcdc65206636abe348c0d7e23242f2e99781fdef16f9bc66ee5650c90"
    type: text/html
---

## Overview

Voyage AI announces a multimodal embedding service that accepts interleaved text and images and evaluates it on three visual retrieval families plus text retrieval. Its six-dataset table/figure group is unusually relevant to searching for a particular diagram: each indexed item is an extracted visual, unlike the page-image corpus in [ViDoRe v1](../colpali-study/). It compares contemporaneous ColQwen2 v0.1, CLIP, SigLIP, and Cohere Embed v3 under Voyage's own protocol. As a vendor-run announcement, this is evidence of its test setup and claims rather than an independent audit or a current v4 comparison. Extracted image retrieval does not establish a figure's position, original caption association, or citation to its source document; the [figure provenance problem](../../concepts/visual-evidence-retrieval/) remains.


## Key points

- The six table/figure datasets are CharXiv, MMTab-test, ChartQA, ChartVE, FinTabNetQA, and PlotQA; queries are descriptions, captions, or references matched against extracted table/figure images (Evaluation Details, Datasets).
- The same study separately evaluates document screenshots on ten ViDoRe v1 tasks; a screenshot hit has a different unit from an extracted figure hit (Evaluation Details, task table).
- It ranks the top ten by cosine similarity and reports nDCG@10, not the original ViDoRe study's nDCG@5 (Evaluation Details, Metrics).
- Voyage reports its model ahead of ColQwen2 v0.1 by 6.14% on table/figure retrieval; Cohere comparator is Embed multimodal **v3**, not v4 (Results, Multimodal retrieval; Evaluation Details, Models).
- It supports a combined text/image input for embedding, but the generated vector does not itself identify the underlying figure's original page or URL (Support for Interleaved Text & Images).
