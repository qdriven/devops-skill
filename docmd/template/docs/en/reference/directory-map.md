# Directory map

| Path | Role |
|------|------|
| `docs/` | Markdown source (`src` in config) |
| `docs/zh/` | Chinese content (default locale at site root) |
| `docs/en/` | English content (URL prefix `/en/`) |
| `docs/*/index.md` | Per-locale landing / section indexes |
| `docs/*/tutorials/` | Learning-oriented pages |
| `docs/*/how-to/` | Task-oriented pages |
| `docs/*/explanation/` | Understanding-oriented pages |
| `docs/*/reference/` | Information-oriented pages |
| `docmd.config.js` | Site configuration (includes `i18n`) |
| `assets/footer.css` | Footer clip fix for sky theme only (not layout widening) |
| `site/` | Build output (`out` in config; gitignored) |
| `.github/workflows/deploy-docs.yml` | GitHub Pages deploy workflow |
