---
title: "Troubleshooting"
summary: Trafilatura explicitly requires an external browser to supply HTML for JavaScript-rendered pages.
url: https://trafilatura.readthedocs.io/en/latest/troubleshooting.html
author: Trafilatura project
publisher: "Trafilatura"
kind: webpage
captures:
  - retrieved: 2026-09-24T07:54:16Z
    sha256: "ad24fff84090bc1b29d1488a2f9aec618080dfde09e871ee8fad695cadcdec9c"
    type: text/html
---

## Overview

The Trafilatura project's troubleshooting guide identifies a crucial boundary in local web capture: the library extracts from HTML, but does not execute the page's JavaScript. For client-rendered pages it shows a Playwright browser visit, a call to retrieve the rendered page HTML, and a separate `extract()` invocation on that HTML. This is authoritative first-party operational advice, not evidence that Playwright always obtains complete content or evades paywalls and bot controls. Its recommendation is complementary to the [Python usage guide](../trafilatura-extraction-options/), which documents content and output controls once HTML exists. Archival workflows should keep the raw or rendered evidence separately from any extracted reading copy.

## Key points
- Trafilatura reads raw HTML and requires an external browser renderer when content is inserted by JavaScript. (Page requires JavaScript)
- The guide demonstrates using Playwright to obtain `page.content()` and pass it to `extract()`. (Page requires JavaScript)
