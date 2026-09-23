---
title: terraform plan command
summary: Terraform previews proposed changes but warns about stale speculative plans and sensitive saved-plan contents.
---

## Source

- **Type:** Mutable official CLI reference
- **Responsible organization:** HashiCorp
- **Original:** [terraform plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- **Publication or version status:** No publication date or immutable version specified
- **Suggested citation:** HashiCorp. "terraform plan command." Terraform documentation. Accessed September 23, 2026.

## Representation

- **ID:** `terraform-plan-2026-09-23`
- **Retrieved:** 2026-09-23T09:21:01Z
- **Preserved representation:** `raw/sources/terraform-plan-2026-09-23.html`
- **Readable extraction:** `raw/sources/terraform-plan-2026-09-23.txt`
- **Format:** HTML
- **Fixity:** `sha256:84cd587d73db2da34cc62085119a1c77e7be8f6e5219b7d960805342ec7df90f`

## Evidence

### `plan-is-not-apply`

- **Source states:** Terraform reads current remote state, compares configuration and prior state, and proposes change actions. Planning alone does not execute them; a saved plan (`-out=FILE`) may be passed to `terraform apply`.
- **Locator:** `Introduction`

### `staleness-and-drift`

- **Source warns:** A speculative plan may differ from the final outcome if the target system changes in the meantime, so the final non-speculative plan must be reviewed again. `-refresh=false` ignores external changes and may produce an incomplete or incorrect plan; routine `-target` use may hide drift.
- **Locator:** `Introduction`, paragraph beginning "In teams that use a version control"; `Planning Options` > `-refresh=false`; `Resource Targeting`

### `saved-plan-secrets`

- **Source warns:** A saved binary plan includes the full configuration, planned change values, input variables, and possibly sensitive data in cleartext despite terminal redaction; treat it as a sensitive artifact.
- **Locator:** `Other Options`, `-out=FILENAME`

## Source criticism

This establishes what Terraform proposes before apply, not actual cloud API outcomes, production performance, or final cost. A formal policy over a plan is conditional on both accurate plan interpretation and the plan's relation to the final applied environment.

## Connections

- [Infrastructure as code](../../concepts/infrastructure-as-code/) distinguishes desired, planned, and deployed states.
- [JSON plan format](../terraform-plan-json/) documents the machine-readable check input.
- [IaC research answer](../../research/iac-formal-verification/) uses it for a bounded workflow.
