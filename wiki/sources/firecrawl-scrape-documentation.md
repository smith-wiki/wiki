---
title: "Scrape | Firecrawl"
summary: Firecrawl's hosted scrape API documents rendered extraction and optional HTML, image URL, and Markdown outputs.
url: https://docs.firecrawl.dev/features/scrape
author: Firecrawl
publisher: "Firecrawl Docs"
kind: webpage
captures:
  - retrieved: 2026-09-24T07:42:54Z
    sha256: "7942cc73582f80ef5e04162d00269fd79f9776e573d2d01637c8036d7aaaa191"
    type: text/html
---

## Overview

Firecrawl's first-party scrape guide describes an API that fetches pages, handles dynamic and JavaScript-rendered content, and returns Markdown alongside optional cleaned HTML, raw HTML, image URLs, and other formats. This is authoritative for the advertised API contract, not independent evidence that any particular Markdown construct survives accurately. The raw response format can aid an archive that stores evidence separately from the reading copy. Screenshots are returned by expiring URLs, and the image-list option identifies URLs rather than proving image files or figure captions were archived. A hosted API's proxying and anti-bot reliability should not be assumed for self-hosted deployments. Compare actual output against raw HTML before making a preservation claim.

For the deployment boundary, see the [self-hosting guide](../firecrawl-self-hosting/); for retention and conversion as separate concerns, see [web capture fidelity](../../concepts/web-capture-fidelity/).

## Key points
- The scrape endpoint advertises dynamic and JavaScript-rendered site handling and Markdown output. (Scrape introduction)
- Format options include Markdown, cleaned HTML, raw HTML, raw response bytes via Base64, screenshots, and an image URL list. (Scrape Formats)
- `rawBase64` must be requested alone and contains only the URL's original response body, not CSS or image subresources; screenshot URLs expire after 24 hours. (Scrape Formats)
- The documentation offers no construct-level guarantees for Markdown tables, code, math, or figure captions. (Scrape Formats)
