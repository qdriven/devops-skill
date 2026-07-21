# devops-skill

Agent skills for Git / GitHub / local task workflows and secret scanning.

Repository: [qdriven/devops-skill](https://github.com/qdriven/devops-skill) · Docs site: [GitHub Pages](https://qdriven.github.io/devops-skill/) (auto-deploys on push to `main`). Local preview and build: [How to build the docs site](./how-to/build-docs.md).

Switch language with **中文 / English** in the sidebar options menu.

## Choose the right documentation type

| If you want to… | Go to |
|-----------------|-------|
| Complete a first install and run a sample workflow | [Tutorials](./tutorials/) |
| Perform a specific install or workflow command | [How-to guides](./how-to/) |
| Understand git-workflow vs local-workflow and no-hook design | [Explanation](./explanation/) |
| Learn how offline site search works and how to use it | [Site search](./explanation/site-search.md) |
| Look up skills, agents, and script flags | [Reference](./reference/) |

## Skills at a glance

| Skill | Description |
|-------|-------------|
| `git-workflow` | GitHub CLI task workflow (Issue as record → plan/execute → close) |
| `git-worktree` | Isolated/parallel development with git worktrees; pairs with the workflows above |
| `local-workflow` | Local task workflow (no GitHub; local tracing) |
| `github-cli-skill` | Lightweight GitHub CLI helper (repos, issues) |
| `gh-create-release` | Create GitHub Releases |
| `scanning-for-secrets` | Secret scanning (token patterns + optional pre-commit hook) |

Full catalog: [Skills catalog](./reference/skills-catalog.md).

## Install overview

The install scripts support **system** (each agent's global skills directory) and **project** (`./.agents/skills/`). Symlink install is available when this repo should stay the source of truth. Hooks are optional (`--hooks`).

- [How to install (system)](./how-to/install-system.md)
- [How to install (project)](./how-to/install-project.md)
- Flags and agent paths: [Install flags](./reference/install-flags.md), [Agents and paths](./reference/agents.md)

## Which workflow to use

| Situation | Prefer |
|-----------|--------|
| Need GitHub Issue lifecycle | `git-workflow` |
| Local / offline / no GitHub | `local-workflow` |
| Isolated dirs / parallel branches | `git-worktree` (often combined with the above) |

Details: [git-workflow vs local-workflow](./explanation/git-vs-local.md). Workflows work fully without hooks; hooks are optional reminders — see [No-hook design](./explanation/no-hook.md).

## Common starting points

- First time here → [Install and run your first local task](./tutorials/first-local-task.md)
- Install into an agent → [How to install (system)](./how-to/install-system.md)
- Need GitHub Issue tracking → [How to run git-workflow](./how-to/run-git-workflow.md)
- Offline / no GitHub → [How to run local-workflow](./how-to/run-local-workflow.md)
- Isolated / parallel checkouts → [How to develop with git worktree](./how-to/run-git-worktree.md)
