# How to install (system)

Install skills into each agent’s global skills directory. Re-running **force-updates** (refreshes content and replaces existing links/directories).

## Steps

```bash
bash dev-workflow-install.sh --system
bash dev-workflow-install.sh --system --agent codex
```

Symlink install (keeps this repo as the live source):

```bash
bash dev-workflow-symlink-install.sh --system
bash dev-workflow-symlink-install.sh --system --agent trae
```

Optional hooks (overwrites if present):

```bash
bash dev-workflow-install.sh --system --hooks
```

Windows PowerShell:

```powershell
pwsh -File dev-workflow-install.ps1 -System -Agent codex
```
