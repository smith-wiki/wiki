---
title: The Future of kagent
summary: kagent's announcement that it will replace its Deployment-based runtime with Agent Substrate.
---

- **Original:** [The Future of kagent](https://kagent.dev/blog/the-future-of-kagent)
- **Suggested citation:** Yarmush, Eitan. “The Future of kagent.” kagent, undated article referencing August 2026. Accessed September 22, 2026.
- **Author:** Eitan Yarmush
- **Status:** Undated first-party project announcement; its text reports project statistics as of August 2026.
- **Retrieved:** September 22, 2026 at 06:34:58 UTC
- **Preserved evidence:** `raw/sources/kagent-future-of-kagent-2026-09-22.html`
- **Content ID:** `sha256:16498947fa776d9f3f74d48fc18f17b5241be3e0b353151a337c118ad12a5d0b`

## Claims and evidence

The announcement says [kagent](../../entities/kagent/) began with declarative Kubernetes APIs for agents and facilities to run, observe, and secure them. It identifies sandboxing, persistent filesystems, and avoiding dedicated compute for idle agents as requirements that became clearer as the project evolved.

kagent had already added an Agent Substrate-backed `SandboxAgent` custom resource, but the article announces a broader replacement of its Deployment-based runtime with [Agent Substrate](../../entities/agent-substrate/). kagent will remain Kubernetes-native while delegating sandboxing, filesystem snapshots, suspend and resume, network controls, and worker sharing to Substrate. The migration also includes a breaking API redesign: the previous runtime remains supported on `release/v0.10.x`, new work moves to `main`, migration guides were still forthcoming, and the linked API proposal remained open.

## Limits

This is a project-direction announcement, not evidence that the migration or proposed API is complete. Its security, density, and latency statements are promotional first-party claims.

**Contradiction:** The article calls sub-100 ms resume a “guarantee,” while the preserved Substrate README claims sub-500 ms resume and the architecture document states 100 ms at the 95th percentile as a target. None of these preserved sources supplies independent benchmark methodology validating those figures.

## Connections

[Research brief](../../research/google-ax-agent-substrate/) · [kagent](../../entities/kagent/) · [kagent repository](../kagent/) · [Agent Substrate](../../entities/agent-substrate/)
