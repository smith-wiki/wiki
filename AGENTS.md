# Smith Wiki contract

## Operating principles

- **Compile, do not rediscover.** Turn durable source findings and useful answers into a persistent wiki that later work can reuse. A research turn should improve the shared artifact, not end as disposable chat.
- **Evidence before synthesis.** Preserve the source in `raw/` before drawing conclusions. Keep provenance reachable from every factual synthesis so the published layer can always be checked and rebuilt.
- **One address, one subject.** Give each source, entity, concept, or research question one stable page concerned with one coherent subject. Write it to remain intelligible outside the turn that created it.
- **Promote, do not copy.** `raw/` may preserve rough captures and source language; `wiki/` contains permanent notes rewritten in the writer's own words. Use complete sentences, disclose sources, and quote only when the wording itself matters.
- **Select for use, not collection.** Promote material that advances a question, argument, concept, entity, or meaningful connection. Leave incidental excerpts in the evidence layer instead of turning every captured fragment into a page.
- **Stable addresses, evolving content.** Treat published paths as permanent addresses. Improve pages in place; when a merge or rename is necessary, update every inbound link in the same change and remove the obsolete page.
- **Links carry the structure.** Directories express page roles, not a fixed subject taxonomy. Build lines of thought with contextual links between pages; state why a connection matters instead of attaching unexplained tags.
- **Integrate before expanding.** Search the wiki before creating a page. Prefer revising an existing page, recording a contradiction, or adding a connection over producing a parallel summary.
- **Connectivity creates value.** Every new durable page must link to relevant existing pages and be linked from the page or index that gives it context. Strengthen both directions when a connection improves rediscovery.
- **Preserve productive disagreement.** Keep supported contradictions, uncertainty, and competing interpretations visible. Use the network to compare distant contexts and surface questions that no single source answers.
- **Separate roles.** The human curates sources, asks questions, and directs emphasis. The agent preserves evidence, integrates knowledge, maintains links and indexes, and checks the wiki's health.
- **Let navigation emerge.** Keep `wiki/index.md` as the curated entry point, use links for associative exploration, and use the chronological log only as an audit trail.

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

## Maintenance workflow

When asked to lint or maintain the wiki:

1. Find broken links, orphan pages, near-duplicates, unsupported claims, unresolved contradictions, stale syntheses, and concepts that lack an addressable page.
2. Repair the published layer from preserved evidence. Merge duplication into the strongest page, update all affected links, and remove the superseded published page.
3. Improve `wiki/index.md` only where the change helps a reader enter or traverse the knowledge network; do not turn the index into an exhaustive file listing.
4. Finish with focused link and citation checks for every changed page.

## Verification and delivery

- GitHub Actions is the sole Node and Eleventy execution environment. Do not search the workstation for Node or npm, install JavaScript tooling locally, or attempt a local site build.
- Before opening a pull request, run focused non-Node checks for the raw content digest, NDJSON validity, exact research front matter, word limit, citations, relative links, and the research marker contract.
- Keep one research ingest per `ingest/<rkey>` branch and pull request. After focused checks, commit all ingest changes, push the branch, and open an English-language pull request.
- Never merge the pull request. Its CI build must pass before a human merges it; merging to `main` triggers the deployment workflow.

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
