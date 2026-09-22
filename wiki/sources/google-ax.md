---
title: Google AX repository
summary: Primary repository documentation for AX, a declarative agent-workload orchestrator built on Agent Substrate.
---

- **Original:** [google/ax](https://github.com/google/ax)
- **Suggested citation:** Google. “AX.” GitHub repository, revision `d8ed0fe38bceb7842d3c47817d53d16ccdfcb601`. Accessed September 22, 2026.
- **Responsible organization:** Google
- **Status:** First-party repository documentation; the README warns that core concepts, protocols, and specifications may change before a stable release.
- **Revision:** `d8ed0fe38bceb7842d3c47817d53d16ccdfcb601`
- **Retrieved:** September 22, 2026 at 06:22:30 UTC
- **Preserved evidence:** `raw/sources/google-ax-readme-d8ed0fe.md` (`sha256:95d27df32ff26887224cdde472b890952b192ae1fb169f40963c3feefb679db1`)
- **Preserved evidence:** `raw/sources/google-ax-design-d8ed0fe.md` (`sha256:34239d8cf86d167069c6dba77ad0c4463e64366002abf8424b145802775fde70`)
- **Preserved evidence:** `raw/sources/google-ax-concepts-d8ed0fe.md` (`sha256:34c884e16717952427691b24decd6c4ce5dc5015abeba3603b608ff958f713df`)

## Claims and evidence

The repository presents [AX](../../entities/google-ax/) as a Kubernetes-shaped declarative orchestrator for autonomous agent workloads. Its `Task`, `Workspace`, `Gateway`, and `Model` resources describe isolated execution, prepared repositories and tools, network boundaries, and model configuration. AX deliberately treats a task as a small composable execution unit rather than attempting to encode an agent’s complete planning and delegation structure.

AX stores task state in Redis rather than Kubernetes custom resources, uses Redis Streams between its gRPC server and horizontally scaled controllers, and asks [Agent Substrate](../../entities/agent-substrate/) to provision atespaces and actors, assign workers, and apply egress policy. Its task runner prepares workspaces, exposes metadata, and supervises the workload inside each sandbox.

## Limits

These are first-party design and project claims, not independent evidence of scale, throughput, security, or operational maturity. The README says AX is actively changing and likely to introduce breaking changes. The “billions” scale statement is an aspiration not substantiated by benchmark data in the preserved files.

## Connections

[Research brief](../../research/google-ax-agent-substrate/) · [Practical answer](../../research/ax-isolated-repository-maintenance/) · [AX](../../entities/google-ax/) · [AX homepage](../google-ax-homepage/) · [Agent Substrate](../../entities/agent-substrate/) · [AX separates orchestration from sandbox execution](../../notes/ax-separates-orchestration-from-sandbox-execution/)
