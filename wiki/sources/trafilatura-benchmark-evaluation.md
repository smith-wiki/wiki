---
title: "Benchmarks and evaluation"
summary: Trafilatura's own 2026 segment-label benchmark contrasts extraction precision and recall on 990 documents.
url: https://trafilatura.readthedocs.io/en/latest/evaluation.html
author: Trafilatura project
publisher: "Trafilatura"
kind: webpage
captures:
  - retrieved: 2026-09-24T07:38:05Z
    sha256: "fb4da39214b4756c625c7e504be1252d07df753f37300dc5986eb4b52ac0ce5b"
    type: text/html
---

## Overview

The Trafilatura project's evaluation page documents its own benchmark methodology, competitors, historical results, and reproduction script. Its August 2026 snapshot reports precision, recall, and F-score on labeled text and boilerplate segments from 990 mostly article-like documents. The comparison is useful for current package versions and for observing the precision-recall tradeoff, but it is vendor-run and uses readability-lxml rather than Mozilla Readability.js. Some input strings are decoded by the test harness, whereas other tools receive raw bytes. The labels measure whether text belongs to a page's main content, not whether Markdown preserves tables, executable code, equations, figures, or captions. For an independent cross-dataset perspective, see [Bevendorff and colleagues' comparison](../web-content-extraction-empirical-comparison/).

## Key points
- The August 2026 set has 990 documents with 2,951 text and 2,966 boilerplate segments, mostly articles with some lists or tables and multilingual examples. (Description; Results 2026-08-04)
- Trafilatura 2.2.0 standard records precision 0.906, recall 0.943, and F-score 0.924; readability-lxml 0.8.4.1 scores 0.898, 0.764, and 0.826. (Results 2026-08-04)
- The compared Readability variant is readability-lxml, not Mozilla Readability.js; input preprocessing differs between packages. (Alternatives; Results 2026-08-04)
- The method evaluates text and boilerplate labels rather than structural features, and results come from the Trafilatura project itself. (Description; Results 2026-08-04)
