---
title: jevbench repository and 500-example comparison
summary: Seeded public-dataset comparison of Jev and Laya with aggregate accuracy and calibration results, but no committed raw predictions.
url: https://raw.githubusercontent.com/dhruvmehra/jevbench/c983cc4a7dd9fc142ca3b6c7a813cae0e963c902/README.md
author: dhruvmehra
kind: repository
retrieved: 2026-09-23T15:02:47Z
sha256: "d421ece0fcf3e1cb178d2a9d6fcd565d8620663a72cbcba90bd380c862f1f114"
---

## Overview

This independently authored repository compares Jev, Laya, and other classifiers on AG News, Banking77, and SST-2. Its author supplies a seeded sample loader, shared label descriptions, a harness, and an aggregate report for 500 examples from each public evaluation split. It is useful as a second, larger comparison alongside [sysone-bench](../sysone-bench-repository/), but its published snapshot does not include the per-example predictions or provider responses that the README says a local run generates. The AG News report includes a separate Jev rerun with changed descriptions but no matching Laya rerun; treat the default row as the comparable one. Neither Laya weights nor the hosted Jev model is pinned to an immutable revision. The [quality comparison](../../notes/laya-and-jev-quality-varies-by-task/) keeps these limits visible.

## Key points

- The loader seeds a shuffle before taking 500 evaluation examples per dataset and defines one label-description map for all zero-shot adapters. (`src/jevbench/datasets.py`, `load` and `DATASETS`; `README.md`, "What is being compared")
- The original AG News report gives Laya 90.6% and Jev 84.3% accuracy; the later Jev-only "new descriptions" row gives 85.8% and is not an unchanged-prompt pairing. (`docs/results/2026-09-22-n500-summary.md`, "agnews")
- On 77-way Banking77, Jev scores 76.4% versus Laya's 38.2%; this is a different option-count regime from sysone-bench's 12-way subset. (`docs/results/2026-09-22-n500-summary.md`, "banking77")
- On binary SST-2, Jev scores 95.4% versus Laya's 92.0%. (`docs/results/2026-09-22-n500-summary.md`, "sst2")
- Accuracy excludes errors; the AG News Jev default row reports 0.4% errors. The published snapshot contains aggregate rows, not the underlying paired predictions. (`README.md`, "What gets measured" and "Run"; `docs/results/2026-09-22-n500-summary.md`, "agnews")
