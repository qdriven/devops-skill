# 系统级安装

将 skills 安装到各 Agent 的全局 skills 目录。重新运行会**强制更新**（刷新内容并替换已有链接/目录）。

## 步骤

```bash
bash dev-workflow-install.sh --system
bash dev-workflow-install.sh --system --agent codex
```

符号链接安装（继续以本仓库为源）：

```bash
bash dev-workflow-symlink-install.sh --system
bash dev-workflow-symlink-install.sh --system --agent trae
```

可选 hooks（已存在则覆盖）：

```bash
bash dev-workflow-install.sh --system --hooks
```

Windows PowerShell：

```powershell
pwsh -File dev-workflow-install.ps1 -System -Agent codex
```
