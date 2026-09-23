---
title: Infrastructure as code
summary: Declarative resource configuration whose plan can be checked against explicit policies, but is not the deployed cloud environment.
---

Infrastructure as code (IaC) records intended infrastructure resources and changes in versioned configuration. In a concrete Terraform workflow, a plan compares configuration with recorded and refreshed remote state, proposes resource actions, and can be rendered as machine-readable JSON. The plan is an input to verification, not proof that the cloud provider will deploy exactly that state: some planned values remain unknown until apply, speculative plans can become stale, and resource changes outside the tool may cause drift. ([HashiCorp, undated](../../sources/terraform-plan/); [HashiCorp, undated](../../sources/terraform-plan-json/))

## Formal-model inputs

**Inference:** Normalize the planned resource graph, security rules, update steps, capacity limits, and price/usage assumptions into explicit models. [Lean](../../entities/lean/) can check a theorem about static predicates or calculations over the normalized model. [TLA+](../../entities/tla-plus/) can explore state transitions during apply, rollback, scaling, or failure. A proof or completed finite exploration covers its modeled assumptions, not all cloud behavior or a separate implementation. ([Lean project, 2026](../../sources/lean-validating-proofs/); [Lamport, 2021](../../sources/lamport-tla-high-level-view/); [HashiCorp, undated](../../sources/terraform-plan-json/))

## Three concerns

- **Security:** Reject known violations such as an overly permissive policy or unwanted exposure in the modeled resource graph. AWS basic policy validation checks grammar and best practices, while deployed-resource access analysis and effective request-time permissions are distinct questions. ([AWS, undated](../../sources/aws-iam-access-analyzer-policy-validation/); [AWS, undated](../../sources/aws-iam-access-analyzer-overview/); [AWS, undated](../../sources/aws-iam-policy-evaluation-logic/))
- **Performance:** Prove conditional capacity or progress properties of a specified workload and scaling model; measure actual latency and throughput under representative load in a production-like environment. ([AWS, undated](../../sources/aws-load-test-workload/))
- **Pricing:** Prove budget inequalities under specified quantities and rates; reconcile estimates with actual usage and billing. The AWS Price List has coverage limits and informational rates, and AWS Pricing Calculator bases estimates on entered usage. ([AWS, undated](../../sources/aws-price-list/); [AWS, undated](../../sources/aws-pricing-calculator/))

[This turn's research card](../../research/iac-formal-verification/) and [the assurance boundary note](../../notes/iac-assurance-depends-on-model-and-measurements/) distinguish these results.
