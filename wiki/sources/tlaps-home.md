---
title: TLA+ Proof System homepage
summary: The TLAPS project states its proof-checking role and captured release's limits on temporal reasoning.
---

## Source

- **Type:** Mutable official tool homepage
- **Responsible organization:** TLA+ Proof System project, developed by the Tools for Proofs project at Microsoft Research-Inria
- **Original:** [TLA+ Proof System](https://proofs.tlapl.us/doc/web/content/Home.html)
- **Publication or version status:** No page date stated; captured page labels current release `1.4.5`
- **Suggested citation:** TLA+ Proof System project. "TLA+ Proof System." Accessed September 23, 2026.

## Representation

- **ID:** `tlaps-home-2026-09-23`
- **Retrieved:** 2026-09-23T09:01:15Z
- **Preserved representation:** `raw/sources/tlaps-home-2026-09-23.html`
- **Readable extraction:** `raw/sources/tlaps-home-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:15c347b3eb1c6caa80a5f552995de813d18e667cc22429bb16d976c770c5bc55`

## Evidence

### `proof-checking-and-limits`

- **Source states:** TLAPS mechanically checks hierarchical TLA+ proofs. The release described on the page is suitable for nontrivial safety properties, but does not perform temporal reasoning and does not support some TLA+ features.
- **Locator:** `About`

### `release-and-stewardship`

- **Source states:** The page names release `1.4.5`, recommends use from the Toolbox, and identifies the Tools for Proofs project at Microsoft Research-Inria as developer.
- **Locator:** `Get it`; `Community`

## Source criticism

This is a mutable homepage without a page-level timestamp. Its limitations pertain to the captured `1.4.5` release; do not infer that every historical or later implementation of TLAPS has identical coverage. The ability to express liveness in TLA+ is distinct from whether this proof checker supports proving it.

## Connections

- [TLA+](../../entities/tla-plus/) distinguishes language expressiveness from this tool's scope.
- [TLAPS tutorial](../tlaps-tutorial-example/) shows a proof workflow.
- [Lamport's tools page](../lamport-tla-tools/) links the proof system.
- [Lean comparison](../../research/lean-versus-tla/) notes that TLA+ is more than TLC, with versioned proof-system limitations.
