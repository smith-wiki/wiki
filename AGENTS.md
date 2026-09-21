# Smith Wiki contract

## Layers

- `raw/` is the immutable evidence layer. Append new records and source captures; never rewrite, rename, or delete existing bytes.
- `wiki/` is the replaceable published layer. Regenerate it from preserved evidence whenever that improves clarity or connections.
- Write English in source files, front matter, labels, alt text, and visible pages. Do not migrate material from an older wiki.
- Write published content as Markdown only. Template syntax and raw HTML are outside the content contract.

## Research turn workflow

1. Append exactly one JSON object to `raw/research-log.ndjson`. Keep one complete object per line; preserve chronological order. Required keys are `rkey`, `uri`, `cid`, `created_at`, `parent_uri`, `root_uri`, and `recorded_at`; use `null` for absent parents.
2. Preserve fetched evidence under `raw/` before interpreting it. Existing evidence remains byte-for-byte unchanged.
3. Create exactly one compact page at `wiki/research/<rkey>.md`. Its front matter must contain exactly `title`, `rkey`, `date`, `brief`, `turn_url`, and `mode`; no other keys are allowed. `mode` must be exactly `SOURCE_BRIEF`, `QUESTION_ANSWER`, or `NOTE_EXPLORE`. The folder data file owns the `/<rkey>/` route and research layout.
4. Put each durable source note in `wiki/sources/`; update relevant pages in `wiki/entities/` and `wiki/concepts/` when the turn adds useful knowledge. Prefer improving an existing page over creating a near-duplicate.
5. Keep `wiki/index.md` useful as the first navigation surface. The generated research log is secondary navigation.
6. Run focused checks for changed links and cited sources. Confirm the rendered turn marker contains the exact `rkey` before publication.

## Page contract

- Keep the research page on one page. Target 140–180 words and never exceed 220 words. Use at most two compact sections and short paragraphs so the complete `.research-card` remains readable in a 1200×1600 capture.
- The first body content must be the heading required by `mode`: `## Source brief` for `SOURCE_BRIEF`, `## Answer` for `QUESTION_ANSWER`, or `## Exploration` for `NOTE_EXPLORE`.
- In a source brief, summarize the sources supplied or linked by the turn, compare what the preserved evidence supports, and separate that evidence from caveats, limits, or disagreement. Do not substitute a broad topic explainer.
- In a question answer, directly resolve the turn's question, state the answer first, support it with the strongest preserved evidence, and make its limits explicit.
- In a note exploration, identify the claim or topic, test it against preserved evidence, and connect it to relevant entities, concepts, or implications without presenting speculation as fact.
- End factual claims or paragraphs with citations to preserved source notes. Use route-relative Markdown links, for example `[S1](../sources/source-slug/)` from a research route; source notes must identify the original URL and the preserved raw evidence.
- Prefix interpretation with **Inference:**, unresolved gaps with **Uncertainty:**, and incompatible evidence with **Contradiction:**. Never hide disagreement behind blended prose.
- Use relative links between research, source, entity, and concept pages. Update both sides when a connection aids navigation.
- Do not put a second title in the body; the layout renders the front-matter title. Keep the page self-contained and omit process narration.

A research page is complete when its turn log record and raw evidence are preserved, every material factual claim is cited, labels expose non-factual reasoning, useful cross-links resolve, and the rendered `.research-card` exposes both `data-research-turn` equal to its `rkey` and `data-research-mode` equal to its exact `mode`.
