---
title: "PyMuPDF4LLM repository: local PDF layout extraction"
summary: "Native CPU Markdown extraction includes columns, tables, headings, code, and selective OCR, but no formula-to-LaTeX guarantee."
url: https://raw.githubusercontent.com/pymupdf/RAG/4203628b899f5d90301a31f065574f30f5d407c6/README.md
author: "Artifex / PyMuPDF"
kind: repository
captures:
  - retrieved: 2026-09-24T08:12:10Z
    sha256: "0fc7f7b768e0782dc32dfaf91190bc64eb4be00696426b5d512c2a9e968513c7"
    type: text/plain
---

## Overview

Artifex's pinned PyMuPDF4LLM README describes a local, CPU-powered PDF extraction library that emits Markdown, JSON, or text. It covers multicolumn reading order, inferred headings, tables, image references, code spans, and selective OCR for scanned or broken regions. This makes it an inexpensive native-path candidate for searchable born-digital documents, although neither the description nor its [historical READoc result](../readoc-study/) supports treating formula glyphs as reliable LaTeX. The README distinguishes optional OCR engines and warns that absent OCR dependencies can leave scans unread; "no GPU" does not imply full OCR by itself. Its open-source license is AGPL-3.0, with a separate commercial Artifex path for proprietary applications. These are vendor claims and capabilities, not a benchmark of current scientific-document fidelity.

## Key points

- Layout reconstruction, heading inference, table detection, fenced code, image references, and page chunks are advertised. ("Key features"; "Markdown output")
- Native processing needs no GPU; OCR is selective and depends on installed Tesseract or RapidOCR, otherwise unavailable by default. ("Hybrid OCR Strategy"; "OCR engine selection")
- Markdown tables can be rendered as HTML to preserve richer cell relationships. ("HTML table output")
- The open-source package is AGPL-3.0 and Artifex offers commercial licensing. ("Licensing")
