---
title: Laya - 33ms Multilingual System 1 Decision Engine
summary: ConvAI founder's account of Laya's architecture, benchmarks, multilingual routing, and claims about Jev.
url: https://laya.convaiinnovations.com/
author: Nandakishor Mukkunnoth
kind: article
retrieved: 2026-09-23T12:51:17Z
sha256: "b131c4ac0c667cdd57229706879c1fd2c36aae3f2334ce03a00d7e3bcbb3b4d5"
---

## Overview

ConvAI Innovations founder Nandakishor Mukkunnoth introduces Laya as an open-weight, non-autoregressive model for typed decisions and contrasts it with [Jev](../../entities/jev/). Written for AI developers considering classification, routing, and guardrails, the article describes three checkpoints, a language router, training by reward on probability distributions, a quickstart, and vendor benchmark tables. It is useful first-party evidence for the product's stated design and deployment goals, not an independent test of its performance or priority claims. Its cross-product table combines Laya's own measurements with published Jev measurements made under different prompts and hardware. Its claim that constrained output cannot hallucinate concerns response shape, not whether a permitted answer is correct.

## Key points

- Laya exposes `choice`, ordinal `score`, and boolean `noul` questions over a state and returns numeric distributions rather than generated prose. (Section 2, "The Three Decision Primitives")
- Three checkpoints target English, multilingual input, and specialized typed-decision workflows; routing chooses the checkpoint before inference. (Section 3, "The Three Checkpoints"; Section 4, "Why Routing Is Essential")
- The author reports 32.8 ms for one multilingual-checkpoint question on a GPU and 7.2 ms per question in a ten-question batch, not equivalent to network-inclusive API latency. (Section 5, "Head-to-Head")
- The article's Jev comparison borrows Jev results from others; it did not run identical inputs through both products. (Section 5, "Head-to-Head")
- It acknowledges poor high-option accuracy, weak untuned base checkpoints on typed-decisions, and the need for domain temperature fitting. (Section 6, "Honest Limitations")
- The author's March 2025 sales-conversion paper predates Jev but addresses a narrower task; it does not establish that Jev copied Laya. (Introduction; [Mukkunnoth, 2025](../sales-rl-agent-paper/), Abstract)
