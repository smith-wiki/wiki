---
title: TLA+ Tools
summary: Leslie Lamport's official inventory distinguishes TLC's explicit-state model checking from TLAPS's mechanical checking of TLA+ proofs.
---

## Source

- **Type:** Mutable official project tools page
- **Author and responsible publisher:** Leslie Lamport, on Lamport's official TLA+ site
- **Original:** [TLA+ Tools](https://lamport.azurewebsites.net/tla/tools.html)
- **Date:** Last modified March 18, 2022
- **Suggested citation:** Lamport, Leslie. "TLA+ Tools." Last modified March 18, 2022. Accessed September 23, 2026.
- **Assessment:** `recorded`

## Representation

- **ID:** `lamport-tla-tools-2026-09-23`
- **Retrieved:** 2026-09-23T08:59:22Z
- **Preserved representation:** `raw/sources/lamport-tla-tools-2026-09-23.html`
- **Readable extraction:** `raw/sources/lamport-tla-tools-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:19feb61d50cc027b69e20f01139b16a14afaf9f06e593cf908bb9c897bc08582`

## Description

Lamport's overview identifies the principal tools in the TLA+ ecosystem and separates their roles. TLC is an explicit-state model checker and simulator for executable TLA+ specifications; the page says it checks both safety and liveness properties. TLAPS is a different tool: a proof system that mechanically checks proofs written in TLA+. The page therefore does not support describing TLA+ as only a model-checking language.

## Evidence

### `tlc-is-an-explicit-state-model-checker`

- **Source states:** TLC is a model checker and simulator for executable TLA+ specifications, including most specifications written by engineers. It uses explicit states and can check safety and liveness properties.
- **Locator:** `The Tools` > `TLC Model Checker`, opening paragraph

### `tlaps-mechanically-checks-proofs`

- **Source states:** TLAPS is a system for mechanically checking proofs written in TLA+, including proofs of properties described in Lamport's linked high-level introduction.
- **Locator:** `The Tools` > `TLAPS Proof System`, opening paragraph

### `model-checking-and-proof-checking-are-separate-capabilities`

- **Source shows:** The page lists TLC and TLAPS as separate tools with different jobs: state-space exploration and simulation for TLC, and proof checking for TLAPS.
- **Locator:** `The Tools` > `TLC Model Checker`; `The Tools` > `TLAPS Proof System`

### `documentation-has-version-drift`

- **Source warns:** The current language and tools differ from the versions in *Specifying Systems*. It points to `Current Versions of the TLA+ Tools` for significant tool changes and TLC command-line options.
- **Locator:** `Documentation`, paragraph beginning "The current versions of the language and tools differ"

## Cross-source scope

This page names both tools but does not establish the scope of their results. The original [TLC paper](../tlc-model-checking-paper/) documents finite model instantiation and counterexample traces; the [TLAPS tutorial](../tlaps-tutorial-example/) documents deductive proof checking. The [captured TLAPS release page](../tlaps-home/) states version-specific proof-system limits.

## Source criticism

This is a concise, first-party inventory by TLA+'s creator. It is authoritative for the intended roles of the named tools, but it is not a complete semantics, soundness argument, or user manual. The page is mutable and was last modified in 2022. Its statement that TLC checks safety and liveness reflects the capability described there; the [1999 TLC paper](../tlc-model-checking-paper/) predates liveness checking and must not be used to claim that current TLC lacks it.

A successful finite TLC run is evidence about the exact model and properties checked, subject to the model, configuration, tool behavior, and completion of exploration; it does not generalize by itself beyond those bounds. Conversely, TLAPS is not limited to finite-state enumeration, but checks only the theorem actually formalized and its proof obligations. The [captured TLAPS homepage](../tlaps-home/) labels release 1.4.5 as suitable for safety proofs but lacking temporal reasoning and some TLA+ features; check the version actually used.

Neither tool by itself establishes that a TLA+ model faithfully represents requirements, implementation code, its runtime environment, or a deployed system.

## Connections

- [Learn TLA+ conceptual overview](../learntla-conceptual-overview/) supplies an instructional explanation of the model/specification distinction behind TLC's finite instances.
- [TLA+](../../entities/tla-plus/) can use this page to present model checking and deductive proof checking as complementary capabilities rather than reducing TLA+ to TLC.
- [Lean versus TLA+](../../research/lean-versus-tla/) can use the bounded-model versus theorem-scope distinction when comparing verification claims.
