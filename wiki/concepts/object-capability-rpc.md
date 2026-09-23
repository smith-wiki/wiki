---
title: Object-capability RPC
summary: Remote invocation in which references identify both callable objects and authority.
---

Object-capability RPC lets a program send references to callable functions or objects across a connection. The recipient gets a stub whose calls execute against the original object. Calls can therefore flow in both directions, and possessing a reference supplies the authority to invoke the interface it exposes. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

## Authorization structure

In [Cap'n Web](../../entities/capn-web/), authentication can return a new session object whose methods represent the operations available to that identity. A peer cannot synthesize that reference within the protocol; it must receive it from an authorized operation. This keeps authority attached to objects rather than mutable connection-wide state or credentials repeated with every call. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

## From local references to network references

[Spritely Goblins](../../entities/spritely-goblins/) applies the same authority model inside and across vats: a reference permits invocation, near objects may be called synchronously, and far objects receive asynchronous messages. [OCapN](../../entities/ocapn/) carries those reference relationships between machines through CapTP while separating transport details into netlayers. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

## Boundaries

Capability possession does not make the whole application secure. Transport authentication, resource limits, revocation policy, and runtime validation of values remain separate responsibilities. TypeScript alone cannot validate data from an untrusted peer because its types do not exist at runtime. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

## Decoy session authority

**Inference:** In a [password-triggered decoy](../password-triggered-decoys/), a synthetic account view must not imply authority over the genuine account. Returning only decoy-scoped references would preserve the distinction this page draws between a visible interface and the operations a session can actually invoke. The [decoy-login oracle](../../notes/decoy-logins-move-the-password-oracle/) is the remaining problem: any observable difference between those scopes can reveal whether the password was genuine. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/); [Smith, 2026](../../sources/andy-smith-every-password-correct/))
