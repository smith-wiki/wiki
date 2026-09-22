---
title: The Future of kagent
summary: Official announcement that kagent is moving its agent runtime to Agent Substrate.
---

## Source

- **Type:** Mutable project announcement
- **Author:** Eitan Yarmush
- **Responsible organization:** kagent
- **Original:** [The Future of kagent](https://kagent.dev/blog/the-future-of-kagent)
- **Publication status:** The page gives no publication date; its body refers to August 2026
- **Suggested citation:** Yarmush, Eitan. “The Future of kagent.” kagent. Accessed September 22, 2026.
- **Assessment:** `recorded`

## Representation

- **ID:** `kagent-future-2026-09-22`
- **Retrieved:** 2026-09-22T06:34:58Z
- **Preserved representation:** `raw/sources/kagent-future-of-kagent-2026-09-22.html`
- **Format:** HTML
- **Fixity:** `sha256:16498947fa776d9f3f74d48fc18f17b5241be3e0b353151a337c118ad12a5d0b`

## Description

First-party announcement explaining kagent's original Kubernetes-agent goals, its SandboxAgent constraints, and the planned migration from a Deployment-based runtime to Agent Substrate.

## Evidence

### `original-requirements`

- **Source states:** kagent aimed to run agents as Kubernetes resources with first-class observability, human-in-the-loop interaction, and reusable agents and tools.
- **Representation:** `kagent-future-2026-09-22`
- **Locator:** Opening section before `The present and the future`, including the three-item requirements list

### `runtime-migration`

- **Source announces:** The project plans to remove its Deployment-based agent runtime and build directly on Agent Substrate.
- **Representation:** `kagent-future-2026-09-22`
- **Locator:** `The present and the future` → passages beginning `At this point` and `This is why we decided`

### `claimed-benefits-and-rollout`

- **Source claims:** The migration provides sandboxing, suspend and resume, resource pools, observability, and sub-100-millisecond start times, with API proposals and migration tooling planned around the v0.10.x line and `main`.
- **Representation:** `kagent-future-2026-09-22`
- **Locator:** `The present and the future` → Agent Substrate benefit list and release-plan paragraphs

## Source criticism

This is a first-party roadmap announcement, not evidence that the migration or performance targets were delivered. Its sub-100-millisecond statement is stronger than the captured Agent Substrate README's documented target and should be treated as an unverified claim.

## Connections

- [kagent](../../entities/kagent/) accumulates cross-source project facts.
- [kagent repository](../kagent/) documents the pre-migration architecture.
- [Agent Substrate repository](../agent-substrate/) documents the target runtime and its maturity limits.
- [Research brief](../../research/google-ax-agent-substrate/) compares the three projects.
