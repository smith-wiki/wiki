---
title: "READoc: A Unified Benchmark for Realistic Document Structured Extraction"
summary: "Multi-page PDF-to-Markdown evaluation separates heading hierarchy, formula, table, and reading-order scores on scientific papers."
url: https://arxiv.org/html/2409.05137
author: "Zichao Li and colleagues"
published: 2025-07-13
kind: paper
captures:
  - retrieved: 2026-09-24T08:09:18Z
    sha256: "b367e75c9e29ebd651ad94802ed4f15731f4a3da2fb8341791f0499dc79edf3e"
    type: text/html
---

## Overview

Li and colleagues from the Chinese Academy of Sciences and Ricoh propose READoc, an evaluation of complete PDF documents converted to structured Markdown. Its arXiv subset is directly relevant to scientific PDFs: the paper reports separate measures for text, heading trees, embedded and isolated formulas, tables, and reading order. The authors supply both the corpus-construction procedure and parser results, providing a useful complement to the page-level [olmOCR-Bench](../olmocr-bench-dataset/) and [OmniDocBench](../omnidocbench-study/). Its ground truth is automatically derived from available LaTeX sources, however, and filters out failed conversions; the parser versions in Table 3 are not pinned to releases. It neither independently scores code fences nor verifies figure-caption association. Treat its scores as a dated experimental snapshot, not performance of current parser releases.

## Key points

- The 3,576-document corpus includes 1,009 arXiv papers averaging 11.67 pages; that subset requires source LaTeX, successful LaTeXML conversion, and valid generated tables. (Section 4, "Benchmark Construction"; Section 4.1, "READoc-arXiv")
- Its scoring splits headings into text and hierarchy measures, formulas into embedded and isolated measures, tables into text and tree similarity, and reading order into block- and token-level similarity. All Table 3 measures are higher-is-better. (Section 5, "Evaluation S3uite"; Table 3)
- On READoc-arXiv, MinerU scores 73.07 average with heading-tree 41.97, embedded/isolated formula 62.77/70.76, table-tree 52.85, and block/token order 98.52/97.90; Marker averages 64.98, Docling 58.83, and PyMuPDF4LLM 40.55. (Table 3)
- Marker reaches 72.36 table-tree but only 3.47 embedded-formula similarity; Docling's embedded/isolated formula results are 0.23/0.00. These historical results expose component tradeoffs that aggregate scores conceal. (Table 3)
- Standardization removes images and link syntax, while segmentation identifies headings, formulas, tables, and residual text; neither code-block formatting nor figure-caption association has a dedicated score. (Sections 5.1-5.3)
