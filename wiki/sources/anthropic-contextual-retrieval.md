---
title: "Introducing Contextual Retrieval"
summary: Anthropic reports lower top-20 retrieval failure after generating document-aware prefixes for each chunk and indexing them with dense and lexical search.
url: https://www.anthropic.com/engineering/contextual-retrieval
author: Daniel Ford
published: 2024-09-19
kind: webpage
captures:
  - retrieved: 2026-09-24T09:00:27Z
    sha256: "a71cd74735b4e65805c871bc53f9bd41c2e24dcdd999709584e01489b2be06a6"
    type: text/html
---

## Overview

Anthropic's engineering post presents Contextual Retrieval for chunks whose isolated text lacks a document title, entity, time frame, or other disambiguating context. A Claude prompt sees the whole source document and each existing chunk, creates a short prefix, and indexes the prefixed text in both vector and BM25 search. Results are averaged across codebases, fiction, and scientific and arXiv papers, with additional reranking experiments. This is first-party deployment evidence for a text-augmentation layer, not a contest among recursive, semantic, and neural boundary algorithms. Its aggregate percentages describe relative reductions in retrieval failures at top 20, not percentage-point gains or answer accuracy. The linked appendix gives examples and plots, but neither artifact supplies a reproducible full dataset, parsing pipeline, or uncertainty estimates for this wiki's mixed corpus. See [web capture fidelity](../../concepts/web-capture-fidelity/) for an upstream issue these results do not test.

## Key points

- Claude 3 Haiku writes a chunk-specific 50-100-token prefix from the whole document and the original chunk; both embedding and BM25 index prefix plus chunk (Introducing Contextual Retrieval; Implementing Contextual Retrieval).
- At top 20 with the leading Gemini Text 004 setup, embedding-only failure falls from 5.7% to 3.7% with contextual embeddings, then 2.9% when contextual BM25 is combined: 35% and 49% relative reductions (Methodology; Performance improvements).
- Reranking the top 150 to 20 with Cohere reduces the reported failure rate to 1.9%, a 67% relative reduction versus the 5.7% reference; this adds query-time work (Further boosting performance; Performance improvements).
- The one-time $1.02 per million source tokens example assumes 800-token chunks, 8,000-token documents, 100-token prefixes, and prompt caching; it excludes a general present-day indexing/search cost measurement (Using Prompt Caching to reduce the costs of Contextual Retrieval).
- Chunk boundaries and embedding models still matter, and the authors suggest evaluating output with the prefix distinguished from original source text (Implementation considerations).
