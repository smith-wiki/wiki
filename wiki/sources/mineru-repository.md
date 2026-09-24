---
title: "MinerU repository and current license"
summary: "MinerU 4 documents local Mac model tiers and structured Markdown export under an Apache-derived license with added commercial terms."
url: https://raw.githubusercontent.com/opendatalab/MinerU/9227669985a7876abe5d3181b1cda11a844e7322/README.md
author: "MinerU Team"
kind: repository
captures:
  - retrieved: 2026-09-24T08:11:27Z
    sha256: "69c967e98536be101b5dc3420703d28cc1e0250eeca3b5bf156b060ac4ccfacb"
    type: text/plain
  - retrieved: 2026-09-24T08:13:05Z
    sha256: "2d9aeb5d15159329a20dd804f251c64860ba954fbd26ec02f802220e6d71cf5c"
    type: text/plain
    url: https://raw.githubusercontent.com/opendatalab/MinerU/9227669985a7876abe5d3181b1cda11a844e7322/LICENSE.md
---

## Overview

The pinned MinerU README documents its current document-parsing product, quality tiers, output formats, local dependencies, and Apple Silicon recommendations. Its paired pinned `LICENSE.md` is essential: the present MinerU Open Source License adds commercial thresholds and attribution conditions to Apache-2.0, so calling the current distribution simply Apache or AGPL would be misleading. The authors present model and memory estimates for ONNX CPU, Torch/MPS, and llama.cpp modes; these are requirements or recommendations, not measured local speed. This is first-party deployment evidence for MinerU 4, not proof that [older MinerU releases scored in olmOCR-Bench](../olmocr-two-study/) or [OmniDocBench](../omnidocbench-repository/) will perform identically. The output contract should preserve structured results as well as Markdown where traceability matters.

## Key points

- MinerU 4 advertises ordered document content and Markdown among multiple output formats, with model tiers that change the OCR/layout/VLM path. ("Features"; "Overview")
- Its Apple Silicon recommendation is the `standard` tier with PyTorch plus llama.cpp; smaller ONNX models can run on CPU, and model bundles require additional memory/downloads. ("Install"; "Hardware and engine selection")
- The pinned license permits commercial use below 100 million monthly active users and USD 20 million monthly revenue, requires visible attribution for third-party online services, and requires a separate license above either threshold. (`LICENSE.md`, sections 1-3)
- Repository licensing does not establish the licenses of all separately downloaded model bundles. ("Model engines"; `LICENSE.md`)
