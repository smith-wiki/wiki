---
title: kagent repository
summary: Primary repository documentation for a Kubernetes-native framework for building and operating AI agents.
---

## Source

- **Type:** Versioned Git repository
- **Creator and responsible organization:** kagent contributors; the README identifies kagent as a Cloud Native Computing Foundation project
- **Original:** [kagent-dev/kagent](https://github.com/kagent-dev/kagent)
- **Revision:** `e8961b8b582e11c852b176acd9f1687ab8ad66a0`
- **Suggested citation:** kagent contributors. “kagent.” GitHub repository, revision `e8961b8b582e11c852b176acd9f1687ab8ad66a0`. Accessed September 22, 2026.
- **Assessment:** `recorded`

## Representation

- **ID:** `kagent-readme-e8961b8`
- **Retrieved:** 2026-09-22T06:34:58Z
- **Preserved representation:** `raw/sources/kagent-readme-e8961b8.md`
- **Format:** Markdown at revision `e8961b8b582e11c852b176acd9f1687ab8ad66a0`
- **Fixity:** `sha256:e7162053426861c5edb801df94553a5a160ca2da0bb4603e032dbfcbb5a63822`

## Description

Repository README describing kagent's Kubernetes resources, model and tool integrations, architecture, design principles, project status, and contributor workflow.

## Evidence

### `agent-resource-model`

- **Source defines:** An `Agent` custom resource combines a system prompt, tools or other agents, and an LLM configuration; reusable model and tool-server resources supply providers and MCP tools.
- **Representation:** `kagent-readme-e8961b8`
- **Locator:** `Technical Details` → `Core Concepts`

### `architecture-and-principles`

- **Source describes:** A Kubernetes controller, management UI, ADK-based engine, and CLI, with declarative configuration, extensibility, observability, and testability as stated principles.
- **Representation:** `kagent-readme-e8961b8`
- **Locator:** `Technical Details` → `Core Principles` and `Architecture`

### `development-status`

- **Source states:** kagent is in active development and points to a public roadmap.
- **Representation:** `kagent-readme-e8961b8`
- **Locator:** `Roadmap`

## Source criticism

The README is authoritative for the repository at the cited commit, not an independent evaluation of usability, security, interoperability, or production maturity. It does not document the separately announced Agent Substrate migration.

## Connections

- [Research brief](../../research/google-ax-agent-substrate/) compares kagent with AX and Agent Substrate.
- [kagent](../../entities/kagent/) accumulates cross-source project facts.
- [The Future of kagent](../kagent-future-of-kagent/) announces the runtime migration absent from this README.
- [Agent Substrate repository](../agent-substrate/) documents that target runtime.
