---
title: "The Heart of Spritely: Distributed Objects and Capability Security"
summary: An early technical paper connecting object capabilities, transactional distributed objects, and OCapN.
---

- **Original:** [Spritely Institute paper](https://files.spritely.institute/papers/spritely-core.html)
- **Suggested citation:** Lemmer-Webber, Christine, Randy Farmer, and Juliana Sims. “The Heart of Spritely: Distributed Objects and Capability Security.” Spritely Institute, early draft, HTML export dated May 21, 2025.
- **Authors:** Christine Lemmer-Webber, Randy Farmer, and Juliana Sims
- **Status:** Early draft under technical review; HTML export dated May 21, 2025
- **Retrieved:** September 21, 2026 at 19:11:20 UTC
- **Preserved evidence:** `raw/sources/spritely-core.html`
- **Content ID:** `sha256:b41043b3c8cdf977d404fc2eeb7792c587e70d355ea13c4ec5588f3f27b44c5c`

## Claims and evidence

The paper presents object-capability security as ordinary reference passing: code begins without ambient authority and can act only through explicitly received references. It develops this model through [Spritely Goblins](../../entities/spritely-goblins/), where objects in the same vat can call synchronously while objects across vats communicate asynchronously without application code needing to distinguish another process from another machine.

Goblins stores each vat’s objects in a transactional actormap. A successful turn commits state changes and outbound messages together; an unhandled error leaves the turn uncommitted. The same object graph supports capability-preserving serialization, planned time-travel debugging, and upgrades. Promise pipelining allows messages to target unresolved results, reducing dependency-driven network waits.

[OCapN](../../entities/ocapn/) supplies the network abstraction. CapTP carries capability-aware messages, distributed garbage collection, and pipelined promises; netlayers separate those semantics from transports and connection timing; URIs or certificates bootstrap references. The paper also specifies requirements for portable encrypted storage but states that Goblins does not implement that storage system.

## Limits

This is a first-party architecture paper and tutorial, not an independent security assessment or performance evaluation. It explicitly remains under technical review. Several parts are prospective: the distributed debugger is planned, portable encrypted storage is future work, and OCapN is described as entering standardization. Examples use the Guile implementation; the claim that the model can transfer to other first-class-function, lexically scoped languages is architectural rather than demonstrated here.

## Connections

[Research brief](../../research/spritely-core/) · [Spritely Goblins](../../entities/spritely-goblins/) · [OCapN](../../entities/ocapn/) · [Object-capability RPC](../../concepts/object-capability-rpc/) · [Transactional vat turns contain failed state and messages](../../notes/transactional-vat-turns-contain-failed-state-and-messages/) · [Promise pipelining collapses dependent RPC round trips](../../notes/promise-pipelining-collapses-dependent-rpc-round-trips/)
