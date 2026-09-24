---
title: What is the most faithful way to capture web pages as Markdown for a research archive in 2026?
rkey: web-to-markdown-archive
date: 2026-09-24
brief: Preserve original and rendered evidence separately from Markdown; no single listed extractor wins both main-text and structural fidelity.
turn_url: https://github.com/smith-wiki/wiki/issues/100
mode: QUESTION_ANSWER
---

## Answer

**Preserve the fetched response (and a rendered DOM plus image assets when JavaScript matters), then generate a separate, auditable Markdown reading copy.** For technical pages, try local Defuddle first: its conversion rules retain simple tables, fenced code, math, and figure captions, with HTML fallback for merged cells. This is a *capability-based choice*, not a measured accuracy winner; no comparable published Defuddle score was found. Trafilatura is a strong text-extraction baseline, but WebMainBench reports substantial code and table-fidelity losses. See the [tool-by-tool comparison and nixpkgs availability](../../concepts/web-capture-fidelity/) and [why main-text benchmarks cannot certify an archive](../../notes/main-content-accuracy-does-not-measure-archive-fidelity/). ([Ango and contributors, n.d.](../../sources/defuddle/); [Ma et al., 2025](../../sources/webmainbench-structure-study/))

For dynamic sites, Crawl4AI can render locally; Firecrawl and Jina Reader offer hosted browser paths and self-hosted alternatives, whereas Cloudflare Markdown for Agents converts origin HTML, not a browser-rendered page. In the captured nixpkgs snapshot, Defuddle, Trafilatura, and Crawl4AI are packaged; Firecrawl clients and Readability wrappers are packaged, but not the Firecrawl/Jina servers or Cloudflare feature. Browser binaries and asset capture need separate provisioning. ([Crawl4AI project, n.d.](../../sources/crawl4ai-browser-configuration/); [Firecrawl, n.d.](../../sources/firecrawl-self-hosting/); [Jina AI, n.d.](../../sources/jina-reader-repository/); [Cloudflare, n.d.](../../sources/cloudflare-markdown-for-agents/); [NixOS Search, n.d.](../../sources/nixpkgs-web-markdown-packages/))
