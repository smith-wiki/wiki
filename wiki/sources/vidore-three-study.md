---
title: "ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios"
summary: ViDoRe v3 separates page retrieval, answer quality, and annotated visual evidence bounding boxes.
url: https://arxiv.org/html/2601.08620v1
author: Antonio Loison, Quentin Mace, Antoine Edy, Victor Xing, Tom Balough, Gabriel Moreira, Bo Liu, Manuel Faysse, Celine Hudelot, and Gautier Viaud
published: 2026-01-13
kind: paper
captures:
  - retrieved: 2026-09-24T08:37:42Z
    sha256: "f84326f47532ba9c965f9010fa50f7e1fad207d76c616aa351109dcabf58a8c6"
    type: text/html
---

## Overview

Loison and colleagues publish a third ViDoRe benchmark covering ten professional document collections, roughly 26,000 pages, and 3,099 human-verified queries translated into six languages. Unlike the [v1](../colpali-study/) and [v2](../vidore-two-study/) papers, it evaluates retrieval, answer quality, and bounding-box grounding separately. The reported page-retrieval rows compare visual and parsed-text pipelines on nDCG@10; candidate-page grounding has a separate region-agreement measure. This source is especially relevant when a retrieved page must be cited as a particular figure, because it shows the difficulty of evidence localization. The benchmark designers evaluate their own corpus, only eight datasets are public, and its localization results condition on candidate pages rather than testing a complete figure-citation system.


## Key points

- Ten datasets comprise about 26,000 pages and 3,099 human-verified queries with six-language translations; annotators label relevant pages, answers, and support boxes (abstract; section 3).
- On its nDCG@10 page retrieval setup, visual Jina-v4 scores 57.6, visual ColQwen2.5 51.9, visual ColQwen2 44.7, and text Jina-v4 over extracted page Markdown 50.4; these do not measure figure precision (section 4.1, Table 1).
- For candidate-page visual grounding, annotator-to-annotator F1 is 0.602 versus 0.089 for Qwen3-VL-30B-A3B and 0.065 for Gemini 3 Pro. Grounding is evaluated apart from retrieval (section 4.3, Table 4; appendix Table 15).
- The paper computes retrieval nDCG@10 rather than the nDCG@5 used by v1/v2; changed datasets and labels preclude interpreting their scores as one time series (section 4.1).
