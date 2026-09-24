---
title: Defuddle repository
summary: Local main-content extractor with explicit Markdown rules for tables, code, equations, and figure captions.
url: https://raw.githubusercontent.com/kepano/defuddle/49d14ecc4089696565c2479b2f57db72be199adc/README.md
author: Steph Ango and Defuddle contributors
publisher: GitHub
kind: repository
captures:
  - retrieved: 2026-09-24T07:46:37Z
    sha256: "1792031d92c3d5fec0ac6fa12862585298bff8720acdd576db36905775dfaa2d"
    type: text/plain
    url: https://raw.githubusercontent.com/kepano/defuddle/49d14ecc4089696565c2479b2f57db72be199adc/README.md
  - retrieved: 2026-09-24T07:46:55Z
    sha256: "dd67ec4d5e1eeafea9a33acee8ae761588e5c9a05b7da0527b5ac4cf0e3c2c36"
    type: text/plain
    url: https://raw.githubusercontent.com/kepano/defuddle/49d14ecc4089696565c2479b2f57db72be199adc/src/markdown.ts
---

## Overview

Defuddle is an MIT-licensed extractor created for Obsidian Web Clipper, usable from a browser, Node.js, or its command-line interface. Its README and pinned Markdown converter code provide unusually concrete evidence for retaining technical structure: pipe tables where possible, fallback HTML for merged cells, fenced code, LaTeX math, images, and a figure's caption as nearby text. The package can run locally but consumes a browser DOM or supplied HTML; it is not itself a managed JavaScript-rendering crawler. These implementation rules show intended behavior, not a measured success rate on representative web pages. No comparable published corpus-level Defuddle extraction or fidelity score was located; [WebMainBench](../webmainbench-structure-study/) tested other tools.

## Key points
- Browser and Node APIs accept a DOM; the CLI accepts a URL or input HTML and emits Markdown, with no documented headless browser in the CLI. (README, Usage: Browser, Node.js, CLI)
- Core, full, and Node bundles differ: the full/Node variants include MathML-to-LaTeX fallback conversion. (README, Bundles)
- Simple tables become pipe tables; merged-cell tables are retained as cleaned HTML rather than flattened into invalid pipes. (src/markdown.ts, table rule)
- Fenced code, inline/block math, Markdown images, and adjacent `figcaption` text have dedicated rules. (src/markdown.ts, code, math, image, figure rules)
