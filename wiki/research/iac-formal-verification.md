---
title: Can Lean and TLA+ verify infrastructure as code for security, performance, and cost?
rkey: iac-formal-verification
date: 2026-09-23
brief: Yes, for explicit plan and system models; security guarantees, performance targets, and budget bounds remain conditional on provider semantics, workload, and prices.
turn_url: https://github.com/smith-wiki/wiki/issues/69
mode: QUESTION_ANSWER
---

## Answer

**Inference:** Yes, but not directly from arbitrary IaC files. Translate a specific configuration or planned resource graph into explicit models; for Terraform, a saved plan can be rendered as JSON, though planned attributes may be unknown until apply. Handle unknowns conservatively, protect plan files containing secrets, and recheck the final plan before applying. ([HashiCorp, undated](../../sources/terraform-plan-json/); [HashiCorp, undated](../../sources/terraform-plan/))

- **Security:** [Lean](../../entities/lean/) can prove modeled access or exposure invariants; [TLA+](../../entities/tla-plus/) can check whether rollout or failure transitions temporarily violate them. Pair this with provider-native policy checks and deployed-access analysis; one policy's validation is not effective authorization. ([AWS, undated](../../sources/aws-iam-access-analyzer-policy-validation/); [AWS, undated](../../sources/aws-iam-access-analyzer-overview/); [AWS, undated](../../sources/aws-iam-policy-evaluation-logic/))
- **Performance:** Model scaling, capacity, and progress under stated workload assumptions, then load-test real latency and throughput in a production-like environment; a formal transition model is not a performance prediction. ([AWS, undated](../../sources/aws-load-test-workload/))
- **Pricing:** Prove a budget inequality over assumed resource counts, usage, and rates; explore scaling scenarios. AWS rates omit some offers, and its calculator estimates only entered usage. ([AWS, undated](../../sources/aws-price-list/); [AWS, undated](../../sources/aws-pricing-calculator/))

[Infrastructure as code](../../concepts/infrastructure-as-code/) and [the assurance boundary](../../notes/iac-assurance-depends-on-model-and-measurements/) carry the method and limits. Neither tool certifies actual provider behavior, future traffic, or the final bill from IaC alone.
