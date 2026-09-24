---
title: "LlamaCloud self-hosting and BYOC"
summary: "LlamaParse is available in licensed enterprise Kubernetes deployments, not as a public Mac-local inference server."
url: https://developers.llamaindex.ai/llamaparse/self_hosting/
author: "LlamaIndex"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:14:46Z
    sha256: "ae3c960fe44fdc4a81ad8364b5cb2dd1d258471e753e4eb3e3f45611a3614741"
    type: text/html
---

## Overview

LlamaIndex's self-hosting guide explains how enterprises deploy LlamaCloud, including LlamaParse, inside their own Kubernetes environment using a Helm chart. It distinguishes a licensed BYOC installation from a freely installed client SDK or a laptop-local parser. The service can keep document data within the customer's infrastructure, but the guide says LlamaParse uses external OpenAI, Anthropic, or Google models and sends calls to configured API or cloud-provider endpoints. This source is authoritative for offered deployment modes and requirements, not evidence that all processing remains offline or that cloud and BYOC outputs are identical. It complements the [Parse configuration guide](../llamaparse-documentation/) and the local-vs-hosted comparison in the linked wiki analysis.

## Key points

- Enterprise self-hosting includes LlamaParse and the complete platform as a Helm deployment on Kubernetes, not a standalone open-source local model. ("What You Get"; "How It Works")
- Model requests go directly from the customer's cluster to provider APIs or enterprise-cloud endpoints using customer credentials. ("LLM Provider Support")
- Access requires an Enterprise plan and license key. ("Get Started")
