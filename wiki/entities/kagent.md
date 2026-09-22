---
title: kagent
summary: A Kubernetes-native framework for declaratively building, deploying, and operating AI agents.
---

kagent is a Cloud Native Computing Foundation project for building and managing AI agents through Kubernetes custom resources. Its `Agent` resource combines a system prompt, tools or subagents, and an LLM configuration. `ModelConfig` resources describe model providers, and reusable `ToolServer` resources expose MCP tools. ([kagent contributors, 2026](../../sources/kagent/))

## Architecture

The repository documents four core components: a Kubernetes controller that reconciles kagent resources, a web UI, an ADK-based agent engine, and a CLI. It presents the framework as declarative, extensible, observable, and testable, with OpenTelemetry tracing for agents and tools. ([kagent contributors, 2026](../../sources/kagent/))

## Agent Substrate transition

kagent’s maintainers announced that the project will replace its Deployment-based runtime with [Agent Substrate](../agent-substrate/) after first integrating Substrate through a `SandboxAgent` custom resource. The intended boundary leaves kagent’s agent, model, tool, UI, and observability abstractions above Substrate’s sandboxing, snapshots, suspend and resume, network policy, and shared worker pools. ([Yarmush, undated](../../sources/kagent-future-of-kagent/))

## Status

The repository calls kagent active development. The runtime transition and accompanying API redesign were plans rather than completed behavior in the preserved announcement: the proposal remained open, breaking changes were expected, the previous runtime continued on `release/v0.10.x`, and migration guides were forthcoming. The announcement’s scale, security, and latency statements are first-party claims, not independent validation. ([Yarmush, undated](../../sources/kagent-future-of-kagent/))
