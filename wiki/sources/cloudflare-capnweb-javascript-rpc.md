---
title: Cap’n Web — a new RPC system for browsers and web servers
summary: Cloudflare's technical introduction to Cap’n Web, its promise-pipelined RPC model, capability security, and wire format.
---

## Source

- **Type:** Mutable technical article
- **Authors:** Kenton Varda and Steve Faulkner
- **Responsible organization:** Cloudflare
- **Original:** [Cap’n Web — a new RPC system for browsers and web servers](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)
- **Publication status:** Published September 22, 2025; page metadata says modified July 15, 2026
- **Suggested citation:** Varda, Kenton, and Steve Faulkner. “Cap’n Web — a new RPC system for browsers and web servers.” Cloudflare Blog, September 22, 2025.
- **Assessment:** `recorded`

## Representation

- **ID:** `cloudflare-capnweb-2026-09-21`
- **Retrieved:** 2026-09-21T17:59:09Z
- **Preserved representation:** `raw/sources/cloudflare-capnweb-javascript-rpc-2026-09-22.md`
- **Format:** Markdown capture of the article
- **Fixity:** `sha256:504f51b74400e2804f20ffacd2a43e75fcd3aff63daafee79dece07c8871aa4c`

## Description

First-party technical article introducing Cap’n Web's JavaScript RPC interface, transport modes, promise pipelining, bidirectional object references, capability-security properties, and JSON-based protocol.

## Evidence

### `promise-pipelining`

- **Source explains:** Calls can be chained on unresolved remote promises so a dependent operation reaches the server before earlier results return to the client.
- **Representation:** `cloudflare-capnweb-2026-09-21`
- **Locator:** `Features you don't find in typical JSON RPC` → `Chained calls (Promise Pipelining)`

### `capability-security`

- **Source argues:** Authorization can follow possession of object references, including attenuated references that expose narrower authority.
- **Representation:** `cloudflare-capnweb-2026-09-21`
- **Locator:** `Did you spot the security?`

### `transport-and-wire-format`

- **Source describes:** Cap’n Web supports WebSocket-style sessions and HTTP batch mode, while encoding its protocol as JSON with reference and call-table conventions.
- **Representation:** `cloudflare-capnweb-2026-09-21`
- **Locator:** `Features you don't find in typical JSON RPC` → `HTTP batch mode`; `Implementation details` → `JSON-based serialization` and `RPC protocol`

## Source criticism

This is a first-party launch article and design explanation. It calls the library new and highly experimental, does not provide independent security review or comparative benchmarks, and should not be read as evidence that every deployment inherits the described capability discipline.

## Connections

- [Cap’n Web](../../entities/capn-web/) accumulates cross-source project facts.
- [Promise pipelining collapses dependent RPC round trips](../../notes/promise-pipelining-collapses-dependent-rpc-round-trips/) derives the latency implication.
