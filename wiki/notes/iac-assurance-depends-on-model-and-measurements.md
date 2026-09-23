---
title: IaC assurance depends on the model and measurements
summary: Formal checks can establish conditional security, capacity, or budget claims, not guarantee deployed behavior or future bills.
---

A [Terraform plan](../../sources/terraform-plan/) proposes changes, and its [JSON representation](../../sources/terraform-plan-json/) exposes resource changes for checking. Neither is the deployed environment: planned values can remain unknown, drift can alter the target, and a saved plan may expose secrets. [Infrastructure as code](../../concepts/infrastructure-as-code/) therefore needs an explicit mapping from a specific plan and provider semantics to the model being checked. ([HashiCorp, undated](../../sources/terraform-plan/); [HashiCorp, undated](../../sources/terraform-plan-json/))

## Different questions need different evidence

| Concern | Formal claim worth checking | Remaining evidence |
| --- | --- | --- |
| Security | No modeled policy or network path grants prohibited access | Provider-native analysis, effective runtime identities, drift detection |
| Performance | A modeled capacity bound or scaling sequence meets a stated demand assumption | Load tests and observed latency/throughput under representative traffic |
| Pricing | Cost formula stays below a budget for stated usage bounds and rates | Current applicable prices, full usage categories, discounts, and bills |

## Security boundary

AWS [basic policy validation](../../sources/aws-iam-access-analyzer-policy-validation/) checks grammar and best practices on submitted IAM policies. [Deployed-resource analysis](../../sources/aws-iam-access-analyzer-overview/) is a separate, scoped capability; actual request authorization combines context with multiple policy types and explicit denies. A modeled security invariant is only as complete as the resources, principals, and provider semantics represented. ([AWS, undated](../../sources/aws-iam-policy-evaluation-logic/))

## Performance boundary

A scaling or queue model can test progress under assumed arrival rates and service capacity. It cannot derive observed tail latency from an IaC plan. AWS recommends production-like [load tests](../../sources/aws-load-test-workload/) with realistic demand, measured response time and throughput, and repeat testing after changes.

**Inference:** [Lean](../../entities/lean/) suits precise functions and arithmetic or access predicates; [TLA+](../../entities/tla-plus/) suits update, recovery, scaling, and adversarial interleavings. A completed TLC run only covers configured finite scenarios; a proved theorem covers its formal statement and assumptions. Neither can infer unknown traffic, provider behavior, or future rate changes from source code alone. ([Lean project, 2026](../../sources/lean-validating-proofs/); [Wayne, undated](../../sources/learntla-conceptual-overview/); [AWS, undated](../../sources/aws-pricing-calculator/))

## Price boundary

AWS Price List provides SKU-level rates but excludes some offers and says its API results are informational. AWS Pricing Calculator explicitly bases estimates on entered values and omits taxes. A machine-checked inequality may be mathematically correct for its assumed usage and rates yet fail as a forecast when inputs, discounts, or covered charge categories differ. ([AWS, undated](../../sources/aws-price-list/); [AWS, undated](../../sources/aws-pricing-calculator/))

This extends [the model-to-code boundary](../a-proof-of-a-model-does-not-certify-separate-production-code/) to cloud provider state, demand, and prices. [The IaC research answer](../../research/iac-formal-verification/) applies it to all three concerns.
