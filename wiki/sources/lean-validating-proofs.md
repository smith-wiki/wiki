---
title: Validating a Lean Proof
summary: The official reference distinguishes kernel acceptance, transitive axioms, and checks for adversarial proofs.
url: https://lean-lang.org/doc/reference/latest/ValidatingProofs/
author: "Lean FRO"
publisher: "Lean Language Reference"
kind: documentation
captures:
  - retrieved: 2026-09-23T08:43:27Z
    sha256: "a8d6648cfe53473daae652994ed453de3548b080c84e539e20c475a868cb2fe7"
    type: text/html
---

## Overview

This chapter of the Lean Language Reference explains what it means for Lean to accept a proof and how to confirm that acceptance means what you think. The editor's check marks and a clean lake build show that the kernel accepted the elaborated statement; #print axioms reveals incomplete dependencies, native evaluation, or extra axioms; lean4checker, comparator, and external checkers add assurance for untrusted proofs. It is official, undated documentation under a mutable latest path. It covers proof checking only, not whether a statement captures the real requirement or whether deployed code behaves like the proved model.

## Key points

- The editor's blue double checks mean the kernel accepted a proof of the *elaborated* theorem statement from definitions, theorems, and axioms in the file and imports. `lake build +Module` without errors or warnings offers the same guarantee. Trust also requires that the formal statement matches the intended meaning. (`The Blue Double Check Marks` > `Significance`, `Trust`, `Comments`)
- A check mark may still appear when an imported dependency contains `sorry`. `#print axioms theoremName` lists transitive axioms; `sorryAx` signals an incomplete dependency, `_native` signals native evaluation, and custom axioms make the claim conditional on their soundness. (`Printing Axioms` > `Instructions`, `Significance`)
- `lean4checker --fresh` can replay stored proofs through the kernel after building; for potentially malicious proofs, an independently authored challenge statement and `lake comparator` with external checkers add protections. (`Re-Checking Proofs with lean4checker` > `Instructions`, `Significance`; `Gold Standard: comparator and external checkers` > `Instructions`, `Significance`)
