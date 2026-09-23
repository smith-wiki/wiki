---
title: A proof of a model does not certify separate production code
summary: Lean can check a universal property of a formal model while its relationship to deployed software requires separate evidence.
---

A [Lean](../../entities/lean/) theorem proves the claim it states about the definitions it uses. In the Cedar example, the checked `forbid_trumps_permit` theorem concerns its executable Lean authorizer: if a forbid policy is satisfied, authorization returns deny. Cedar's Rust authorizer is distinct. Cedar engineers use differential random testing to compare Rust against the Lean model on millions of inputs; this can expose mismatches, but finite samples do not prove the two implementations equivalent for every input. ([Hietala and Torlak, 2024](../../sources/aws-lean-cedar/))

## Consequence

Before treating a proof as assurance about a shipped system, inspect the formal statement and its assumptions, including transitive axioms with [`#print axioms`](../../sources/lean-validating-proofs/); check the match between specification and intended policy, and the connection between modeled and deployed behavior. A checked theorem about a weak or mistaken requirement may be true yet insufficient. **Inference:** This mirrors [schema validity does not imply semantic correctness](../schema-validity-does-not-imply-semantic-correctness/): passing a formal gate establishes the gate's stated condition, not every higher-level claim about the world. ([Lean project, 2026](../../sources/lean-validating-proofs/))

The same boundary applies to [TLA+](../../entities/tla-plus/): [Lamport](../../sources/lamport-tla-high-level-view/) explicitly distinguishes an above-code system model from its implementation and warns that modeling does not prevent coding errors. [Lean and TLA+ emphasize different verification questions](../lean-and-tla-prove-different-claims-about-software/), but neither makes the model-to-code connection automatic. ([Lamport, 2021](../../sources/lamport-tla-high-level-view/))

[The verification task](../../research/lean-software-verification/) applies this boundary to an authorization rule.
