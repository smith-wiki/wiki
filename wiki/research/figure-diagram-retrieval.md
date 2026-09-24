---
title: How should figures and diagrams in PDFs and web pages be made searchable and citable?
rkey: figure-diagram-retrieval
date: 2026-09-24
brief: Index original page and figure images alongside authored captions and optional generated descriptions; cite verified source crops, not embeddings or Mermaid.
turn_url: https://github.com/smith-wiki/wiki/issues/105
mode: QUESTION_ANSWER
---

## Answer

**Use a hybrid index:** render PDF pages or captured web pages for broad visual recall, extract source-linked figure crops for figure search, and index author captions and nearby text. VLM prose can add search terms; Mermaid is an optional, lossy generated annotation, not evidence or a tested retrieval winner. Retain the original visual and verify its caption and source box before citing it ([visual evidence retrieval](../../concepts/visual-evidence-retrieval/); [page relevance is not figure provenance](../../notes/page-retrieval-does-not-localize-a-figure/)).

ColPali beats a specific captioning pipeline on **ViDoRe v1 page nDCG@5**, while ArXivDoc's scientific whole-paper figure queries favor source text plus captions over page images. Neither score proves exact figure citation. ViDoRe v2/v3 differ in tasks and metric; Jina v4, Cohere Embed v4, Voyage multimodal-3.5, and ColQwen have different index, query, and service costs, not one interchangeable leaderboard ([comparisons and costs](../../concepts/visual-evidence-retrieval/)).

Cite the immutable PDF hash, page, verified crop coordinates and caption, or the web capture, figure fragment/asset, and authored caption. Keep generated descriptions separate from source text ([PDF structure](../../concepts/scientific-pdf-structure-extraction/); [web capture fidelity](../../concepts/web-capture-fidelity/)).
