# How to run local-workflow

Use for local / offline task tracing without GitHub Issues.

## Steps

1. Point at a task markdown file:

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py init tasks/my-task.md
   ```

2. Implement the task.
3. Mark complete (no commit unless you ask for it):

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py finish
   ```

Optional commit / push (only when explicitly requested):

```bash
python3 .agents/skills/local-workflow/scripts/orchestrate.py finish --commit
python3 .agents/skills/local-workflow/scripts/orchestrate.py finish --commit --push
```
