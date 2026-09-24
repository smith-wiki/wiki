---
title: Terraform JSON output format
summary: Machine-readable plans expose proposed resource changes and unknown values for policy analysis.
url: https://developer.hashicorp.com/terraform/internals/json-format
author: "HashiCorp"
kind: documentation
retrieved: 2026-09-23T09:21:01Z
sha256: "a958239b188388d24de4989e4a290300e5a87a0b9269914c7a114e2a1b3427dc"
---

## Overview

HashiCorp's reference for Terraform's JSON output explains how terraform show -json renders a saved plan, state, and configuration for other tools, covering the resource changes a plan proposes, the planned values, how values unknown until apply are marked, and the compatibility rules of format_version. It is undated product documentation not pinned to a Terraform release. It describes the format only, not what cloud providers will do, and anyone checking policies against a plan must handle unknown values explicitly and pin supported format versions. [The terraform plan command](../terraform-plan/) covers drift and sensitive-data caveats.

## Key points

- `terraform plan -out=FILE` writes a binary plan; `terraform show -json FILE` renders a JSON representation of planned changes, state, and configuration for other tools to inspect. (`Introduction`)
- A plan contains `resource_changes` and partial `planned_values`. Attributes not known until apply are omitted from planned values, with `proposed_unknown` marking whether attributes are known. Change actions include creation, update, deletion, and replacement. (`Plan Representation`, descriptions of `planned_values`, `proposed_unknown`, `resource_changes`; `Change Representation`)
- The JSON output has a `format_version` with major/minor compatibility rules; `Values Representation` loses some source type distinctions and treats unknown or null values as absent or null. Callers needing more detail should use the change/configuration representations. (`Introduction`, `format_version`; `Values Representation`)
