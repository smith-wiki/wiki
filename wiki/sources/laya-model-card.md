---
title: Laya model card
summary: ConvAI's published Laya checkpoint metadata, intended use, benchmark claims, and disclosed constraints.
url: https://huggingface.co/convaiinnovations/laya/raw/main/README.md
author: ConvAI Innovations
kind: documentation
retrieved: 2026-09-23T12:55:13Z
sha256: "65f2960bb1aba9e1764d4e8c45e9843e69dc4c3c4878b2b55baa2fdad49a0ed1"
---

## Overview

ConvAI Innovations' Hugging Face model card documents the published [Laya](../../entities/laya/) family and links its weights and Python implementation. It is the most direct first-party description of the downloadable checkpoints, Apache-2.0 license metadata, typed request format, language router, and intended deployment. Written for prospective model users, it gives example predictions and extensive benchmark tables. Those tables use the company's own runs for Laya and import other authors' Jev numbers, so the apparent ranking is not a matched-input trial. The card usefully discloses that its strongest typed-decisions result comes from fine-tuning on that task's training set, and that calibration requires held-out domain data. License metadata and repository code support the ability to self-host; operational cost is not zero.

## Key points

- Card metadata declares Apache-2.0 and names the three published checkpoints with English, multilingual, and specialized roles. (YAML front matter; "What's new"; "Architecture")
- The recommended `Router` detects scripts/languages before model selection; an English checkpoint can be confidently wrong on other scripts. ("Quickstart: Route Mode"; "Why Route")
- Local `laya-serve` offers a Jev-shaped endpoint; absent `LAYA_API_KEY`, the documented default binds publicly without authentication. ("Self-hosting: Jev-compatible HTTP server")
- The Laya-Jev table explicitly says Jev was not measured in the same run and that prompts and sample sizes differ. ("Laya (with routing) vs TypeSafe Jev")
- Its 0.766 typed-decisions result is for a specialized fine-tuned checkpoint, while base checkpoints are near chance and below the majority-class baseline. ("typed-decisions"; "Honest Limits")
- The card identifies high-option choice budgets and raw versus post-fit ECE as limits on unqualified "fast and calibrated" claims. ("Where Jev leads"; "Honest Limits")
