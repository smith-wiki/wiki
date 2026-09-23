---
title: How can Lean support formal verification of software?
rkey: lean-software-verification
date: 2026-09-23
brief: Specify a software invariant in Lean, prove it for an executable model, then establish how that model relates to deployed code.
turn_url: https://github.com/smith-wiki/wiki/issues/65
mode: QUESTION_ANSWER
---

## Answer

Use [Lean](../../entities/lean/) to turn a software requirement into a precise, kernel-checked theorem about an executable program or model--not merely a collection of passing test cases. For an authorization task, model policy evaluation and prove that any satisfied `forbid` forces `deny`, even if a `permit` also matches. Cedar's engineers show this exact `forbid_trumps_permit` theorem: define `isAuthorized`, quantify over requests and policy sets, then use tactics and supporting lemmas to complete the proof. ([Hietala and Torlak, 2024](../../sources/aws-lean-cedar/); [Lean FRO, 2026](../../sources/lean-homepage/))

The [official tutorial](../../sources/theorem-proving-in-lean-induction-and-recursion/) shows the define-state-prove loop. For an accepted theorem, inspect [`#print axioms`](../../sources/lean-validating-proofs/) to catch incomplete imported proofs or extra assumptions. ([Avigad et al., 2026](../../sources/theorem-proving-in-lean-induction-and-recursion/); [Lean project, 2026](../../sources/lean-validating-proofs/))

For independently implemented production code, a model proof is not an end-to-end proof of the shipped binary. Cedar compares its Lean model against Rust on millions of generated inputs; that is strong sampled evidence, not universal equivalence. Review the property and assumptions, keep proofs current as the model changes, and separately establish model/code correspondence. [The model-implementation boundary](../../notes/a-proof-of-a-model-does-not-certify-separate-production-code/) and [Cedar case study](../../sources/lean-cedar-verification/) carry the detail. ([Hietala and Torlak, 2024](../../sources/aws-lean-cedar/))
