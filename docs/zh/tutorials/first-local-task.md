# 安装并跑通第一个本地任务

完成本教程后，你将为项目 Agent 安装好 devops-skill，并完成一次 local-workflow 追踪的初始化与收尾。

## 前置条件

- 技能本身不依赖 Node；需要 Python 3 与 git。
- 能从 `.agents/skills`（Codex）或等价路径加载 skills 的 AI Agent。
- 可在其中创建 `tasks/` 的 git 仓库。

## 步骤

1. Clone 或打开 [devops-skill](https://github.com/qdriven/devops-skill) 仓库。
2. 在目标项目根目录做项目级安装（若仓库路径不同请自行调整）：

   ```bash
   bash /path/to/devops-skill/dev-workflow-install.sh --project
   ```

3. 创建示例任务文件：

   ```bash
   mkdir -p tasks
   cat > tasks/hello.md <<'EOF'
   # Hello local workflow

   写一行笔记，说明 local-workflow 追踪可用。
   EOF
   ```

4. 初始化追踪：

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py init tasks/hello.md
   ```

5. 完成这个小任务（例如新增 `notes/hello.txt` 写一行），然后收尾：

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py finish
   ```

6. 打开 `tasks/tracing/hello.md`，确认状态为 completed。

你已经在不创建 GitHub Issue 的情况下跑通了第一次 local-workflow。
