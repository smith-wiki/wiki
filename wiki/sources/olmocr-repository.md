---
title: "olmOCR repository: deployment and Markdown output"
summary: "olmOCR's official pipeline supports local NVIDIA/CUDA or remote inference, not a documented Apple Silicon backend."
url: https://raw.githubusercontent.com/allenai/olmocr/f7cfe4c22098b154c76b6ec950d1c0a464eecf8d/README.md
author: "Allen Institute for AI"
kind: repository
captures:
  - retrieved: 2026-09-24T08:11:50Z
    sha256: "1383b3f0f5a10cc9a7eebab46e929cddaedf370a80d17b379d21dc380b31ada3"
    type: text/plain
---

## Overview

The Allen Institute for AI's pinned olmOCR README describes the released pipeline and its intended reading-order, mathematical, and table behavior for PDF-to-Markdown conversion. It also states specific hardware for local GPU inference: recent NVIDIA cards, CUDA package installation, and at least 12 GB of GPU RAM. An OpenAI-compatible remote inference server can perform the model work elsewhere, but that does not constitute Apple-local execution. Unlike a rich document-tree parser, the primary result is linear Markdown, with no promised figure-caption relationship or standalone code-block guarantee in this overview. The code is Apache-2.0; the [olmOCR 2 paper](../olmocr-two-study/) and model card identify weights separately. The README is first-party operational guidance, not an independent cross-parser benchmark.

## Key points

- It targets clean Markdown with natural reading order, equations, tables, and complex formatting, suppressing headers and footers. ("Features")
- Official local-GPU requirements name NVIDIA devices, CUDA wheels, and at least 12 GB GPU RAM; a remote OpenAI-compatible server is the documented alternative. ("Installation"; "Use Remote Inference Server")
- The repository code is Apache-2.0; its latest named olmOCR 2 release is v0.4.0. ("License"; "News")
