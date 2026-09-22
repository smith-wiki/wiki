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
- `wiki/sources/` contains one page per independently citable original source. A source page records that original's identity, preserved representations, supported statements, and source-specific assessment; it is not a topic dossier.
- `wiki/entities/` contains named people, organizations, projects, products, and places. Entity pages answer “what is this?” and accumulate sourced facts over time.
- `wiki/concepts/` contains recurring terms or model categories that need a stable definition. Use a noun phrase as the title.
- `wiki/notes/` contains atomic permanent notes written in the wiki's voice. Each page states one reusable claim, distinction, relationship, or implication; use a declarative title and support it with source links.

## Research threads and turns

- A **research turn** is one user message that adds evidence, asks a research question, or requests a note exploration. Multiple related sources in the same message form one source bundle and one turn. A later message that adds a source starts a new turn even when it continues the same topic. Delivery instructions such as merge approval do not start a research turn.
- Give every research turn its own task Issue, `issue/<number>-<slug>` branch, pull request, and exactly one created or revised request-bound page in `wiki/research/`. Do not enlarge an earlier turn's Issue or pull request with research input from a later message.
- A **research thread** is a GitHub Milestone that starts with its first turn and may span multiple OMP sessions. Assign every turn Issue and its pull request to that milestone. Milestones are workflow metadata and do not appear on the published wiki.
- Continue an existing thread only when the user explicitly asks to continue it and supplies its milestone name or URL. If the request omits the identifier, ask for it rather than enumerating milestones. Never infer a thread from topic similarity, shared sources or entities, labels, recent activity, or conversation history. Without an explicit continuation request, create a new milestone for the turn.
- A research milestone may remain open indefinitely. Close it only when the user explicitly retires the thread or directs that it be superseded or merged into another milestone.
- If a new turn starts while the preceding turn's pull request is open, stack the new pull request on the preceding branch, assign it to the same explicitly named milestone, and declare `Depends on #<pull-request>`. After the base merges, retarget the stacked pull request to `main`, rebase its branch onto `origin/main`, push with `--force-with-lease`, and require fresh passing CI before merge.

## Issue intake

- Every user request that would change tracked files, change repository settings, or publish research must have a GitHub issue before implementation begins. If the user supplies an existing issue, use it and do not create a duplicate.
- Write every issue in English and make it self-contained for an agent without access to the originating conversation. Use the fields and order in `.github/ISSUE_TEMPLATE/task.yml`: task type, research milestone, dependency, request, inputs and sources, context, acceptance criteria, constraints and non-goals, execution mode, and handoff readiness.
- **Queue only:** create the issue with `Execution mode` set to `Queue only`, return its URL, and stop. Do not create a branch or begin implementation.
- **Implement now:** create or adopt the issue first, set `Execution mode` to `Implement now`, then execute the task in the same session.
- For changes to versioned files, use one `issue/<number>-<slug>` branch and pull request per issue. The pull request must contain `Closes #<number>` so merge closes the issue.
- For repository-setting changes that cannot have a pull request, execute only after creating the issue, then add a result comment with verification and close the issue.

## Research turn workflow

1. Preserve fetched evidence under the local `raw/` directory before interpreting it. Existing evidence remains byte-for-byte unchanged; compute a content digest for provenance.
2. Create or revise exactly one compact page at `wiki/research/<rkey>.md`. Its front matter must contain exactly `title`, `rkey`, `date`, `brief`, `turn_url`, and `mode`; no other keys are allowed. Set `turn_url` to the turn Issue URL. `mode` must be exactly `SOURCE_BRIEF`, `QUESTION_ANSWER`, or `NOTE_EXPLORE`. The folder data file owns the `/<rkey>/` route and research layout.
3. Put each durable source note in `wiki/sources/`. Record the original URL, retrieval time, content digest, and local raw path; the raw capture itself stays outside Git.
4. Update relevant pages in `wiki/entities/` and `wiki/concepts/` only when the turn adds reusable knowledge. Create or improve a page in `wiki/notes/` when the evidence supports a durable claim, distinction, relationship, or implication. Prefer improving an existing page over creating a near-duplicate.
5. Add the turn to `wiki/log.md` and keep `wiki/index.md` useful as the first navigation surface.

## Maintenance workflow

When asked to lint or maintain the wiki:

1. Find broken links, orphan pages, near-duplicates, unsupported claims, unresolved contradictions, stale syntheses, and concepts that lack an addressable page.
2. Repair the published layer from preserved evidence. Merge duplication into the strongest page, update all affected links, and remove the superseded published page.
3. Improve `wiki/index.md` only where the change helps a reader enter or traverse the knowledge network; do not turn the index into an exhaustive file listing.

## Verification and delivery

- GitHub Actions is the sole automated verification environment. For versioned work, commit and push the issue branch, then inspect the pull-request checks. Do not search the workstation for Node or npm, install JavaScript tooling locally, attempt a local site build, or recreate CI checks with ad hoc local scripts.
- Format every commit subject as Conventional Commits 1.0.0: `<type>[optional scope]: <description>`.
- For versioned work, follow `.github/pull_request_template.md`, commit all task changes, push the issue branch, and open an English-language pull request containing `Closes #<number>`.
- Merge a pull request only after its CI checks pass and the user explicitly authorizes that merge in the current conversation; merging to `main` closes the issue and triggers the deployment workflow.

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

## Source page profile

- The source-page contract governs evidence semantics, not visible layout. Do not require one universal sequence of headings, render empty sections, or copy a template mechanically; use the blocks that fit the source type.
- Distinguish the independently citable intellectual source from its representations. Alternate formats or repeated captures of the same content may share a page; materially changed editions or revisions need separately addressable source identity. Never overwrite a representation cited by published evidence.
- Every source page must identify the title, source type, creator or responsible organization when known, publication or version status, canonical original URL or identifier, and a suggested citation for that original alone.
- Give every source page a short neutral description of what the source is and covers. Cross-source synthesis, original ideas, deductions, comparisons, recommendations, research plans, and task state belong in research, entity, concept, or note pages.
- Record at least one representation with a stable local ID, retrieval time in UTC, local raw path, format or media type, and digest algorithm and value. Add edition, revision, commit, language, resolved URL, capture method, rights, or relations to other representations when they affect later verification.
- Record an assessment state as `not_assessed`, `none_recorded`, or `recorded`. Add source criticism only when material; `none_recorded` means no limitation was recorded for the present use, not that the source is universally authoritative. Never emit an empty criticism section.
- Every source-supported statement used by the wiki must identify what the source states or shows, the exact representation used, and a precise locator. Keep exact quotations distinct from source-attributable paraphrases; quotations are optional and must remain short and purposeful. Wiki inference never belongs in an evidence entry.
- Match locators to the source type. For a mutable webpage, prefer the preserved representation plus a heading, table cell, fragment, or exact text with context. For a machine-readable specification, prefer the immutable representation plus a labeled structural locator such as JSON Pointer and a human-readable operation or path. For a paper, identify the edition and page, section, figure, table, or equation. For a repository, identify the commit plus path and symbol, heading, or line range.
- Use contextual, typed links for versions, formats, parts, replacements, citations, and downstream use. A source-family or collection page may aid navigation, but claims must still terminate at the independently identified member that supports them.
