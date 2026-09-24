---
title: "Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models"
summary: Late chunking encodes long documents before pooling preselected spans, improving average BEIR document retrieval but not every task or chunk size.
url: https://arxiv.org/html/2409.04701
author: Michael Guenther, Isabelle Mohr, Daniel James Williams, Bo Wang, and Han Xiao
published: 2025-07-07
kind: paper
captures:
  - retrieved: 2026-09-24T09:00:08Z
    sha256: "6f4a9dbe1b74c6a8658e5beb01e510444a3eb92ba051885707ffe7ab4156b771"
    type: text/html
---

## Overview

This Jina AI paper introduces late chunking: choose text boundaries as usual, run the document through a long-context embedding transformer, then pool contextual token states within each chosen span. Its third arXiv version reports document-level retrieval across four BEIR datasets and three embedding models, with fixed, five-sentence, and semantic-sentence boundaries. The controlled naive-versus-late comparison shows a modest average gain, not a replacement for boundary selection. Long-document experiments describe overlapping macro-windows where a model cannot encode the whole source. The work is first-party, with method and dataset details, but its principal nDCG is calculated after collapsing chunk hits to documents; it does not establish passage localization in a mixed PDF/web/code corpus. Its single fictional comparison to generated prefixes is not a head-to-head benchmark; see [scientific PDF structure extraction](../../concepts/scientific-pdf-structure-extraction/) for a separate prerequisite.

## Key points

- Boundaries remain inputs; the transformer processes long text before mean pooling the token states within each specified chunk span (Section 3, Algorithm 1).
- Across three models and four BEIR datasets, fixed 256-token naive/late document nDCG@10 averages 52.2/54.0; five-sentence grouping averages 52.4/54.3; semantic-sentence grouping 52.4/53.8 (Section 4.1, Table 2).
- Ranked chunks are mapped back to parent documents, retaining the first occurrence for nDCG; this does not score evidence-span retrieval (Section 4.1, evaluation protocol).
- Some tasks tie or favor naive chunking, and large chunks with unrelated surrounding text can favor naive in reading-comprehension or synthetic needle tests (Sections 4.1-4.2, Table 2 and Figure 3).
- Documents longer than the model window require independently encoded, overlapping macro-windows rather than genuine whole-document context (Section 3.1, Algorithm 2).
- The illustrative comparison with Anthropic-style generated context has only five fictional sentences and cosine similarities, not comparable multi-domain retrieval results (Section 4.5, Table 4).
