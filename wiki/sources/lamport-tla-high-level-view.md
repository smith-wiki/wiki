---
title: A High-Level View of TLA+
summary: Lamport explains state-based behavioral specifications, invariants, fairness, liveness, and the separation from code.
---

## Source

- **Type:** Mutable first-person technical exposition
- **Author:** Leslie Lamport
- **Original:** [A High-Level View of TLA+](https://lamport.azurewebsites.net/tla/high-level-view.html)
- **Last modified:** August 10, 2021 (page statement)
- **Suggested citation:** Lamport. "A High-Level View of TLA+." Last modified 2021; accessed September 23, 2026.

## Representation

- **ID:** `lamport-tla-high-level-view-2026-09-23`
- **Retrieved:** 2026-09-23T08:58:58Z
- **Preserved representation:** `raw/sources/lamport-tla-high-level-view-2026-09-23.html`
- **Readable extraction:** `raw/sources/lamport-tla-high-level-view-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:d8cc04b089ced4b2755ab0b55b372fe23be8750b1aa74e365b24818511c92bc1`

## Evidence

### `abstract-behaviors`

- **Author defines:** TLA+ is above-code-level modeling. An execution is a sequence of states; an initial condition defines starting states and a next-state relation defines possible steps. The resulting specification denotes possible behaviors.
- **Locator:** `Introduction`; `Models`; `Modeling Above the Code Level`; `State Machines`

### `concurrency-and-properties`

- **Author explains:** Concurrent and distributed systems are prominent targets. Safety invariants concern every state of every behavior; liveness asserts eventual progress and may require fairness assumptions because a next-state relation alone specifies what may happen, not what must happen.
- **Locator:** `Modeling Concurrent Systems`; `State Machines`, paragraph beginning "The next-state action specifies what steps may happen"; `Checking Properties`

### `pluscal-and-proof-checking`

- **Author explains:** PlusCal offers program-like syntax for nondeterministic/concurrent algorithms and translates to TLA+. TLC is most commonly used by engineers; a proof checker also exists.
- **Locator:** `Introduction`; `PlusCal`

### `code-boundary`

- **Author cautions:** An above-code model leaves implementation details unspecified and does not prevent coding errors. Testing code alone also struggles to expose errors in a vague high-level design.
- **Locator:** `Modeling Above the Code Level`, paragraphs beginning "Code to compute" and "Writing a model above the code level doesn't prevent coding errors"

## Source criticism

This is Lamport's 2021 first-person exposition, not a current tool specification or an independent assessment. Its benefits and industrial examples are his claims. A model's abstraction must be reviewed against the intended system and an implementation must be related to that model separately.

## Connections

- [TLA+](../../entities/tla-plus/) defines the modeled object and assurance boundary.
- [Lamport's homepage](../lamport-tla-homepage/) links the project's entry points.
- [Lean comparison](../../research/lean-versus-tla/) contrasts behavioral modeling with program proofs.
