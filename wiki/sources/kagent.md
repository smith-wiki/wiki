---
title: kagent repository
summary: Primary repository documentation for a Kubernetes-native framework for building and operating AI agents.
---

- **Original:** [kagent-dev/kagent](https://github.com/kagent-dev/kagent)
- **Suggested citation:** kagent contributors. “kagent.” GitHub repository, revision `e8961b8b582e11c852b176acd9f1687ab8ad66a0`. Accessed September 22, 2026.
- **Responsible organization:** kagent contributors; the README identifies kagent as a Cloud Native Computing Foundation project.
- **Status:** First-party repository documentation for a project in active development.
- **Revision:** `e8961b8b582e11c852b176acd9f1687ab8ad66a0`
- **Retrieved:** September 22, 2026 at 06:34:58 UTC
- **Preserved evidence:** `raw/sources/kagent-readme-e8961b8.md`
- **Content ID:** `sha256:e7162053426861c5edb801df94553a5a160ca2da0bb4603e032dbfcbb5a63822`

## Claims and evidence

The repository presents [kagent](../../entities/kagent/) as a Kubernetes-native framework for building, deploying, and managing AI agents. Its `Agent` custom resource combines a system prompt, tools or other agents, and an LLM configuration. `ModelConfig` resources describe model providers, while reusable `ToolServer` resources expose MCP tools.

The documented architecture has four components: a Kubernetes controller that reconciles kagent resources, a management UI, an ADK-based engine that runs agents, and a CLI. The README also identifies declarative configuration, extensibility, observability, and testability as design principles and documents OpenTelemetry tracing.

## Limits

The README is a first-party overview, not an independent evaluation of usability, security, interoperability, or production maturity. It describes the repository at one revision while the project is in active development. It does not document the announced Agent Substrate migration; that future direction appears in the separate [kagent announcement](../kagent-future-of-kagent/).

## Connections

[Research brief](../../research/google-ax-agent-substrate/) · [kagent](../../entities/kagent/) · [The Future of kagent](../kagent-future-of-kagent/) · [Agent Substrate](../../entities/agent-substrate/)
