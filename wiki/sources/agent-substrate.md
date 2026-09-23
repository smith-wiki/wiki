---
title: Agent Substrate repository
summary: Primary documentation for a stateful actor runtime that multiplexes sandboxed workloads over warm workers.
url: https://github.com/agent-substrate/substrate
author: Agent Substrate contributors
kind: repository
captures:
  - retrieved: 2026-09-22T06:22:30Z
    sha256: "7e0a509b8f54933cf3313210c0132388a040252537f2f55a5ca06fe12769bbfb"
    type: text/markdown
    url: https://raw.githubusercontent.com/agent-substrate/substrate/cdac9baef81dd319b46086d695266e6161e9e592/README.md
  - retrieved: 2026-09-22T06:22:30Z
    sha256: "6e933104b0df4a53242728be70f8ada54711d4a4598e7190714287d322a8192d"
    type: text/markdown
    url: https://raw.githubusercontent.com/agent-substrate/substrate/cdac9baef81dd319b46086d695266e6161e9e592/docs/architecture.md
  - retrieved: 2026-09-22T06:22:30Z
    sha256: "46e2ffd885a31c48db6c8b22deb0cf86a077fcec750db1d395efccdc03cabeb8"
    type: text/markdown
    url: https://raw.githubusercontent.com/agent-substrate/substrate/cdac9baef81dd319b46086d695266e6161e9e592/docs/glossary.md
  - retrieved: 2026-09-22T06:22:30Z
    sha256: "d481f97914bcbd97019ca72146178e51d673020111dcb54b0cfa510050dc17af"
    type: text/markdown
    url: https://raw.githubusercontent.com/agent-substrate/substrate/cdac9baef81dd319b46086d695266e6161e9e592/docs/threat-model.md
---

## Overview

The repository documents Agent Substrate, a framework-agnostic runtime that keeps stateful, sandboxed actors separate from the workers that host them, so idle actors can be snapshotted, suspended, and resumed on warm workers. The README, architecture notes, glossary, and threat model, captured at commit `cdac9ba`, are written by the project's contributors for engineers building agent platforms; the README says it is not an officially supported Google product. They are authoritative for the design at that commit, not for claims about scale, density, or latency: the architecture calls much of itself aspirational, the project says it is not production-ready, and the threat model lists planned rather than completed hardening. [AX](../google-ax/) and [kagent](../kagent-future-of-kagent/) build on this runtime.

## Key points

- Substrate is a framework-agnostic runtime for sandboxed, stateful workloads that advertises worker multiplexing plus suspend and resume. (README, "What is Agent Substrate?" and "Framework Agnostic & Compatibility")
- Kubernetes provisions infrastructure and worker pods, while Substrate's own control plane handles high-frequency actor lifecycle, assignment, routing, and suspend or resume. (Architecture, "A Focused Control Plane" and "Agent-Aware Routing")
- `WorkerPool` and `ActorTemplate` are declarative resources, Actor and Worker are dynamic records, and snapshots are scoped `Full` or `Data`. (Glossary, "Resources", "Records", and "Snapshots")
- The project is not production-ready, its APIs may change, and its threat model records little to no security hardening. (README, "Status and compatibility"; threat model, "Overview")
