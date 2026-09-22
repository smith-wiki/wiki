---
title: Kagi API OpenAPI specification
summary: Kagi's machine-readable API contract for Search request controls, result schemas, pagination, and extraction.
---

## Source

- **Type:** OpenAPI description
- **Creator and publisher:** Kagi
- **Published:** Not stated
- **Original:** [Kagi API OpenAPI specification](https://kagi.com/api/docs/_spec/openapi.yaml)
- **Suggested citation:** Kagi. “Kagi API.” OpenAPI 3.0.0 description, API version `1`. Accessed September 22, 2026.
- **Assessment:** Recorded

## Representation

- **ID:** `kagi-openapi-yaml-2026-09-22T09:20:23Z`
- **Retrieved:** 2026-09-22T09:20:23Z
- **Preserved representation:** `raw/2026-09-22/kagi-ai-value-assessment/kagi-openapi.yaml`
- **Format:** `application/yaml`
- **OAS dialect:** `openapi: 3.0.0`
- **API designation:** `info.version: '1'`
- **Fixity:** `sha256:6b438426481d385b6e29d027d4252fe516683e81acce336a2f8d0f04e3d63bdf`

## Description

Machine-readable contract for Kagi API version 1. This source defines accepted Search parameters and response shapes; it does not demonstrate the behavior of a deployed request.

## Evidence

### `search-request-controls`

- **Source defines:** `POST /search` accepts web, image, video, news, and podcast workflows; date and region filters; reusable or inline Lenses; safe search; domain-ranking rules; and regular-expression URL rewrites.
- **Representation:** `kagi-openapi-yaml-2026-09-22T09:20:23Z`
- **Locator:** JSON Pointer `/paths/~1search/post/requestBody/content/application~1json/schema/properties`

### `search-personalization-bounds`

- **Source defines:** Domain and regular-expression personalization collections each permit up to 1,000 rules; domain actions are `block`, `lower`, `raise`, or `pin`.
- **Representation:** `kagi-openapi-yaml-2026-09-22T09:20:23Z`
- **Locator:** JSON Pointer `/paths/~1search/post/requestBody/content/application~1json/schema/properties/personalizations/properties`

### `search-pagination-and-extraction`

- **Source defines:** Search pages range from 1 through 10; the result `limit` ranges from 1 through 1,024 but does not increase retrieval; optional extraction replaces snippets with page Markdown for up to ten results and incurs separate Extract API charges.
- **Representation:** `kagi-openapi-yaml-2026-09-22T09:20:23Z`
- **Locator:** JSON Pointers `/paths/~1search/post/requestBody/content/application~1json/schema/properties/page`, `/limit`, and `/extract`

### `search-response-kinds`

- **Source defines:** Search responses may separate web, image, video, podcast, news, direct-answer, adjacent-question, infobox, code, public-record, archived-page, related-search, and Small Web result kinds.
- **Representation:** `kagi-openapi-yaml-2026-09-22T09:20:23Z`
- **Locator:** JSON Pointer `/paths/~1search/post/responses/200/content/application~1json/schema/properties/data/properties`

## Source criticism

The description is authoritative for the captured contract, not proof that a deployment implements it or that returned results are relevant. The live URL is mutable and exposes no immutable revision identifier, so evidence remains bound to the preserved representation and digest.

## Connections

- [Kagi Search API value assessment](../../research/kagi-ai-value-assessment/) uses this source for request controls, bounds, and response types.
- [Kagi API pricing](../kagi-api-pricing/) supplies the separately maintained public prices.
