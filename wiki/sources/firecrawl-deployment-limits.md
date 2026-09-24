---
title: "Firecrawl open-source and cloud deployment comparison"
summary: "Self-hosting runs core APIs but specialized extraction and LLM-backed capabilities require additional providers and services."
url: https://docs.firecrawl.dev/contributing/open-source-or-cloud
author: "Firecrawl"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:15:01Z
    sha256: "905ae8e456c5af344791ce1d8eb1d19422478614096345b535b786db2336f347"
    type: text/html
---

## Overview

Firecrawl's deployment comparison explains which capabilities a self-hosted open-source stack includes and which supporting services an operator must configure. It is a product-authored operating guide rather than a quality benchmark. The default stack covers core scraping and browser processing; LLM-backed formats require a configured model provider, and specialized extraction or advanced anti-bot processing needs separately operated services. This matters for comparing local PDF conversion with the [managed Parse API](../firecrawl-parse-documentation/): having a shared endpoint or native parser component does not prove identical OCR, formula, layout, or caption output on a self-hosted installation. The guide does not supply an Apple Silicon end-to-end performance measurement or a Firecrawl Parse row in either requested benchmark.

## Key points

- Core scrape, crawl, map, and search APIs are present in the default self-host stack; operators own security and runtime. ("Compare the operating model")
- LLM-backed formats require an OpenAI-compatible provider or Ollama, while specialized extraction services require separate configuration. ("Use open source when"; "Compare the operating model")
- Managed Cloud operates additional services and product surfaces; shared core APIs are not an output-parity guarantee. ("Use Firecrawl Cloud when"; "Compare the operating model")
