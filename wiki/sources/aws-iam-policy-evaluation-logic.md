---
title: Policy evaluation logic
summary: AWS request-time authorization depends on request context and multiple interacting policy types.
url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html
author: "Amazon Web Services"
kind: documentation
captures:
  - retrieved: 2026-09-23T09:25:35Z
    sha256: "c89f839064a26a0832b99613f691ef312edd02778f951ff24e577766cb822b2f"
    type: text/html
---

## Overview

AWS's reference on policy evaluation describes how a request is authorized: the principal is authenticated, the applicable policies are chosen from the request context, and identity policies, resource policies, permissions boundaries, and organization policies are combined, with explicit denies overriding allows. It is undated, mutable vendor documentation and a general overview rather than a per-service trace. It shows why a valid or tested single policy does not settle what a principal can actually do, which is the gap [Using IAM Access Analyzer](../aws-iam-access-analyzer-overview/) addresses with separately scoped analyses.

## Key points

- AWS authenticates the principal where necessary, determines applicable policies from request context, and evaluates their combination to allow or deny the request. (`Policy evaluation logic`, opening numbered steps)
- Identity and resource policy permissions can combine; permission boundaries and organization policies constrain grants, and explicit denies override allows in the described combinations. (`Evaluating identity-based policies with resource-based policies`; `Evaluating identity-based policies with permissions boundaries`; `Evaluating identity-based policies with AWS Organizations SCPs or RCPs`)
