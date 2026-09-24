---
title: "Is Semantic Chunking Worth the Computational Cost?"
summary: Controlled sentence-grouping comparison finds no consistent retrieval benefit for semantic boundaries over simple fixed groups on unstitched documents.
url: https://arxiv.org/html/2410.13070
author: Renyi Qu, Forrest Bao, and Ruixuan Tu
published: 2024-10-16
kind: paper
captures:
  - retrieved: 2026-09-24T08:59:44Z
    sha256: "5a5c4a10897694fcd84d3acb9d3c2a55bfd1b2d79a073974d95e11d79b06c1ab"
    type: text/html
---

## Overview

Qu, Bao, and Tu compare fixed-size sentence groups with embedding-distance breakpoints and sentence clustering on document retrieval, evidence retrieval, and answer generation. Their October 2024 preprint spans both original long documents and artificially stitched collections, using several embedding models and a sentence-based evaluation. Fixed grouping is competitive or better on the original-document datasets; semantic boundaries can benefit unusually mixed-topic stitched documents. This is valuable counterevidence to blanket claims that a semantic splitter beats a simple baseline. It is not a recursive-token or software-code benchmark. Hyperparameters are selected per dataset from the evaluated queries, and the title's computational-cost concern is not accompanied by measured latency, resource, or dollar comparisons. Chroma's different synthetic-query and span-level protocol cannot be numerically combined with this paper's F1 scores, nor does it validate [scientific PDF extraction](../../concepts/scientific-pdf-structure-extraction/).

## Key points

- Every input is first split into sentences; the fixed baseline groups consecutive sentences, while breakpoint and clustering methods use sentence embeddings (Sections 2 and 3; Appendix B).
- Fixed grouping leads on all four original document-retrieval datasets at F1@5; breakpoint gains on stitched MIRACL and NQ are 69.45 to 81.89 and 43.79 to 63.93 respectively, in high-topic-diversity synthetic composites (Section 4.2, Table 1).
- Fixed grouping leads on three of five evidence-retrieval datasets, with small differences on most rows; semantic methods do not consistently improve evidence F1@5 (Section 4.3, Table 2).
- Top-five answer-generation BERTScores differ by at most 0.01 across the three methods in the five reported datasets (Section 4.4, Table 3).
- Source-document and gold-evidence-sentence labels are used instead of independent chunk-level relevance judgments; displayed chunker settings maximize F1 over tested k on each dataset (Sections 3.1-3.3 and 4.1).
- The study discusses added computation but reports no controlled wall time, hardware, indexing tokens, or cost measurements; its cost-benefit conclusion is qualitative (Sections 3-5).
