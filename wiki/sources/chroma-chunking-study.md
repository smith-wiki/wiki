---
title: "Evaluating Chunking Strategies for Retrieval"
summary: Synthetic query-to-excerpt retrieval comparison of recursive, token, semantic, cluster, and GPT-4o chunking with token-coverage and efficiency metrics.
url: https://www.trychroma.com/research/evaluating-chunking
author: Brandon Smith and Anton Troynikov
kind: webpage
captures:
  - retrieved: 2026-09-24T08:59:25Z
    sha256: "364da998f61b48d886812662cd2aa5106785c9c3f43609a9cf7e54b793937d7b"
    type: text/html
---

## Overview

This July 2024 Chroma technical report asks whether chunk boundary strategies change how well an embedding retriever finds exact evidence excerpts, rather than whole relevant documents. Smith and Troynikov construct queries and matched excerpts with GPT-4-Turbo over five small corpora, then compare recursive, token, sentence-semantic, clustering, and GPT-4o splitting with two embedders. Its practical contribution is measuring retrieved evidence coverage against the volume of irrelevant and duplicated text. The report is a useful boundary-and-budget comparison, not a mixed web/PDF/code benchmark: questions and gold spans are synthetic, the primary embedder also filters examples, and indexing time is not measured. Its appendix and summary even disagree on the top-five leader, limiting the strength of any winner claim. Compare the sentence-semantic results with Qu et al.; [PDF structure extraction](../../concepts/scientific-pdf-structure-extraction/) is outside its tested scope.

## Key points

- Five corpora contain 472 queries by the corpus table, while an example caption says 474; examples are generated with GPT-4-Turbo, filtered for exact excerpt matches and embedding similarity, and do not exhaust all relevant passages (Dataset Generation; Chunking Evaluation Dataset > Corpora and Generation & Prefiltering).
- The report defines evidence-position recall, precision, and intersection-over-union; retrieved overlaps add duplicate material to the precision denominator (Evaluating Retrieval for AI Applications > Metrics).
- At five chunks with `text-embedding-3-large`, recursive 400/0 reaches 89.5% recall and 3.6% IoU; recursive 200/0 reaches 88.1% and 6.9%; cluster 200/0 reaches 87.3% and 8.0% (Results, main table).
- GPT-4o splitting reaches 91.9% recall in the main table, but the appendix's all-corpora table instead gives cluster 400/0 92.1% and GPT-4o 91.7%; neither is a reliable universal winner (Results; Appendices > All Results).
- On `all-MiniLM-L6-v2`, token splitting 250/125 has the best listed recall, 82.4%, while cluster 200/0 has the best IoU, 7.2%; model and objective change the ranking (Results, second table).
- Reported sizes and overlap change the amount retrieved at a fixed five chunks; the authors exclude chunker runtime and note LLM splitting may take tens of minutes (Chunking Algorithms; Results; Limitations).
