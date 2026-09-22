---
title: AX homepage
summary: Official AX product page describing its task model, scale ambition, and generative-platform positioning.
---

## Source

- **Type:** Mutable product webpage
- **Responsible organization:** Google
- **Original:** [agentexecutor.io](https://agentexecutor.io/)
- **Publication or version status:** No publication date or page version stated
- **Suggested citation:** Google. “AX.” AgentExecutor.io. Accessed September 22, 2026.
- **Assessment:** `recorded`

## Representation

- **ID:** `ax-homepage-2026-09-22`
- **Retrieved:** 2026-09-22T06:37:21Z
- **Preserved representation:** `raw/sources/agentexecutor-ax-homepage-2026-09-22.html`
- **Format:** HTML
- **Fixity:** `sha256:804ee320d0ddebc08a82ba6a1145774f6423f521da8213bd56ba0d28001235cf`

## Description

Official marketing page presenting AX as infrastructure for declarative agent tasks, repository-driven configuration, large-scale execution, and generated agent systems.

## Evidence

### `declared-task-workflow`

- **Source states and shows:** Users declare an agentic task and manage it with apply, watch, SSH, suspend, resume, and delete commands.
- **Representation:** `ax-homepage-2026-09-22`
- **Locator:** Hero heading `Declare an agentic task. AX runs it at scale.` and its terminal example

### `workload-and-scale-positioning`

- **Source claims:** Agents are a distinct workload and AX scales from one to billions of tasks.
- **Representation:** `ax-homepage-2026-09-22`
- **Locator:** `Why AX` → `Agents are a new kind of workload.`; `How it works` → `Scales up to billions of tasks.`

### `generative-platform-positioning`

- **Source states:** AX is intended to let agents create and operate other agents by exposing its resources as tools.
- **Representation:** `ax-homepage-2026-09-22`
- **Locator:** `Generative platform`

## Source criticism

This is a first-party promotional page. It provides no benchmark for the “billions” claim, and its production-oriented language is in tension with the captured repository's warning that AX is pre-stable and changing. The page can establish product positioning, not operational maturity.

## Connections

- [AX](../../entities/google-ax/) accumulates cross-source facts about the project.
- [Google AX repository](../google-ax/) preserves the more qualified technical documentation.
- [Research brief](../../research/google-ax-agent-substrate/) compares AX with kagent and Agent Substrate.
