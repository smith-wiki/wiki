---
title: "Document-as-Image Representations Fall Short for Scientific Retrieval"
summary: ArXivDoc compares source-text, caption-augmented, figure, page-image, and interleaved retrieval over scientific papers.
url: https://arxiv.org/html/2604.18508v1
author: Ghazal Khalighinejad, Raghuveer Thirukovalluru, Alexander H. Oh, and Bhuwan Dhingra
published: 2026-04-20
kind: paper
captures:
  - retrieved: 2026-09-24T08:35:54Z
    sha256: "b7eed5b063ee4e31d12fd24cf323771f4d1a67a250bf91d6067f7cba8cb42ab4"
    type: text/html
---

## Overview

Khalighinejad and colleagues introduce ArXivDoc, a retrieval benchmark of 8,210 scientific papers and 547 manually checked queries grounded in figures, tables, or text. They derive alternative representations from original LaTeX, then compare single- and multi-vector models on whole-document nDCG@10 and index size. Its controlled figure/text comparisons are a useful counterpoint to page-image-first readings of [ColPali](../colpali-study/) and to the wiki's [scientific PDF structure extraction](../../concepts/scientific-pdf-structure-extraction/). The authors control their own dataset and hyperparameters; the 100 figure queries and source-LaTeX setting limit transfer to arbitrary scanned PDFs or websites. Crucially, ranking the correct paper does not prove the specific figure or its caption was found or that an answer cited it accurately.


## Key points

- The benchmark contains 8,210 papers, 144,653 pages, and 547 queries: 100 figure, 218 table, and 229 text; queries originate from LaTeX and receive human review (sections 1 and 3).
- In document-level nDCG@10, ColQwen2 v1 reaches 0.90 on figure queries with text plus VLM captions, 0.87 with extracted figures alone, and 0.84 with page images; these are different retrieval units, not figure-citation accuracy (section 4, Table 4).
- Qwen3-Embedding text alone scores 0.76 on figure queries; caption augmentation raises it to 0.80. Captions and surrounding prose can recover evidence that pure image-page ranking misses, under these source-access conditions (section 4, Table 4).
- ColQwen page-image index is 70.56 GB versus 52.10 GB for text plus captions and 49.59 GB for interleaved inputs over this corpus; other model/dimension/resolution choices change footprint (section 4, Table 4).
- The study evaluates whole-paper retrieval on verified, evidence-grounded queries, unlike ViDoRe page retrieval and figure-only ArXivQA; neither task directly certifies figure-box localization (sections 1-2 and 4.1).
