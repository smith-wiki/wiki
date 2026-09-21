---
title: Spritely composes secure distributed systems from capabilities
rkey: spritely-core
date: 2026-09-22
brief: The Spritely paper connects reference-based authority, transactional actors, and interoperable distributed objects.
turn_url: null
mode: SOURCE_BRIEF
---

## Source brief

Christine Lemmer-Webber, Randy Farmer, and Juliana Sims frame object-capability security as ordinary reference passing: holding a reference grants authority; code without it cannot invoke the object. Least authority becomes explicit object relationships and delegation rather than ambient, identity-based permissions. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

[Spritely Goblins](../../entities/spritely-goblins/) combines that model with vats of encapsulated actors. Near objects in one vat call synchronously; near and far objects exchange asynchronous messages through promises. Each queued message opens a turn whose state changes and outgoing messages commit together; an unhandled error commits neither. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

[OCapN](../../entities/ocapn/) layers CapTP, transport-agnostic secure netlayers, and URI or certificate bootstrapping so independent systems could exchange capabilities across languages and peer-to-peer networks without a central authority. This is [object-capability RPC](../../concepts/object-capability-rpc/). **Inference:** one reference-and-message model spans authorization, local composition, and remote cooperation. **Uncertainty:** this is an early draft under technical review; OCapN is described as a draft headed toward standardization, and Goblins remains a library whose guarantees depend on a trusted runtime and safe evaluation environment. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))
