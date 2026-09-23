# Smith Wiki contract

Smith Wiki is a public research wiki. Everything written to this repository or to GitHub is English: files, commit messages, Issues, pull requests, and milestones, whatever language the conversation uses.

## Messages

- **Research turn:** a message that starts with `/turn` adds knowledge to the wiki. Read [Research work](agents/research-work.md) before acting.
- **Everything else** is conversation or repository work. Answer questions and discussion in chat. A request to adjust the current turn's pages amends that turn's open pull request.

## Repository work

Repository work changes tracked files, scripts, CI, the site, or GitHub settings.

- One coherent outcome is one Issue, one `issue/<number>-<slug>` branch, and one pull request that closes the Issue. Follow-up requests go into that pull request while it is open.
- Start with `sw task SLUG TITLE REQUEST`. Add `--queue` to record a task for later; start a queued Issue with `sw start ISSUE SLUG`.
- Commit with `sw commit` using Conventional Commits. Open the pull request with `sw pr TITLE BODY`, where the body says what changed and why. Changes under `wiki/` follow the content rules in [Research work](agents/research-work.md).
- GitHub Actions is the only verification environment; watch it with `sw checks` instead of building the site locally.
- Merge with `sw merge` only after checks pass and the user authorizes that merge in the current conversation.
