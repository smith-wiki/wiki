---
title: Agent Substrate
summary: A runtime for multiplexing stateful sandboxed actors over a smaller pool of warm workers.
---

Agent Substrate is a framework-agnostic execution runtime for agent-like workloads. It separates a stateful Actor from the Worker that currently hosts it: idle actors can be snapshotted and suspended, then restored onto an available pre-started worker when traffic arrives. An actor-aware router locates or resumes the actor before forwarding a request. ([Agent Substrate contributors, 2026](../../sources/agent-substrate/))

## Resource and lifecycle model

Kubernetes provisions infrastructure and worker pods through resources such as `WorkerPool`, while Substrate stores frequently changing Actor and Worker records in its own control-plane database. `ActorTemplate` defines a checkpointable workload version. Full snapshots preserve process memory, root-filesystem changes, and durable data; data-only snapshots preserve configured durable directories. ([Agent Substrate contributors, 2026](../../sources/agent-substrate/))

## Higher-level systems

[AX](../google-ax/) builds its `Task`, `Workspace`, `Gateway`, and `Model` interface on Substrate’s atespaces, actors, workers, sandbox lifecycle, and network controls. [AX separates orchestration from sandbox execution](../../notes/ax-separates-orchestration-from-sandbox-execution/) describes that boundary. ([Google, 2026](../../sources/google-ax/))

[kagent](../kagent/) announced that it will replace its Deployment-based runtime with Substrate while retaining its Kubernetes-native agent, model, tool, UI, and observability abstractions. The preserved announcement describes a transition and open API proposal, not completed behavior. ([Yarmush, undated](../../sources/kagent-future-of-kagent/))

## Status and security boundary

The project describes itself as early development, not production-ready, and without backward-compatibility guarantees. Its architecture document labels substantial design as aspirational. Its June 2026 threat model says the implementation had little to no security hardening and treats sandbox escape, worker reuse, snapshot integrity, credentials, stale policy, and control-plane separation as risks requiring invariants and mitigation. ([Agent Substrate contributors, 2026](../../sources/agent-substrate/))
