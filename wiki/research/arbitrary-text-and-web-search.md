---
title: How does OMP handle arbitrary text and web research?
rkey: arbitrary-text-and-web-search
date: 2026-09-22
brief: OMP routes supplied evidence, static URLs, web discovery, and interactive pages through distinct research paths.
turn_url: https://github.com/smith-wiki/wiki/issues/39
mode: QUESTION_ANSWER
---

## Answer

Treat inputs by required discovery and interaction. Pasted text and local files are supplied evidence; read local files directly. Known static URLs go through `read`; open-ended questions use `web_search` for discovery. Authenticated, interactive, or JavaScript-dependent pages require `browser`. **Inference:** this is a routing rule, not a publication rule: privately pasted material remains input unless the workflow deliberately promotes a supported synthesis. ([OMP tooling, 2026](../sources/omp-web-search-runtime/); [Smith Wiki workflow, 2026](../sources/smith-wiki-research-workflow/))

Search is currently enabled. Provider order and exclusion lists are empty, and each provider transport has a 60-second ceiling. A live probe selected Anthropic with `claude-haiku-4-5-20251001`; **Uncertainty:** that observation does not establish a permanent provider because automatic search walks the available chain sequentially and falls through after failures or empty results. ([OMP web-search runtime, 2026](../sources/omp-web-search-runtime/))

Search results are leads, not final evidence. Fetch promising source bodies with `read` (or `browser` when necessary), preserve immutable captures under ignored `raw/`, and record URL, retrieval time, digest, and raw path in `wiki/sources/`. Synthesis then promotes only material useful to the question, in the wiki’s own words, with provenance links. ([Smith Wiki workflow, 2026](../sources/smith-wiki-research-workflow/))
