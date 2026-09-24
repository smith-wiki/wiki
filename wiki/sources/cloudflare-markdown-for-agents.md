---
title: "Markdown for Agents"
summary: Cloudflare's opt-in edge transform serves origin HTML as Markdown on Accept-header requests.
url: https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/
author: Cloudflare
publisher: "Cloudflare Docs"
kind: webpage
captures:
  - retrieved: 2026-09-24T07:43:49Z
    sha256: "d1813bcf13693ba48668c4643d35cd53e8339acabd58f0831707a1eda90f9af7"
    type: text/html
---

## Overview

Cloudflare's documentation specifies Markdown for Agents as an opt-in transformation on enabled website zones, triggered when a client requests `Accept: text/markdown`. Cloudflare fetches origin HTML and converts it at the edge. This is not a general-purpose local extractor or a headless browser service, and Cloudflare's page gives no structure-fidelity benchmark. Its front matter may include an Open Graph image; that metadata is not a guarantee that figures and captions in the body survive. The documentation's claims are useful for the delivery mechanism and output shape, but not for accuracy against other tools. The separate Browser Run service addresses dynamic rendering and should not be conflated with this transform.

Cloudflare documents the browser-rendered path as a [separate conversion product](../cloudflare-markdown-conversion/).

## Key points
- Conversion requires an enabled Cloudflare zone and `Accept: text/markdown`; the network fetches HTML from origin before conversion. (What is Markdown for Agents; How to use)
- Output is optional metadata front matter, body Markdown after stripping navigation and scripts, and appended JSON-LD if present. (Output format)
- The feature changes body-related HTTP headers and supplies estimated original and Markdown token counts. (Response headers; Token count headers)
- This page promises neither JavaScript execution nor table, code, math, and figure-caption preservation. (How to use; Output format)
