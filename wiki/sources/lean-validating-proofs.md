---
title: Validating a Lean Proof
summary: The official reference distinguishes kernel acceptance, transitive axioms, and checks for adversarial proofs.
---

## Source

- **Type:** Mutable official language-reference page
- **Responsible organization:** Lean project
- **Original:** [Validating a Lean Proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
- **Publication or version status:** Versioned reference under `latest`; no fixed version or publication date stated in the capture
- **Suggested citation:** Lean project. "Validating a Lean Proof." Lean Language Reference. Accessed September 23, 2026.

## Representation

- **ID:** `lean-validating-proofs-2026-09-23`
- **Retrieved:** 2026-09-23T08:43:27Z
- **Preserved representation:** `raw/sources/lean-validating-proofs-2026-09-23-2026-09-23.html`
- **Readable extraction:** `raw/sources/lean-validating-proofs-2026-09-23-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:a8d6648cfe53473daae652994ed453de3548b080c84e539e20c475a868cb2fe7`

## Evidence

### `proof-accepted`

- **Source states:** The editor's blue double checks mean the kernel accepted a proof of the *elaborated* theorem statement from definitions, theorems, and axioms in the file and imports. `lake build +Module` without errors or warnings offers the same guarantee. Trust also requires that the formal statement matches the intended meaning.
- **Locator:** `The Blue Double Check Marks` > `Significance`, `Trust`, `Comments`

### `transitive-axioms`

- **Source states:** A check mark may still appear when an imported dependency contains `sorry`. `#print axioms theoremName` lists transitive axioms; `sorryAx` signals an incomplete dependency, `_native` signals native evaluation, and custom axioms make the claim conditional on their soundness.
- **Locator:** `Printing Axioms` > `Instructions`, `Significance`

### `escalating-assurance`

- **Source recommends:** `lean4checker --fresh` can replay stored proofs through the kernel after building; for potentially malicious proofs, an independently authored challenge statement and `lake comparator` with external checkers add protections.
- **Locator:** `Re-Checking Proofs with lean4checker` > `Instructions`, `Significance`; `Gold Standard: comparator and external checkers` > `Instructions`, `Significance`

## Source criticism

The page documents proof-validation guarantees and their assumptions, not a claim that a particular software model correctly captures the real requirement or that a deployed binary behaves like the proved model. Its `latest` path is mutable; guarantees and tooling should be checked against the toolchain version used in a particular project.

## Connections

- [Lean](../../entities/lean/) explains how checked claims enter a software-verification workflow.
- [A proof of a model does not certify separate production code](../../notes/a-proof-of-a-model-does-not-certify-separate-production-code/) distinguishes kernel acceptance from deployment assurance.
- [Research answer](../../research/lean-software-verification/) applies the checks to an authorization task.
