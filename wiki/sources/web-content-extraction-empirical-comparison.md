---
title: An Empirical Comparison of Web Content Extraction Algorithms
summary: Eight-dataset reproducibility study comparing main-text extraction, not Markdown structural fidelity.
url: https://downloads.webis.de/publications/papers/bevendorff_2023c.pdf
author: Janek Bevendorff, Sanket Gupta, Johannes Kiesel, and Benno Stein
published: 2023-07-23
kind: paper
captures:
  - retrieved: 2026-09-24T07:39:12Z
    sha256: "af91f46f5b7478bd9dddacd3fe04b04dc43e4a82d2fe16f1e027196412e406e8"
    type: application/pdf
---

## Overview

Bevendorff and colleagues consolidate eight human-labeled web-content datasets and compare fourteen extraction systems under a common text-based evaluation. This SIGIR 2023 study is stronger comparative evidence than a tool vendor's own benchmark because it includes diverse page sets and releases a reproducible method. It is still not a test of archival fidelity: the authors reduce structural ground truth to plain text and compare word sequences, so correctly preserved table cells, code formatting, math, image references, and captions cannot be inferred from its scores. Its Readability entry is a Python reimplementation, not necessarily Mozilla's current JavaScript release. The corpus includes older snapshots and some flawed annotations; dynamically loaded content absent from source HTML limits direct conclusions about browser rendering.

The archival implication is explored in [main-content accuracy does not measure archive fidelity](../../notes/main-content-accuracy-does-not-measure-archive-fidelity/).

## Key points
- Eight public datasets include CleanEval (738), CETD (700), Dragnet (1,379), Readability (115), and Scrapinghub (181) pages; some ground-truth errors and JavaScript-only content required caution. (Sections 3.1-3.2)
- The authors turn all ground truth into plain text and score word-order agreement with ROUGE-LSum F1, not structural Markdown fidelity. (Sections 3.2 and 4.3)
- Trafilatura has the strongest individual macro-mean F1, 0.883; Readability has the highest macro-median F1, 0.970, with smaller spread. (Section 4.4, Table 3 and discussion)
- The paper uses a Python reimplementation of Readability; it does not compare Firecrawl, Defuddle, Jina Reader, Crawl4AI, or Cloudflare's conversion. (Sections 4.1-4.2)
