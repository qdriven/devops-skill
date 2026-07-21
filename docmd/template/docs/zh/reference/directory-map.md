# 目录结构

| 路径 | 作用 |
|------|------|
| `docs/` | Markdown 源目录（配置中的 `src`） |
| `docs/zh/` | 中文内容（默认语言，URL 在站点根路径） |
| `docs/en/` | 英文内容（URL 前缀 `/en/`） |
| `docs/*/index.md` | 各语言落地 / 分区首页 |
| `docs/*/tutorials/` | 学习导向 |
| `docs/*/how-to/` | 任务导向 |
| `docs/*/explanation/` | 理解导向 |
| `docs/*/reference/` | 信息导向 |
| `docmd.config.js` | 站点配置（含 `i18n`） |
| `assets/footer.css` | 仅修复 sky 主题页脚裁切（非布局加宽） |
| `site/` | 构建输出（gitignored） |
| `.github/workflows/deploy-docs.yml` | GitHub Pages 部署工作流 |
