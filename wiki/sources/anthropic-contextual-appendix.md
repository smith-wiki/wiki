---
title: "Contextual Retrieval Appendix II"
summary: Anthropic's supplementary top-k plots and example gold chunks show domain slices of contextual retrieval without exposing a complete reusable benchmark.
url: https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf
author: Anthropic
kind: paper
captures:
  - retrieved: 2026-09-24T09:03:22Z
    sha256: "24d4a563ebaa787ed82697d08642c0c216cdfc35e47e2c62aabc5926bc8b3a88"
    type: application/pdf
---

## Overview

This appendix supplements Anthropic's Contextual Retrieval engineering post with plots broken out by domain, embedding provider, retrieval depth, lexical fusion, and reranking, plus representative question, answer, gold chunk, and generated-context examples. It is useful for seeing that the headline aggregate masks different codebase, fiction, and paper query types. Its gold code snippets also illustrate why a file path, symbol, and surrounding context can distinguish otherwise ambiguous source passages. The material comes from the same team that designed the method, not an independent replication. It does not disclose the full collection, query and corpus counts, extraction configuration, or uncertainty intervals; plots in the available Markdown capture do not yield all numeric cells. Interpret it alongside the main post and the separate [web capture fidelity](../../concepts/web-capture-fidelity/) concern, not as a standalone reproducible quality ranking.

## Key points

- The supplement includes 1-minus-recall plots for retrieval at 20, 10, and 5, plus NDCG plots across domains and embedding providers (Full breakdown of experiment results).
- Its examples show separate ordinary and vague codebase questions, fiction, arXiv, and science-paper passages with gold snippets and generated context (Codebases; Codebases with Vague Questions; later examples).
- The BasicConfigurator example grounds a code query in a concrete C++ function body, while the context supplies project and class identity; this is an illustrative example, not a measured benefit of syntax-aware chunk boundaries (Codebases).
- The supplement supplies neither an independently runnable labeled corpus nor per-domain confidence intervals; the plotted results should not be used to infer passage-level superiority over other chunkers (Full breakdown of experiment results).
