# 项目级安装

安装到当前项目（例如 `./.agents/skills/`）。重新运行会**强制更新**。

## 步骤

```bash
bash dev-workflow-install.sh --project
bash dev-workflow-symlink-install.sh --project
```

附带 hooks（Claude Code；已存在则覆盖）：

```bash
bash dev-workflow-install.sh --project --hooks --agent claude-code
```

PowerShell：

```powershell
pwsh -File dev-workflow-install.ps1 -Project
```

Codex 项目级安装到 `.agents/skills`；Claude Code 使用 `.claude/skills`；Trae 使用 `.trae/skills`。
