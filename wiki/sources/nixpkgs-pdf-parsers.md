---
title: "nixpkgs unstable PDF parser package searches"
summary: "Rendered unstable searches distinguish installable Docling and PyMuPDF4LLM from absent engines and client-only API packages."
url: https://search.nixos.org/packages?channel=unstable&query=docling
author: "NixOS / nixpkgs"
kind: documentation
captures:
  - retrieved: 2026-09-24T08:15:56Z
    sha256: "02231c54f42185fff180eb49e096cecefc2d00f9777ff249f5ef65e19d5a6742"
    type: text/html
  - retrieved: 2026-09-24T08:16:15Z
    sha256: "a2f21fa486d04cd6d49430216d55ad2c355b2e9e0250bf605bab3eaf5f2597d0"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=marker-pdf
  - retrieved: 2026-09-24T08:16:23Z
    sha256: "fbef5068a44e487d7f32f658e79db1917999a534e5c73239bba73628aaea9fe5"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=mineru
  - retrieved: 2026-09-24T08:16:31Z
    sha256: "e48c18d97fda012cd37110492cf525e6be9f3049886d9b339d9be32bd3002214"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=olmocr
  - retrieved: 2026-09-24T08:16:40Z
    sha256: "c15b17207bcd8b8606878c9c62dcceb74a897dab6a296189f68c5ee7ea2e4bda"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=pymupdf4llm
  - retrieved: 2026-09-24T08:16:48Z
    sha256: "820d6b3942140458b82ca2927ae3d57bb1826b839208d81856aae17eee485bd9"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=grobid
  - retrieved: 2026-09-24T08:16:54Z
    sha256: "2c031e475c8e9d4dd9285438333cd8cd47a4098bc9f43fe07379bcab86f918e2"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=mistralai
  - retrieved: 2026-09-24T08:17:01Z
    sha256: "cb9b3951f7f1763cc72fca14680be3f929b1c8512904dc6375c9accb0374b868"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=llama-cloud
  - retrieved: 2026-09-24T08:17:08Z
    sha256: "6825d46e943e8a5002e42bec5630323efac46c1a536b7b882e7210fbcd0d7650"
    type: text/html
    url: https://search.nixos.org/packages?channel=unstable&query=firecrawl
---

## Overview

These saved, JavaScript-rendered NixOS package searches inspect nine parser-related names against unstable index revision `4975466d324710c576dc11ad614684e6bd8cad8e`. They are an availability snapshot for developers planning reproducible local installations, not evidence that the packages contain downloaded model weights or reproduce a vendor's hosted service. The search interface displays exact attributes, versions, declared license labels, and supported platforms; a negative result means no matching package was shown for the searched name at that revision, not that packaging is impossible. In particular, `mistralai`, `llama-cloud`, and Firecrawl packages are API clients or integrations, not local OCR engines. Compare actual deployment and weight terms in the [parser descriptions](../../concepts/scientific-pdf-structure-extraction/) before inferring an Apple-local path.

## Key points

- Docling appears as `python313Packages.docling` and `python314Packages.docling` at 2.118.0, along with related model/core and serve packages; the index lists `aarch64-darwin`. (`docling` search, "Showing results")
- PyMuPDF4LLM appears as `python313Packages.pymupdf4llm` and `python314Packages.pymupdf4llm` at 0.3.4, marked AGPL-3.0-only. (`pymupdf4llm` search, "Showing results")
- Searches for `marker-pdf` and `olmocr` show no packages; `mineru` and `grobid` return only unrelated names. (`marker-pdf`, `olmocr`, `mineru`, and `grobid` searches)
- `mistralai` 2.10.1 and `llama-cloud` 2.16.0 are Python API clients, not packaged OCR model servers. (`mistralai` and `llama-cloud` searches)
- `firecrawl-cli`, `firecrawl-mcp`, and `firecrawl-py` are clients/integrations, not the Firecrawl parsing server. (`firecrawl` search)
