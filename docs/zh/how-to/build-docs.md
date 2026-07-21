# 构建并预览本站文档

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
