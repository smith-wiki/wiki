---
title: System One Models
summary: TypeSafe AI's proposed model class for fast, typed probabilistic decisions.
---

“System One Model” is [TypeSafe AI](../../entities/typesafe-ai/)'s name for a model that evaluates bounded questions against program state and returns typed values and probabilities instead of text. [Jev](../../entities/jev/) is the first announced instance. The name invokes fast, intuitive “System 1” cognition, but here denotes a product architecture rather than an established model category. [S1](../../sources/typesafe-system-one-jev/)

## Composition pattern

The model handles small independent judgments; code retains domain policy, weighting, invariants, and final branching. This division can make interfaces more predictable than free-form generation and allows applications to route uncertain cases differently. It also narrows the model's role: explanations, open-ended generation, multi-step reasoning, and correctness guarantees remain outside the typed response contract. [S1](../../sources/typesafe-system-one-jev/)

Constraining possible outputs prevents malformed values, not valid-but-wrong decisions; correctness remains an empirical property of the model and its operating context. [S1](../../sources/typesafe-system-one-jev/)
