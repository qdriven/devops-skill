# How to build and preview this docs site

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
