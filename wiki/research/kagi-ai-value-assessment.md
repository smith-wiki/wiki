---
title: Is Kagi worth paying for personally and for automated research?
rkey: kagi-ai-value-assessment
date: 2026-09-22
brief: Start cheaply for personal search, and evaluate Kagi’s separately billed Search API for automated research.
turn_url: https://github.com/smith-wiki/wiki/issues/40
mode: QUESTION_ANSWER
---

## Answer

**Recommendation:** start with Starter: $5/month buys 300 searches and 300 standard-model AI interactions, enough to test Search and web-assisted Assistant personally. Upgrade only if usage proves it: Professional is $10/month for unlimited Search, Summarize, and standard-model Assistant; Ultimate is $25/month and mainly adds premium Assistant models. ([Kagi plans and Assistant](../../sources/kagi-plans-and-assistant/))

Treat automation separately. OMP uses the metered Search API with `KAGI_API_KEY` or a stored Kagi credential, not consumer Assistant; Ultimate is unnecessary, and subscriptions should not be assumed to cover API spend. Use Search API results for discovery. FastGPT instead generates an LLM answer with references for $15 per 1,000 prepaid web-search queries. Either way, fetch, inspect, and preserve primary sources rather than treating snippets or generated answers as evidence. ([Kagi API services](../../sources/kagi-api-services/); [OMP web search](../../sources/omp-web-search-runtime/))

Privacy helps, but is not anonymity: Kagi says it loads no analytics or telemetry, does not track result clicks, and does not use Assistant data to train models; threads default to deletion after 24 hours. Paid accounts require some data, sampled debug logs persist 7 or 90 days, and AI may involve third-party providers. ([Kagi privacy](../../sources/kagi-privacy/))
