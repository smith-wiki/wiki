---
title: "Browser, Crawler & LLM Config - Crawl4AI Documentation (v0.9.x)"
summary: Crawl4AI's local browser and crawl configuration includes browser engine, JavaScript, and waiting controls.
url: https://docs.crawl4ai.com/core/browser-crawler-config/
author: Crawl4AI project
kind: webpage
captures:
  - retrieved: 2026-09-24T07:48:59Z
    sha256: "ee27b745103e9a673ca07155f05afce42062efb443d2a79e1bc0f18ad36aeced"
    type: text/html
---

## Overview

Crawl4AI's browser configuration guide describes how a local Python crawler drives a headless browser before applying HTML and Markdown extraction. Its browser settings expose engine selection, viewport, user agent, and execution mode; crawler settings control JavaScript execution, CSS waiting, page-scrolling, and content selection. This documentation establishes that JavaScript-rendered content can be captured if the browser and wait policy are configured, not that every single-page application or protected site will succeed. It complements the [Markdown generation guide](../crawl4ai-markdown-generation/), which separates unfiltered conversion from additional pruning. The guide is first-party operational documentation rather than a population-level benchmark of rendering or archival quality.

## Key points
- BrowserConfig selects Chromium, Firefox, or WebKit and supports headless execution. (BrowserConfig: engine, headless)
- CrawlerRunConfig supports JavaScript evaluation, `wait_for` selectors/conditions, and scrolling to expose dynamic content. (CrawlerRunConfig: page interaction and waiting)
- Browser rendering and Markdown conversion are separate stages; the latter may receive cleaned rather than raw HTML. (BrowserConfig and CrawlerRunConfig; Markdown Generation Basics)
