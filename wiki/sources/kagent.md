---
title: kagent repository
summary: Primary repository documentation for a Kubernetes-native framework for building and operating AI agents.
url: https://github.com/kagent-dev/kagent
author: kagent contributors
kind: repository
captures:
  - retrieved: 2026-09-22T06:34:58Z
    sha256: "e7162053426861c5edb801df94553a5a160ca2da0bb4603e032dbfcbb5a63822"
    type: text/markdown
    url: https://raw.githubusercontent.com/kagent-dev/kagent/e8961b8b582e11c852b176acd9f1687ab8ad66a0/README.md
---

## Overview

The kagent README, captured at commit `e8961b8`, describes a Cloud Native Computing Foundation project for building and running AI agents as Kubernetes resources: its custom resources, model and tool integrations, architecture, design principles, and development status. Written by the contributors for prospective users and developers, it is authoritative for the repository at that commit, not an independent assessment of usability, security, interoperability, or production maturity. It predates the runtime change announced in [The Future of kagent](../kagent-future-of-kagent/) and does not mention it.

## Key points

- An `Agent` custom resource combines a system prompt, tools or other agents, and an LLM configuration; reusable model and tool-server resources supply providers and MCP tools. (Section "Technical Details" > "Core Concepts")
- kagent consists of a Kubernetes controller, a management UI, an ADK-based engine, and a CLI, and names declarative configuration, extensibility, observability, and testability as principles. (Section "Technical Details" > "Core Principles" and "Architecture")
- The project is in active development and publishes a roadmap. (Section "Roadmap")
