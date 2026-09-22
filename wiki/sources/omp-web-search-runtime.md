---
title: OMP web-search runtime
summary: Primary OMP tool documentation plus a point-in-time inspection of the active search configuration and provider.
---

- **Original:** [web_search documentation](omp://tools/web_search.md), [read documentation](omp://tools/read.md), [browser documentation](omp://tools/browser.md), and [settings documentation](omp://settings.md)
- **Suggested citation:** Oh My Pi contributors. “Web search, read, browser, and settings documentation.” OMP `18.1.10`. Accessed September 22, 2026.
- **Responsible organization:** Oh My Pi contributors.
- **Status:** Primary runtime documentation and local configuration inspection.
- **Version:** `omp/18.1.10`
- **Retrieved:** September 22, 2026 at 08:39:16 UTC
- **Preserved evidence:** `raw/2026-09-22/research-tooling-workflow/omp-web-search-capture.md` (`sha256:cb8f2be52e82c7d12675eaa2f673da18afb23406e7dff640ca89a597cba41f5b`)
- **Preserved evidence:** `raw/2026-09-22/research-tooling-workflow/omp-read-capture.md` (`sha256:b0d080c6b37f18b6c199028481e07d773ef58a9d87fb939b3f789a0d9d6a0e47`)
- **Preserved evidence:** `raw/2026-09-22/research-tooling-workflow/omp-browser-capture.md` (`sha256:f5e41070d9553a9bc25ad4bd84ba0a7a149b28e8447a003b42e90d537f179044`)
- **Preserved evidence:** `raw/2026-09-22/research-tooling-workflow/omp-settings-capture.md` (`sha256:34a71f3dfeb2034e7066ef096c3bc1d169049bc8bec057243e3b2c63780df47b`)
- **Preserved evidence:** `raw/2026-09-22/research-tooling-workflow/effective-settings-capture.txt` (`sha256:4ffa48737cba4b34890d18b12c6ce87e85cae41da704003171a81033afeb649f`)
- **Preserved evidence:** `raw/2026-09-22/research-tooling-workflow/search-probe.json` (`sha256:13ef23bc7d2b91058e401a170ceb9ca30ae5862d9a14b3dcf3f92af5d1a75907`)

## Claims and evidence

OMP distinguishes direct reading from discovery and interaction. `read` handles local files, documents, and known URLs; `web_search` sends an open-ended query through the first available provider in an ordered fallback chain; the browser facade is intended for JavaScript execution, authenticated state, and interaction.

At retrieval, `web_search.enabled` was `true`, provider order and exclusion lists were empty, and the per-provider timeout was 60 seconds. A live probe selected Anthropic using `claude-haiku-4-5-20251001`.

## Limits

The selected provider is a point-in-time observation, not a fixed configuration: availability, credentials, failures, and fallback order can change the provider used by a later query. Search output may contain a generated answer, source URLs, or both; discovered pages still need direct inspection before their claims become evidence.

## Connections

[Kagi value assessment](../../research/kagi-ai-value-assessment/) · [Kagi API services](../kagi-api-services/)

