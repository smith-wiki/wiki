---
title: "jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval"
summary: Jina v4 paper documents dense and late-interaction embeddings and visual retrieval results with a metric-label conflict.
url: https://arxiv.org/html/2506.18902
author: Michael Gunther, Saba Sturua, Mohammad Kalim Akram, Isabelle Mohr, Andrei Ungureanu, Bo Wang, Sedigheh Eslami, Scott Martens, Maximilian Werk, Nan Wang, and Han Xiao
published: 2025-07-07
kind: paper
captures:
  - retrieved: 2026-09-24T08:37:09Z
    sha256: "4b41c6a9fcb21ed8e8634dba3b93f2c8fa37766e75f77f8bedc75834883eee66"
    type: text/html
---

## Overview

Gunther and colleagues present Jina Embeddings v4, a 3.8-billion-parameter Qwen2.5-VL-derived model with task adapters and either one dense vector or token-level late-interaction output. They introduce Jina-VDR, extending visual document tests beyond questions to descriptions, maps, charts, and multilingual screenshots. The paper is primary evidence for architecture and its own evaluation, but its ViDoRe metric cutoff conflicts between the main comparison and appendix; published averages should not be ranked against other authors' scores without reconciliation. It complements [ColPali's page retrieval study](../colpali-study/) and [ViDoRe v3's independent page and grounding evaluation](../vidore-three-study/). Neither its reported image ranking nor its token-level matches identify a verified source figure box.


## Key points

- The model offers one 2048-dimensional vector truncatable to 128 or variable-length 128-dimensional token vectors scored by late interaction; text and image share a 3.8B-parameter backbone (section 4, Table 1).
- In its own ViDoRe table Jina v4 reports 84.11 dense and 90.17 late, while Jina-VDR reports 73.98 and 80.55. Main-table notes call them nDCG@5, whereas Appendix Table A3 calls ViDoRe nDCG@10; cutoff is unresolved (section 7, Table 3; appendix Table A3).
- Jina-VDR incorporates ViDoRe and 30 added tests spanning maps, diagrams, charts, and multilingual image/screenshot retrieval; this still scores whole images, not source-localized regions (section 6).
- Per-token late-interaction output varies in length with image/text tokenization, whereas a dense index is one vector per item; published benchmark scores do not include equivalent total indexing and query cost (sections 3-4, 7).
