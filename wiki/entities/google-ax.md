---
title: AX
summary: A declarative control plane for composing isolated agent tasks over Agent Substrate.
---

AX is an open-source, Kubernetes-shaped orchestrator for agent workloads. It exposes four `ax.io/v1alpha1` resources: `Task` for an isolated execution unit, `Workspace` for repositories and tools, `Gateway` for network policy, and `Model` for model-provider configuration. The design keeps the task primitive small so an agent can compose a tree of tasks without AX modeling the agent’s internal planning structure. ([Google, 2026](../../sources/google-ax/))

## Control plane

The `ax-server` gRPC service validates manifests, stores state in Redis, and publishes events. Horizontally scaled `ax-controller` workers consume Redis Streams and reconcile desired task state. An `ax-task-runner` inside each sandbox prepares workspaces, exposes metadata, and supervises the task command. This avoids representing large volumes of short-lived task state as Kubernetes custom resources. ([Google, 2026](../../sources/google-ax/))

## Execution boundary

AX delegates atespace provisioning, actor lifecycle, worker assignment, sandboxing, and egress enforcement to [Agent Substrate](../agent-substrate/). This makes AX the workload-facing orchestration layer and Substrate the lower-level execution substrate; see [AX separates orchestration from sandbox execution](../../notes/ax-separates-orchestration-from-sandbox-execution/). ([Google, 2026](../../sources/google-ax/))

## Status

The repository warns that AX’s core concepts, protocols, and specifications are still changing and may break before a stable release. Its claims about running billions of tasks are not benchmarked in the preserved repository documentation. ([Google, 2026](../../sources/google-ax/))

**Contradiction:** The public homepage says AX was “built for production,” while the repository warns of likely pre-stable breaking changes and Agent Substrate says its underlying runtime is not production-ready. The homepage’s scale and sub-second-resumption claims are promotional and unverified in the preserved evidence. ([AX project, undated](../../sources/google-ax-homepage/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))

## Practical example

[AX can orchestrate an isolated Go dependency upgrade](../../research/ax-isolated-repository-maintenance/) by preparing the repository and toolchain, limiting the supplied coding agent’s network and compute access, exposing its progress for inspection, and preserving task state during human review. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))
