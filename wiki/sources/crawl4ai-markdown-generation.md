---
title: "Markdown Generation - Crawl4AI Documentation (v0.9.x)"
summary: Crawl4AI's Markdown generator distinguishes raw converted output from aggressively filtered reading copies.
url: https://docs.crawl4ai.com/core/markdown-generation/
author: Crawl4AI project
kind: webpage
captures:
  - retrieved: 2026-09-24T07:43:13Z
    sha256: "4b0fc906a863c1941280d076490fc604253aa308f9d306e0dc8ed262f8e798f9"
    type: text/html
---

## Overview

Crawl4AI's first-party tutorial explains how a browser crawl is converted to Markdown and optionally filtered for relevance or boilerplate. It documents separate raw and fit versions and lets the caller select raw, cleaned, or fit HTML as the conversion input. This distinction matters for an archive: a pruning or query filter can intentionally remove evidence that should remain available in a preserved original. The page promises headings and code blocks and exposes image/link controls, but it is not a fidelity benchmark and does not guarantee equations, complex tables, or figure-caption associations. Its JavaScript advice is operational guidance rather than a measured browser success rate.

## Key points
- `DefaultMarkdownGenerator` converts fetched HTML, preserving headings and code blocks, and can retain reference-style link citations. (How Markdown Generation Works)
- Input can be raw, cleaned, or fit HTML, while `raw_markdown` and `fit_markdown` separate unfiltered output from pruned results. (Selecting the HTML Source; Using Fit Markdown)
- Options include `ignore_images`; heavy JavaScript pages may need dynamic rendering or waiting for elements. (Configuring the Default Markdown Generator; Troubleshooting)
