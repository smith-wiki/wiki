---
title: "OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations"
summary: "The original 981-page benchmark separates text, display-formula, table, and reading-order metrics and excludes captions from scores."
url: https://arxiv.org/html/2412.07626
author: "Linke Ouyang and colleagues"
published: 2025-03-25
kind: paper
captures:
  - retrieved: 2026-09-24T08:04:38Z
    sha256: "fb3cc9890bf0abce518d5916267fca9fa4700c0a29d92e3bed6eb4fb3e20523c"
    type: text/html
---

## Overview

Ouyang and colleagues at Shanghai AI Laboratory and partner organizations introduce OmniDocBench for researchers comparing PDF parsing systems across academic papers, textbooks, and other layouts. This paper documents the original 981-page release, its annotation scheme, extraction and matching methods, and tool-version-specific results. Its methodology is more informative for technical-document components than a single aggregate OCR score. It is a primary benchmark paper, but its authors' project also maintains the MinerU parser, and its reported parser versions are old. Captions receive annotations yet are excluded from the main scoring; code blocks and inline formulas are normalized into text rather than separately tested. The [living repository](../omnidocbench-repository/) now describes a larger, differently scored release, so its leaderboard is not numerically interchangeable with this paper.

## Key points

- The original release covers 981 PDF pages in nine types, including academic papers, with block, span, and reading-order annotations. (Section 3.3, "Dataset Statistics")
- Its Markdown evaluation extracts tables and display formulas, folds code blocks into text, and converts inline formulas to Unicode within text rather than separately scoring them. (Section 4.1, "Extraction")
- Figure, table, and footnote captions participate in matching but are excluded from metric calculation because their placements vary across parsers. (Section 4.2, "Ignore Handling")
- The original English results give MinerU 0.9.3 a formula CDM of 57.3, table TEDS of 78.6, and reading-order edit distance of 0.079; Marker 1.2.3 scores 17.6, 67.6, and 0.114 respectively. These lower-is-better edit and higher-is-better recognition measures must retain their versions. (Table 2; Section V, "More Details on Methods")
