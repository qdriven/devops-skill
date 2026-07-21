# No-hook philosophy

Hooks are optional reminders, not the control plane.

Agents such as Codex, OpenCode, Trae, and Kimi should follow `AGENTS.md`, installed `SKILL.md` files, and explicit CLI calls (`orchestrate.py init` / `finish`). Claude Code may use prompt-submit hooks as a nudge; git hooks may append refs or event logs on commit.

Codex does not execute Claude Code’s `.claude/settings.json` hooks. Prefer the no-hook path so workflows remain portable across agents.
