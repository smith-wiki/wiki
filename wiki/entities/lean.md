---
title: Lean
summary: A programming language and proof assistant whose kernel checks formal claims about executable models and programs.
---

[Lean](../../sources/lean-homepage/) is an open-source programming language and proof assistant. Programs, specifications, and proofs can all be expressed in Lean. A theorem states a property as a type; proof automation and interactive tactics construct evidence that Lean's kernel checks. The [official tutorial](../../sources/theorem-proving-in-lean-induction-and-recursion/) demonstrates defining a recursive function, proving a statement over every input by induction, and evaluating examples. The homepage points to software-verification projects including Cedar, Veil, and Aeneas. ([Avigad et al., 2026](../../sources/theorem-proving-in-lean-induction-and-recursion/); [Lean FRO, 2026](../../sources/lean-homepage/))

## Software-verification task

Consider an authorization service: a satisfied deny rule must override any allow rule. Model its decision function and policy inputs in Lean, state the invariant over *all* requests and policy sets, then prove it from the function and supporting lemmas. The Cedar team demonstrates this with an executable `isAuthorized` model and a `forbid_trumps_permit` theorem. The proof is checked for the model and the assumptions expressed in its statement, not for an unrelated implementation. ([Hietala and Torlak, 2024](../../sources/aws-lean-cedar/))

## Checking the claim

The [language reference](../../sources/lean-validating-proofs/) distinguishes an accepted proof from its meaning: editor confirmation or a clean `lake build +Module` shows kernel acceptance of the elaborated statement relative to its definitions and axioms. Run `#print axioms` on the theorem to inspect transitive `sorryAx`, native evaluation, or custom assumptions. Even without these, confirm the policy encoded by the theorem is the policy required by the system. ([Lean project, 2026](../../sources/lean-validating-proofs/))

## From proof to shipped code

Cedar's production authorizer is Rust, separate from its Lean model. Its engineers compare outputs on millions of random inputs to find model/implementation discrepancies and keep model, proofs, and differential tests current before release. This strengthens the engineering case but does not prove Rust/model equivalence for all inputs. [A proof of a model does not certify separate production code](../../notes/a-proof-of-a-model-does-not-certify-separate-production-code/). ([Hietala and Torlak, 2024](../../sources/aws-lean-cedar/); [Lean FRO, 2026](../../sources/lean-cedar-verification/))

**Inference:** Choose a narrow security property and explicit model boundary first; reviewers must still decide whether the specification matches the real requirement and whether production behavior matches the model. Compare this semantic boundary with [schema validity does not imply semantic correctness](../../notes/schema-validity-does-not-imply-semantic-correctness/).

[This turn's research card](../../research/lean-software-verification/) gives the short task-oriented answer.
