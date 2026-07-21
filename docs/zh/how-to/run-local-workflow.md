# 运行 local-workflow

用于本地 / 离线任务追踪，不依赖 GitHub Issue。

## 步骤

1. 指定任务 Markdown：

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py init tasks/my-task.md
   ```

2. 实现任务。
3. 标记完成（除非明确要求，否则不提交）：

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py finish
   ```

可选提交 / 推送（仅在明确要求时）：

```bash
python3 .agents/skills/local-workflow/scripts/orchestrate.py finish --commit
python3 .agents/skills/local-workflow/scripts/orchestrate.py finish --commit --push
```
