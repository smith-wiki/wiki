---
title: Introducing System One Models & Jev
summary: TypeSafe AI's launch article for Jev, a model for fast typed probabilistic decisions inside software workflows.
---

## Source

- **Type:** Mutable company launch article
- **Author:** Diogo Almeida
- **Responsible organization:** TypeSafe AI
- **Original:** [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- **Publication status:** Visible date September 15, 2026; machine-readable metadata reported September 21, 2026
- **Suggested citation:** Almeida, Diogo. “Introducing System One Models & Jev.” TypeSafe AI, September 15, 2026.
- **Assessment:** `recorded`

## Representation

- **ID:** `typesafe-system-one-jev-2026-09-21`
- **Retrieved:** 2026-09-21T16:26:00Z
- **Preserved representation:** `raw/sources/typesafe-ai-introducing-system-one-models-and-jev-2026-09-21.html`
- **Format:** HTML
- **Fixity:** `sha256:8af0f9569aa95e8e217bf571fdff9adb79c45f7a03778234afb563e1c438f8f6`

## Description

First-party launch article describing TypeSafe AI's “System One Model” category, the Jev model's typed probabilistic interface, and company-reported latency, pricing, and workflow evaluations.

## Evidence

### `typed-probabilistic-interface`

- **Source states:** Jev accepts unstructured program state and predefined questions, then returns type-constrained values with probabilities and confidence scores rather than generated prose.
- **Representation:** `typesafe-system-one-jev-2026-09-21`
- **Locator:** Opening product description; `Frontiers, Old and New` → `Inputs`, `Outputs`, and `Confidence`

### `performance-and-pricing`

- **Source reports:** End-to-end response times of 70–500 milliseconds, input pricing of $0.042 per million tokens, and unmetered output.
- **Representation:** `typesafe-system-one-jev-2026-09-21`
- **Locator:** `Frontiers, Old and New` → `Cost` and `Speed`; `Evidence / Technical Results` opening verification list

### `workflow-evaluations`

- **Source reports:** Four company-created workflows compare Jev with external models using the latter's averaged probability outputs as reference answers.
- **Representation:** `typesafe-system-one-jev-2026-09-21`
- **Locator:** `Evidence / Technical Results` → `Workflow evals` and its `Nuance` list

## Source criticism

The article is a first-party launch source. Its workflow content was produced by the model-capabilities team, its references are model outputs rather than independent ground truth, and it publishes no architecture, sampler, training, or independent replication details. Schema conformance establishes output shape, not semantic correctness, while the pricing and latency claims remain company-reported.

## Connections

- [System One models](../../concepts/system-one-models/) defines the category in the wiki.
- [TypeSafe AI](../../entities/typesafe-ai/) and [Jev](../../entities/jev/) accumulate cross-source facts.
- [Research brief](../../research/typesafe-system-one-jev/) answers the originating question.
- [Schema validity does not imply semantic correctness](../../notes/schema-validity-does-not-imply-semantic-correctness/) records the relevant output-safety limit.
