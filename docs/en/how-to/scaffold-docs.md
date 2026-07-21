# How to scaffold a docs site from the docmd template

Use this when creating a Diátaxis docs site for another project (or a new skillset). This repository’s own site already follows the same conventions; for preview/build of **this** site see [How to build and preview this docs site](./build-docs.md).

Full steps and conventions: skill `docmd/SKILL.md` (template at `docmd/template/`).

## Prerequisites

- Node.js 18+
- npm

## Steps (summary)

1. Copy `docmd/template/` into the target project (or flatten to the repo root, same as devops-skill).
2. Change `package.json` `name`, and `docmd.config.js` `title` / `url` / footer copy.
3. Write content under `docs/zh/` and `docs/en/` in tutorials / how-to / explanation / reference.
4. `npm install && npm run dev` to preview; `npm run build && npm run validate` to check.
5. Use the bundled `.github/workflows/deploy-docs.yml` (Node 24: `checkout@v6` / `setup-node@v6` / `upload-pages-artifact@v5` / `deploy-pages@v5`) and set Pages Source to **GitHub Actions**. Canonical copy: `docmd/SKILL.md`.
