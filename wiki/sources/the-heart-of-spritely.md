---
title: The Heart of Spritely
summary: Early-draft technical paper describing Spritely Goblins, its object-capability model, and the OCapN protocol.
url: https://files.spritely.institute/papers/spritely-core.html
author: Christine Lemmer-Webber, Randy Farmer, and Juliana Sims
publisher: Spritely Institute
published: 2025-05-21
kind: paper
retrieved: 2026-09-21T19:11:20Z
sha256: "b41043b3c8cdf977d404fc2eeb7792c587e70d355ea13c4ec5588f3f27b44c5c"
---

## Overview

Three Spritely Institute authors explain the design at the core of Spritely: object-capability security, the vat-and-turn execution model of Goblins, transactional state, promise pipelining, the OCapN protocol for communication between vats, and planned encrypted storage. The paper is written for developers and protocol designers and labels itself an early draft; the captured HTML export is dated May 21, 2025. It is authoritative for the authors' intended design, but several features, including parts of debugging and portable encrypted storage, are still prospective, and it offers no independent security evaluation or deployment benchmark. [Cap'n Web](../cloudflare-capnweb-javascript-rpc/) applies the same capability model to JavaScript RPC.

## Key points

- Possessing an unforgeable object reference carries the authority to invoke that object, and passing the reference delegates that authority. (Section "Capabilities as programming", `#caps-as-programming`)
- A vat runs one turn at a time, and local actormap interactions are transactional, so an uncaught error can roll the turn back. (Sections "Vat model of computation", "Transactions make errors survivable", and "Turns are cheap transactions")
- Messages can be sent to unresolved promises and are forwarded toward the eventual target, which removes dependent network round trips. (Section "Promise pipelining", `#promise-pipelining`)
- OCapN, with CapTP and netlayers, carries communication between vats, while portable encrypted storage is a planned design rather than an implemented subsystem. (Sections "OCapN" and "Portable encrypted storage")
