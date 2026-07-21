# 如何构建并部署

## 步骤

1. 执行生产构建：

   ```bash
   npm run build
   ```

2. 确认 `site/` 下已生成静态文件。
3. 将 `site/` 部署到 GitHub Pages、Netlify、Cloudflare Pages 或任意静态托管。

使用 GitHub Actions 时：在 Pages 源选择 **GitHub Actions** 后，推送到 `main` 即可。
