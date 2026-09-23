---
title: Theorem Proving in Lean 4 - Induction and Recursion
summary: Official tutorial chapter that defines executable recursive functions, states behavioral theorems, proves them by induction and tactics, and evaluates completed programs.
---

## Source

- **Type:** Mutable tutorial chapter in the official *Theorem Proving in Lean 4* book
- **Authors:** Jeremy Avigad, Leonardo de Moura, Soonho Kong, and Sebastian Ullrich, with contributions from the Lean Community
- **Responsible organization:** The Lean project; the chapter is published with Lean's official documentation and links to source under the `leanprover` organization
- **Original:** [8. Induction and Recursion](https://lean-lang.org/theorem_proving_in_lean4/Induction-and-Recursion/)
- **Publication status:** No page-level publication date or immutable revision is given; the containing book says the captured version assumes Lean `4.33.0`
- **Suggested citation:** Avigad, Jeremy, Leonardo de Moura, Soonho Kong, and Sebastian Ullrich. "Induction and Recursion." *Theorem Proving in Lean 4*. Accessed September 23, 2026.
- **Assessment:** `recorded`

## Representations

- **`tpil-induction-recursion-2026-09-23`:** Retrieved 2026-09-23T08:46:31Z as HTML; `raw/sources/lean-tpil-induction-recursion-2026-09-23-2026-09-23.html`; `sha256:c24e2c141a7ba812602c76a2290f0068c02ddc66c3d479536eba678f3a02ea73`
- **`tpil-book-metadata-2026-09-23`:** Retrieved 2026-09-23T08:46:39Z as HTML; `raw/sources/lean-theorem-proving-book-2026-09-23-2026-09-23.html`; `sha256:2f22e8a292535dfec457a0adf2e5e68e4128e4354497c6697a5704f91a3f509f`

Readable `.txt` extractions are stored beside both HTML captures.

## Description

A tutorial chapter on defining functions by pattern matching and structural or well-founded recursion, then proving propositions about those definitions by cases and induction. Its `add` example supplies the full minimal workflow in one section: executable recursive code, equations as behavioral propositions, a theorem quantified over every input, recursive and tactic-style induction proofs, and Lean's completed-goal feedback. Later examples use `#eval` to execute recursive functions while explicitly distinguishing the kernel representation used to justify termination from generated run-time code.

## Evidence

### `recursive-programs-and-inductive-proofs`

- **Source states:** Lean supports recursive function definitions, pattern matching, and inductive proofs. Its equation compiler translates convenient definitions and proofs to primitive recursors; the compiler itself is not in the trusted code base because its output is checked by the kernel.
- **Representation:** `tpil-induction-recursion-2026-09-23`
- **Locator:** `8. Induction and Recursion`, opening paragraphs

### `executable-function-and-behavioral-statements`

- **Source demonstrates:** The recursive function `add` computes on its second natural-number argument. The chapter immediately states `add_zero` and `add_succ` equations and the universally quantified behavioral theorem `zero_add : forall n, add zero n = n`.
- **Representation:** `tpil-induction-recursion-2026-09-23`
- **Locator:** `8.3. Structural Recursion and Induction`, first code block beginning `open Nat` and `def add`

### `proof-by-recursion-is-induction`

- **Source demonstrates:** `zero_add` is proved with a base case using `rfl` and a successor case that recursively invokes `zero_add n` and lifts the equality through `succ` with `congrArg`. The text identifies this as proof by induction expressed as recursion.
- **Representation:** `tpil-induction-recursion-2026-09-23`
- **Locator:** `8.3. Structural Recursion and Induction`, the first `theorem zero_add` and the sentence "The proof of zero_add makes it clear that proof by induction is really a form of recursion in Lean."

### `tactic-proof-and-completion-feedback`

- **Source demonstrates:** The same theorem can be written in tactic blocks. `simp [add]` closes the base case, `simp [add, zero_add]` uses the induction hypothesis in the successor case, and the rendered proof state reports `All goals completed!` for both branches.
- **Representation:** `tpil-induction-recursion-2026-09-23`
- **Locator:** `8.3. Structural Recursion and Induction`, paragraph beginning "The following proof of zero_add works this way" and its second `theorem zero_add`

### `executing-recursive-programs`

- **Source demonstrates:** The chapter defines a structurally recursive `fibFast` and evaluates `fibFast 100` with `#eval`; it also defines `listAdd` and evaluates it on two lists, yielding `[5, 7, 9]`.
- **Representation:** `tpil-induction-recursion-2026-09-23`
- **Locator:** `8.3. Structural Recursion and Induction`, examples beginning `def fibFast` and `def listAdd`

### `termination-proof-versus-generated-code`

- **Source distinguishes:** Course-of-values recursion is used to justify termination to Lean's kernel, but this kernel-facing representation does not determine code generation; the code generator compiles recursive functions as functional-language compilers do.
- **Representation:** `tpil-induction-recursion-2026-09-23`
- **Locator:** `8.3. Structural Recursion and Induction`, paragraph beginning "The use of course-of-values recursion is one of the techniques"

### `nonstructural-termination-obligations`

- **Source explains:** When structural recursion is unavailable, a definition can be justified with a well-founded relation and proofs that recursive calls decrease. Lean first attempts structural recursion, then well-founded recursion, and uses `decreasing_tactic` or a user-supplied `decreasing_by` proof for those obligations.
- **Representation:** `tpil-induction-recursion-2026-09-23`
- **Locator:** `8.5. Well-Founded Recursion and Induction`, opening paragraph; paragraphs beginning "When Lean encounters a recursive definition" and "By default, Lean uses the tactic decreasing_tactic"

### `captured-edition`

- **Source states:** The book is authored by Avigad, de Moura, Kong, and Ullrich with Lean Community contributions, and the captured edition assumes Lean `4.33.0`.
- **Representation:** `tpil-book-metadata-2026-09-23`
- **Locator:** `Theorem Proving in Lean 4`, author line and opening version note immediately above `Contents`

## Source criticism

This first-party chapter is authoritative instructional evidence for Lean's proof-development mechanics, not independent evidence about industrial verification outcomes. Its main finished proof concerns natural-number addition and its execution examples are small recursive functions; applying the method to software requires a faithful specification of the real inputs, state, errors, and environment. `All goals completed!` means the displayed goals were discharged, while `#eval` demonstrates execution of a term; neither should be conflated with proof that a deployed binary, foreign code, operating system, or hardware satisfies the theorem. The chapter itself emphasizes that the kernel's termination representation and generated run-time code are distinct.

The page is mutable and has no page-level revision identifier. Later in `8.5`, it deliberately uses `sorry` in unfinished termination examples and then warns that `sorry` is equivalent to adding a new axiom and should be avoided. Those pedagogical examples are not evidence of completed verification. Stronger validation such as inspecting transitive axioms requires the separate official proof-validation guidance.

## Connections

- [Lean](../../entities/lean/) can cite this page for the end-to-end core workflow: define a recursive function, state a proposition over all inputs, prove it by induction and tactics, inspect completed goals, and separately execute examples.
- [How can Lean support formal verification of software?](../../research/lean-software-verification/) can use the chapter's kernel/code-generation distinction to avoid treating theorem acceptance as automatic verification of a deployed executable.
