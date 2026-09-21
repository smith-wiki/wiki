---
title: "Cap'n Web"
summary: A JavaScript-native object-capability RPC protocol and TypeScript implementation.
---

Cap'n Web is an open-source RPC protocol and pure TypeScript implementation introduced by Cloudflare. It is designed for JavaScript applications in browsers and servers, uses JSON with preprocessing for additional value types, and works over HTTP batch requests, WebSockets, `postMessage()`, and custom transports. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

## Model

The protocol combines bidirectional calls, functions and objects passed by remote reference, and [object-capability RPC](../../concepts/object-capability-rpc/). Its RPC promises can be used before resolution, letting dependent operations travel together rather than forcing one network round trip per call. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

Cap'n Web extends this record-and-replay model to synchronous array `map()` callbacks: the client executes a callback against placeholders, records a restricted RPC expression, and asks the remote side to apply it. ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))

## Limits

The launch article describes the project as highly experimental. Its optional TypeScript interfaces provide compile-time checking but no runtime validation against malformed or malicious inputs. See [Promise pipelining collapses dependent RPC round trips](../../notes/promise-pipelining-collapses-dependent-rpc-round-trips/). ([Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))
