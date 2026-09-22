---
title: Kagi Search API
summary: Official documentation for Kagi's programmable search results, controls, response types, extraction, and billing.
---

- **Original:** [API pricing](https://kagi.com/api/pricing), [Quick Start](https://help.kagi.com/kagi/api/api-portal.html), [Search API](https://help.kagi.com/kagi/api/search.html), and [OpenAPI specification](https://kagi.com/api/docs/_spec/openapi.yaml)
- **Suggested citation:** Kagi. “Search API documentation and pricing.” Accessed September 22, 2026.
- **Responsible organization:** Kagi.
- **Status:** First-party API and billing documentation.
- **Retrieved:** September 22, 2026 between 08:49:56 and 09:28 UTC
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/apiOverview.md` (`sha256:1648db41156a0bbe88edde5d4f7bc8e9ab2e486ceba5a4a4af3515630f810ac1`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/api-quick-start.md` (`sha256:cf43e3772a917a7f668dbf77c4c59c5145e4d1a2ac442959ee8edf74bc89c534`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/api-pricing.md` (`sha256:a5875ce280733f34bf307c6edd96b5cd0ffb558e740bfb703ea7722330029500`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/searchApi.md` (`sha256:18afbd1ba63e768d2593710a708467a0bcfe78518d0c34f48bf28171c6b62b93`)
- **Preserved evidence:** `raw/2026-09-22/kagi-ai-value-assessment/kagi-openapi.yaml` (`sha256:6b438426481d385b6e29d027d4252fe516683e81acce336a2f8d0f04e3d63bdf`)

## Claims and evidence

Search costs $12 per 1,000 requests, or $0.012 each, through a separately funded API balance. A request can select web, image, video, news, or podcast results and apply dates, region, safe-search, account settings, a reusable or inline Lens, up to 1,000 domain-ranking rules, and up to 1,000 regular-expression URL rewrites.

The JSON response separates result types and can include URLs, titles, snippets, timestamps, language metadata, direct answers, adjacent questions, infoboxes, code, public records, archived pages, and Kagi's Small Web results. Pages range from 1 to 10. The result limit ranges from 1 to 1,024 but only caps returned results; it does not make Kagi retrieve more.

Full-page Markdown is not part of the base result. The optional extraction setting replaces snippets with extracted content for up to ten result pages and adds Extract API charges, publicly priced at $4 per 1,000 pages.

## Limits

Kagi calls the results “premium,” but these sources provide no independent quality comparison. A configurable timeout of 0.5–4 seconds trades lower latency for potentially lower-quality or inconsistent results. Search requests, extracted pages, and downstream model tokens are separate cost units.

## Connections

[Kagi Search API value assessment](../../research/kagi-ai-value-assessment/) · [Search API pricing comparison](../search-api-pricing-comparison/) · [Kagi privacy](../kagi-privacy/)
