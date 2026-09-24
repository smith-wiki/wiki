---
title: Kagi API OpenAPI specification
summary: Kagi's machine-readable API contract for Search request controls, result schemas, pagination, and extraction.
url: https://kagi.com/api/docs/_spec/openapi.yaml
author: Kagi
kind: specification
retrieved: 2026-09-22T09:20:23Z
sha256: "6b438426481d385b6e29d027d4252fe516683e81acce336a2f8d0f04e3d63bdf"
---

## Overview

Kagi's machine-readable contract for API version 1, written in OpenAPI 3.0.0, defines what the Search endpoint accepts and returns: search types, filters, Lenses, domain-ranking and URL-rewrite rules, pagination, optional page extraction, and the kinds of results a response can contain. Published by Kagi for developers, it is authoritative for the captured contract but shows neither that a deployment behaves this way nor that results are relevant. The live file changes without a revision identifier, so claims rest on the preserved capture. Prices for the same operations are on [Kagi API pricing](../kagi-api-pricing/).

## Key points

- `POST /search` accepts web, image, video, news, and podcast searches, date and region filters, reusable or inline Lenses, safe search, domain-ranking rules, and regular-expression URL rewrites. (JSON Pointer `/paths/~1search/post/requestBody/content/application~1json/schema/properties`)
- Domain and regular-expression personalization lists each allow up to 1,000 rules, and domains can be blocked, lowered, raised, or pinned. (`.../schema/properties/personalizations/properties`)
- Pages run from 1 to 10; `limit` ranges from 1 to 1,024 but does not retrieve more; optional extraction replaces snippets with page Markdown for up to ten results and is charged separately as Extract. (`.../schema/properties/page`, `/limit`, and `/extract`)
- A response can separate web, image, video, podcast, news, direct-answer, adjacent-question, infobox, code, public-record, archived-page, related-search, and Small Web results. (`/paths/~1search/post/responses/200/content/application~1json/schema/properties/data/properties`)
