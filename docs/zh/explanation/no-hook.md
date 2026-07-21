# 无 Hook 设计理念

Hook 是可选提醒，不是控制面。

Codex、OpenCode、Trae、Kimi 等 Agent 应遵循 `AGENTS.md`、已安装的 `SKILL.md`，以及显式 CLI（`orchestrate.py init` / `finish`）。Claude Code 可用 prompt-submit hook 作提示；git hook 可在 commit 时追加 refs 或事件日志。

Codex 不会执行 Claude Code 的 `.claude/settings.json` hooks。优先走无 Hook 路径，工作流才能跨 Agent 移植。
