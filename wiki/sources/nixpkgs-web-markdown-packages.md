---
title: Nixpkgs unstable web extraction package search
summary: Captured NixOS package-search snapshot distinguishes extractors from client SDKs and hosted-only features.
url: https://search.nixos.org/packages?channel=unstable&query=defuddle
author: NixOS Search
kind: webpage
captures:
  - retrieved: 2026-09-24T07:50:39Z
    sha256: "323c06b7a20f2693255917874537ce646a9882cdd649d1a1fd1607cc1f0157f4"
    type: text/html
  - retrieved: 2026-09-24T07:50:55Z
    sha256: "be15ac84cf62b49a2059a46626d41eee24de58021f83f9bfaaf29bd1d4f1fd6e"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=trafilatura
  - retrieved: 2026-09-24T07:51:07Z
    sha256: "269b1200cfb265f2410f7d457d18de79b9744ae6885622f002e0559724cc7b55"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=crawl4ai
  - retrieved: 2026-09-24T07:51:19Z
    sha256: "6825d46e943e8a5002e42bec5630323efac46c1a536b7b882e7210fbcd0d7650"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=firecrawl
  - retrieved: 2026-09-24T07:51:31Z
    sha256: "3073402ff79b0ddac7368ed67f4e953dfe77104fabffb47d895fedc4e30fbe3b"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=readability
  - retrieved: 2026-09-24T07:51:42Z
    sha256: "0b48226e7a53b703fbb9619af323e71d269da15e57274aba517e5ccb5c54732a"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=jina
  - retrieved: 2026-09-24T07:51:56Z
    sha256: "c170a22ae4131861760a2d5b2a8e5e6e6507c207cc7ba1ea6510c671f0135b98"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=jina-reader
  - retrieved: 2026-09-24T07:52:08Z
    sha256: "89e3664d9e11143d2eac5c0f1e8d40304a4f05c446d6d1d31d4b506c253d218d"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=mozilla-readability
  - retrieved: 2026-09-24T07:52:33Z
    sha256: "1dddfdb15a70a08868e4a55e2d04c6c77cc6ae6ac7183d8409cf1f7d6e846398"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=markdown-for-agents
---

## Overview

These rendered search-result captures record the NixOS unstable index at nixpkgs revision `4975466d324710c576dc11ad614684e6bd8cad8e`. Each query is a snapshot rather than a proof that no differently named package can exist. The index lists Trafilatura, Defuddle, and Crawl4AI executables or Python packages; Firecrawl results are a CLI, MCP adapter, and Python SDK rather than its server. Readability results include runnable wrappers around Mozilla's algorithm and a distinct Python port, but not the standalone npm package as its own attribute. Jina Reader and Cloudflare Markdown for Agents have no matching server/feature package in these searches. Packaging does not ensure that a headless browser binary is installed or that a hosted API becomes local.

For the implications of this package boundary for local capture, see [web capture fidelity](../../concepts/web-capture-fidelity/).

## Key points
- `defuddle` 0.19.3; `python313Packages.trafilatura` and `python314Packages.trafilatura` 2.2.0; `python313Packages.crawl4ai` and `python314Packages.crawl4ai` 0.9.1 are listed. (Search queries: defuddle, trafilatura, crawl4ai; revision 4975466d)
- Firecrawl results are `firecrawl-cli`, `firecrawl-mcp`, and `python31{3,4}Packages.firecrawl-py`, not the self-hosted Firecrawl server. (Search query: firecrawl)
- `readability-cli` and `readability-extractor` wrap Mozilla Readability; `readability-lxml` is a separate Python port; exact `mozilla-readability` search finds no package. (Search queries: readability, mozilla-readability)
- Searches for `jina-reader` and `markdown-for-agents` find no package; the broader `jina` results include a Jina API client, not the Reader service. (Search queries: jina-reader, jina, markdown-for-agents)
