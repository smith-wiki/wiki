---
title: The Future of kagent
summary: Official announcement that kagent is moving its agent runtime to Agent Substrate.
url: https://kagent.dev/blog/the-future-of-kagent
author: Eitan Yarmush
publisher: kagent
kind: article
retrieved: 2026-09-22T06:34:58Z
sha256: "16498947fa776d9f3f74d48fc18f17b5241be3e0b353151a337c118ad12a5d0b"
---

## Overview

Writing on the kagent project blog, Eitan Yarmush explains what kagent set out to do, where its SandboxAgent approach hit limits, and why the project will replace its Deployment-based runtime with [Agent Substrate](../agent-substrate/). It is a first-party roadmap for kagent users and contributors; the post has no date, though its text refers to August 2026. It announces plans rather than delivered results, and its sub-100-millisecond start-time claim is stronger than the target in the Agent Substrate README, so it remains unverified. The [kagent repository](../kagent/) still describes the design before the migration.

## Key points

- kagent aimed to run agents as Kubernetes resources with first-class observability, human-in-the-loop interaction, and reusable agents and tools. (Opening section, the three-item requirements list)
- The project plans to remove its Deployment-based agent runtime and build directly on Agent Substrate. (Section "The present and the future", passages beginning "At this point" and "This is why we decided")
- The migration is claimed to bring sandboxing, suspend and resume, resource pools, observability, and start times under 100 milliseconds, with API proposals and migration tooling planned around the v0.10.x line. (Section "The present and the future", benefit list and release-plan paragraphs)
