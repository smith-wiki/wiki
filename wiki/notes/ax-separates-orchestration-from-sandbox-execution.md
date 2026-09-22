---
title: AX separates orchestration from sandbox execution
summary: AX declares agent work and policy while Agent Substrate owns stateful sandbox lifecycle and placement.
---

[AX](../../entities/google-ax/) and [Agent Substrate](../../entities/agent-substrate/) divide one runtime stack at a clear boundary. AX describes what an agent task needs through tasks, workspaces, gateways, and model configurations. Its controller translates that desired state into Substrate operations. Substrate owns where and how the resulting stateful actor runs: worker assignment, sandbox activation, snapshotting, suspend and resume, request routing, and lower-level egress enforcement. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))

## Consequence

The split lets AX remain opinionated about developer-facing agent workload composition while Substrate remains relatively agnostic about frameworks and workload semantics. It also keeps high-frequency actor placement and lifecycle changes out of both AX manifests and the Kubernetes API server. Kubernetes continues to provision the slower-changing worker infrastructure. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))

## Boundary of the claim

This is an architectural separation, not proof that the stack reaches its advertised scale, latency, density, or security goals. Both repositories mark the projects as early or unstable, and Substrate’s architecture and threat model explicitly distinguish aspirations and required security invariants from implemented guarantees. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))

## Practical example

[An isolated Go dependency upgrade](../../research/ax-isolated-repository-maintenance/) applies this separation: AX configures and supervises the environment, while the supplied coding agent changes the repository and runs its tests. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))
