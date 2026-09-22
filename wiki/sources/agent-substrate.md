---
title: Agent Substrate repository
summary: Primary repository documentation for a stateful actor runtime that multiplexes sandboxed workloads over warm workers.
---

## Source

- **Type:** Versioned Git repository
- **Creator and responsible organization:** Agent Substrate contributors; the README says this is not an officially supported Google product
- **Original:** [agent-substrate/substrate](https://github.com/agent-substrate/substrate)
- **Revision:** `cdac9baef81dd319b46086d695266e6161e9e592`
- **Suggested citation:** Agent Substrate contributors. “Agent Substrate.” GitHub repository, revision `cdac9baef81dd319b46086d695266e6161e9e592`. Accessed September 22, 2026.
- **Assessment:** `recorded`

## Representations

All representations were retrieved at 2026-09-22T06:22:30Z as Markdown from the cited revision.

- **`substrate-readme-cdac9ba`:** `raw/sources/agent-substrate-readme-cdac9ba.md`; `sha256:7e0a509b8f54933cf3313210c0132388a040252537f2f55a5ca06fe12769bbfb`
- **`substrate-architecture-cdac9ba`:** `raw/sources/agent-substrate-architecture-cdac9ba.md`; `sha256:6e933104b0df4a53242728be70f8ada54711d4a4598e7190714287d322a8192d`
- **`substrate-glossary-cdac9ba`:** `raw/sources/agent-substrate-glossary-cdac9ba.md`; `sha256:46e2ffd885a31c48db6c8b22deb0cf86a077fcec750db1d395efccdc03cabeb8`
- **`substrate-threat-model-cdac9ba`:** `raw/sources/agent-substrate-threat-model-cdac9ba.md`; `sha256:d481f97914bcbd97019ca72146178e51d673020111dcb54b0cfa510050dc17af`

## Description

Repository documentation for Agent Substrate's actor lifecycle, control plane, snapshots, routing, resource model, and security design at one commit.

## Evidence

### `runtime-positioning`

- **Source states:** Agent Substrate is a framework-agnostic runtime for sandboxed, stateful workloads and advertises worker multiplexing plus suspend and resume.
- **Representation:** `substrate-readme-cdac9ba`
- **Locator:** `What is Agent Substrate?` and `Framework Agnostic & Compatibility`

### `control-plane-separation`

- **Source describes:** Kubernetes provisions infrastructure and worker pods, while Substrate's focused control plane handles high-frequency actor lifecycle, assignment, routing, and suspend or resume operations.
- **Representation:** `substrate-architecture-cdac9ba`
- **Locator:** `Core Concepts and Approaches` → `A Focused Control Plane` and `Agent-Aware Routing`

### `resource-and-snapshot-model`

- **Source defines:** `WorkerPool` and `ActorTemplate` as declarative resources, Actor and Worker as dynamic records, and `Full` versus `Data` snapshot scopes.
- **Representation:** `substrate-glossary-cdac9ba`
- **Locator:** `Resources (declarative)`, `Records (dynamic state, in the control-plane store)`, and `Snapshots`

### `security-maturity`

- **Source states:** The project is not production-ready, its APIs may change, and its threat model had little to no security hardening at the captured revision.
- **Representations:** `substrate-readme-cdac9ba`; `substrate-threat-model-cdac9ba`
- **Locators:** `Status and compatibility`; `Overview`

## Source criticism

The repository is authoritative for its own design at the cited commit, not independent evidence of scale, density, latency, or security. The architecture labels much of itself aspirational; its north-star metrics are targets, and the threat model records planned mitigations rather than completed hardening.

## Connections

- [Research brief](../../research/google-ax-agent-substrate/) compares this runtime with AX and kagent.
- [Practical answer](../../research/ax-isolated-repository-maintenance/) applies its lifecycle model to a repository-maintenance task.
- [Agent Substrate](../../entities/agent-substrate/) accumulates cross-source facts about the project.
- [AX](../../entities/google-ax/) and [kagent](../../entities/kagent/) depend on this runtime.
- [AX separates orchestration from sandbox execution](../../notes/ax-separates-orchestration-from-sandbox-execution/) derives a reusable architectural distinction from the preserved evidence.
