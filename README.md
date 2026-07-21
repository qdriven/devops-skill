# devops-skill

开发工作流相关的 AI Agent Skill 集合。

源自我仓库 `fire-skills/skills/devops`，现已独立为 GitHub 仓库：[qdriven/devops-skill](https://github.com/qdriven/devops-skill)。

文档站点（docmd + Diátaxis，中文 / English）：源码在 [`docs/zh/`](./docs/zh/)、[`docs/en/`](./docs/en/)，构建后发布到 GitHub Pages：https://qdriven.github.io/devops-skill/

本站按 [`docmd`](./docmd/SKILL.md) Skill 的模版约定搭建；可复制骨架在 [`docmd/template/`](./docmd/template/)。

```bash
npm install
npm run docs:dev      # 本地预览（侧栏可切换中英文）
npm run docs:build    # 输出到 site/
```

推送到 `main` 时由 [`.github/workflows/deploy-docs.yml`](./.github/workflows/deploy-docs.yml) 自动部署。仓库 Settings → Pages → Source 需选择 **GitHub Actions**。

## 技能列表

| Skill | 说明 |
|-------|------|
| **git-workflow** | 基于 GitHub CLI 的任务工作流（创建 Issue body 主记录 → 计划/执行/检查 → 更新并关闭 Issue） |
| **git-worktree** | 用 git worktree 做隔离/并行开发；可与 git-workflow、local-workflow 组合 |
| **git-pr** | 推送分支并创建/更新 GitHub PR（可选；可接在 git-workflow finish 之后） |
| **local-workflow** | 本地任务工作流（无需 GitHub，本地追踪记录） |
| **docmd** | 用捆绑的 Diátaxis 模版搭建 / 构建 docmd 文档站（本仓库文档站即活示例） |
| **github-cli-skill** | 简化版 GitHub CLI 工具（仓库创建、Issue 管理） |
| **gh-create-release** | GitHub Release 创建工具 |
| **scanning-for-secrets** | 代码安全扫描（9 种 Token 模式 + Pre-commit Hook） |

## 安装

推荐使用本目录下的统一脚本（**默认强制更新**：刷新内容并替换已有链接/目录）：

```bash
# macOS / Linux / WSL2 / Git Bash
# System 级（安装到各 agent 的全局 skills 目录）
bash skillsets/devops-skill/dev-workflow-install.sh --system
bash skillsets/devops-skill/dev-workflow-install.sh --system --agent codex

# Project 级（安装到当前项目 ./.agents/skills/）
bash skillsets/devops-skill/dev-workflow-install.sh --project

# 附带 git hooks（已存在则覆盖）
bash skillsets/devops-skill/dev-workflow-install.sh --system --hooks
```

符号链接安装（推荐，便于本仓库继续作为源）：

```bash
bash skillsets/devops-skill/dev-workflow-symlink-install.sh --system
bash skillsets/devops-skill/dev-workflow-symlink-install.sh --system --agent trae
bash skillsets/devops-skill/dev-workflow-symlink-install.sh --project
```

Windows PowerShell：

```powershell
pwsh -File skillsets/devops-skill/dev-workflow-install.ps1 -Scope system -Agent codex
pwsh -File skillsets/devops-skill/dev-workflow-install.ps1 -Scope project
```

Codex project level 安装到 `.agents/skills`；system/global 安装到 `$CODEX_HOME/skills`（未设置时为 `~/.codex/skills`）。Claude Code 使用 `.claude/skills`，Trae 使用 `.trae/skills`。

## No-Hook 使用方式

不需要安装 hook 也可以完整使用 Git/Local workflow。推荐把 hook 当成可选提醒，而不是主控制机制。

Codex 下的 GitHub Issue 工作流：

```bash
python3 .agents/skills/git-workflow/scripts/orchestrate.py init \
  --title "任务标题" \
  --description "任务描述"

# Agent 执行计划、修改和测试

python3 .agents/skills/git-workflow/scripts/orchestrate.py finish \
  --agent-expansion "范围澄清、关键假设、验收标准" \
  --plan "执行计划" \
  --execution "变更内容、测试和检查" \
  --message "完成总结"
```

Codex 下的本地工作流：

```bash
python3 .agents/skills/local-workflow/scripts/orchestrate.py init tasks/my-task.md
# Agent 执行任务
python3 .agents/skills/local-workflow/scripts/orchestrate.py finish
```

只有在确实需要自动提醒或 commit 事件日志时，再安装 hook：

```bash
bash skillsets/devops-skill/dev-workflow-install.sh --project --hooks --agent claude-code
```

注意：Codex 不执行 Claude Code 的 `.claude/settings.json` hook。Codex 的控制入口是 `AGENTS.md`、已安装的 `.agents/skills/*/SKILL.md`，以及上面的显式 CLI。

## 选择建议

| 场景 | 推荐 Skill |
| --- | --- |
| 任务需要 GitHub Issue 生命周期 | `git-workflow` |
| 隔离目录 / 并行分支 / 不弄脏主工作区 | `git-worktree`（常与上面两个 workflow 组合） |
| 本地/离线/无需 GitHub 的任务追踪 | `local-workflow` |
| 用模版新建 / 构建 docmd 文档站 | `docmd` |
| 只需要 GitHub CLI 命令速查 | `github-cli-skill` |
| 创建 GitHub Release | `gh-create-release` |
| commit/push 前查 secret | `scanning-for-secrets` |
