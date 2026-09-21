---
title: Introducing System One Models & Jev
summary: TypeSafe AI's launch announcement for a constrained probabilistic decision model.
---

- **Original:** [TypeSafe AI announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- **Author:** Diogo Almeida, founder of TypeSafe AI
- **Published:** Machine metadata says September 21, 2026 at 05:52 UTC; the visible dateline says September 15, 2026.
- **Preserved evidence:** `raw/sources/typesafe-ai-introducing-system-one-models-and-jev-2026-09-21.html`
- **Content ID:** `sha256:8af0f9569aa95e8e217bf571fdff9adb79c45f7a03778234afb563e1c438f8f6`

## Claims and evidence

TypeSafe AI introduces [Jev](../../entities/jev/) as the first [System One Model](../../concepts/system-one-models/). The model accepts unstructured state and predefined questions, then emits typed values, probabilities, and confidence information rather than free-form text. The announced primitives cover binary judgments, choices, and scores; independent questions can be sampled in parallel and composed by ordinary code.

The post reports 70–500 ms end-to-end latency, $0.042 per million input tokens, unmetered output, and large gains on four company-designed workflow evaluations. It attributes these properties to a new architecture, a parallel sampler, and “Reinforcement Learning for Calibrated Decisions,” but does not publish their implementation.

## Limits

The benchmark is first-party evidence, not an independent replication. TypeSafe says its model-capabilities team authored the workflows, external frontier-model probabilities serve as reference answers rather than ground truth, the headline gains may be near the high end of real-world results, and sustainable pricing remains unproved.

The guarantee against type errors concerns the allowed output schema. A valid choice can still be factually or operationally wrong, so schema conformance does not by itself support the broader “can’t hallucinate” wording. See [Schema validity versus semantic truth](../../concepts/schema-validity-vs-semantic-truth/).

## Connections

[Research brief](../../typesafe-system-one-jev/) · [TypeSafe AI](../../entities/typesafe-ai/) · [Jev](../../entities/jev/) · [System One Models](../../concepts/system-one-models/)
