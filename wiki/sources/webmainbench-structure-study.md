---
title: "AICC: Parse HTML Finer, Make Models Better"
summary: WebMainBench's 545-page subset measures code, formula, and table fidelity separately from main-text overlap.
url: https://arxiv.org/html/2511.16397
author: Ren Ma et al.
published: 2025-11-26
kind: paper
captures:
  - retrieved: 2026-09-24T07:42:14Z
    sha256: "c42bbc88e6810ad5ab163a3ab4114328427794fcdb3fe8c30af140447b4883be"
    type: text/html
---

## Overview

Ma and colleagues describe a model-based HTML parser and publish WebMainBench with a 545-page subset annotated for code, mathematical formulas, and tables. Unlike text-only extraction studies, the subset tests representation fidelity with character-edit and table-tree metrics. It reports weak structural preservation for Trafilatura despite strong main-text extraction in other benchmarks. The paper is also an evaluation by the authors of the best-performing system, MinerU-HTML, and evaluates complete extraction/conversion paths rather than isolating the Markdown serializer. It does not score image URL retention or the association of figures with captions, so an archive still needs its own checks for those materials. The [WCXB benchmark](../wcxb-content-extraction-benchmark/) answers the distinct main-content boundary question.

## Key points
- WebMainBench-Structured contains 545 pages: 257 with formulas, 127 with code, and 179 with tables. (Section 3.1.3, Table 5)
- Formula and code fidelity use normalized Levenshtein string similarity; table structure uses TEDS tree similarity. (Section 3.2.1)
- Trafilatura scores 0.1305 for code, 0.6107 for formulas, and 0.3405 table TEDS; the authors' MinerU-HTML scores 0.9093, 0.9399, and 0.7388 respectively. (Section 3.3, Table 2)
- Figures and their captions have no dedicated fidelity measure in this reported subset. (Sections 3.1.3 and 3.2.1)
