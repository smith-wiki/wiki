---
title: TypeSafe AI model documentation
summary: Official Jev 1.13 API model pricing, limits, customization, language support, and data-handling claims.
url: https://docs.typesafe.ai/models
author: TypeSafe AI
publisher: TypeSafe AI
kind: documentation
captures:
  - retrieved: 2026-09-23T12:58:27Z
    sha256: "3a1e2c0927cae38c2d019a94a61bd0675c4bf4593629b89ad511899efa683253"
    type: text/html
---

## Overview

TypeSafe AI's model-reference page documents [Jev](../../entities/jev/) as a hosted System One decision model. It describes the current versioned ID, metered input pricing, request context and rate limits, model aliases, customization methods, multilingual caveats, and the company's data-handling policy. Written for developers integrating the API, it is authoritative for its published interface and current commercial terms but not independent evidence of accuracy, calibration, or security. The version alias can move without an application change; official language guidance says English performs best and others need evaluation. Unlike the open [Laya](../../entities/laya/) checkpoints, customers cannot fine-tune Jev with their data; they express domain rules in each request. Commercial terms and model behavior may change after the captured date.

## Key points

- Jev 1.13 is `jev-1.13.0`, priced at $0.042 per million input tokens with free output; the endpoint accepts text, objects, or arrays of text. ("Current models")
- Context limits are 64,000 tokens per request and 32,000 for state plus the longest question; questions are evaluated against the state in parallel. ("Current models")
- The `jev-latest` alias moves with releases, so applications calibrating thresholds should pin a versioned ID. ("Aliases")
- Jev does not receive customer-specific fine-tuning or LoRA; customers place rules and reference material in the state and question criteria. ("Customizing Jev")
- English is its best-supported language; other languages, including CJK, are accepted but should be tested on the target workload. ("Language support")
- TypeSafe states customer requests and responses are not used to train Jev; enterprise zero-retention arrangements are documented separately. ("Data handling")
