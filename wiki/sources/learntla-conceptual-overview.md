---
title: Learn TLA+ conceptual overview
summary: A two-transfer overdraft example illustrates interleaving, invariants, counterexample traces, and bounded TLC models.
---

## Source

- **Type:** Mutable worked tutorial in the Learn TLA+ guide
- **Author:** Hillel Wayne
- **Original:** [Conceptual Overview](https://learntla.com/intro/conceptual-overview.html)
- **Publication or version status:** Guide footer says copyright 2022; no page-level revision date stated
- **Suggested citation:** Wayne. "Conceptual Overview." Learn TLA+. Accessed September 23, 2026.

## Representation

- **ID:** `learntla-conceptual-overview-2026-09-23`
- **Retrieved:** 2026-09-23T08:58:58Z
- **Preserved representation:** `raw/sources/learntla-conceptual-overview-2026-09-23.html`
- **Readable extraction:** `raw/sources/learntla-conceptual-overview-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:d9815d46131f3bb9da136101e779b808bd17708a50538fa01178c7b925145cdf`

## Evidence

### `two-transfer-counterexample`

- **Author demonstrates:** Two nonatomic transfers can each pass a sufficient-funds guard before either withdraws; starting from a balance of six, withdrawals of three and four leave minus one. One transfer alone does not exhibit the flaw.
- **Locator:** `Conceptual Overview`, transfer narrative from "Imagine we're building a wire transfer service" through "leaving her with -1"

### `behaviors-and-properties`

- **Author explains:** A specification describes possible behaviors; the `NoOverdrafts` invariant must hold in every state of every behavior. Labels in the PlusCal example determine where interleaving can occur.
- **Locator:** `Structure`; `Specifications`, paragraph beginning "Each step of the algorithm belongs to a separate label"

### `bounded-model-checking`

- **Author explains:** TLC explores behaviors for a configured model and returns a counterexample trace upon violation. Because system parameters can range without bound, a passing finite model does not establish the property for every possible configuration.
- **Locator:** `Structure`, paragraphs beginning "Once we've written a spec" and "Now we can't check every possible behavior"; `Specifications` > `Models`

## Source criticism

An instructional toy model, not a claim that a bank transfer implementation was tested. The tutorial says a small passing model increases confidence but does not prove the unbounded specification or deployed code correct. Its discussion of TLC should not be generalized to the separate [TLAPS proof system](../lamport-tla-tools/).

## Connections

- [TLA+](../../entities/tla-plus/) draws out the workflow and bounds.
- [Lean and TLA+ make different kinds of claims](../../notes/lean-and-tla-prove-different-claims-about-software/) relates this design check to Lean's program proof.
- [Research comparison](../../research/lean-versus-tla/) uses this counterexample as a concrete decision point.
