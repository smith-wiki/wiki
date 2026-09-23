---
title: TLA+
summary: A mathematical specification language for reasoning about all possible behaviors of a modeled system, especially concurrent ones.
---

[TLA+](../../sources/lamport-tla-homepage/) is Leslie Lamport's high-level formal specification language. A specification describes possible executions as state sequences: an initial condition admits starting states and a next-state relation admits steps. This makes concurrency and nondeterminism explicit without committing to implementation details. PlusCal can express an algorithm in a more program-like notation and translate it into TLA+. ([Lamport, 2021](../../sources/lamport-tla-high-level-view/); [Lamport, 2025](../../sources/lamport-tla-homepage/))

## Verification workflow

State a property such as "no account balance is negative" as an invariant, then explore a finite configuration with TLC. In [Hillel Wayne's two-transfer example](../../sources/learntla-conceptual-overview/), both transactions pass their guards before either withdraws, violating the invariant; the model checker can give a trace of the interleaving. A clean result covers the configured model, not arbitrary numbers of accounts, amounts, or transfers. ([Wayne, undated](../../sources/learntla-conceptual-overview/))

The language also has the [TLAPS proof system](../../sources/lamport-tla-tools/): its tutorial describes checking a hierarchy of proof obligations for a theorem, not enumerating a single finite model. TLA+ can state invariants and liveness claims about unbounded specifications; fairness assumptions matter for progress properties. The captured [TLAPS 1.4.5 homepage](../../sources/tlaps-home/) says that release is suited to safety proofs but lacks temporal reasoning, even though TLC can check liveness in finite models. A proof of an abstract model, like a finite TLC check, still needs a justified connection to deployed code. ([TLAPS project, undated](../../sources/tlaps-tutorial-example/); [Lamport, 2021](../../sources/lamport-tla-high-level-view/); [Lamport, 2022](../../sources/lamport-tla-tools/))

## Infrastructure configuration

For [infrastructure as code](../../concepts/infrastructure-as-code/), a TLA+ specification can model apply, rollback, scaling, and failure interleavings; a TLC result covers the finite configuration checked. These transitions must be related to real provider behavior before treating the result as a production guarantee. [IaC assurance depends on the model and measurements](../../notes/iac-assurance-depends-on-model-and-measurements/). ([Lamport, 2021](../../sources/lamport-tla-high-level-view/); [HashiCorp, undated](../../sources/terraform-plan/))

See [the comparison with Lean](../../research/lean-versus-tla/) and [the distinction in verification questions](../../notes/lean-and-tla-prove-different-claims-about-software/).
