---
title: TLAPS tutorial example
summary: Official TLAPS tutorial explains hierarchical proof obligations and a theorem about Euclid's algorithm.
---

## Source

- **Type:** Mutable official tool tutorial
- **Responsible organization:** TLA+ Proof System project
- **Original:** [The example](https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/The_example.html) (the archived documentation URL redirects here)
- **Publication or version status:** No date or specific tool version stated on the page
- **Suggested citation:** TLA+ Proof System project. "The example." TLAPS Tutorial. Accessed September 23, 2026.

## Representation

- **ID:** `tlaps-tutorial-example-2026-09-23`
- **Retrieved:** 2026-09-23T09:00:30Z
- **Preserved representation:** `raw/sources/tlaps-tutorial-example-2026-09-23.html`
- **Readable extraction:** `raw/sources/tlaps-tutorial-example-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:a47a83f7cfe0d08eba4a2405a34eb55e537d15962142c9d363c148da84bf36b1`

## Evidence

### `hierarchical-proof`

- **Source explains:** TLAPS checks user-provided hierarchical claims by validating each justified claim against cited facts. If a theorem's proof has no unjustified claims, the checker verifies the theorem.
- **Locator:** `The example`, opening paragraph beginning "Broadly speaking, a TLA+ proof is a collection of claims"

### `general-specification-example`

- **Source illustrates:** A PlusCal Euclidean algorithm can translate to a TLA+ specification; the tutorial states an initial condition, next-state relation, and theorem `Correctness` for a directly written TLA+ version.
- **Locator:** `The example` > `The algorithm`; `The specification`, through the paragraph introducing `Correctness`

## Source criticism

The page establishes that TLAPS performs deductive proof checking rather than simply enumerating one finite TLC model. It does not by itself guarantee that an arbitrary theorem has a completed proof, or that a separately implemented program matches the specification. The captured [TLAPS project page](../tlaps-home/) describes tool-version restrictions on temporal reasoning.

## Connections

- [TLA+](../../entities/tla-plus/) includes both TLC and TLAPS workflows.
- [Lamport's tools page](../lamport-tla-tools/) names both tools.
- [Lean comparison](../../research/lean-versus-tla/) avoids treating TLA+ as only bounded checking.
