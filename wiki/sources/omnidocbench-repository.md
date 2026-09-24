---
title: "OmniDocBench repository and v1.6 full leaderboard"
summary: "Pinned repository README defines the 1,651-page v1.6 evaluation and reports MinerU, olmOCR, Mistral, and Marker separately."
url: https://github.com/opendatalab/OmniDocBench
author: "OpenDataLab"
kind: repository
captures:
  - retrieved: 2026-09-24T08:05:49Z
    sha256: "e9953ed9cd4cabd9530015042c841e24e70496c5e15e7ce39af197a84221c022"
    type: text/html
  - retrieved: 2026-09-24T08:06:24Z
    sha256: "a799f3dabee0d8e2be9f990fc325c3fefadb8d7f8d0cf56148406547d495a3ad"
    type: text/plain
    url: https://raw.githubusercontent.com/opendatalab/OmniDocBench/f133a71e9e91c3621c7ce8994200a7b394a06eb3/README.md
---

## Overview

OpenDataLab's OmniDocBench repository supplies annotation and evaluation code, version history, inference scripts, and a public parser leaderboard. The preserved README is pinned to commit `f133a71e9e91c3621c7ce8994200a7b394a06eb3`, avoiding a silently changing main-branch comparison. Its v1.6 full table scores Markdown output against text, formula, and table metrics, with reading-order error shown separately; the aggregate does not include reading order. This is first-party benchmark documentation rather than a neutral independent audit, and the release notes record substantial corpus and metric changes since the [981-page paper](../omnidocbench-study/). The comparison is useful for a same-version snapshot, but does not establish code-fence fidelity or preserved association between captions and figures; tested parser versions must be read from this repository, not assumed current.

## Key points

- The pinned README calls v1.6 a 1,651-page, multi-document-type benchmark; its April 2026 release added 296 difficult pages and changed matching and metric implementation from v1.5. ("Benchmark Introduction"; release notes, 2026/04/10)
- In the v1.6 full leaderboard, the overall value is the mean of normalized text accuracy, table TEDS, and formula CDM; reading-order edit distance is displayed separately and lower is better. ("End-to-End Evaluation")
- MinerU-Pipeline scores 86.47 overall, 83.07 formula CDM, 81.88 table TEDS, and 0.153 reading-order edit; olmOCR scores 85.74, 88.10, 83.00, and 0.216 respectively. ("Comprehensive evaluation of document parsing on OmniDocBench (v1.6_full)")
- Mistral OCR scores 85.66 overall, 89.91 formula CDM, 76.78 table TEDS, and 0.171 reading-order edit; Marker scores 78.44, 85.24, 65.77, and 0.243. ("Comprehensive evaluation of document parsing on OmniDocBench (v1.6_full)")
- Its method-version table identifies MinerU-Pipeline 3.4.0, Marker 1.8.2, and Mistral OCR 2503; the leaderboard lists olmOCR but does not explicitly establish that it is olmOCR 2. ("Model Information")
- The repository recommends its end-to-end evaluation over Markdown-to-Markdown evaluation because the former retains attributes and ignore rules. ("End-to-End Evaluation Method - end2end"; "Markdown-to-Markdown Evaluation - md2md")
