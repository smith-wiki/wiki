---
title: Schema validity does not imply semantic correctness
summary: A type-correct model response can still make the wrong judgment.
---

Schema validity guarantees that an output belongs to an expected structure and value set. It does not guarantee that the selected value is correct about the world. A constrained model can return an allowed label, score, or probability that is false or operationally unsafe.

## Consequence for model interfaces

[TypeSafe AI](../../entities/typesafe-ai/) frames [Jev](../../entities/jev/)'s constrained output as eliminating type errors and preventing hallucination. The interface can eliminate malformed responses, but the broader claim holds only if “hallucination” means an out-of-schema value. It does not cover a valid-but-wrong decision. [S1](../../sources/typesafe-system-one-jev/)

Reliable automation therefore needs two separate controls: interface constraints for structural validity, and empirical evaluation, thresholds, deterministic invariants, and escalation for decision quality. This boundary applies directly to [System One Models](../../concepts/system-one-models/) and other structured model interfaces.
