# Research work

Read this file for evidence-backed knowledge about a subject, source, entity, concept, claim, or question, and for maintenance of the published knowledge network. Also apply repository [Issue intake](repository-work.md#issue-intake) and [Verification and delivery](repository-work.md#verification-and-delivery).

## Scope

- A **topical research turn** is one user message whose requested deliverable is evidence-backed knowledge. Source briefs, question answers, and note explorations are topical research.
- Discussion, design, evaluation, or implementation of the research process itself is repository work, not a topical research turn. This includes intake design, search or tool configuration, evidence handling, publication rules, Issue, pull-request, and milestone mechanics, and workflows for supplied writing.

## Research orientation

- Start topical research and published-wiki discovery with bare `sw` and scan its bounded titled-page, research-milestone, Issue, and pull-request summaries.
- Apply [Integrate before expanding](#integrate-before-expanding) before creating or revising a page.
- Treat `sw` as discovery and workflow context, not evidence. Preserve and assess original sources through the research workflow below.

## Named methods

### Compile, do not rediscover

Turn durable source findings and useful answers into a persistent wiki that later work can reuse. A research turn improves the shared artifact rather than ending as disposable chat.

### Evidence before synthesis

Preserve the source locally in the Git-ignored `raw/` directory before drawing conclusions. Keep provenance reachable from every factual synthesis so the published layer can be checked and rebuilt.

### One address, one subject

Give each source, entity, concept, permanent note, or research question one stable page concerned with one coherent subject. Write it to remain intelligible outside the turn that created it.

### Promote, do not copy

`raw/` may preserve rough captures and source language; `wiki/` contains permanent notes rewritten in the writer's own words. Use complete sentences, disclose sources, and quote only when wording matters.

### Select for use, not collection

Promote material that advances a question, argument, concept, entity, or meaningful connection. Leave incidental excerpts in the evidence layer.

### Stable addresses, evolving content

Treat published paths as permanent addresses. Improve pages in place; when a merge or rename is necessary, update every inbound link in the same change and remove the obsolete page.

### Links carry the structure

Directories express page roles, not a fixed subject taxonomy. Build lines of thought with contextual links and state why a connection matters.

### Integrate before expanding

Search the published wiki before creating or revising a page with `sw search PATTERN`. Read relevant pages and connections, then prefer revising an existing page, recording a contradiction, or adding a connection over producing a parallel summary.

### Connectivity creates value

Every new durable page links to relevant existing pages and is linked from the page or index that gives it context. Strengthen both directions when that improves rediscovery.

### Preserve productive disagreement

Keep supported contradictions, uncertainty, and competing interpretations visible. Use the network to compare distant contexts and surface questions no single source answers.

### Separate roles

The human curates sources, asks questions, and directs emphasis. The agent preserves evidence, integrates knowledge, maintains links and indexes, and checks wiki health.

### Let navigation emerge

Keep `wiki/index.md` as the curated entry point, use links for associative exploration, and use the chronological log only as an audit trail.

## Evidence layers

- `raw/` is the local immutable evidence layer. Append source captures, never rewrite existing bytes, and never stage, commit, or push this directory.
- `wiki/` is the replaceable published layer. Regenerate it from preserved evidence whenever that improves clarity or connections.
- Write English in source files, front matter, labels, alt text, and visible pages. Do not migrate material from an older wiki.
- Write published content as Markdown only. Template syntax and raw HTML are outside the content contract.

These rules implement [Evidence before synthesis](#evidence-before-synthesis) and [Promote, do not copy](#promote-do-not-copy).

## Published page roles

- `wiki/research/` contains the compact, request-bound artifact for one research turn. It answers or explores the turn; it is not the canonical home of every idea it mentions.
- `wiki/sources/` contains one page per independently citable original source. It records that original's identity, preserved representations, supported statements, and source-specific assessment; it is not a topic dossier.
- `wiki/entities/` contains named people, organizations, projects, products, and places. Entity pages answer "what is this?" and accumulate sourced facts over time.
- `wiki/concepts/` contains recurring terms or model categories that need a stable definition. Use a noun phrase as the title.
- `wiki/notes/` contains atomic permanent notes in the wiki's voice. Each page states one reusable claim, distinction, relationship, or implication; use a declarative title and support it with source links.

These roles apply [One address, one subject](#one-address-one-subject).

## Research threads and turns

Use `sw issue research MODE SLUG TITLE BRIEF_FILE (--new-thread | THREAD)` for turn intake. `--new-thread` explicitly creates a thread; `THREAD` continues the supplied milestone and stacks on its open pull request. Use `sw sync` after a stacked base merges. Use `sw thread retire` or `sw thread merge` only on the user's explicit direction.

- A topical research turn may contain multiple related sources in one message; they form one source bundle and one turn. A later message that adds a source starts a new turn in the conversation's active thread even when it changes topic. Delivery instructions such as merge approval neither start a research turn nor change the active thread.
- Give every topical research turn its own task Issue, `issue/<number>-<slug>` branch, pull request, and exactly one created or revised request-bound page in `wiki/research/`. Do not enlarge an earlier turn's Issue or pull request with research input from a later message.
- A **research thread** is a GitHub Milestone. A conversation session has at most one active research thread; its first topical turn creates one with `--new-thread` unless the user explicitly resumes a named thread.
- Reuse the active thread automatically for every later topical turn in the same conversation; the user does not need to repeat its milestone identifier. Conversation history is authoritative only for this session-local state. In a later session, resume only when the user explicitly supplies the milestone name or URL; otherwise create a new thread. Never infer cross-session continuity from topic similarity, sources, entities, labels, recency, or repository state.
- Starting a different thread in the same conversation requires explicit user direction and replaces the active thread. A research milestone may remain open indefinitely; close it only when the user explicitly retires the thread or directs that it be superseded or merged.
- If a new topical turn starts while the active thread's preceding pull request is open, stack the new pull request on the preceding branch and declare `Depends on #<pull-request>`. After the base merges, retarget the stacked pull request to `main`, rebase its branch onto `origin/main`, push with `--force-with-lease`, and require fresh passing CI before merge.

This per-turn granularity belongs only to topical research. Repository setup follows [Coherent task](repository-work.md#coherent-task).

## Research turn workflow

Apply [Compile, do not rediscover](#compile-do-not-rediscover) to the turn as a whole, and preserve the human-agent boundary in [Separate roles](#separate-roles) while executing it.

1. Apply [Evidence before synthesis](#evidence-before-synthesis): preserve fetched evidence under `raw/` before interpreting it. Existing evidence remains byte-for-byte unchanged; compute a content digest for provenance.
2. Apply [One address, one subject](#one-address-one-subject): create or revise exactly one compact page at `wiki/research/<rkey>.md`. Its front matter contains exactly `title`, `rkey`, `date`, `brief`, `turn_url`, and `mode`; no other keys are allowed. Set `turn_url` to the turn Issue URL. `mode` is exactly `SOURCE_BRIEF`, `QUESTION_ANSWER`, or `NOTE_EXPLORE`. The folder data file owns the `/<rkey>/` route and research layout.
3. Apply [Promote, do not copy](#promote-do-not-copy): put each durable source note in `wiki/sources/`. Record the original URL, retrieval time, content digest, and local raw path; raw capture stays outside Git.
4. Apply [Select for use, not collection](#select-for-use-not-collection) and [Integrate before expanding](#integrate-before-expanding): update entity and concept pages only when the turn adds reusable knowledge. Create or improve a note when evidence supports a durable claim, distinction, relationship, or implication.
5. Apply [Let navigation emerge](#let-navigation-emerge): add the turn to `wiki/log.md` and keep `wiki/index.md` useful as the first navigation surface.

## Maintenance workflow

When asked to lint or maintain the wiki, apply this file with repository [Issue intake](repository-work.md#issue-intake) and [Verification and delivery](repository-work.md#verification-and-delivery):

1. Find broken links, orphan pages, near-duplicates, unsupported claims, unresolved contradictions, stale syntheses, and concepts without an addressable page.
2. Apply [Stable addresses, evolving content](#stable-addresses-evolving-content) and [Integrate before expanding](#integrate-before-expanding): repair the published layer from preserved evidence, merge duplication into the strongest page, update affected links, and remove the superseded page.
3. Apply [Let navigation emerge](#let-navigation-emerge): improve `wiki/index.md` only where the change helps a reader enter or traverse the network; do not turn it into an exhaustive file listing.

## Research page contract

- Keep the research page on one page. Target 140-180 words and never exceed 220 words. Use at most two compact sections and short paragraphs so the complete `.research-card` remains readable in a 1200x1600 capture.
- The first body content is the heading required by `mode`: `## Source brief` for `SOURCE_BRIEF`, `## Answer` for `QUESTION_ANSWER`, or `## Exploration` for `NOTE_EXPLORE`.
- In a source brief, summarize the sources supplied or linked by the turn, compare what preserved evidence supports, and separate that evidence from caveats, limits, or disagreement. Do not substitute a broad topic explainer.
- In a question answer, resolve the turn's question directly, state the answer first, support it with the strongest preserved evidence, and make limits explicit.
- In a note exploration, identify the claim or topic, test it against preserved evidence, and connect it to relevant entities, concepts, or implications without presenting speculation as fact.
- End factual claims or paragraphs with readable author-date links to preserved source notes. Use a relative target such as `../sources/<source-slug>/`. Use the named author when available, otherwise the responsible organization, then a short source title when neither exists. Never use opaque labels such as `[S1]`. Source notes identify the original URL, retrieval time, content digest, local raw evidence path, and suggested full citation.
- Apply [Preserve productive disagreement](#preserve-productive-disagreement): prefix interpretation with **Inference:**, unresolved gaps with **Uncertainty:**, and incompatible evidence with **Contradiction:**.
- Apply [Links carry the structure](#links-carry-the-structure) and [Connectivity creates value](#connectivity-creates-value): use relative links between research, source, entity, and concept pages and update both sides when a connection aids navigation.
- Do not put a second title in the body; the layout renders front-matter title. Keep the page self-contained and omit process narration.

A research page is complete when local raw evidence and the published chronology entry exist, every material factual claim is cited, labels expose non-factual reasoning, useful cross-links resolve, and rendered `.research-card` attributes `data-research-turn` and `data-research-mode` equal the exact `rkey` and `mode`.

## Source page profile

- The source-page contract governs evidence semantics, not visible layout. Do not require one universal sequence of headings, render empty sections, or copy a template mechanically; use blocks that fit the source type.
- Distinguish the independently citable intellectual source from its representations. Alternate formats or repeated captures of the same content may share a page; materially changed editions or revisions need separate source identity. Never overwrite a representation cited by published evidence.
- Every source page identifies title, source type, creator or responsible organization when known, publication or version status, canonical original URL or identifier, and a suggested citation for that original alone.
- Give every source page a short neutral description of what the source is and covers. Cross-source synthesis, original ideas, deductions, comparisons, recommendations, research plans, and task state belong in research, entity, concept, or note pages.
- Record at least one representation with a stable local ID, retrieval time in UTC, local raw path, format or media type, and digest algorithm and value. Add edition, revision, commit, language, resolved URL, capture method, rights, or representation relations when they affect verification.
- Record assessment state as `not_assessed`, `none_recorded`, or `recorded`. Add source criticism only when material; `none_recorded` means no limitation was recorded for the present use, not that the source is universally authoritative. Never emit an empty criticism section.
- Every source-supported statement used by the wiki identifies what the source states or shows, the exact representation used, and a precise locator. Keep exact quotations distinct from source-attributable paraphrases; quotations are optional and short. Wiki inference never belongs in an evidence entry.
- Match locators to source type. For a mutable webpage, prefer the preserved representation plus a heading, table cell, fragment, or exact text with context. For a machine-readable specification, prefer the immutable representation plus a labeled structural locator such as JSON Pointer and a human-readable operation or path. For a paper, identify edition and page, section, figure, table, or equation. For a repository, identify commit plus path and symbol, heading, or line range.
- Use contextual, typed links for versions, formats, parts, replacements, citations, and downstream use. A source-family or collection page may aid navigation, but claims still terminate at the independently identified member that supports them.
