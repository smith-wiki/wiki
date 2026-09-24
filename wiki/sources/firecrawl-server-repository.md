---
title: "Firecrawl server license and native PDF integration"
summary: "The AGPL-3.0 server invokes pdf-inspector for a native CPU Markdown path, distinct from managed extraction services."
url: https://raw.githubusercontent.com/firecrawl/firecrawl/fd9c74cc0e3a2d00258248670e4d04db5f75b31d/LICENSE
author: "Firecrawl"
kind: repository
captures:
  - retrieved: 2026-09-24T08:21:17Z
    sha256: "9b4649365c4f29d8f41301f4cda1e5bd9da51cf1bbb19ab9d568ff57d56e3b33"
    type: text/plain
  - retrieved: 2026-09-24T08:21:32Z
    sha256: "6e6ce782d758e1c530f79d0f466e2f4c1451f9e20dbd74b9d39f24d1d967297b"
    type: text/plain
    url: https://raw.githubusercontent.com/firecrawl/firecrawl/fd9c74cc0e3a2d00258248670e4d04db5f75b31d/apps/api/native/src/pdf.rs
---

## Overview

Two files from a pinned Firecrawl server revision establish its repository license and a specific native PDF integration. The license file contains the GNU Affero General Public License version 3. The Rust binding imports `pdf_inspector`, extracts Markdown from text-based PDFs, and reports type, page count, confidence, and pages needing OCR; it runs CPU-bound work outside the Node event loop. This is direct source evidence for an inspectable local parser component, not for the full managed service's OCR/layout/formula parity or its commercial terms. In combination with the [pdf-inspector README](../pdf-inspector-repository/) and Firecrawl's [deployment comparison](../firecrawl-deployment-limits/), it separates library capabilities from service packaging. No supported Apple Silicon end-to-end Firecrawl server benchmark is established by these files.

## Key points

- The repository license file is GNU AGPL version 3. (`LICENSE`, title)
- The native PDF binding calls `pdf_inspector::process_pdf_with_options` and returns Markdown for text-based documents plus pages identified as needing OCR. (`apps/api/native/src/pdf.rs`, `process_pdf`)
- PDF work is dispatched to a blocking thread pool because extraction is CPU-bound; this file does not implement the full hosted OCR fallback. (`apps/api/native/src/pdf.rs`, `process_pdf` comments and body)
