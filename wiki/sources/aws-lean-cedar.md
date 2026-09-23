---
title: Lean Into Verified Software Development
summary: Cedar engineers explain their Lean authorizer theorem, validator proof, and differential testing against Rust.
---

## Source

- **Type:** First-party engineering blog post
- **Authors:** Kesha Hietala and Emina Torlak, Cedar team at AWS
- **Original:** [Lean Into Verified Software Development](https://aws.amazon.com/blogs/opensource/lean-into-verified-software-development/)
- **Published:** April 8, 2024
- **Suggested citation:** Hietala and Torlak. "Lean Into Verified Software Development." AWS Open Source Blog, 2024.

## Representation

- **ID:** `aws-lean-cedar-2026-09-23`
- **Retrieved:** 2026-09-23T08:40:52Z
- **Preserved representation:** `raw/sources/aws-lean-cedar-2026-09-23.html`
- **Readable extraction:** `raw/sources/aws-lean-cedar-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:51b24c2135d6f4c501a104b047914e9bc603bf711041dd9d92e9580c957458c8`

## Evidence

### `verification-guided-development`

- **Authors report:** Cedar maintains executable Lean models of core components and proves properties of those models, while a separate optimized Rust implementation is checked against them using millions of randomly generated differential test inputs; model, proofs, and tests are refreshed before a release.
- **Locator:** `How Cedar uses Lean for verification-guided development`

### `forbid-trumps-permit`

- **Authors show:** `isAuthorized` returns `allow` only with no satisfied `forbid` and at least one satisfied `permit`. Their `forbid_trumps_permit` theorem states that any satisfied forbid in the policy set entails a `deny` decision for every request, entity set, and policy set satisfying that premise. Its proof uses `intro`, `unfold`, and `simp` with an auxiliary theorem.
- **Locator:** `A quick tour of modeling and verifying Cedar with Lean` > `def isAuthorized` and `theorem forbid_trumps_permit`

### `validator-soundness-and-effort`

- **Authors report:** The validator soundness proof establishes that a policy accepted by the validator does not cause a type error on evaluation; its proof used 4,686 lines and 18 person-days. Modeling recursive structures required accommodating Lean's well-founded termination checker.
- **Locator:** `A quick tour of modeling and verifying Cedar with Lean` > table, following two paragraphs, and `One challenge of using Lean is its strict termination checking`

### `practical-guidance`

- **Authors advise:** Start with simple proof automation, build tailored `simp` lemmas, and allow for a learning curve and changes to recursive definitions.
- **Locator:** `Takeaways`

## Source criticism

This is a first-party account from Cedar's engineers, with project-specific performance, effort, and testing results that are not independent benchmarks. The Lean proof establishes properties of the formal model; differential random testing adds sampled evidence about Rust behavior, not a proof of equivalence on every possible input. The written policy requirement itself must be reviewed for adequacy.

## Connections

- [Lean](../../entities/lean/) distinguishes the model proof from the Rust implementation.
- [Lean FRO's Cedar overview](../lean-cedar-verification/) summarizes the same project.
- [Research answer](../../research/lean-software-verification/) applies this pattern to a verification task.
