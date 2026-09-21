---
title: OCapN
summary: A layered protocol effort for interoperable object-capability communication across networks.
---

OCapN, the Object Capability Network, is a protocol effort for carrying object-capability relationships across network boundaries without requiring a central authority. Spritely Goblins implements the model, while the paper presents OCapN as language-independent infrastructure intended for interoperable implementations. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

## Layers

CapTP provides secure distributed-object messaging, distributed garbage collection, and promise pipelining. Beneath it, netlayers abstract secure connections across transports including conventional TLS networks, peer-to-peer systems, and delayed store-and-forward links. URI structures and certificates provide different ways to bootstrap an initial object reference. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

This layering lets [Spritely Goblins](../spritely-goblins/) preserve the same asynchronous programming model for near-process and remote objects while keeping authority attached to references. It is one realization of [object-capability RPC](../../concepts/object-capability-rpc/). ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

## Status

The source is an early draft under technical review and describes OCapN as a draft specification beginning a standardization process. It establishes architecture and intended properties, not independent evidence of interoperability, security review, or production performance. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))
