---
title: "WCXB: A Multi-Type Web Content Extraction Benchmark"
summary: Modern multi-page-type main-text benchmark exposes the gap between article and non-article extraction.
url: https://arxiv.org/html/2605.21097
author: Murrough Foley
published: 2026-05-20
kind: paper
captures:
  - retrieved: 2026-09-24T07:42:38Z
    sha256: "56f180da504aef43a88ff96be7543ca8f8991cc2a94c896d511b070a682d39f0"
    type: text/html
---

## Overview

Foley introduces a 2,008-page benchmark drawn from 1,613 domains across seven page types, with held-out test pages and per-type results. Its modern HTML and broader page mix improve on article-only evaluations. The author also developed rs-trafilatura, a strong entry in the comparison; development-set tuning and one-person review of model-assisted ground truth constrain independence. Its bag-of-words score measures which text was recovered or wrongly included, not token order or Markdown structure. The separate [WebMainBench structured subset](../webmainbench-structure-study/) tests some of the representation questions that WCXB does not. Static captured HTML also makes WCXB an unsuitable direct measure of JavaScript-rendering reliability.

## Key points
- The set has 1,497 development and 511 held-out pages spanning article, forum, product, collection, listing, documentation, and service types. (Sections 4.1 and 4.5)
- On development pages Trafilatura has F1 0.791 and Readability 0.674; on held-out pages they reach 0.841 and 0.736 respectively. (Tables 5 and 8)
- Trafilatura scores 0.924 on articles but 0.575 on forums, 0.562 on products, 0.518 on collections, and 0.550 on listings in the development split. (Table 7)
- Scores use normalized bag-of-words precision and recall, not table, code, equation, or image fidelity. The author developed one of the compared systems and the truth was model-assisted with human review. (Sections 4.3-4.4, 6.1, and 8)
