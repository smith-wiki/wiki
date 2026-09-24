---
title: "olmOCR 2: Unit Test Rewards for Document OCR"
summary: "AI2 reports 82.4 on its English-language olmOCR-Bench for the 7B olmOCR 2 model, with explicit competitor versions and coverage limits."
url: https://arxiv.org/html/2510.19817
author: "Jake Poznanski, Luca Soldaini, and Kyle Lo"
published: 2025-10-22
kind: paper
captures:
  - retrieved: 2026-09-24T08:05:31Z
    sha256: "6e3e3ef0414b75f0e58e65303817ed56e0bad585bb9dc52d374178577de0040f"
    type: text/html
---

## Overview

Poznanski, Soldaini, and Lo at the Allen Institute for AI present olmOCR 2, a seven-billion-parameter vision-language parser trained with synthetic-document unit-test rewards. The paper reports versioned comparisons on the team's English-language olmOCR-Bench, including category scores for mathematical PDFs, multi-column pages, tables, and old scans. It is primary evidence for the specific model and evaluation conditions, not independent proof of universal scientific-document fidelity: its authors created the model and benchmark, competitor versions differ, and the reported metric does not independently measure heading hierarchy, code formatting, or caption linkage. The [benchmark dataset card](../olmocr-bench-dataset/) defines the tests; [OmniDocBench](../omnidocbench-repository/) uses a different corpus and metrics. The paper's license table distinguishes permissive model weights from restricted competing weights and API-only services.

## Key points

- On the authors' latest olmOCR-Bench, olmOCR 2 scores 82.4 +/- 1.1; Marker 1.10.1 scores 76.1 +/- 1.1, MinerU 2.5.4 scores 75.2 +/- 1.1 (self-reported), and Mistral OCR API scores 72.0 +/- 1.1. The initial olmOCR release scores 68.2 in this table, not the historical 77.4 in the older dataset card. (Table 1 and Table 3)
- In the category table, olmOCR 2 scores 84.9 on table tests, 83.7 on multi-column tests, 83.0 on arXiv math, and 47.7 on old scans; individual categories expose failure modes hidden by the aggregate. (Table 3)
- The paper says the 7B model, data, training code, and inference code are released under permissive licenses; its legend marks olmOCR's model license Apache 2.0, contrasted with OpenRAIL-M for Marker, AGPL v3 for MinerU, and API terms for Mistral. (Abstract; Table 1 and legend)
- This study is an evaluation by olmOCR's own authors using an English-language benchmark they develop, and several competitor results marked with an asterisk are reported by those competitors rather than reproduced in-house. (Abstract; Table 1 note)
