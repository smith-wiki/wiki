---
title: Promise pipelining collapses dependent RPC round trips
summary: Dependent remote calls can travel together when later calls reference unresolved earlier results.
---

A conventional client waits for one remote result before it can construct a call that depends on that result. Each dependency therefore adds a network round trip. Promise pipelining instead represents the dependency in the protocol: a later call points to the unresolved result of an earlier call, so both can be sent before either resolves. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

## Consequence

[Cap'n Web](../../entities/capn-web/) exposes this mechanism through proxy-backed RPC promises. Application code can call a method on an unresolved remote object or pass an unresolved result into another call. In HTTP batch mode, the resulting chain is evaluated remotely in one request and response. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

This reduces latency caused by dependency waterfalls; it does not make remote execution local. Failure, cancellation, authorization, resource use, and runtime input validation still cross a distributed-systems boundary. The mechanism depends on the protocol expressing future-result references, not merely on JavaScript's ordinary `Promise` syntax. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

## Goblins and OCapN

[Spritely Goblins](../../entities/spritely-goblins/) lets code send a message to an unresolved promise; the message is forwarded when that promise resolves. [OCapN](../../entities/ocapn/) includes the same capability in CapTP so a dependency chain can cross network boundaries without one request-response wait per step. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))
