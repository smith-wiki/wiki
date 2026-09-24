---
title: Firecrawl self-hosting guide
summary: Revision-pinned deployment guide details the local browser-backed stack and production caveats.
url: https://raw.githubusercontent.com/firecrawl/firecrawl/fd9c74cc0e3a2d00258248670e4d04db5f75b31d/SELF_HOST.md
author: Firecrawl
kind: repository
captures:
  - retrieved: 2026-09-24T07:48:38Z
    sha256: "087dfa9b1c0e70c07b203f1b2821e357fdea45be12033def713751f77848d356"
    type: text/plain
---

## Overview

Firecrawl's revision-pinned self-hosting guide documents a real local deployment, not just an SDK pointing to the hosted API. Its Compose stack includes workers and Playwright alongside queue, cache, and database services. That makes JavaScript rendering possible without sending page content to Firecrawl Cloud, but it is operationally heavier than a single local extractor. The guide explicitly treats the checked-in Compose configuration as a starting point: the default API lacks authentication and its databases and queues need persistence and backups for production. It also distinguishes optional AI providers and separate scraping engines from the baseline. The [scrape API guide](../firecrawl-scrape-documentation/) describes response formats, but hosted reliability should not be inferred for this baseline.

## Key points
- Baseline scraping includes Playwright with a basic fetch fallback; model-backed features require an additional provider. (Keep the first run simple)
- Compose runs API, workers, Playwright, Redis, RabbitMQ, NuQ PostgreSQL, and optional FoundationDB; only API port 3002 is exposed by default. (What the stack runs)
- Default API authentication is disabled and no persistent volumes are defined for queue/cache/database; production setup requires added controls. (Before production)
