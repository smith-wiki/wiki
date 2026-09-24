---
title: TLA+ Tools
summary: Leslie Lamport's official inventory distinguishes TLC's explicit-state model checking from TLAPS's mechanical checking of TLA+ proofs.
url: https://lamport.azurewebsites.net/tla/tools.html
author: "Leslie Lamport"
published: 2022-03-18
kind: webpage
retrieved: 2026-09-23T08:59:22Z
sha256: "19feb61d50cc027b69e20f01139b16a14afaf9f06e593cf908bb9c897bc08582"
---

## Overview

Lamport's TLA+ Tools page lists the main tools of the TLA+ ecosystem and separates their roles: TLC, an explicit-state model checker and simulator that checks safety and liveness properties of executable specifications, and TLAPS, which mechanically checks proofs written in TLA+. Last modified in March 2022, it is the creator's authoritative inventory of what each tool is for, not a manual or soundness argument, and it warns that today's language and tools differ from those described in Specifying Systems. The [TLC paper](../tlc-model-checking-paper/) and the [TLAPS homepage](../tlaps-home/) state the limits of each tool's results.

## Key points

- TLC is a model checker and simulator for executable TLA+ specifications, including most specifications written by engineers. It uses explicit states and can check safety and liveness properties. (`The Tools` > `TLC Model Checker`, opening paragraph)
- TLAPS is a system for mechanically checking proofs written in TLA+, including proofs of properties described in Lamport's linked high-level introduction. (`The Tools` > `TLAPS Proof System`, opening paragraph)
- The page lists TLC and TLAPS as separate tools with different jobs: state-space exploration and simulation for TLC, and proof checking for TLAPS. (`The Tools` > `TLC Model Checker`; `The Tools` > `TLAPS Proof System`)
- The current language and tools differ from the versions in *Specifying Systems*. It points to `Current Versions of the TLA+ Tools` for significant tool changes and TLC command-line options. (`Documentation`, paragraph beginning "The current versions of the language and tools differ")
