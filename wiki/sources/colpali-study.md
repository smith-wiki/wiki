---
title: "ColPali: Efficient Document Retrieval with Vision Language Models"
summary: Original ColPali and ViDoRe v1 study comparing page-image retrieval with OCR and generated visual captions.
url: https://arxiv.org/html/2407.01449
author: Manuel Faysse, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, Celine Hudelot, and Pierre Colombo
published: 2025-02-28
kind: paper
captures:
  - retrieved: 2026-09-24T08:33:08Z
    sha256: "bcc9fdbf29ee37ce36c6e129354c17248a994ae2fb6625f66f846a6bdbfd4361"
    type: text/html
---

## Overview

Faysse and colleagues introduce a page-image multi-vector retriever and ViDoRe v1, a page-level benchmark spanning scientific figures, infographics, tables, and other documents. The study compares end-to-end retrieval pipelines, including OCR and proprietary-model descriptions of visual elements, on nDCG@5. It reports indexing latency and embedding footprint under specified hardware and corpus settings. Its released benchmark and documented baselines make it more useful for this question than an isolated model announcement, although the authors also developed ColPali and do not evaluate exact figure localization, answer correctness, or Mermaid conversion. It complements the harder [ViDoRe v2 study](../vidore-two-study/) and the wiki's [PDF structure extraction](../../concepts/scientific-pdf-structure-extraction/) account: a relevant page still needs a grounded figure reference.


## Key points

- ViDoRe v1 ranks document pages; arXiVQA uses scientific figures and InfoVQA infographics, but the gold unit is a page, not a figure box (section 3.1 and Table 1).
- A Claude-3 Sonnet description of visual elements plus Unstructured and BGE-M3 scores 67.0 average nDCG@5, including 35.7 on ArxivQ; ColPali scores 81.3 and 79.1 respectively. Text-only averages are unavailable for visual-only tasks (Table 2 and section 3.2).
- ColPali maps page-image patches to 128-dimensional vectors and sums query-token maximum similarities; this is a page score, not a validated figure localization (section 4, Late Interaction).
- The measured L4 indexing path takes 7.22 seconds/page for the Unstructured captioning baseline versus 0.39 seconds/page for ColPali, under the study's settings; it is not a general hosted API quote (appendix B.4, Table 5).
- The float16 ColPali index averages 257.5 KB/page on DocVQA versus 8.60 KB/page for BGE-M3 and 1.56 +/- 0.51 KB/page for sparse BM25; compression changes the tradeoff (appendix B.3, Table 4).
- Token pooling to one third of image vectors retained 97.8% of baseline performance in its reported experiment, with text-dense Shift an outlier (section 5.2, Token pooling).
