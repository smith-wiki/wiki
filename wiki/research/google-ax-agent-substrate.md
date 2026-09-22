---
title: AX and kagent layer declarative agents over Agent Substrate
rkey: google-ax-agent-substrate
date: 2026-09-22
brief: AX and kagent expose different declarative agent abstractions while sharing Agent Substrate’s sandbox lifecycle foundation.
turn_url: https://github.com/smith-wiki/wiki/issues/28
mode: SOURCE_BRIEF
---

## Source brief

[AX](../../entities/google-ax/) and [kagent](../../entities/kagent/) offer declarative layers over [Agent Substrate](../../entities/agent-substrate/). AX defines Task, Workspace, Gateway, and Model resources for execution, environments and tools, networks, and models; its homepage positions these as agentic abstractions and generative runtime components. kagent defines Agent, ModelConfig, and ToolServer resources plus observability. AX uses Substrate today; kagent says SandboxAgent support preceded a planned replacement of its Deployment-based runtime. ([Google, 2026](../../sources/google-ax/); [AX project, undated](../../sources/google-ax-homepage/); [kagent contributors, 2026](../../sources/kagent/); [Yarmush, undated](../../sources/kagent-future-of-kagent/))

Substrate multiplexes stateful actors over fewer warm workers in gVisor or microVM sandboxes. Snapshots preserve memory and filesystem state for suspend/resume; a proxy resumes and routes each actor to its assigned worker. ([Agent Substrate contributors, 2026](../../sources/agent-substrate/))

**Uncertainty:** kagent’s transition has breaking changes and an open API proposal; this evidence does not show completion. All sources are first-party. Substrate is early, not production-ready, and partly aspirational. Claims about billions of tasks, density, resume speed, isolation, and security remain independently unverified. ([AX project, undated](../../sources/google-ax-homepage/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/); [Yarmush, undated](../../sources/kagent-future-of-kagent/))
