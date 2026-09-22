---
title: Your Privacy and Kagi
summary: Kagi's policy statements about search-query logging, billing metadata, and debugging retention.
---

## Source

- **Type:** Mutable privacy policy
- **Creator and publisher:** Kagi
- **Published:** Not stated; the page describes itself as a living document
- **Original:** [Your Privacy and Kagi](https://kagi.com/privacy)
- **Suggested citation:** Kagi. “Your Privacy and Kagi.” Accessed September 22, 2026.
- **Assessment:** Recorded

## Representation

- **ID:** `kagi-privacy-web-2026-09-22T08:49:56Z`
- **Retrieved:** 2026-09-22T08:49:56Z
- **Preserved representation:** `raw/2026-09-22/kagi-ai-value-assessment/privacy-browser-extract.md`
- **Format:** Markdown browser extraction from `text/html`
- **Fixity:** `sha256:980d58cbe2025e4d4b8acdc5e37fee8c05f1f7547dc70faf0da794109c53d639`

## Description

Kagi's public privacy policy for its paid services. It describes browser and server data, debugging retention, billing records, AI services, security, and privacy-oriented access options.

## Evidence

### `temporary-search-query-logging`

- **Source states:** Search queries may be logged temporarily for debugging and are automatically purged after a short period.
- **Representation:** `kagi-privacy-web-2026-09-22T08:49:56Z`
- **Locator:** `Payment information`

### `debugging-retention`

- **Source states:** Sampled load-balancer and virtual-machine logs have seven-day retention, while sampled Sentry server-error data has 90-day retention; temporarily stored browser requests are not linked to an account.
- **Representation:** `kagi-privacy-web-2026-09-22T08:49:56Z`
- **Locator:** `On our servers` → `Debugging retention periods`

### `billing-usage-volume`

- **Source states:** Kagi retains usage volume for billing while treating search-query text as temporary debugging data.
- **Representation:** `kagi-privacy-web-2026-09-22T08:49:56Z`
- **Locator:** `Payment information`

## Source criticism

This is Kagi's policy rather than an independent audit. It does not separately specify Search API retention or promise Zero Data Retention for that endpoint. The policy is mutable, and its debugging language leaves the exact meaning of “short period” unspecified for search-query text.

## Connections

- [Kagi Search API value assessment](../../research/kagi-ai-value-assessment/) uses this source to distinguish temporary query logging from a Zero Data Retention claim.
- [Brave Search API announcement](../brave-search-api-announcement/) supplies Brave's contrasting first-party retention statement.
