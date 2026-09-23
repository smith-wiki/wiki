---
title: TLAPS tutorial example
summary: Official TLAPS tutorial explains hierarchical proof obligations and a theorem about Euclid's algorithm.
url: https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/The_example.html
author: "TLA+ Proof System project"
kind: documentation
captures:
  - retrieved: 2026-09-23T09:00:30Z
    sha256: "a47a83f7cfe0d08eba4a2405a34eb55e537d15962142c9d363c148da84bf36b1"
    type: text/html
---

## Overview

The first page of the official TLAPS tutorial explains how TLA+ proofs are structured: a proof is a hierarchy of claims, each justified by cited facts, and TLAPS verifies a theorem once every claim is justified. Its running example specifies Euclid's greatest-common-divisor algorithm, first in PlusCal and then directly in TLA+, and states a Correctness theorem. It is undated project documentation, authoritative for how the proof checker works, but it neither completes a proof on this page nor relates a specification to real code. Version limits of the tool are on the [TLAPS homepage](../tlaps-home/).

## Key points

- TLAPS checks user-provided hierarchical claims by validating each justified claim against cited facts. If a theorem's proof has no unjustified claims, the checker verifies the theorem. (`The example`, opening paragraph beginning "Broadly speaking, a TLA+ proof is a collection of claims")
- A PlusCal Euclidean algorithm can translate to a TLA+ specification; the tutorial states an initial condition, next-state relation, and theorem `Correctness` for a directly written TLA+ version. (`The example` > `The algorithm`; `The specification`, through the paragraph introducing `Correctness`)
