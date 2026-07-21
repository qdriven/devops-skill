# 构建并预览本站文档

本站按 `docmd` Skill（仓库内 `docmd/SKILL.md`）的模版约定搭建。若要**给其他项目新建**文档站，复制 `docmd/template/` 并按该 Skill 操作；下面只覆盖**本仓库站点**的预览与构建。

## 步骤

1. 在仓库根目录安装 Node 依赖：

   ```bash
   npm install
   ```

2. 预览：

   ```bash
   npm run docs:dev
   ```

3. 生产构建：

   ```bash
   npm run docs:build
   ```

4. 输出在 `site/`。推送到 `main` 会触发 `.github/workflows/deploy-docs.yml` 部署到 GitHub Pages。

侧栏选项菜单可在 **中文 / English** 间切换。
