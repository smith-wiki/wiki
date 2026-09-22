---
title: Kagi API services
summary: Official documentation for Kagi Search API billing, programmable results, and FastGPT answer generation.
---

- **Original:** [API Portal](https://help.kagi.com/kagi/api/overview.html), [Quick Start](https://help.kagi.com/kagi/api/api-portal.html), [API pricing](https://kagi.com/api/pricing), [Search API](https://help.kagi.com/kagi/api/search.html), and [FastGPT](https://help.kagi.com/kagi/api/fastgpt.html)
- **Suggested citation:** Kagi. “API Portal, Search API, and FastGPT documentation.” Accessed September 22, 2026.
- **Responsible organization:** Kagi.
- **Status:** First-party API and billing documentation.
- **Retrieved:** September 22, 2026 at 08:49:56 UTC
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/apiOverview.md` (`sha256:1648db41156a0bbe88edde5d4f7bc8e9ab2e486ceba5a4a4af3515630f810ac1`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/api-quick-start.md` (`sha256:cf43e3772a917a7f668dbf77c4c59c5145e4d1a2ac442959ee8edf74bc89c534`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/api-pricing.md` (`sha256:a5875ce280733f34bf307c6edd96b5cd0ffb558e740bfb703ea7722330029500`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/searchApi.md` (`sha256:18afbd1ba63e768d2593710a708467a0bcfe78518d0c34f48bf28171c6b62b93`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/fastgpt.md` (`sha256:dff6ff9dd8567d84b423528687c7f8882cf3834e71de4a6b795d2b31e03dd624`)

## Claims and evidence

The Search API provides programmable premium search results and costs $12 per 1,000 queries. Setup requires a separately generated API token and funds in an API balance. The v1 portal tracks API spend, supports limits, and describes pay-per-use invoicing; consumer subscription entitlement is not presented as API credit.

FastGPT produces an LLM answer with web references. Its web-search mode costs $15 per 1,000 queries, uses prepaid API credits, and currently requires web search to remain enabled. Cached API responses are free.

## Limits

Search API charges are separate from consumer-plan allowances. FastGPT costs more per request because it adds generated synthesis, currently requires web search to stay enabled, and rejects attempts to disable it.

## Connections

[Kagi value assessment](../../research/kagi-ai-value-assessment/) · [Kagi plans and Assistant](../kagi-plans-and-assistant/)
