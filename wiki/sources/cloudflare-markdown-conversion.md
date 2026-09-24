---
title: "Markdown Conversion"
summary: Cloudflare distinguishes zone-level HTML conversion from its separately browser-rendered Markdown endpoint.
url: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/
author: Cloudflare
publisher: "Cloudflare Docs"
kind: webpage
captures:
  - retrieved: 2026-09-24T07:49:16Z
    sha256: "9fa157528653652e98256e62ae5b34acc8e4d19c093087a61e6ada5e7ddb981d"
    type: text/html
---

## Overview

Cloudflare's brief Markdown Conversion overview is useful mainly because it distinguishes three separate products: a Workers AI conversion utility, Browser Run's browser-rendered `/markdown` endpoint, and the zone-level Markdown for Agents content negotiation feature. The distinction matters for dynamic pages. The zone feature converts HTML fetched from origin but does not itself claim to execute a browser; Cloudflare directs users who need a rendered application to Browser Run instead. This overview does not evaluate extraction accuracy or technical-structure preservation. For the zone feature's exact request and response contract, see [Markdown for Agents](../cloudflare-markdown-for-agents/). Its claim is a product boundary, not a benchmark.

## Key points
- Browser Run `/markdown` is for dynamic pages needing a real browser before conversion. (Other Markdown conversion features)
- Markdown for Agents serves a converted response through zone-level HTTP content negotiation, separately from Browser Run. (Other Markdown conversion features)
