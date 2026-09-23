---
title: "Cap'n Web: A new RPC system for browsers and web servers"
summary: Cloudflare's technical introduction to Cap'n Web, its promise-pipelined RPC model, capability security, and wire format.
url: https://blog.cloudflare.com/capnweb-javascript-rpc-library/
author: Kenton Varda and Steve Faulkner
publisher: Cloudflare Blog
published: 2025-09-22
kind: article
captures:
  - retrieved: 2026-09-21T17:59:09Z
    sha256: "504f51b74400e2804f20ffacd2a43e75fcd3aff63daafee79dece07c8871aa4c"
    type: text/markdown
---

## Overview

Two Cloudflare engineers introduce Cap'n Web, a TypeScript RPC library for browsers and servers that passes functions and objects by reference, lets calls chain on results that have not arrived yet, and runs over WebSocket sessions or HTTP batches with a JSON-based protocol. Written for JavaScript developers at launch, it explains the design and its object-capability security model rather than evaluating them: there is no independent security review or comparative benchmark, and the authors call the library highly experimental. The capture is a Markdown copy of the article; the page was modified in July 2026. Its reference-as-authority model is the one [The Heart of Spritely](../the-heart-of-spritely/) develops for distributed objects.

## Key points

- Calls can be chained on unresolved remote promises, so a dependent call reaches the server before earlier results come back. (Section "Features you don't find in typical JSON RPC", "Chained calls (Promise Pipelining)")
- Authorization follows possession of object references, including attenuated references that expose narrower authority. (Section "Did you spot the security?")
- The library supports WebSocket-style sessions and an HTTP batch mode, and encodes its protocol as JSON with reference and call-table conventions. (Sections "HTTP batch mode" and "Implementation details", "JSON-based serialization" and "RPC protocol")
