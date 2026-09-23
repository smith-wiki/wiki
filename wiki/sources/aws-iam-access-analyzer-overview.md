---
title: Using IAM Access Analyzer
summary: AWS separates policy validation from scoped analysis of external, internal, and unused access to deployed resources.
---

## Source

- **Type:** Mutable official IAM documentation
- **Responsible organization:** Amazon Web Services
- **Original:** [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- **Publication or version status:** No page-level publication date or pinned version stated
- **Suggested citation:** AWS. "Using AWS Identity and Access Management Access Analyzer." Accessed September 23, 2026.

## Representation

- **ID:** `aws-iam-access-analyzer-overview-2026-09-23`
- **Retrieved:** 2026-09-23T09:22:59Z
- **Preserved representation:** `raw/sources/aws-iam-access-analyzer-overview-2026-09-23-2026-09-23.html`
- **Readable extraction:** `raw/sources/aws-iam-access-analyzer-overview-2026-09-23-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:9f0b1f221c6a9c9033937f6879ebc8cbcf4d724200d89ebe78ed061e76f215aa`

## Evidence

### `separate-capabilities`

- **Source distinguishes:** Basic policy validation checks grammar and best practices; custom policy checks examine security standards; external, internal, and unused access analysis are distinct capabilities.
- **Locator:** `Using AWS Identity and Access Management Access Analyzer`, capability list; `Validating policies against AWS best practices`; `Validating policies against your specified security standards`

### `deployed-scope`

- **Source describes:** External analyzers use policy reasoning to identify supported deployed resources shared outside a zone of trust; internal analyzers inspect access to selected resources. External analysis only covers supported resources in enabled Regions and findings can lag policy changes.
- **Locator:** `Identifying resources shared with an external entity`, opening paragraphs and `Important`; `Identifying internal access to business-critical resources`

## Source criticism

A scoped deployed-resource analysis is stronger evidence than validation of one policy document for those supported resources, but it is not a universal proof of every principal's request-time authorization. Region, resource-type, analyzer configuration, and finding delays matter. The [IAM evaluation reference](../aws-iam-policy-evaluation-logic/) describes the additional policies and request context involved.

## Connections

- [Infrastructure as code](../../concepts/infrastructure-as-code/) connects proposed policy to deployed access checks.
- [Basic policy validation](../aws-iam-access-analyzer-policy-validation/) has a narrower scope.
- [IaC research answer](../../research/iac-formal-verification/) separates these evidence types.
