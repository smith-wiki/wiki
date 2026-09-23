---
title: Lean's Cedar software verification case study
summary: Lean FRO's account of Cedar's executable models, proofs, and differential testing against Rust.
---

## Source

- **Type:** Mutable official project case-study webpage
- **Responsible organization:** Lean FRO
- **Original:** [Lean Powers Secure Software at AWS: Cedar's Journey with Verified Development](https://lean-lang.org/use-cases/cedar/)
- **Publication or version status:** No publication date or pinned version stated
- **Suggested citation:** Lean FRO. "Lean Powers Secure Software at AWS." Accessed September 23, 2026.

## Representation

- **ID:** `lean-cedar-verification-2026-09-23`
- **Retrieved:** 2026-09-23T08:40:36Z
- **Preserved representation:** `raw/sources/lean-cedar-verification-2026-09-23.html`
- **Readable extraction:** `raw/sources/lean-cedar-verification-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:87e57374dc192669709940486100b44e500ebaa7af0b18cc2fe10d642bc976e7`

## Evidence

### `cedar-components`

- **Source describes:** Cedar's evaluator determines expression values, authorizer makes authorization decisions, and validator type-checks policies to prevent evaluation errors.
- **Locator:** `The Cedar Verification Approach`

### `model-prove-test`

- **Source describes:** The Cedar team writes executable Lean models beside production Rust, proves correctness and security properties about the models, and compares model and implementation on millions of random inputs before release.
- **Locator:** `The Cedar Verification Approach`

### `kernel-and-trust`

- **Source claims:** Lean's small trusted proof-checking kernel supports the proofs; the production verification process incorporates the model, proofs, and testing.
- **Locator:** `Benefits for Production Software`

## Source criticism

A first-party overview of a user's work, not an independent proof of Cedar's production correctness. Its performance and scale numbers are reported by the project; the underlying [AWS engineering account](../aws-lean-cedar/) gives more precise scope. Differential random testing checks sampled behaviors, not universal equivalence.

## Connections

- [Lean](../../entities/lean/) situates the case study among software-verification workflows.
- [Research answer](../../research/lean-software-verification/) uses it as a concrete task.
- [AWS engineering account](../aws-lean-cedar/) contains the worked theorem and implementation boundary.
