---
title: Transactional vat turns contain failed state and messages
summary: A vat can commit local state changes and outbound messages together or discard both after an unhandled error.
---

A distributed object can update several nearby objects and schedule remote work during one event-loop turn. If those effects escape independently, a late error can leave partially changed state or messages that describe work the local system never completed. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

## Commit boundary

[Spritely Goblins](../../entities/spritely-goblins/) executes a vat turn against a transactional actormap. Changes to object behavior, spawned objects, and asynchronous messages become visible only when the turn completes successfully. An unhandled error leaves the new heap uncommitted and prevents queued outbound messages from being sent. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))

The guarantee is local to one vat turn, not a transaction spanning every remote participant. Once a committed message crosses into another vat, that vat processes it in its own turn. The useful boundary is therefore failure containment before effects leave the sender, rather than global rollback across the network. ([Lemmer-Webber, Farmer, and Sims, 2025](../../sources/the-heart-of-spritely/))
