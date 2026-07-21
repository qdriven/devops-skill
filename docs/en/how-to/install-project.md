# How to install (project)

Install skills into the current project (for example `./.agents/skills/`). Re-running **force-updates**.

## Steps

```bash
bash dev-workflow-install.sh --project
bash dev-workflow-symlink-install.sh --project
```

With hooks (Claude Code; overwrites if present):

```bash
bash dev-workflow-install.sh --project --hooks --agent claude-code
```

PowerShell:

```powershell
pwsh -File dev-workflow-install.ps1 -Project
```

Codex project installs go to `.agents/skills`. Claude Code uses `.claude/skills`. Trae uses `.trae/skills`.
