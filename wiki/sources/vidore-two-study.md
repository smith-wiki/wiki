---
title: "ViDoRe Benchmark V2: Raising the Bar for Visual Retrieval"
summary: Harder multilingual page-retrieval benchmark with cross-document queries and model-specific nDCG@5 results.
url: https://arxiv.org/html/2505.17166
author: Quentin Mace, Antonio Loison, and Manuel Faysse
published: 2025-09-19
kind: paper
captures:
  - retrieved: 2026-09-24T08:33:28Z
    sha256: "3a2661f21d85b98967107bb846ef483bcaac04a061ee7bbbb9aaf47151f1bc05"
    type: text/html
---

## Overview

Mace, Loison, and Faysse propose a second visual document retrieval benchmark because leading systems were saturating ViDoRe v1. The paper describes blind contextual query writing, human review, cross-document questions, multilingual variants, and page-level relevance judgments across biomedical, economics, ESG, and an insurance collection later removed for copyright reasons. Its model table offers a named ColPali/ColQwen comparison on the harder dataset, but the Voyage row lacks a model version, uses a specific image resizing procedure, and cannot validate current vendor offerings. The study is primary evidence for its own benchmark, not a figure-grounding or web-image localization test. Read it alongside the original [ColPali study](../colpali-study/) and [PDF benchmark scope limits](../../notes/pdf-benchmark-scores-do-not-certify-structure/).


## Key points

- ViDoRe v2 counters v1's extractive, single-page-query bias with blind contextual and cross-document queries; it uses hybrid synthetic and human-reviewed judgments (sections 1-2).
- The collection spans biomedical, economics, ESG, and insurance, but insurance was later removed for legal copyright reasons; the displayed table still includes its columns (section 3, Table 1; section 5, Table 2).
- Reported mean nDCG@5 is 0.505 for colpali-v1.2, 0.546 for colpali-v1.3, 0.583 for colqwen2-v1.0, and 0.597 for colqwen2.5-v0.2; distinguish exact versions and historical corpus composition (section 5, Table 2).
- The 0.550 voyageai row does not name a model checkpoint; authors say they resized images to at most 1200 pixels high, affecting comparison with Voyage's v1 number (section 5, note before Table 2).
- V2 still evaluates relevant document pages; its figure does not measure correct figure-box identification, visual-answer accuracy, or author-caption fidelity (sections 3-5).
