# 用 git worktree 隔离开发

主工作区有未提交改动、或需要并行分支 / Agent 隔离目录时使用。常与 [git-workflow](./run-git-workflow.md) 或 [local-workflow](./run-local-workflow.md) 组合。

## 前置条件

- Git 2.5+（支持 `git worktree`）

## 步骤（配合 git-workflow）

1. 按 git-workflow `init` 创建 Issue，记下编号 `N`。
2. 从**主仓库**另开 worktree（分支名建议以 Issue 编号开头）：

   ```bash
   REPO_NAME="$(basename "$(git rev-parse --show-toplevel)")"
   git worktree add -b "${N}-short-slug" "../${REPO_NAME}-wt-${N}" main
   cd "../${REPO_NAME}-wt-${N}"
   ```

3. 在 worktree 目录内实现、测试、提交；需要时 `git push -u origin HEAD`。
4. 在同一 worktree 内跑 `orchestrate.py finish`。
5. 清理：

   ```bash
   cd /path/to/main-repo
   git worktree remove "../${REPO_NAME}-wt-${N}"
   ```

## 注意

- 同一分支不能同时被两个 worktree 检出。
- 删除用 `git worktree remove`；若曾手动删目录，再 `git worktree prune`。
- 完整约定见 skill：`git-worktree/SKILL.md`。
