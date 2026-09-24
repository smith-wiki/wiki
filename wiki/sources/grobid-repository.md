---
title: "GROBID repository: scientific PDF to TEI"
summary: "Scientific-article segmentation and caption/citation extraction produce TEI XML locally on Apple ARM, not Markdown."
url: https://raw.githubusercontent.com/kermitt2/grobid/3a84929734d9ba4218af8138d70fee272085c2e4/Readme.md
author: "Patrice Lopez and GROBID contributors"
kind: repository
captures:
  - retrieved: 2026-09-24T08:12:31Z
    sha256: "f68f61368314599f362c19de029b259fb749c0a1a18a93166957ae122c2073a3"
    type: text/plain
---

## Overview

GROBID's pinned project README introduces a machine-learning parser specializing in scientific and technical publications, producing structured TEI XML with bibliographic metadata, section hierarchy, figures, tables, reference callouts, and captions. This is valuable when scholarly relationships and citations matter more than Markdown as an immediate output: a separate TEI-to-Markdown transform would have to preserve those relationships and be evaluated independently. The README identifies macOS ARM native builds and a CPU-oriented default CRF path, with optional deep-learning models and optional NVIDIA acceleration; its published high-throughput example is on Linux, not Apple hardware. It is first-party feature and deployment evidence, not a result on [olmOCR-Bench](../olmocr-bench-dataset/) or [OmniDocBench](../omnidocbench-study/). The software is Apache-2.0 licensed.

## Key points

- Scientific-article full-text segmentation includes section titles, paragraphs, figures, tables, captions, reference markers, and coordinates in TEI XML. ("Features")
- The project explicitly supports native macOS ARM and defaults to CPU-compatible CRF models; optional NVIDIA GPU improves certain deep-learning paths. ("Requirements"; "Run GROBID")
- Its cited throughput example is on a 16-CPU Linux host, not an Apple Silicon measurement. ("Performance")
- GROBID is Apache-2.0 licensed, with separate documentation and data licenses. ("License")
