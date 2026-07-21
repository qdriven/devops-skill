# 运行 git-workflow

当任务需要 GitHub Issue 生命周期时使用。

## 前置条件

- 已登录的 `gh`
- 带有 GitHub remote 的仓库

## 步骤

1. 初始化：

   ```bash
   python3 .agents/skills/git-workflow/scripts/orchestrate.py init \
     --title "任务标题" \
     --description "任务描述"
   ```

2. 实现工作（计划、改代码、测试）。
   - 需要隔离目录时，见 [用 git worktree 隔离开发](./run-git-worktree.md)。
3. 收尾并关闭 Issue：

   ```bash
   python3 .agents/skills/git-workflow/scripts/orchestrate.py finish \
     --agent-expansion "范围澄清、关键假设、验收标准" \
     --plan "执行计划" \
     --execution "变更内容、测试和检查" \
     --message "完成总结"
   ```
