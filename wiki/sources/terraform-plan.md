---
title: terraform plan command
summary: Terraform previews proposed changes but warns about stale speculative plans and sensitive saved-plan contents.
url: https://developer.hashicorp.com/terraform/cli/commands/plan
author: "HashiCorp"
kind: documentation
captures:
  - retrieved: 2026-09-23T09:21:01Z
    sha256: "84cd587d73db2da34cc62085119a1c77e7be8f6e5219b7d960805342ec7df90f"
    type: text/html
---

## Overview

HashiCorp's reference for the terraform plan command explains how Terraform compares configuration with prior and current remote state to propose change actions without executing them, how a saved plan can be applied later, and which options risk incomplete or stale plans, such as skipping refresh or routinely targeting resources. It also warns that saved plans hold configuration, variables, and possibly secrets in cleartext. It is undated product documentation that establishes what Terraform proposes before apply, not what cloud APIs actually do; the machine-readable form of a plan is documented in [Terraform JSON output format](../terraform-plan-json/).

## Key points

- Terraform reads current remote state, compares configuration and prior state, and proposes change actions. Planning alone does not execute them; a saved plan (`-out=FILE`) may be passed to `terraform apply`. (`Introduction`)
- A speculative plan may differ from the final outcome if the target system changes in the meantime, so the final non-speculative plan must be reviewed again. `-refresh=false` ignores external changes and may produce an incomplete or incorrect plan; routine `-target` use may hide drift. (`Introduction`, paragraph beginning "In teams that use a version control"; `Planning Options` > `-refresh=false`; `Resource Targeting`)
- A saved binary plan includes the full configuration, planned change values, input variables, and possibly sensitive data in cleartext despite terminal redaction; treat it as a sensitive artifact. (`Other Options`, `-out=FILENAME`)
