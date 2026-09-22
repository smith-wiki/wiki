---
title: Google AX repository
summary: Primary repository documentation for AX, a declarative agent-workload orchestrator built on Agent Substrate.
---

## Source

- **Type:** Versioned Git repository
- **Creator and responsible organization:** Google
- **Original:** [google/ax](https://github.com/google/ax)
- **Revision:** `d8ed0fe38bceb7842d3c47817d53d16ccdfcb601`
- **Suggested citation:** Google. “AX.” GitHub repository, revision `d8ed0fe38bceb7842d3c47817d53d16ccdfcb601`. Accessed September 22, 2026.
- **Assessment:** `recorded`

## Representations

All representations were retrieved at 2026-09-22T06:22:30Z as Markdown from the cited revision.

- **`ax-readme-d8ed0fe`:** `raw/sources/google-ax-readme-d8ed0fe.md`; `sha256:95d27df32ff26887224cdde472b890952b192ae1fb169f40963c3feefb679db1`
- **`ax-design-d8ed0fe`:** `raw/sources/google-ax-design-d8ed0fe.md`; `sha256:34239d8cf86d167069c6dba77ad0c4463e64366002abf8424b145802775fde70`
- **`ax-concepts-d8ed0fe`:** `raw/sources/google-ax-concepts-d8ed0fe.md`; `sha256:34c884e16717952427691b24decd6c4ce5dc5015abeba3603b608ff958f713df`

## Description

Repository documentation for AX's task, workspace, network, model, storage, controller, and Agent Substrate integration model at one commit.

## Evidence

### `declarative-resource-model`

- **Source defines:** `Task` as the smallest isolated execution unit, `Workspace` as prepared data and tools, `Gateway` as a network boundary, and `Model` as a named provider configuration.
- **Representation:** `ax-concepts-d8ed0fe`
- **Locator:** `Task`, `Workspace`, `Gateway`, and `Model`

### `control-plane-architecture`

- **Source describes:** AX stores task state in Redis, uses Redis Streams between its API server and controllers, and delegates sandbox provisioning and policy to Agent Substrate.
- **Representation:** `ax-design-d8ed0fe`
- **Locator:** `Architecture` and `Components`

### `task-lifecycle-example`

- **Source shows:** The CLI applying a multi-resource task, observing it, entering its sandbox, and managing it with Kubernetes-shaped verbs.
- **Representation:** `ax-readme-d8ed0fe`
- **Locator:** `Quick start` → `Run your first task`; `CLI usage`

## Source criticism

The repository is authoritative for AX's design at the cited commit, not independent evidence of scale, throughput, security, or operational maturity. The README warns that concepts and protocols are changing; the “billions” scale language is an aspiration without a preserved benchmark.

## Connections

- [Research brief](../../research/google-ax-agent-substrate/) compares AX, kagent, and Agent Substrate.
- [Practical answer](../../research/ax-isolated-repository-maintenance/) maps an isolated maintenance job onto these primitives.
- [AX](../../entities/google-ax/) accumulates cross-source facts about the project.
- [AX homepage](../google-ax-homepage/) is a separate promotional representation of the project.
- [Agent Substrate repository](../agent-substrate/) documents the runtime AX delegates sandbox lifecycle to.
- [AX separates orchestration from sandbox execution](../../notes/ax-separates-orchestration-from-sandbox-execution/) derives the architectural seam.
