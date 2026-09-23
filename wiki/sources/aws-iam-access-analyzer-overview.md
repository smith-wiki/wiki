---
title: Using IAM Access Analyzer
summary: AWS separates policy validation from scoped analysis of external, internal, and unused access to deployed resources.
url: https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
author: "Amazon Web Services"
kind: documentation
captures:
  - retrieved: 2026-09-23T09:22:59Z
    sha256: "9f0b1f221c6a9c9033937f6879ebc8cbcf4d724200d89ebe78ed061e76f215aa"
    type: text/html
---

## Overview

AWS's IAM User Guide page introduces IAM Access Analyzer and separates its capabilities: basic policy validation against grammar and best practices, custom policy checks against your own security standards, and analyzers that find external, internal, and unused access to deployed resources. It is undated, mutable vendor documentation for AWS administrators, authoritative for what the service says it covers. Analysis is limited to supported resource types in enabled Regions, and findings can lag policy changes, so a clean result is scoped evidence rather than proof of every principal's effective access. [Policy evaluation logic](../aws-iam-policy-evaluation-logic/) explains what request-time authorization also depends on.

## Key points

- Basic policy validation checks grammar and best practices; custom policy checks examine security standards; external, internal, and unused access analysis are distinct capabilities. (`Using AWS Identity and Access Management Access Analyzer`, capability list; `Validating policies against AWS best practices`; `Validating policies against your specified security standards`)
- External analyzers use policy reasoning to identify supported deployed resources shared outside a zone of trust; internal analyzers inspect access to selected resources. External analysis only covers supported resources in enabled Regions and findings can lag policy changes. (`Identifying resources shared with an external entity`, opening paragraphs and `Important`; `Identifying internal access to business-critical resources`)
