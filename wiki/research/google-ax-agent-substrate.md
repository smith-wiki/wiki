---
title: AX layers declarative orchestration over Agent Substrate
rkey: google-ax-agent-substrate
date: 2026-09-22
brief: AX turns Agent Substrate’s execution machinery into declarative task, workspace, gateway, and model resources.
turn_url: https://github.com/smith-wiki/wiki/issues/28
mode: SOURCE_BRIEF
---

## Source brief

[AX](../../entities/google-ax/) is a Kubernetes-shaped declarative layer over [Agent Substrate](../../entities/agent-substrate/). Task, Workspace, Gateway, and Model manifests describe isolated execution, prepared filesystems and tools, network boundaries, and model configuration. AX controllers reconcile that desired state through Substrate by provisioning atespaces and actors, assigning workers, and applying egress policy. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))

Substrate supplies lower-level execution: it maps many stateful actors over fewer prestarted workers; uses gVisor or microVM sandboxes; snapshots memory and filesystem state for suspend/resume; and routes requests through a proxy that can activate an actor before forwarding to its assigned worker. AX presents these mechanisms as task lifecycle operations. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))

**Uncertainty:** Both projects remain early, first-party evidence. AX claims billions of tasks per cluster; Substrate claims millions of sandboxes, 10× container density, sub-500 ms resume, and over 500 activations per second. Substrate’s architecture calls much aspirational and its README rejects production readiness; AX warns of major pre-stable breaking changes. No independent evidence here validates the scale or performance figures. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))
