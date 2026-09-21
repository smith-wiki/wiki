---
title: Jev
summary: TypeSafe AI's first model for typed probabilistic judgments embedded in software.
---

Jev is [TypeSafe AI](../typesafe-ai/)'s first public [System One Model](../../concepts/system-one-models/). It consumes program state and predefined questions, then returns constrained binary judgments, choices, or scores with probability information rather than generated prose. [S1](../../sources/typesafe-system-one-jev/)

## Intended role

Jev is designed for narrow decisions such as classification, routing, scoring, extraction, and guardrails. Applications compose independent model judgments with deterministic policy and branching in ordinary code. The launch post reports major latency and cost advantages on four internal workflow evaluations. [S1](../../sources/typesafe-system-one-jev/)

**Uncertainty:** TypeSafe has not published the model architecture, training implementation, weights, independent evaluations, or quantitative calibration evidence. Its type-safety claim constrains output shape but does not guarantee a correct decision. [S1](../../sources/typesafe-system-one-jev/)
