# How to develop with git worktree

Use when the main tree has uncommitted work, or you need a parallel branch / isolated Agent checkout. Often combined with [git-workflow](./run-git-workflow.md) or [local-workflow](./run-local-workflow.md).

## Prerequisites

- Git 2.5+ (`git worktree`)

## Steps (with git-workflow)

1. Run git-workflow `init` and note Issue number `N`.
2. From the **main repo**, add a linked worktree (prefer branch names starting with the Issue number):

   ```bash
   REPO_NAME="$(basename "$(git rev-parse --show-toplevel)")"
   git worktree add -b "${N}-short-slug" "../${REPO_NAME}-wt-${N}" main
   cd "../${REPO_NAME}-wt-${N}"
   ```

3. Implement, test, and commit inside the worktree; push with `git push -u origin HEAD` when needed.
4. Run `orchestrate.py finish` from the same worktree.
5. Clean up:

   ```bash
   cd /path/to/main-repo
   git worktree remove "../${REPO_NAME}-wt-${N}"
   ```

## Notes

- The same branch cannot be checked out in two worktrees at once.
- Prefer `git worktree remove`; if a directory was deleted manually, run `git worktree prune`.
- Full agent rules: `git-worktree/SKILL.md`.
