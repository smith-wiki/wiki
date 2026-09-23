---
title: Google AX repository
summary: Primary repository documentation for AX, a declarative agent-workload orchestrator built on Agent Substrate.
url: https://github.com/google/ax
author: Google
kind: repository
captures:
  - retrieved: 2026-09-22T06:22:30Z
    sha256: "95d27df32ff26887224cdde472b890952b192ae1fb169f40963c3feefb679db1"
    type: text/markdown
    url: https://raw.githubusercontent.com/google/ax/d8ed0fe38bceb7842d3c47817d53d16ccdfcb601/README.md
  - retrieved: 2026-09-22T06:22:30Z
    sha256: "34239d8cf86d167069c6dba77ad0c4463e64366002abf8424b145802775fde70"
    type: text/markdown
    url: https://raw.githubusercontent.com/google/ax/d8ed0fe38bceb7842d3c47817d53d16ccdfcb601/DESIGN.md
  - retrieved: 2026-09-22T06:22:30Z
    sha256: "34c884e16717952427691b24decd6c4ce5dc5015abeba3603b608ff958f713df"
    type: text/markdown
    url: https://raw.githubusercontent.com/google/ax/d8ed0fe38bceb7842d3c47817d53d16ccdfcb601/docs/concepts.md
---

## Overview

The google/ax repository, captured at commit `d8ed0fe`, documents AX, a Kubernetes-shaped orchestrator for agent workloads. Its README, design document, and concepts guide define the task, workspace, network, and model resources, the Redis-backed control plane, and the handoff of sandboxes to [Agent Substrate](../agent-substrate/). Written by Google for engineers evaluating or running AX, it is authoritative for the design at that commit but not for scale, throughput, security, or operational maturity: the README warns that concepts and protocols are still changing, and the "billions of tasks" language repeated on the [homepage](../google-ax-homepage/) has no benchmark behind it.

## Key points

- `Task` is the smallest isolated execution unit, `Workspace` holds prepared data and tools, `Gateway` is a network boundary, and `Model` is a named provider configuration. (docs/concepts.md, "Task", "Workspace", "Gateway", and "Model")
- AX stores task state in Redis, connects its API server and controllers through Redis Streams, and delegates sandbox provisioning and policy to Agent Substrate. (DESIGN.md, "Architecture" and "Components")
- The CLI applies a multi-resource task, observes it, enters its sandbox, and manages it with Kubernetes-shaped verbs. (README, "Quick start" > "Run your first task" and "CLI usage")
