---
title: Spritely Goblins
summary: A distributed object programming environment with capability security and transactional vat turns.
---

Spritely Goblins is a distributed object programming environment that combines object-capability security, synchronous local calls, asynchronous message passing, and transactional state management. The paper’s examples use its Guile implementation, while presenting the design as portable to languages with lexical scope and first-class functions. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

## Architecture

A Goblins vat is an event loop containing a transactional object heap called an actormap. Objects in one vat are “near” and may invoke one another synchronously; objects in different vats are “far” and communicate asynchronously. The same asynchronous operation works across vats whether they share a process or communicate through [OCapN](../ocapn/). ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

Each vat handles one queued message per turn. State changes, newly spawned objects, and outbound asynchronous messages commit only when the turn succeeds; an unhandled error leaves the turn uncommitted. See [Transactional vat turns contain failed state and messages](../../notes/transactional-vat-turns-contain-failed-state-and-messages/). ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

## Persistence and status

Goblins serializes an object graph from designated roots while limiting each object’s self-description to authority it already possesses. Restoration can apply upgrade logic. The paper also describes time-travel debugging as planned and says Goblins does not itself implement the proposed portable encrypted storage system. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

## Implementations

At capture time, Spritely’s project page listed Goblins 0.18.0 implementations for Guile and Racket and said objects written in the two supported languages could interact. It also linked application articles about Mandy, Brassica Chat, GoblinShare, and Shepherd. These are first-party project claims rather than independent evidence of implementation completeness or interoperability. ([Spritely Institute, undated](../../sources/spritely-goblins-project/))
