---
title: Which PDF-to-Markdown parser best preserves scientific and technical document structure?
rkey: pdf-to-markdown-scientific
date: 2026-09-24
brief: MinerU has the strongest published scientific-paper evidence among the named parsers; Docling is the practical Apple-local structured-output starting point, subject to math checks.
turn_url: https://github.com/smith-wiki/wiki/issues/102
mode: QUESTION_ANSWER
---

## Answer

**For measured scientific-paper structure, choose MinerU as the quality candidate; for a nixpkgs-packaged Apple Silicon local workflow with MIT-licensed code, start with Docling and retain its structured JSON (check chosen model weights separately).** This is not a single universal winner: READoc's historical whole-paper comparison favors MinerU across headings, formulas, and tables, while Docling's tested formula conversion was poor. olmOCR 2 leads its own page-level unit-test benchmark; OmniDocBench v1.6 favors MinerU-2.5 VLM among the named evaluated parsers. Those scores concern different releases and metrics, not current MinerU 4 or a proven Mac speed ranking. See the [nine-parser comparison, Apple paths, license separation, and nixpkgs snapshot](../../concepts/scientific-pdf-structure-extraction/) and [what the benchmarks omit](../../notes/pdf-benchmark-scores-do-not-certify-structure/).

**No cited benchmark certifies code fences or figure-caption association.** GROBID produces scholarly TEI rather than Markdown; PyMuPDF4LLM is a CPU text baseline; Mistral OCR and LlamaParse are primarily hosted, and Firecrawl's local native parser is not its managed OCR service. Preserve PDFs and assets, then visually check a representative formula-, code-, table-, and caption-heavy sample before selecting a production parser.
