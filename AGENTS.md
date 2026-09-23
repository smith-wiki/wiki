# Smith Wiki contract

Smith Wiki is a public research wiki. Everything written to this repository or to GitHub is English: files, commit messages, Issues, pull requests, and milestones, whatever language the conversation uses.

## Messages

- **Research turn:** a message that starts with `/turn` adds knowledge to the wiki. Follow [Research turns](#research-turns).
- **Everything else** is conversation or repository work. Answer questions and discussion in chat. A request to adjust the current turn's pages amends that turn's open pull request.

## Repository work

Repository work changes tracked files, scripts, CI, the site, or GitHub settings.

- One coherent outcome is one Issue, one `issue/<number>-<slug>` branch, and one pull request that closes the Issue. Follow-up requests go into that pull request while it is open.
- Start with `sw task SLUG TITLE REQUEST`. Add `--queue` to record a task for later; start a queued Issue with `sw start ISSUE SLUG`.
- Commit with `sw commit` using Conventional Commits. Open the pull request with `sw pr TITLE BODY`, where the body says what changed and why. Changes under `wiki/` follow [Wiki content](#wiki-content).
- GitHub Actions is the only verification environment; watch it with `sw checks` instead of building the site locally.
- Merge with `sw merge` only after checks pass and the user authorizes that merge in the current conversation.

## Research turns

- A **research thread** is a GitHub milestone. A **turn** is one Issue (the question) and one pull request (the answer) in that milestone, plus one research card in `wiki/research/`.
- A conversation has one active thread. Its first turn passes `--new-thread`, or the milestone the user names to resume. Every later turn in the conversation passes that same milestone, whatever its topic. In a new conversation, resume a thread only from a name, number, or URL the user supplies; if the user asks to resume without one, ask which. Start a different thread mid-conversation only when the user says so.
- Open a turn with `sw turn (--new-thread | THREAD) SLUG TITLE REQUEST`. TITLE and REQUEST are English even when the user writes in another language: translate the user's question, never paste it. The Issue body is the request with its source URLs. When the thread already has an open turn pull request, the new branch stacks on it; after that base merges, run `sw sync`.

Doing a turn:

1. **Orient.** Run `sw` and read the existing pages the turn touches.
2. **Preserve evidence.** Capture every source you rely on with `sw fetch URL`. It stores the original and a Markdown reading copy in the private R2 store under the SHA-256 of the original, and prints the capture record (URL, retrieval time, digest, type), metadata found on the page, and the path of the local Markdown copy. Read that Markdown instead of fetching the page again. For a copy you saved from a browser, such as a paywalled page, add `--file FILE`; `sw fetch --hash SHA` restores any stored capture. Never link to stored originals. For a repository, fetch files by their raw URL at a fixed commit. Read sources yourself; use a subagent only for discovery across many sources.
3. **Build the graph.** Depth lives in source, entity, concept, and note pages, not on the card. Ask what the turn adds to what the wiki already holds: new facts go to the entity or concept they describe, a reusable claim, distinction, or relationship becomes a note, and a connection to an existing page is stated on both pages with why it matters. Revise existing pages before creating new ones.
4. **Write the card.** Answer the turn's question briefly and link the graph pages that carry the depth.
5. **Deliver.** `sw commit`, then `sw pr TITLE BODY`, where the body is the answer: findings, pages added or changed, connections, and open questions. Watch `sw checks`.

A turn is complete when the card answers the question, every claim on the card is backed by a linked page, every new page links to and from at least one existing page, and the pull request states the answer.

## Wiki content

- `wiki/research/`: one card per turn. Front matter has exactly `title`, `rkey`, `date`, `brief`, `turn_url` (the turn Issue URL), and `mode` (`SOURCE_BRIEF`, `QUESTION_ANSWER`, or `NOTE_EXPLORE`). The body starts with `## Source brief`, `## Answer`, or `## Exploration` to match the mode and stays under 200 words: the answer first, then links into the graph.
- `wiki/sources/`: one page per independently citable original source. State the original URL, author or responsible organization, publication date or version when given, retrieval time (UTC), and SHA-256 digest. List the statements the wiki relies on, each with a locator: a heading or exact text for a webpage, a page or section for a paper, a commit and path for a repository. Record caveats such as promotional framing, staleness, or self-reported results when they matter.
- `wiki/entities/`: named people, organizations, projects, products, and places; answers "what is this?"
- `wiki/concepts/`: recurring terms that need a stable definition; titled with a noun phrase.
- `wiki/notes/`: one reusable claim, distinction, relationship, or implication per page; titled with a declarative sentence.

Source, entity, concept, and note pages have `title` and `summary` front matter; the summary feeds the generated section indexes. Section indexes, the research log, and recent research are generated from front matter; edit only the curated starting points in `wiki/index.md`, and only when a turn opens a new area. Page paths are permanent: when merging or renaming, update every inbound link in the same change.

Write Markdown in your own words and quote only when the wording matters. Cite with readable author-date links to source pages, such as `([Lamport, 2025](../../sources/leslie-lamport-tla-homepage/))`. Attribute strong claims to their source. Prefix interpretation with **Inference:**, open gaps with **Uncertainty:**, and conflicting evidence with **Contradiction:**.
