# How to create a GitHub Release

Use the `gh-create-release` skill with the GitHub CLI.

## Prerequisites

- `gh` authenticated with permission to create releases
- A tag strategy agreed for the repository

## Steps

1. Ensure the skill is installed for your agent.
2. Follow `gh-create-release/SKILL.md` for flag details, or run a typical publish:

   ```bash
   gh release create v1.0.0 --title "v1.0.0" --notes "Release notes"
   ```

3. For drafts or assets, see the skill reference under `gh-create-release/references/`.
