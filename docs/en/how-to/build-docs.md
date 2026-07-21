# How to build and preview this docs site

This site follows the `docmd` skill (`docmd/SKILL.md`) template conventions. To **scaffold a new docs site** for another project, copy `docmd/template/` and follow that skill. The steps below only cover preview/build for **this** repository's site.

## Steps

1. Install Node dependencies from the repository root:

   ```bash
   npm install
   ```

2. Preview:

   ```bash
   npm run docs:dev
   ```

3. Production build:

   ```bash
   npm run docs:build
   ```

4. Output is written to `site/`. Pushing to `main` runs `.github/workflows/deploy-docs.yml` and deploys to GitHub Pages.

Switch language with **中文 / English** in the sidebar options menu.
