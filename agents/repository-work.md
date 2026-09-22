# Repository work

Read this file for repository setup, tooling, automation, site changes, workflow design, maintenance mechanics, and GitHub administration. Topical research adds the separate requirements in [Research work](research-work.md).

## Coherent task

Repository work is not a research turn. The per-turn Issue, pull-request, research-page, and research-milestone rules do not apply.

- Treat one coherent repository outcome as one task Issue, `issue/<number>-<slug>` branch, and pull request.
- Keep explicit follow-up requests in that existing Issue, branch, and pull request while the task remains open. A later message alone does not create another repository task.
- Create a new task only for an independently scoped outcome or when the user explicitly requests an independent pull request.
- Group related process tasks in one dedicated process-development milestone or leave them without a milestone. Never create per-turn process milestones or use a topical research milestone.
- Process work may remain a chat discussion. When it changes tracked files or repository settings, apply [Issue intake](#issue-intake) and [Verification and delivery](#verification-and-delivery).
- Do not create or update published research, source, entity, concept, note, log, or index pages merely to record process work. Process artifacts belong in Issues, pull requests, and the repository files that implement the workflow.

## Issue intake

- Every new independently scoped repository, process, maintenance, or site task that changes tracked files or repository settings needs a GitHub Issue before implementation. If the user supplies an existing Issue, use it and do not create a duplicate.
- Write every Issue in English and make it self-contained for an agent without the originating conversation. Use the fields and order in `.github/ISSUE_TEMPLATE/task.yml`: task type, research milestone, process milestone, dependency, request, inputs and sources, context, acceptance criteria, constraints and non-goals, execution mode, and handoff readiness.
- **Queue only:** create the Issue with `Execution mode` set to `Queue only`, return its URL, and stop. Do not create a branch or begin implementation.
- **Implement now:** create or adopt the Issue first, set `Execution mode` to `Implement now`, then execute the task in the same session.
- For changes to versioned files, use one branch and pull request per Issue. The pull request must contain `Closes #<number>` so merge closes the Issue.
- For repository-setting changes that cannot have a pull request, execute only after creating the Issue, then add a result comment with verification and close the Issue.

## Verification and delivery

- GitHub Actions is the sole automated verification environment. For versioned work, commit and push the Issue branch, then inspect the pull-request checks. Do not search the workstation for Node or npm, install JavaScript tooling locally, attempt a local site build, or recreate CI checks with ad hoc local scripts.
- Format every commit subject as Conventional Commits 1.0.0: `<type>[optional scope]: <description>`.
- Follow `.github/pull_request_template.md`. Open an English-language pull request containing `Closes #<number>`.
- Merge only after CI passes and the user explicitly authorizes that merge in the current conversation. Merging to `main` closes the Issue and triggers deployment.
