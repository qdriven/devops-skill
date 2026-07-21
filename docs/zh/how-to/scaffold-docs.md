# 用 docmd 模版新建文档站

给其他项目（或新 skillset）搭 Diátaxis 文档站时使用。本仓库站点本身已按同一约定落地；只预览/构建本站见 [构建并预览本站文档](./build-docs.md)。

完整步骤与约定见 Skill：`docmd/SKILL.md`（模版在 `docmd/template/`）。

## 前置条件

- Node.js 18+
- npm

## 步骤（摘要）

1. 复制 `docmd/template/` 到目标项目（或摊到项目根，与 devops-skill 相同）。
2. 改 `package.json` 的 `name`，以及 `docmd.config.js` 的 `title` / `url` / 页脚文案。
3. 在 `docs/zh/` 与 `docs/en/` 按 tutorials / how-to / explanation / reference 写内容。
4. `npm install && npm run dev` 预览；`npm run build && npm run validate` 检查。
5. 用附带的 `.github/workflows/deploy-docs.yml`，仓库 Pages Source 选 **GitHub Actions**。
