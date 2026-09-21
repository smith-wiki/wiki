---
title: Cap’n Web maps RPC authority onto JavaScript references
rkey: cloudflare-capnweb-javascript-rpc
date: 2026-09-22
brief: Cloudflare presents a schema-free, object-capability RPC system for JavaScript runtimes.
turn_url: null
mode: SOURCE_BRIEF
---

## Source brief

Kenton Varda and Steve Faulkner introduce Cap’n Web as a schema-free, TypeScript-friendly RPC system whose wire representation is JSON with preprocessing. The MIT-licensed implementation supports HTTP batching, WebSockets, and `postMessage()`; its object-capability model permits bidirectional calls and passes functions or `RpcTarget` objects by reference. Promise pipelining lets dependent calls travel in one network round trip instead of forcing sequential waits. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

The security example returns an authenticated session object: possession of that unforgeable remote reference grants authority to invoke its methods. TypeScript provides compile-time API checking, not runtime validation; the authors warn that a malicious peer can send wrongly typed parameters. The launch post also calls Cap’n Web highly experimental despite Cloudflare already using it for Wrangler remote bindings. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

**Inference:** Cap’n Web’s central trade is not merely lower RPC boilerplate; it moves API composition and authorization into JavaScript object references while retaining distributed-system and runtime-validation responsibilities. **Uncertainty:** the post offers examples and design claims, but no independent performance, security, or interoperability evaluation. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))
