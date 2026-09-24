---
title: Which chunking strategy best retrieves passages across web pages, papers, and repositories?
rkey: mixed-corpus-chunking
date: 2026-09-24
brief: No cross-corpus winner is established; start with structure-aware recursive and sentence baselines, then compare boundary and contextualization layers against labeled source spans at equal token budgets.
turn_url: https://github.com/smith-wiki/wiki/issues/109
mode: QUESTION_ANSWER
---

## Answer

**No published winner transfers to this mixed corpus.** Start with structure-aware recursive chunks and adjacent-sentence groups, preserving source offsets and headings, PDF structure, and code paths/symbols. Compare semantic, Chonkie Neural, and Slumber boundaries only after measuring passage retrieval against this inexpensive baseline. Late chunking contextualizes embeddings *after* boundaries; Anthropic's Contextual Retrieval adds generated prefixes *before* dense/BM25 indexing. Neither chooses boundaries, and Slumber has no published comparable retrieval score ([methods and evidence](../../concepts/evidence-aware-retrieval-chunking/)).

Chroma's synthetic top-five table favors its GPT-4o splitter on recall but not evidence efficiency, with a contradictory appendix; Qu et al. find no consistent semantic gain over fixed sentence groups. Jina reports modest document-ranking gains for late pooling; Anthropic reports lower top-20 failure with generated prefixes and reranking, under a different protocol. These are not head-to-head scores ([published comparisons](../../concepts/evidence-aware-retrieval-chunking/); [unit-and-budget distinction](../../notes/chunking-winners-depend-on-evidence-unit-and-budget/)).

For web, PDFs, and repository files, freeze source versions/parsers and label known query-to-*source-passage* pairs, including all required evidence spans. Judge pooled candidate passages, hold out documents for tuning, and compare all arms with the same embedder/search stack at equal prompt-token budgets and top-k. Report complete-evidence hit, span coverage, duplicate-billed irrelevant tokens, domain slices, uncertainty, and ingestion/search costs ([evaluation protocol](../../concepts/evidence-aware-retrieval-chunking/)).
