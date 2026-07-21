# devops-skill

面向 AI Agent 的 Git / GitHub / 本地任务工作流与密钥扫描技能集合。

仓库：[qdriven/devops-skill](https://github.com/qdriven/devops-skill) · 文档站点：[GitHub Pages](https://qdriven.github.io/devops-skill/)（推送到 `main` 自动部署）。本地预览与构建见 [构建文档站点](./how-to/build-docs.md)。

## 选择合适的文档类型

| 如果你想… | 去这里 |
|-----------|--------|
| 完成第一次安装并跑通示例工作流 | [教程](./tutorials/) |
| 执行具体的安装或工作流命令 | [操作指南](./how-to/) |
| 理解 git-workflow 与 local-workflow、以及无 Hook 设计 | [解释](./explanation/) |
| 了解本站离线搜索如何工作与怎么用 | [本站搜索](./explanation/site-search.md) |
| 查阅技能列表、Agent 与脚本参数 | [参考](./reference/) |

## 技能一览

| Skill | 说明 |
|-------|------|
| `git-workflow` | 基于 GitHub CLI 的任务工作流（Issue 作主记录 → 计划/执行 → 关闭） |
| `git-worktree` | 用 git worktree 做隔离/并行开发；可与上述 workflow 组合 |
| `local-workflow` | 本地任务工作流（无需 GitHub，本地追踪记录） |
| `github-cli-skill` | 简化版 GitHub CLI 工具（仓库、Issue） |
| `gh-create-release` | 创建 GitHub Release |
| `scanning-for-secrets` | 代码安全扫描（Token 模式 + 可选 pre-commit hook） |

完整说明见 [技能目录](./reference/skills-catalog.md)。

## 安装概览

统一安装脚本支持 **system**（各 Agent 全局 skills 目录）与 **project**（`./.agents/skills/`）；也可用符号链接安装，便于本仓库继续作为源。可选 `--hooks`。

- [系统级安装](./how-to/install-system.md)
- [项目级安装](./how-to/install-project.md)
- 参数与 Agent 路径见 [安装参数](./reference/install-flags.md)、[Agent 与路径](./reference/agents.md)

## 何时用哪个 workflow

| 场景 | 推荐 |
|------|------|
| 需要 GitHub Issue 生命周期 | `git-workflow` |
| 本地 / 离线 / 无需 GitHub | `local-workflow` |
| 隔离目录 / 并行分支 | `git-worktree`（常与上面组合） |

对比细节：[git-workflow 与 local-workflow](./explanation/git-vs-local.md)。不装 hook 也能完整使用工作流；hook 仅为可选提醒，见 [无 Hook 设计](./explanation/no-hook.md)。

## 常见入口

- 第一次来 → [安装并跑通第一个本地任务](./tutorials/first-local-task.md)
- 安装到 Agent → [系统级安装](./how-to/install-system.md)
- 需要 GitHub Issue 追踪 → [运行 git-workflow](./how-to/run-git-workflow.md)
- 离线 / 不用 GitHub → [运行 local-workflow](./how-to/run-local-workflow.md)
- 隔离目录 / 并行分支 → [用 git worktree 隔离开发](./how-to/run-git-worktree.md)
