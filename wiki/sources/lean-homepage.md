---
title: Lean programming language homepage
summary: Lean FRO's overview of Lean's language, proof checker, automation, and software-verification examples.
url: https://lean-lang.org/
author: "Lean FRO"
kind: webpage
captures:
  - retrieved: 2026-09-23T08:39:50Z
    sha256: "ee25ff6f7a28270a2e4020200d31a3ab5d415d5306d569478a84bf38fe53c16c"
    type: text/html
---

## Overview

The Lean homepage presents Lean as an open-source programming language and proof assistant, attributes its trustworthiness to a minimal proof-checking kernel, shows proof automation such as the grind tactic, and points to software-verification projects including Cedar, Aeneas, and Veil. It is an undated, mutable page maintained by the Lean FRO and written to attract users, so its assurance language is promotional rather than independently assessed; the captured version lists news through September 2026. What a checked proof actually guarantees is explained in [Validating a Lean Proof](../lean-validating-proofs/).

## Key points

- Lean is an open-source programming language and proof assistant; the homepage attributes proof checking to a minimal trusted kernel. (Opening description; `Trustworthy`)
- Lean definitions and theorems use proof tactics, including `grind` in an example about primes; metaprogramming can extend notation and proof automation. (`Powerful automation`, `Mathematics`, and `Extensible`)
- Cedar uses Lean executable models, proofs of security properties, and differential testing against production Rust; Aeneas translates Rust to a form amenable to verification; Veil combines model checking, SMT-based automation, and interactive proving for distributed protocols. (`Lean in Action` > `Cedar`, `Aeneas`, `Veil`)
