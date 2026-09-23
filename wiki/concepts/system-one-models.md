---
title: System One Models
summary: TypeSafe AI's proposed model class for fast, typed probabilistic decisions.
---

"System One Model" is [TypeSafe AI](../../entities/typesafe-ai/)'s name for a model that evaluates bounded questions against program state and returns typed values and probabilities instead of text. [Jev](../../entities/jev/) is its first announced instance; [Laya](../../entities/laya/) is a separately released open-weight model family built around similar typed-decision primitives. The name invokes fast, intuitive "System 1" cognition, but here denotes a product architecture rather than an established model category. ([Almeida, 2026](../../sources/typesafe-system-one-jev/); [ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/))

## Composition pattern

The model handles small independent judgments; code retains domain policy, weighting, invariants, and final branching. This division can make interfaces more predictable than free-form generation and allows applications to route uncertain cases differently. It also narrows the model's role: explanations, open-ended generation, multi-step reasoning, and correctness guarantees remain outside the typed response contract. ([Almeida, 2026](../../sources/typesafe-system-one-jev/))

[Schema validity does not imply semantic correctness](../../notes/schema-validity-does-not-imply-semantic-correctness/): constraining possible outputs prevents malformed values, not valid-but-wrong decisions; correctness remains an empirical property of the model and its operating context. ([Almeida, 2026](../../sources/typesafe-system-one-jev/))

[Calibration depends on the task and checkpoint](../../notes/calibration-depends-on-task-and-checkpoint/): probability-valued output and a proper-scoring objective do not establish trustworthy confidence on unseen tasks, languages, or model revisions. ([ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/))

[A shared decision API does not reveal a shared model](../../notes/a-shared-decision-api-does-not-reveal-a-shared-model/): Laya's documented encoder and heads cannot be equated with Jev's unpublished internals solely from matching primitives. ([ConvAI Innovations, n.d.](../../sources/laya-model-card/); [TypeSafe AI, n.d.](../../sources/typesafe-system-one-documentation/))
