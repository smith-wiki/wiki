---
title: Agent Substrate repository
summary: Primary repository documentation for a stateful actor runtime that multiplexes sandboxed workloads over warm workers.
---

- **Original:** [agent-substrate/substrate](https://github.com/agent-substrate/substrate)
- **Suggested citation:** Agent Substrate contributors. “Agent Substrate.” GitHub repository, revision `cdac9baef81dd319b46086d695266e6161e9e592`. Accessed September 22, 2026.
- **Responsible organization:** Agent Substrate contributors; the README says this is not an officially supported Google product.
- **Status:** First-party repository documentation for an early-development project that disclaims production readiness and backward compatibility.
- **Revision:** `cdac9baef81dd319b46086d695266e6161e9e592`
- **Retrieved:** September 22, 2026 at 06:22:30 UTC
- **Preserved evidence:** `raw/sources/agent-substrate-readme-cdac9ba.md` (`sha256:7e0a509b8f54933cf3313210c0132388a040252537f2f55a5ca06fe12769bbfb`)
- **Preserved evidence:** `raw/sources/agent-substrate-architecture-cdac9ba.md` (`sha256:6e933104b0df4a53242728be70f8ada54711d4a4598e7190714287d322a8192d`)
- **Preserved evidence:** `raw/sources/agent-substrate-glossary-cdac9ba.md` (`sha256:46e2ffd885a31c48db6c8b22deb0cf86a077fcec750db1d395efccdc03cabeb8`)
- **Preserved evidence:** `raw/sources/agent-substrate-threat-model-cdac9ba.md` (`sha256:d481f97914bcbd97019ca72146178e51d673020111dcb54b0cfa510050dc17af`)

## Claims and evidence

[Agent Substrate](../../entities/agent-substrate/) is a framework-agnostic execution runtime for stateful, sandboxed workloads. It maps many actors onto fewer pre-started workers, snapshots actor state when work is suspended, restores that state on resume, and routes incoming traffic to the actor’s current worker. Kubernetes provisions worker infrastructure, while Substrate’s own control plane handles high-frequency actor lifecycle and assignment state.

The glossary distinguishes declarative `WorkerPool` and immutable `ActorTemplate` definitions from dynamic Actor and Worker records. Full snapshots can preserve memory, root-filesystem changes, and durable directories; data-only snapshots preserve configured volumes. The threat model identifies worker reuse, snapshots, sandbox escape, stale policy, credentials, and control-plane separation as security boundaries rather than proven guarantees.

## Limits

The architecture document explicitly says much of its design is aspirational. Performance, density, and scale figures in the README are first-party claims, while north-star metrics in the architecture document are targets. The README says the project is not production-ready; the threat model says it had little to no security hardening at its June 2026 update.

## Connections

[Research brief](../../research/google-ax-agent-substrate/) · [Agent Substrate](../../entities/agent-substrate/) · [AX](../../entities/google-ax/) · [kagent](../../entities/kagent/) · [AX separates orchestration from sandbox execution](../../notes/ax-separates-orchestration-from-sandbox-execution/)
