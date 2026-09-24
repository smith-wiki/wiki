---
title: Learn TLA+ conceptual overview
summary: A two-transfer overdraft example illustrates interleaving, invariants, counterexample traces, and bounded TLC models.
url: https://learntla.com/intro/conceptual-overview.html
author: "Hillel Wayne"
publisher: "Learn TLA+"
kind: documentation
retrieved: 2026-09-23T08:58:58Z
sha256: "d9815d46131f3bb9da136101e779b808bd17708a50538fa01178c7b925145cdf"
---

## Overview

The conceptual overview of Hillel Wayne's Learn TLA+ guide teaches TLA+ through one small example: two concurrent wire transfers that each pass a balance check before withdrawing can overdraw an account. It shows how a PlusCal specification, an invariant, and the TLC model checker find this flaw and return a counterexample trace, and why a model is checked only for bounded parameters. It is instructional material by a TLA+ trainer, not evidence about any real system, and Wayne himself says a passing small model raises confidence without proving the specification. Its account of TLC does not extend to [proof checking with TLAPS](../lamport-tla-tools/).

## Key points

- Two nonatomic transfers can each pass a sufficient-funds guard before either withdraws; starting from a balance of six, withdrawals of three and four leave minus one. One transfer alone does not exhibit the flaw. (`Conceptual Overview`, transfer narrative from "Imagine we're building a wire transfer service" through "leaving her with -1")
- A specification describes possible behaviors; the `NoOverdrafts` invariant must hold in every state of every behavior. Labels in the PlusCal example determine where interleaving can occur. (`Structure`; `Specifications`, paragraph beginning "Each step of the algorithm belongs to a separate label")
- TLC explores behaviors for a configured model and returns a counterexample trace upon violation. Because system parameters can range without bound, a passing finite model does not establish the property for every possible configuration. (`Structure`, paragraphs beginning "Once we've written a spec" and "Now we can't check every possible behavior"; `Specifications` > `Models`)
