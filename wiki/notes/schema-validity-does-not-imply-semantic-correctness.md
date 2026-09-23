---
title: Schema validity does not imply semantic correctness
summary: A type-correct model response can still make the wrong judgment.
---

Schema validity guarantees that an output belongs to an expected structure and value set. It does not guarantee that the selected value is correct about the world. A constrained model can return an allowed label, score, or probability that is false or operationally unsafe.

## Consequence for model interfaces

[TypeSafe AI](../../entities/typesafe-ai/) frames [Jev](../../entities/jev/)'s constrained output as eliminating type errors and preventing hallucination. The interface can eliminate malformed responses, but the broader claim holds only if “hallucination” means an out-of-schema value. It does not cover a valid-but-wrong decision. ([Almeida, 2026](../../sources/typesafe-system-one-jev/))

[Laya](../../entities/laya/) makes the same "cannot hallucinate" claim because its response is constrained to numbers and permitted options; its own benchmarks nevertheless show weak or confidently wrong answers on some tasks and scripts. This supports the structural distinction rather than a semantic guarantee. ([Mukkunnoth, n.d.](../../sources/laya-research-announcement/); [ConvAI Innovations and Laya contributors, n.d.](../../sources/laya-repository/))

Reliable automation therefore needs two separate controls: interface constraints for structural validity, and empirical evaluation, thresholds, deterministic invariants, and escalation for decision quality. This boundary applies directly to [System One Models](../../concepts/system-one-models/) and other structured model interfaces.

## Related verification boundary

A [Lean proof of a model does not certify separate production code](../a-proof-of-a-model-does-not-certify-separate-production-code/) for the same reason that schema-valid output need not be a correct judgment: each formal check establishes only its stated condition. A security requirement and the deployed implementation require separate review or evidence.
