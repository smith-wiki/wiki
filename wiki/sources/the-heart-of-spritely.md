---
title: The Heart of Spritely
summary: Early-draft technical paper describing Spritely Goblins, its object-capability model, and the OCapN protocol.
---

## Source

- **Type:** Technical paper, HTML edition
- **Authors:** Christine Lemmer-Webber, Randy Farmer, and Juliana Sims
- **Responsible organization:** Spritely Institute
- **Original:** [The Heart of Spritely](https://files.spritely.institute/papers/spritely-core.html)
- **Edition status:** Early draft; HTML export dated May 21, 2025
- **Suggested citation:** Lemmer-Webber, Christine, Randy Farmer, and Juliana Sims. “The Heart of Spritely.” Early draft, HTML edition, May 21, 2025.
- **Assessment:** `recorded`

## Representation

- **ID:** `heart-of-spritely-html-2025-05-21`
- **Retrieved:** 2026-09-21T19:11:20Z
- **Preserved representation:** `raw/sources/spritely-core.html`
- **Format:** HTML
- **Fixity:** `sha256:b41043b3c8cdf977d404fc2eeb7792c587e70d355ea13c4ec5588f3f27b44c5c`

## Description

An early-draft paper explaining Spritely's object-capability security model, Goblins vat and turn semantics, transactional actormaps, promise pipelining, inter-vat communication, and planned encrypted storage.

## Evidence

### `ocap-reference-authority`

- **Source explains:** In an object-capability system, possession of an unforgeable object reference carries the authority to invoke that object; authority can be delegated by passing references.
- **Representation:** `heart-of-spritely-html-2025-05-21`
- **Locator:** `Capabilities as programming` (`#caps-as-programming`)

### `vat-and-transaction-model`

- **Source defines:** A vat runs one turn at a time; Goblins' local actormap interactions are transactional so an uncaught error can roll back the turn.
- **Representation:** `heart-of-spritely-html-2025-05-21`
- **Locator:** `Vat model of computation` (`#vat-model-of-computation`); `Transactions make errors survivable` (`#transactions-make-errors-survivable`); `Turns are cheap transactions` (`#turns-are-cheap-transactions`)

### `promise-pipelining`

- **Source describes:** Messages may be sent to unresolved promises and forwarded toward the eventual target, reducing dependent network round trips.
- **Representation:** `heart-of-spritely-html-2025-05-21`
- **Locator:** `Promise pipelining` (`#promise-pipelining`)

### `network-and-storage-status`

- **Source describes:** OCapN and its CapTP and netlayer components provide inter-vat communication, while portable encrypted storage is a planned design rather than an implemented subsystem in this draft.
- **Representation:** `heart-of-spritely-html-2025-05-21`
- **Locator:** `OCapN` (`#ocapn`) and `Portable encrypted storage` (`#portable-encrypted-storage`)

## Source criticism

The paper is authoritative for the authors' design but labels itself an early draft. Several operational features, including aspects of debugging and portable encrypted storage, are prospective, and the paper provides no independent security evaluation or deployment benchmark.

## Connections

- [Spritely Goblins](../../entities/spritely-goblins/) accumulates cross-source project facts.
- [Spritely Goblins project page](../spritely-goblins-project/) records the public implementation overview.
- [Research brief](../../research/spritely-core/) synthesizes the paper's architecture and limits.
- [Transactional vat turns contain failed state and messages](../../notes/transactional-vat-turns-contain-failed-state-and-messages/) derives the turn model's fault-containment implication.
- [Promise pipelining collapses dependent RPC round trips](../../notes/promise-pipelining-collapses-dependent-rpc-round-trips/) derives the latency implication.
