---
title: Lean and TLA+ emphasize different verification questions
summary: Lean often checks properties of modeled programs, while TLA+ makes possible system behaviors explicit; neither alone certifies separate deployed code.
---

**Inference:** The choice of notation should follow the failure mode. To check a function's result for every input, [Lean](../../entities/lean/) can define an executable function, state a theorem about it, and have the kernel check its proof; Cedar models its authorizer and proves that a satisfied forbid entails denial. To examine whether concurrent steps can violate a system invariant, [TLA+](../../entities/tla-plus/) can describe initial states, possible transitions, and requirements; TLC finds a two-transfer overdraft interleaving in Hillel Wayne's example. These are characteristic workflows, not exclusive expressive limits: TLA+ also has a proof system, and Lean can host verification frameworks for distributed protocols. ([Hietala and Torlak, 2024](../../sources/aws-lean-cedar/); [Wayne, undated](../../sources/learntla-conceptual-overview/); [Lamport, 2021](../../sources/lamport-tla-high-level-view/); [Lean FRO, 2026](../../sources/lean-homepage/))

| Question | Typical Lean route | Typical TLA+ route |
| --- | --- | --- |
| What is modeled? | A function or program with a formal property | Initial states, possible steps, and behaviors |
| What does checking return? | Kernel acceptance of a theorem relative to definitions and axioms | TLC: a bounded-model result or error trace; TLAPS: a checked theorem relative to its assumptions |
| What remains? | Adequacy of property and model-to-code connection | Adequacy of abstraction, finite bounds for TLC, and model-to-code connection |

These scopes follow the [Lean validation reference](../../sources/lean-validating-proofs/), the original [TLC finite-model account](../../sources/tlc-model-checking-paper/), and the [TLAPS proof tutorial](../../sources/tlaps-tutorial-example/).

## Assurance boundary

A Lean theorem says what follows from its definitions and axioms. TLC checks a configured finite model, whereas a completed TLAPS proof can establish the theorem actually stated for symbolic parameters and assumptions, rather than enumerating one instance. The captured TLAPS 1.4.5 release is suited to safety proofs but lacks temporal reasoning; this is a tool-version limit, not a claim that TLA+ cannot express liveness. None of these results, by themselves, shows that a separately implemented production service faithfully implements the model. [A proof of a model does not certify separate production code](../a-proof-of-a-model-does-not-certify-separate-production-code/). ([Lean project, 2026](../../sources/lean-validating-proofs/); [Yu et al., 1999](../../sources/tlc-model-checking-paper/); [TLAPS project, undated](../../sources/tlaps-tutorial-example/); [TLAPS project, undated](../../sources/tlaps-home/))

**Inference:** For a concurrent authorization service, check decision logic as a function and race-prone policy-update or request interleavings as a system behavior; separately test or prove the correspondence of both models to implementation. [The research comparison](../../research/lean-versus-tla/) gives a task-oriented choice.
