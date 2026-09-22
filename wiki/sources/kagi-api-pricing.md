---
title: Kagi API pricing
summary: Kagi's public price list and advertised capabilities for Search and Extract API requests.
---

## Source

- **Type:** Mutable pricing webpage
- **Creator and publisher:** Kagi
- **Published:** Not stated
- **Original:** [API pricing](https://kagi.com/api/pricing)
- **Suggested citation:** Kagi. “API pricing.” Accessed September 22, 2026.
- **Assessment:** Recorded

## Representation

- **ID:** `kagi-api-pricing-web-2026-09-22T08:51:33Z`
- **Retrieved:** 2026-09-22T08:51:33Z
- **Preserved representation:** `raw/2026-09-22/kagi-ai-value-assessment/api-pricing.md`
- **Format:** Markdown extraction from `text/html`
- **Fixity:** `sha256:a5875ce280733f34bf307c6edd96b5cd0ffb558e740bfb703ea7722330029500`

## Description

Kagi's provider-maintained price list for its commercial APIs. The captured page describes Search, Extract, and enterprise offerings; it is not an invoice or a historical price series.

## Evidence

### `search-request-price`

- **Source states:** Search costs $12 per 1,000 requests and is billed according to use.
- **Representation:** `kagi-api-pricing-web-2026-09-22T08:51:33Z`
- **Locator:** `Search` price card
- **Exact:** “$12 /1k requests”

### `search-capabilities`

- **Source states:** Search covers web, images, news, videos, and podcasts and supports Lenses, country and language filters, domain ranking, custom URL rules, and optional full-content snippets.
- **Representation:** `kagi-api-pricing-web-2026-09-22T08:51:33Z`
- **Locator:** `Search` feature list

### `extract-page-price`

- **Source states:** Extract costs $4 per 1,000 pages, accepts up to ten URLs per request, and returns clean Markdown.
- **Representation:** `kagi-api-pricing-web-2026-09-22T08:51:33Z`
- **Locator:** `Extract` price card and feature list
- **Exact:** “$4 /1k pages”

## Source criticism

This is authoritative for Kagi's advertised public prices at capture time but is mutable first-party sales material. It does not preserve earlier prices, define every billable edge case, or independently establish result quality.

## Connections

- [Kagi Search API value assessment](../../research/kagi-ai-value-assessment/) uses this source for Kagi's public Search and Extract prices.
- [Kagi OpenAPI specification](../kagi-openapi-specification/) supplies the request and response contract that the pricing page summarizes.
