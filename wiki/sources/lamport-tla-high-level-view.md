---
title: A High-Level View of TLA+
summary: Lamport explains state-based behavioral specifications, invariants, fairness, liveness, and the separation from code.
url: https://lamport.azurewebsites.net/tla/high-level-view.html
author: "Leslie Lamport"
published: 2021-08-10
kind: article
captures:
  - retrieved: 2026-09-23T08:58:58Z
    sha256: "d8cc04b089ced4b2755ab0b55b372fe23be8750b1aa74e365b24818511c92bc1"
    type: text/html
---

## Overview

Leslie Lamport's essay explains what TLA+ is for: modeling systems above the level of code as state machines, where an initial condition and a next-state relation define the possible behaviors, safety invariants must hold in every state, and liveness needs fairness assumptions. It also introduces PlusCal, the TLC model checker, and the proof checker, with concurrent systems as the main target. Last modified in 2021 by the language's creator, it is authoritative for TLA+'s intended semantics and use but is a first-person argument, not a tool manual or independent assessment, and it stresses that a model does not prevent coding errors. [Learn TLA+](../learntla-homepage/) offers a practical introduction.

## Key points

- TLA+ is above-code-level modeling. An execution is a sequence of states; an initial condition defines starting states and a next-state relation defines possible steps. The resulting specification denotes possible behaviors. (`Introduction`; `Models`; `Modeling Above the Code Level`; `State Machines`)
- Concurrent and distributed systems are prominent targets. Safety invariants concern every state of every behavior; liveness asserts eventual progress and may require fairness assumptions because a next-state relation alone specifies what may happen, not what must happen. (`Modeling Concurrent Systems`; `State Machines`, paragraph beginning "The next-state action specifies what steps may happen"; `Checking Properties`)
- PlusCal offers program-like syntax for nondeterministic/concurrent algorithms and translates to TLA+. TLC is most commonly used by engineers; a proof checker also exists. (`Introduction`; `PlusCal`)
- An above-code model leaves implementation details unspecified and does not prevent coding errors. Testing code alone also struggles to expose errors in a vague high-level design. (`Modeling Above the Code Level`, paragraphs beginning "Code to compute" and "Writing a model above the code level doesn't prevent coding errors")
