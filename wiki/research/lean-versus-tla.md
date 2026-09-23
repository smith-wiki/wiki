---
title: How do Lean and TLA+ compare for software verification?
rkey: lean-versus-tla
date: 2026-09-23
brief: Lean is a natural fit for proved program properties; TLA+ foregrounds system behaviors and interleavings, with both bounded checking and deductive proofs.
turn_url: https://github.com/smith-wiki/wiki/issues/67
mode: QUESTION_ANSWER
---

## Answer

**Inference:** Choose by question, not by a claim that one tool is stronger. [Lean](../../entities/lean/) naturally expresses executable functions and kernel-checked theorems about them: Cedar proves a satisfied `forbid` forces `deny` for every modeled request. [TLA+](../../entities/tla-plus/) specifies possible state transitions, making concurrency and nondeterminism explicit: two individually guarded transfers can interleave and overdraft an account. ([Hietala and Torlak, 2024](../../sources/aws-lean-cedar/); [Wayne, undated](../../sources/learntla-conceptual-overview/); [Lamport, 2021](../../sources/lamport-tla-high-level-view/))

TLC finds counterexample traces or checks a configured finite model; passing one does not prove the unrestricted design. TLA+ also has TLAPS for deductive proofs, so it is not merely a testing notation. The captured TLAPS 1.4.5 release is suited to safety proofs but lacks temporal reasoning. Lean can model systems too; these are workflow strengths, not exclusive capabilities. ([Yu et al., 1999](../../sources/tlc-model-checking-paper/); [TLAPS project, undated](../../sources/tlaps-home/); [Lean FRO, 2026](../../sources/lean-homepage/))

**Inference:** For a concurrent service, model the protocol and failure interleavings in TLA+, prove critical functional invariants in Lean where useful, and separately establish that deployed code matches the models. [The comparison note](../../notes/lean-and-tla-prove-different-claims-about-software/) and [model-to-code boundary](../../notes/a-proof-of-a-model-does-not-certify-separate-production-code/) explain why neither check alone certifies the binary.
