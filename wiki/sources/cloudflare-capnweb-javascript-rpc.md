---
title: "Cap'n Web: A new RPC system for browsers and web servers"
summary: Cloudflare's launch article for a JavaScript-native object-capability RPC protocol.
---

- **Original:** [Cloudflare announcement](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)
- **Suggested citation:** Varda, Kenton, and Steve Faulkner. “Cap'n Web: A new RPC system for browsers and web servers.” Cloudflare, 2025.
- **Authors:** Kenton Varda and Steve Faulkner
- **Published:** September 22, 2025; machine metadata says the article was modified July 15, 2026.
- **Retrieved:** September 21, 2026 at 17:59:09 UTC
- **Preserved evidence:** `raw/sources/cloudflare-capnweb-javascript-rpc-2026-09-22.md`
- **Content ID:** `sha256:504f51b74400e2804f20ffacd2a43e75fcd3aff63daafee79dece07c8871aa4c`

## Claims and evidence

Cloudflare introduces [Cap'n Web](../../entities/capn-web/) as a schema-free RPC protocol and pure TypeScript implementation for browsers, servers, Workers, and other modern JavaScript runtimes. Its JSON-based encoding carries structured-clone-compatible values and remote object or function references over HTTP batch requests, WebSockets, `postMessage()`, or custom transports.

Its [object-capability RPC](../../concepts/object-capability-rpc/) model supports calls in both directions and treats possession of an unforgeable remote reference as authority to invoke it. The article's authentication example returns a restricted session object rather than changing connection-wide state or repeatedly transmitting credentials.

[Promise pipelining collapses dependent RPC round trips](../../notes/promise-pipelining-collapses-dependent-rpc-round-trips/) by allowing later calls to refer to unresolved earlier results. Cap'n Web also records synchronous `map()` callbacks against placeholder values and replays the resulting restricted RPC expression remotely, so per-item work can remain in the same round trip.

## Limits

The article is a project announcement by its creators, not an independent performance or security assessment. It describes Cap'n Web as new and highly experimental. TypeScript types are erased at runtime, so the protocol does not stop an untrusted peer from sending values of the wrong type; applications still need runtime validation. Its latency argument is architectural and example-based rather than benchmarked in the article.

## Connections

[Research brief](../../research/cloudflare-capnweb-javascript-rpc/) · [Cap'n Web](../../entities/capn-web/) · [Object-capability RPC](../../concepts/object-capability-rpc/) · [Promise pipelining collapses dependent RPC round trips](../../notes/promise-pipelining-collapses-dependent-rpc-round-trips/)
