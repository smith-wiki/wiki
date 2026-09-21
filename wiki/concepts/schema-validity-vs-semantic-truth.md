---
title: Schema validity versus semantic truth
summary: A type-correct model response can still make the wrong judgment.
---

Schema validity asks whether an output conforms to an allowed structure and value set. Semantic truth asks whether the selected value is correct about the world. The first can be guaranteed by a constrained interface; the second remains an empirical property of the model, data, question, and operating context.

## Why the distinction matters

[TypeSafe AI](../../entities/typesafe-ai/) says [Jev](../../entities/jev/) cannot make type errors and “can’t hallucinate” because it returns predefined typed values instead of arbitrary strings. The narrow type-safety claim is meaningful: software need not parse an unexpected response. The broader wording overreaches because an allowed label or score may still be wrong. [S1](../../sources/typesafe-system-one-jev/)

For [System One Models](../system-one-models/), reliability therefore requires both interface guarantees and measured decision quality. Calibration, use-case testing, thresholds, deterministic invariants, and escalation policies address semantic risk; the schema alone does not.
