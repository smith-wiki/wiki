---
title: Theorem Proving in Lean 4 - Induction and Recursion
summary: Official tutorial chapter that defines executable recursive functions, states behavioral theorems, proves them by induction and tactics, and evaluates completed programs.
url: https://lean-lang.org/theorem_proving_in_lean4/Induction-and-Recursion/
author: "Jeremy Avigad, Leonardo de Moura, Soonho Kong, and Sebastian Ullrich"
publisher: "Theorem Proving in Lean 4"
kind: book
retrieved: 2026-09-23T08:46:31Z
sha256: "c24e2c141a7ba812602c76a2290f0068c02ddc66c3d479536eba678f3a02ea73"
---

## Overview

The Induction and Recursion chapter of Theorem Proving in Lean 4, the official Lean textbook by Jeremy Avigad, Leonardo de Moura, Soonho Kong, and Sebastian Ullrich, shows how to define recursive functions by pattern matching and structural or well-founded recursion, state properties about them, prove those properties by induction and with tactics, and run the functions. The captured edition assumes Lean 4.33.0. It is authoritative teaching material for the define, state, and prove workflow, but its examples are small arithmetic and list functions, and it notes that the kernel's account of a recursive definition differs from the compiled code, so it says nothing about verifying deployed software.

## Key points

- Lean supports recursive function definitions, pattern matching, and inductive proofs. Its equation compiler translates convenient definitions and proofs to primitive recursors; the compiler itself is not in the trusted code base because its output is checked by the kernel. (`8. Induction and Recursion`, opening paragraphs)
- The recursive function `add` computes on its second natural-number argument. The chapter immediately states `add_zero` and `add_succ` equations and the universally quantified behavioral theorem `zero_add : forall n, add zero n = n`. (`8.3. Structural Recursion and Induction`, first code block beginning `open Nat` and `def add`)
- `zero_add` is proved with a base case using `rfl` and a successor case that recursively invokes `zero_add n` and lifts the equality through `succ` with `congrArg`. The text identifies this as proof by induction expressed as recursion. (`8.3. Structural Recursion and Induction`, the first `theorem zero_add` and the sentence "The proof of zero_add makes it clear that proof by induction is really a form of recursion in Lean.")
- The same theorem can be written in tactic blocks. `simp [add]` closes the base case, `simp [add, zero_add]` uses the induction hypothesis in the successor case, and the rendered proof state reports `All goals completed!` for both branches. (`8.3. Structural Recursion and Induction`, paragraph beginning "The following proof of zero_add works this way" and its second `theorem zero_add`)
- The chapter defines a structurally recursive `fibFast` and evaluates `fibFast 100` with `#eval`; it also defines `listAdd` and evaluates it on two lists, yielding `[5, 7, 9]`. (`8.3. Structural Recursion and Induction`, examples beginning `def fibFast` and `def listAdd`)
- Course-of-values recursion is used to justify termination to Lean's kernel, but this kernel-facing representation does not determine code generation; the code generator compiles recursive functions as functional-language compilers do. (`8.3. Structural Recursion and Induction`, paragraph beginning "The use of course-of-values recursion is one of the techniques")
