---
title: Calling AWS services and prices using the AWS Price List
summary: AWS pricing catalogs expose SKU-level rates but omit some offer types and remain informational.
---

## Source

- **Type:** Mutable official billing documentation
- **Responsible organization:** Amazon Web Services
- **Original:** [Calling AWS services and prices using the AWS Price List](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html)
- **Publication or version status:** No page-level publication date or pinned price revision stated
- **Suggested citation:** AWS. "Calling AWS services and prices using the AWS Price List." Accessed September 23, 2026.

## Representation

- **ID:** `aws-price-list-2026-09-23`
- **Retrieved:** 2026-09-23T09:21:02Z
- **Preserved representation:** `raw/sources/aws-price-list-2026-09-23.html`
- **Readable extraction:** `raw/sources/aws-price-list-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:5ce3083f8d4eaae0bbae481d740e59d01deac9d01c01f1c47c8094a15f85f106`

## Evidence

### `sku-pricing`

- **Source states:** AWS Price List catalogs products by SKU and attributes. Query API prices can support scenario planning, forecasts, and cost control; Bulk API publishes region/service price files in JSON and CSV.
- **Locator:** `Overview`, `Product`, `Attribute`, `AWS Price List Query API`, `AWS Price List Bulk API`

### `coverage-and-authority`

- **Source warns:** The catalog excludes EC2 Spot prices and time-limited free-tier offers; the Query API excludes Savings Plan prices. Price List API values are informational; where they differ from service pricing pages, the service page governs AWS charges.
- **Locator:** Opening paragraphs below title; `Overview`, note below `AWS Price List Query API`, note below `AWS Price List Bulk API`

## Source criticism

A price catalog gives rates, not a bill: total spend depends on workload usage, resource lifecycle, region, discounts, and charge types. A mathematical budget bound depends on supplied usage assumptions and current applicable rates. The [calculator guide](../aws-pricing-calculator/) explicitly distinguishes an estimate from incurred charges.

## Connections

- [Infrastructure as code](../../concepts/infrastructure-as-code/) connects resource plans with workload and price assumptions.
- [IaC assurance note](../../notes/iac-assurance-depends-on-model-and-measurements/) describes the cost boundary.
- [IaC research answer](../../research/iac-formal-verification/) applies the scope to Lean and TLA+.
