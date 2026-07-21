# Install script flags

| Flag / arg | Meaning |
|------------|---------|
| `--system` | Install into agent global skills directories |
| `--project` | Install into the current project skills directory |
| `--agent <name>` | Limit install to one agent (for example `codex`, `claude-code`, `trae`) |
| `--hooks` | Also install optional hooks where supported; overwrites if present |
| Symlink scripts | `dev-workflow-symlink-install.sh` keeps this repo as the source |

**Force update**: Re-running an install script refreshes the canonical copy and replaces existing links/directories (no more `[SKIP]`).

PowerShell mirror: `dev-workflow-install.ps1` with `-System` / `-Project` and `-Agent`.
