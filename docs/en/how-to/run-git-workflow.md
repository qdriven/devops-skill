# How to run git-workflow

Use when the task needs a GitHub Issue lifecycle.

## Prerequisites

- Authenticated `gh`
- Repository with a GitHub remote

## Steps

1. Initialize:

   ```bash
   python3 .agents/skills/git-workflow/scripts/orchestrate.py init \
     --title "任务标题" \
     --description "任务描述"
   ```

2. Implement the work (plan, code, tests).
   - For an isolated checkout, see [How to develop with git worktree](./run-git-worktree.md).
3. Finish and close the Issue:

   ```bash
   python3 .agents/skills/git-workflow/scripts/orchestrate.py finish \
     --agent-expansion "范围澄清、关键假设、验收标准" \
     --plan "执行计划" \
     --execution "变更内容、测试和检查" \
     --message "完成总结"
   ```
