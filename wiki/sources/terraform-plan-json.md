---
title: Terraform JSON output format
summary: Machine-readable plans expose proposed resource changes and unknown values for policy analysis.
---

## Source

- **Type:** Mutable official product reference
- **Responsible organization:** HashiCorp
- **Original:** [JSON Output Format Overview](https://developer.hashicorp.com/terraform/internals/json-format)
- **Publication or version status:** No publication date; documentation path is not pinned to a release
- **Suggested citation:** HashiCorp. "JSON Output Format Overview." Terraform documentation. Accessed September 23, 2026.

## Representation

- **ID:** `terraform-plan-json-2026-09-23`
- **Retrieved:** 2026-09-23T09:21:01Z
- **Preserved representation:** `raw/sources/terraform-plan-json-2026-09-23.html`
- **Readable extraction:** `raw/sources/terraform-plan-json-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:a958239b188388d24de4989e4a290300e5a87a0b9269914c7a114e2a1b3427dc`

## Evidence

### `machine-readable-plan`

- **Source states:** `terraform plan -out=FILE` writes a binary plan; `terraform show -json FILE` renders a JSON representation of planned changes, state, and configuration for other tools to inspect.
- **Locator:** `Introduction`

### `change-and-unknown-values`

- **Source documents:** A plan contains `resource_changes` and partial `planned_values`. Attributes not known until apply are omitted from planned values, with `proposed_unknown` marking whether attributes are known. Change actions include creation, update, deletion, and replacement.
- **Locator:** `Plan Representation`, descriptions of `planned_values`, `proposed_unknown`, `resource_changes`; `Change Representation`

### `format-and-sensitive-data`

- **Source documents:** The JSON output has a `format_version` with major/minor compatibility rules; `Values Representation` loses some source type distinctions and treats unknown or null values as absent or null. Callers needing more detail should use the change/configuration representations.
- **Locator:** `Introduction`, `format_version`; `Values Representation`

## Source criticism

This documents a Terraform format, not a cloud provider's actual security or performance. A policy checker must handle unknown values explicitly rather than treating an omitted value as safe, and must pin supported format versions. See the separate [plan command documentation](../terraform-plan/) for drift, preview, and sensitive-plan caveats.

## Connections

- [Infrastructure as code](../../concepts/infrastructure-as-code/) explains how to connect a generated plan to formal checks.
- [IaC research answer](../../research/iac-formal-verification/) uses this as a concrete, not universal, IaC adapter.
- [Terraform plan command](../terraform-plan/) covers the pre-apply boundary.
