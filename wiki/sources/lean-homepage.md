---
title: Lean programming language homepage
summary: Lean FRO's overview of Lean's language, proof checker, automation, and software-verification examples.
---

## Source

- **Type:** Mutable official project webpage
- **Responsible organization:** Lean FRO
- **Original:** [Lean Programming Language](https://lean-lang.org/)
- **Publication or version status:** No page publication date or pinned version stated; page displays September 2026 news
- **Suggested citation:** Lean FRO. "Lean Programming Language." Accessed September 23, 2026.

## Representation

- **ID:** `lean-homepage-2026-09-23`
- **Retrieved:** 2026-09-23T08:39:50Z
- **Preserved representation:** `raw/sources/lean-homepage-2026-09-23.html`
- **Readable extraction:** `raw/sources/lean-homepage-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:ee25ff6f7a28270a2e4020200d31a3ab5d415d5306d569478a84bf38fe53c16c`

## Evidence

### `language-and-kernel`

- **Source states:** Lean is an open-source programming language and proof assistant; the homepage attributes proof checking to a minimal trusted kernel.
- **Locator:** Opening description; `Trustworthy`

### `automation-and-examples`

- **Source shows:** Lean definitions and theorems use proof tactics, including `grind` in an example about primes; metaprogramming can extend notation and proof automation.
- **Locator:** `Powerful automation`, `Mathematics`, and `Extensible`

### `software-verification-projects`

- **Source describes:** Cedar uses Lean executable models, proofs of security properties, and differential testing against production Rust; Aeneas translates Rust to a form amenable to verification; Veil combines model checking, SMT-based automation, and interactive proving for distributed protocols.
- **Locator:** `Lean in Action` > `Cedar`, `Aeneas`, `Veil`

## Source criticism

First-party project overview: its assurance and project descriptions are promotional, not independent audits. A checked theorem establishes its formal statement, not automatically the fidelity of a separate production implementation or the adequacy of the stated property. The webpage is mutable.

## Connections

- [Lean](../../entities/lean/) explains the language and software-verification boundary.
- [Cedar case study](../lean-cedar-verification/) expands the homepage's production example.
- [Research answer](../../research/lean-software-verification/) applies these claims to a concrete verification task.
