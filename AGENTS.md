# Smith Wiki contract

## Operating principles

- **Compile, do not rediscover.** Turn durable source findings and useful answers into a persistent wiki that later work can reuse. A research turn should improve the shared artifact, not end as disposable chat.
- **Evidence before synthesis.** Preserve the source locally in the Git-ignored `raw/` directory before drawing conclusions. Keep provenance reachable from every factual synthesis so the published layer can be checked and rebuilt.
- **One address, one subject.** Give each source, entity, concept, permanent note, or research question one stable page concerned with one coherent subject. Write it to remain intelligible outside the turn that created it.
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

- `raw/` is the local immutable evidence layer. Append source captures, never rewrite existing bytes, and never stage, commit, or push this directory.
- `wiki/` is the replaceable published layer. Regenerate it from preserved evidence whenever that improves clarity or connections.
- Write English in source files, front matter, labels, alt text, and visible pages. Do not migrate material from an older wiki.
- Write published content as Markdown only. Template syntax and raw HTML are outside the content contract.

## Published page roles

- `wiki/research/` contains the compact, request-bound artifact for one research turn. It answers or explores the turn; it is not the canonical home of every idea it mentions.
- `wiki/sources/` contains one page per original source, including provenance, supported claims, and source-specific limits.
- `wiki/entities/` contains named people, organizations, projects, products, and places. Entity pages answer “what is this?” and accumulate sourced facts over time.
- `wiki/concepts/` contains recurring terms or model categories that need a stable definition. Use a noun phrase as the title.
- `wiki/notes/` contains atomic permanent notes written in the wiki's voice. Each page states one reusable claim, distinction, relationship, or implication; use a declarative title and support it with source links.

## Research turn workflow

1. Preserve fetched evidence under the local `raw/` directory before interpreting it. Existing evidence remains byte-for-byte unchanged; compute a content digest for provenance.
2. Create exactly one compact page at `wiki/research/<rkey>.md`. Its front matter must contain exactly `title`, `rkey`, `date`, `brief`, `turn_url`, and `mode`; no other keys are allowed. `mode` must be exactly `SOURCE_BRIEF`, `QUESTION_ANSWER`, or `NOTE_EXPLORE`. The folder data file owns the `/<rkey>/` route and research layout.
3. Put each durable source note in `wiki/sources/`. Record the original URL, retrieval time, content digest, and local raw path; the raw capture itself stays outside Git.
4. Update relevant pages in `wiki/entities/` and `wiki/concepts/` only when the turn adds reusable knowledge. Create or improve a page in `wiki/notes/` when the evidence supports a durable claim, distinction, relationship, or implication. Prefer improving an existing page over creating a near-duplicate.
5. Add the turn to `wiki/log.md` and keep `wiki/index.md` useful as the first navigation surface.
6. Run focused checks for changed links and cited sources. Confirm the rendered turn marker contains the exact `rkey` before publication.

## Maintenance workflow

When asked to lint or maintain the wiki:

1. Find broken links, orphan pages, near-duplicates, unsupported claims, unresolved contradictions, stale syntheses, and concepts that lack an addressable page.
2. Repair the published layer from preserved evidence. Merge duplication into the strongest page, update all affected links, and remove the superseded published page.
3. Improve `wiki/index.md` only where the change helps a reader enter or traverse the knowledge network; do not turn the index into an exhaustive file listing.
4. Finish with focused link and citation checks for every changed page.

## Verification and delivery

- GitHub Actions is the sole Node and Eleventy execution environment. Do not search the workstation for Node or npm, install JavaScript tooling locally, or attempt a local site build.
- Before opening a pull request, run focused non-Node checks for the raw content digest, exact research front matter, word limit, citations, relative links, and the research marker contract.
- Keep one research ingest per `ingest/<rkey>` branch and pull request. After focused checks, commit all ingest changes, push the branch, and open an English-language pull request.
- Never merge the pull request. Its CI build must pass before a human merges it; merging to `main` triggers the deployment workflow.

## Page contract

- Keep the research page on one page. Target 140–180 words and never exceed 220 words. Use at most two compact sections and short paragraphs so the complete `.research-card` remains readable in a 1200×1600 capture.
- The first body content must be the heading required by `mode`: `## Source brief` for `SOURCE_BRIEF`, `## Answer` for `QUESTION_ANSWER`, or `## Exploration` for `NOTE_EXPLORE`.
- In a source brief, summarize the sources supplied or linked by the turn, compare what the preserved evidence supports, and separate that evidence from caveats, limits, or disagreement. Do not substitute a broad topic explainer.
- In a question answer, directly resolve the turn's question, state the answer first, support it with the strongest preserved evidence, and make its limits explicit.
- In a note exploration, identify the claim or topic, test it against preserved evidence, and connect it to relevant entities, concepts, or implications without presenting speculation as fact.
- End factual claims or paragraphs with readable author-date links to preserved source notes, for example `([Almeida, 2026](../sources/source-slug/))`. Use the named author when available, otherwise the responsible organization, then a short source title when neither exists. Never use opaque labels such as `[S1]`. Source notes must identify the original URL, retrieval time, content digest, local raw evidence path, and suggested full citation.
- Prefix interpretation with **Inference:**, unresolved gaps with **Uncertainty:**, and incompatible evidence with **Contradiction:**. Never hide disagreement behind blended prose.
- Use relative links between research, source, entity, and concept pages. Update both sides when a connection aids navigation.
- Do not put a second title in the body; the layout renders the front-matter title. Keep the page self-contained and omit process narration.

A research page is complete when its local raw evidence and published chronology entry exist, every material factual claim is cited, labels expose non-factual reasoning, useful cross-links resolve, and the rendered `.research-card` exposes both `data-research-turn` equal to its `rkey` and `data-research-mode` equal to its exact `mode`.
