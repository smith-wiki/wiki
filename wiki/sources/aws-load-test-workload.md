---
title: Load test your workload
summary: AWS recommends production-like load tests with observed latency and throughput rather than inferring performance from configuration.
---

## Source

- **Type:** Mutable official AWS Well-Architected guidance
- **Responsible organization:** Amazon Web Services
- **Original:** [PERF05-BP04 Load test your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_load_test.html)
- **Publication or version status:** No page-level publication date or pinned revision stated
- **Suggested citation:** AWS. "PERF05-BP04 Load test your workload." Accessed September 23, 2026.

## Representation

- **ID:** `aws-load-test-workload-2026-09-23`
- **Retrieved:** 2026-09-23T09:22:59Z
- **Preserved representation:** `raw/sources/aws-load-test-workload-2026-09-23-2026-09-23.html`
- **Readable extraction:** `raw/sources/aws-load-test-workload-2026-09-23-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:de22af980ff8ecba01196a8fb67fabdd45b10ca4eac4947d23c951b55df076df`

## Evidence

### `realistic-load`

- **Source recommends:** Load-test the entire workload in a production-like environment under realistic expected user demand, and go beyond expected demand to identify scaling limits and bottlenecks.
- **Locator:** `PERF05-BP04 Load test your workload`, `Common anti-patterns`; `Implementation guidance`

### `measurement-and-repetition`

- **Source recommends:** Define KPIs such as throughput and response time, generate scenarios, collect metrics, compare results against thresholds, and repeat after system changes. Use synthetic or sanitized production data.
- **Locator:** `Implementation guidance`; `Implementation steps`

## Source criticism

This is prescriptive provider guidance, not an independent benchmark. A load test yields evidence under its chosen conditions, not proof of every future workload or deployment. A configuration or transition model may show conditional progress or capacity properties, but cannot establish measured tail latency without a justified performance model and observations.

## Connections

- [Infrastructure as code](../../concepts/infrastructure-as-code/) needs measurements to assess performance outcomes.
- [IaC assurance note](../../notes/iac-assurance-depends-on-model-and-measurements/) distinguishes proved assumptions from latency observations.
- [IaC research answer](../../research/iac-formal-verification/) includes performance evidence.
