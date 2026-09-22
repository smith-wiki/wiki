---
title: Kagi privacy policy
summary: Kagi's first-party statements about search-query logging, billing metadata, and debugging retention.
---

- **Original:** [Your Privacy and Kagi](https://kagi.com/privacy)
- **Suggested citation:** Kagi. “Your Privacy and Kagi.” Accessed September 22, 2026.
- **Responsible organization:** Kagi.
- **Status:** First-party privacy policy and product commitments.
- **Retrieved:** September 22, 2026 at 08:49:56 UTC
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/privacy-browser-extract.md` (`sha256:980d58cbe2025e4d4b8acdc5e37fee8c05f1f7547dc70faf0da794109c53d639`)

## Claims and evidence

Kagi says search queries are logged temporarily for debugging and automatically purged after a short period. Usage volume remains for billing. Sampled load-balancer and virtual-machine logs have seven-day retention, while sampled server-error data in Sentry has 90-day retention; Kagi says temporarily stored browser requests are not linked to an account.

## Limits

These are Kagi's policy statements rather than an independent audit. The policy does not promise Zero Data Retention for Search API requests or separately specify that endpoint's retention. API keys, account metadata, usage volume, and billing records necessarily remain operational data.

## Connections

[Kagi Search API value assessment](../../research/kagi-ai-value-assessment/) · [Kagi Search API](../kagi-api-services/) · [Search API pricing comparison](../search-api-pricing-comparison/)
