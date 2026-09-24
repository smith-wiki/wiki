---
title: Jev
summary: TypeSafe AI's first model for typed probabilistic judgments embedded in software.
---

Jev is [TypeSafe AI](../typesafe-ai/)'s first public [System One Model](../../concepts/system-one-models/). It consumes program state and predefined questions, then returns constrained binary judgments, choices, or scores with probability information rather than generated prose. ([Almeida, 2026](../../sources/typesafe-system-one-jev/))

## Intended role

Jev is designed for narrow decisions such as classification, routing, scoring, extraction, and guardrails. Applications compose independent model judgments with deterministic policy and branching in ordinary code. The launch post reports major latency and cost advantages on four internal workflow evaluations. ([Almeida, 2026](../../sources/typesafe-system-one-jev/))

**Uncertainty:** TypeSafe has not published Jev's model architecture, training implementation, weights, or quantitative calibration across deployment domains. Its type-safety claim constrains output shape but does not guarantee a correct decision. See [Schema validity does not imply semantic correctness](../../notes/schema-validity-does-not-imply-semantic-correctness/) and [Calibration depends on the task and checkpoint](../../notes/calibration-depends-on-task-and-checkpoint/). ([Almeida, 2026](../../sources/typesafe-system-one-jev/))

TypeSafe documents Jev's `choice`/`score`/`noul` contract and its RLCD training goal, but not its model backbone or decision-head topology. Laya publishes those internals; matching output types therefore cannot answer whether their neural architectures match. See [A shared decision API does not reveal a shared model](../../notes/a-shared-decision-api-does-not-reveal-a-shared-model/). ([TypeSafe AI, n.d.](../../sources/typesafe-system-one-documentation/); [TypeSafe AI, n.d.](../../sources/typesafe-machine-learning-primer/); [ConvAI Innovations, n.d.](../../sources/laya-model-card/))

## Compared with Laya

[Laya](../laya/) exposes the same three decision primitives with Apache-2.0 code and downloadable weights, language routing, and optional fine-tuning. Jev 1.13 remains a hosted proprietary API at $0.042 per million input tokens; TypeSafe describes English as its strongest language and offers no customer-specific fine-tuning. In the paired-input [sysone-bench](../../sources/sysone-bench-repository/) sample, Jev wins most curated, twelve-way intent, ordinal, and small multilingual suites, while Laya wins AG News and MNLI. The benchmark's small samples and M2 CPU versus hosted API setup cannot establish universal accuracy or inference-speed superiority. ([ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/); [TypeSafe AI, n.d.](../../sources/typesafe-models-documentation/); [instax-dutta, n.d.](../../sources/sysone-bench-repository/))

A secondary [DEV comparison](../../sources/jev-versus-laya-dev/) describes the open-versus-hosted tradeoff, but its cross-vendor score and latency figures did not use matched prompts. The later paired benchmark is stronger evidence for the tasks it sampled. ([jamilxt, 2026](../../sources/jev-versus-laya-dev/); [instax-dutta, n.d.](../../sources/sysone-bench-repository/))

The independent [Laya-MLX](../laya-mlx/) port runs Laya checkpoints on Apple Silicon; its local timings and upstream parity tests do not compare Jev on equivalent hardware. ([mizorewww and Laya-MLX contributors, n.d.](../../sources/laya-mlx-repository/))

The complete suite-by-suite percentage-point comparison is in [Laya and Jev quality varies by task](../../notes/laya-and-jev-quality-varies-by-task/); neither product wins every sampled task. ([instax-dutta, n.d.](../../sources/sysone-bench-repository/))
