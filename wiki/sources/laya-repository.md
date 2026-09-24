---
title: Laya source repository
summary: Pinned ConvAI code and benchmark documentation for typed decisions, routing, training, and limitations.
url: https://raw.githubusercontent.com/NandhaKishorM/laya/010bacef009c855ccba814b51f7c8e1d38ab5e3f/README.md
author: ConvAI Innovations and Laya contributors
kind: repository
retrieved: 2026-09-23T12:51:56Z
sha256: "24971edc9322807240370d0e53d043b0043530aa64a02bb93c9c96ba6d10748d"
---

## Overview

This pinned repository documents the upstream Python implementation of [Laya](../../entities/laya/), its Apache-2.0 license, model-loading and routing interface, inference heads, training code, and benchmark scripts. ConvAI Innovations and contributors address developers who want to self-host or adapt a typed decision model. The captured README and BENCHMARKS files expose both product strengths and limitations, including multilingual routing, choice-option budgets, weak zero-shot transfer on a specialized benchmark, and calibration drift. Code and recorded measurements are more inspectable than a product announcement, but the vendor selected and ran its own workloads; the Jev figures in its benchmark table came from other parties using different prompts. Read this alongside the independent [sysone-bench](../sysone-bench-repository/).

## Key points

- Apache-2.0 Python runtime implements `choice`, `score`, `noul`, three checkpoints, a language `Router`, and a Jev-compatible HTTP endpoint. (`README.md`, "Quickstart", "Self-Hosting", "Architecture")
- The 421M English model uses ModernBERT; the 322M multilingual model uses mmBERT, with question/state context and a shared option-token budget. (`README.md`, "Architecture", "Limits")
- The specialized checkpoint scores 0.766 on typed-decisions after fitting to that benchmark's training split; untuned base checkpoints score 0.361 and 0.342, below the 0.461 majority-class baseline. (`BENCHMARKS.md`, "typed-decisions")
- The 51-language MASSIVE sweep reports 45 of 51 languages above three times random for the multilingual checkpoint, not uniform high accuracy; some calibration figures predate a later temperature clamp. (`BENCHMARKS.md`, "Languages", introduction)
- The T4 runs report 32.8 ms for one short multilingual question; Jev comparisons import published, differently prompted measurements. (`BENCHMARKS.md`, "Speed", introduction)
- Raw ECE on one run falls from 0.466 to 0.081 for English after temperature refitting; out-of-domain calibration cannot be inferred from this. (`BENCHMARKS.md`, "Calibration")
- The README warns about `noul` label bias, multilingual `score` position bias, and an unusable `action.act_probability` signal. (`README.md`, "Limits")
