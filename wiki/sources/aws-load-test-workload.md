---
title: Load test your workload
summary: AWS recommends production-like load tests with observed latency and throughput rather than inferring performance from configuration.
url: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_load_test.html
author: "Amazon Web Services"
kind: documentation
retrieved: 2026-09-23T09:22:59Z
sha256: "de22af980ff8ecba01196a8fb67fabdd45b10ca4eac4947d23c951b55df076df"
---

## Overview

A best practice from the Performance Efficiency pillar of the AWS Well-Architected Framework, this page recommends load testing the whole workload in a production-like environment under realistic and higher-than-expected demand, with defined metrics such as throughput and response time, and repeating the tests after changes. It is prescriptive, undated vendor guidance, not a benchmark. The wiki uses it for the difference between measured and inferred performance: a load test is evidence only for the conditions it ran under, and a configuration or model cannot establish tail latency without observations.

## Key points

- Load-test the entire workload in a production-like environment under realistic expected user demand, and go beyond expected demand to identify scaling limits and bottlenecks. (`PERF05-BP04 Load test your workload`, `Common anti-patterns`; `Implementation guidance`)
- Define KPIs such as throughput and response time, generate scenarios, collect metrics, compare results against thresholds, and repeat after system changes. Use synthetic or sanitized production data. (`Implementation guidance`; `Implementation steps`)
