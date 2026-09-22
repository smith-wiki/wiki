---
title: Can AX orchestrate an isolated Go dependency upgrade?
rkey: ax-isolated-repository-maintenance
date: 2026-09-22
brief: AX can isolate and supervise a supplied coding agent that upgrades a Go repository and runs its tests.
turn_url: https://github.com/smith-wiki/wiki/issues/30
mode: QUESTION_ANSWER
---

## Answer

Yes. [AX](../../entities/google-ax/) can orchestrate a supplied coding-agent image and command to upgrade dependencies in one Go repository and run its tests inside an isolated, resumable [Agent Substrate](../../entities/agent-substrate/) environment. AX supplies orchestration and execution boundaries; the coding agent decides and performs the upgrade. ([Google, 2026](../../sources/google-ax/); [AX project, undated](../../sources/google-ax-homepage/); [AX separates orchestration from sandbox execution](../../notes/ax-separates-orchestration-from-sandbox-execution/))

A `Workspace` clones the repository and can bootstrap the Go toolchain from a plain-language goal. A `Task` runs the agent command in its sandbox with CPU and memory limits. Its `Gateway` should allowlist only the required Git, model-provider, and package hosts, while `Model` centralizes provider, model, parameters, and credential references. `ax watch` shows lifecycle progress; `ax ssh` permits inspection when debugging is enabled. Suspend the task while a human reviews the diff and test result, then resume it without discarding task state. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))

**Uncertainty:** AX and Substrate are early. The preserved first-party evidence does not establish production readiness, nor independently verify advertised scale, isolation, or security. ([Google, 2026](../../sources/google-ax/); [Agent Substrate contributors, 2026](../../sources/agent-substrate/))
