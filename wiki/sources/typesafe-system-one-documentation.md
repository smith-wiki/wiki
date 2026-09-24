---
title: TypeSafe AI System One guide
summary: Official account of Jev's typed decision interface, without an implementation disclosure.
url: https://docs.typesafe.ai/concepts/system-one
author: TypeSafe AI
publisher: TypeSafe AI
kind: documentation
retrieved: 2026-09-23T14:52:47Z
sha256: "a5deb2f825347ecc1a98b785fbb8423c24e371821fbe6dbc7c04bc150c91a293"
---

## Overview

TypeSafe AI's System One guide explains the public contract of [Jev](../../entities/jev/) for software developers. The model takes text or structured text state plus predefined questions and returns bounded choices, scores, or boolean probabilities rather than prose, so an application can ask several independent questions and combine the answers with deterministic checks. This first-party page is authoritative for the exposed interface. It does not identify Jev's backbone, parameter count, token-level representation, decision-head topology, weights, or training implementation, so it cannot establish architectural identity with open-weight [Laya](../../entities/laya/). The company's account of how it trains such decisions is in the [TypeSafe AI machine learning primer](../typesafe-machine-learning-primer/). Shared terminology is weaker evidence than a disclosed implementation.

## Key points

- Jev is TypeSafe AI's flagship System One model; it accepts state and emits typed decisions and probabilities through `choice`, `score`, and `noul`. (Opening and "How it differs from an LLM")
- Inputs are text, JSON objects, or arrays of text; the model does not accept image, audio, or video directly. (Opening note)
- Applications can ask several independent questions and combine answers with deterministic checks. ("Fast judgments inside a larger workflow")
- The page does not identify Jev's encoder, parameter count, decision-head implementation, or trainable weights. (Entire page)
