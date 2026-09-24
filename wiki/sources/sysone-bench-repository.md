---
title: sysone-bench head-to-head repository
summary: Independent paired-input Laya-Jev runs and reproducible comparisons with small-suite and hardware limits.
url: https://raw.githubusercontent.com/instax-dutta/sysone-bench/1ac3650a65e3783ac9615f26b02bc7c1d5ad3b23/README.md
author: instax-dutta
kind: repository
retrieved: 2026-09-23T12:52:52Z
sha256: "1af63fa865685ef50618fb22b155db226668fed42a55601be11373ca15cec2aa"
---

## Overview

The independent sysone-bench project compares [Laya](../../entities/laya/) and [Jev](../../entities/jev/) through one harness, storing runs and publicly available comparison code. It targets developers who need stronger evidence than cross-vendor tables. Its v2 README calls the run "751 states"; the captured JSON contains 541 states and 751 decisions across nine suites. Its earlier REPORT covers only the initial curated suites. The code verifies question hashes but not state hashes, and Laya weights are not revision-pinned. Laya ran locally on an M2 CPU and Jev over an API, so latency is not a controlled model-speed comparison. Curated labels come from one author and public subsets are small. This is useful evidence for sampled tasks, not a universal ranking.

## Key points

- The harness sends shared states and question dictionaries, but hashes only questions; Jev is pinned to `jev-1.13.0`, whereas the Laya weights are not revision-pinned. (`run.py`, `question_hash` and `main`; `compare.py`, `main`; `README.md`, "Fairness rules")
- **Contradiction:** the README calls the v2 run "751 states," while its comparison JSON totals 541 states and 751 decisions. (`README.md`, "Results"; `results/compare_laya-router_vs_jev-1.13.0.json`, `suites.*.a.states` and `decisions`)
- In v2, Jev leads on curated triage, guardrails, moderation, twelve-way banking intents, ordinal SST-5, and a five-language sample; Laya wins AG News and MNLI; emotion is close. (`README.md`, "Results", v2 table)
- The v3 Router run lifts multilingual intent from 0.360 to 0.840 versus Jev's 1.000, while only 15 of 590 calls route multilingual in the recorded setup. (`README.md`, "v3")
- At a confidence threshold of 0.85, 58% of Laya decisions reach 0.878 accuracy, versus 78% at 0.917 for Jev; coverage is per decision, not per request. (`README.md`, "Results"; `run.py`, `main`, `gating`)
- The earlier three-suite report finds 0.800 versus 0.894 on triage and 0.833 versus 0.989 on moderation; it is not the nine-suite v2 run. (`REPORT.md`, "Headline", "Limits")
- Local M2 CPU versus hosted API latency is not a model-speed comparison; the reported API token usage counts public suites but omits curated, warmup, and speed calls. (`README.md`, "Results"; `REPORT.md`, "Latency and cost"; `run.py`, `main`, `TrackUsage`)
