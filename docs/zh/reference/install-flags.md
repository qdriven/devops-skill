# 安装脚本参数

| 参数 | 含义 |
|------|------|
| `--system` | 安装到 Agent 全局 skills 目录 |
| `--project` | 安装到当前项目 skills 目录 |
| `--agent <name>` | 限定某个 Agent（如 `codex`、`claude-code`、`trae`） |
| `--hooks` | 同时安装可选 hooks（若支持）；已存在则覆盖 |
| Symlink 脚本 | `dev-workflow-symlink-install.sh` 以本仓库为源 |

**强制更新**：重新运行安装脚本会刷新 canonical 副本并替换已有链接/目录（不再 `[SKIP]`）。

PowerShell 对应：`dev-workflow-install.ps1`，参数 `-System` / `-Project` 与 `-Agent`。
