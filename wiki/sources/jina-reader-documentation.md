---
title: "Reader API - Jina AI"
summary: Jina Reader API explains browser rendering, Markdown controls, and optional generated image descriptions.
url: https://jina.ai/reader/
author: Jina AI
kind: webpage
captures:
  - retrieved: 2026-09-24T07:43:30Z
    sha256: "3a2fe369075bdf0aa29d8e25cf87d0d5bbc0d729ef6d40d98410da2749f73338"
    type: text/html
---

## Overview

Jina's Reader API documentation describes server-side fetching and conversion of a page into Markdown, with a browser engine that executes client-side JavaScript and a faster direct HTTP alternative. The API exposes image retention, optional generated alternative text, GitHub-flavored Markdown, browser viewport, and custom JavaScript controls. It is authoritative about public service behavior but not a side-by-side structural accuracy benchmark. Generated image descriptions are model output rather than a recovered author's caption, so using them as archival evidence without a label would be misleading. The page discusses commercial offline model containers separately from its public API; those are not proof that a complete open-source self-hosted browser service behaves identically.

The pinned [open-source Reader implementation](../jina-reader-repository/) specifies local Docker operation and the actual Markdown conversion rules.

## Key points
- The FAQ describes default headless-browser fetching and `X-Engine: direct` as a plain HTTP fetch; **Contradiction:** the pinned repository calls its default `auto` a hybrid that can prefer curl. Force browser for JavaScript-dependent pages. (Reader API FAQ: fetching engines; [Reader repository, Using request headers](../jina-reader-repository/))
- Controls cover retained images, GFM output, viewport, and JavaScript before extraction. (Reader API controls)
- `x-with-generated-alt` adds model-written descriptions to images lacking alt text, not recovered original figure captions. (Image Caption; Reader FAQ)
- On-prem offline model containers are a commercial product distinct from the public Reader API. (Reader API FAQ: self-hosting)
