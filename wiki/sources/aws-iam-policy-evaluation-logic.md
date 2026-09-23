---
title: Policy evaluation logic
summary: AWS request-time authorization depends on request context and multiple interacting policy types.
---

## Source

- **Type:** Mutable official IAM evaluation reference
- **Responsible organization:** Amazon Web Services
- **Original:** [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- **Publication or version status:** No page-level publication date or pinned version stated
- **Suggested citation:** AWS. "Policy evaluation logic." IAM User Guide. Accessed September 23, 2026.

## Representation

- **ID:** `aws-iam-policy-evaluation-logic-2026-09-23`
- **Retrieved:** 2026-09-23T09:25:35Z
- **Preserved representation:** `raw/sources/aws-iam-policy-evaluation-logic-2026-09-23-2026-09-23.html`
- **Readable extraction:** `raw/sources/aws-iam-policy-evaluation-logic-2026-09-23-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:c89f839064a26a0832b99613f691ef312edd02778f951ff24e577766cb822b2f`

## Evidence

### `request-time-context`

- **Source states:** AWS authenticates the principal where necessary, determines applicable policies from request context, and evaluates their combination to allow or deny the request.
- **Locator:** `Policy evaluation logic`, opening numbered steps

### `combined-policies-and-deny`

- **Source explains:** Identity and resource policy permissions can combine; permission boundaries and organization policies constrain grants, and explicit denies override allows in the described combinations.
- **Locator:** `Evaluating identity-based policies with resource-based policies`; `Evaluating identity-based policies with permissions boundaries`; `Evaluating identity-based policies with AWS Organizations SCPs or RCPs`

## Source criticism

This is a general overview, not a complete per-service authorization trace. It shows why a valid or tested individual IAM policy does not by itself establish the effective permissions of every principal, action, resource, and context in an account. The [Access Analyzer overview](../aws-iam-access-analyzer-overview/) documents additional, separately scoped provider checks.

## Connections

- [Infrastructure as code](../../concepts/infrastructure-as-code/) must account for relevant policies and request context before claiming security.
- [IaC assurance note](../../notes/iac-assurance-depends-on-model-and-measurements/) describes the model boundary.
- [IaC research answer](../../research/iac-formal-verification/) identifies remaining security evidence.
