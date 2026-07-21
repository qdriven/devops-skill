# docmd Diátaxis Template

基于 [docmd](https://github.com/docmd-io/docmd) 与 [Diátaxis](https://diataxis.fr)（参考 [diataxisSkills](https://github.com/trogera/diataxisSkills)）的文档站点模版。

本目录是 **devops-skill 的 `docmd` Skill** 捆绑模版：Agent 按 [`../SKILL.md`](../SKILL.md) 复制本目录即可新建文档站。活示例见 devops-skill 仓库根的 `docs/` 与 [在线站点](https://qdriven.github.io/devops-skill/)。

## 目录结构

```text
docs/
├── zh/                   # 中文（默认语言，站点根路径）
│   ├── index.md
│   ├── tutorials/
│   ├── how-to/
│   ├── explanation/
│   └── reference/
└── en/                   # English（URL 前缀 /en/）
    └── …
```

| 类型 | 用途 | 读者在做什么 |
|------|------|--------------|
| **Tutorial** | 第一次完成一件完整的事 | 跟着学 |
| **How-to** | 解决一个具体问题 | 按步骤做 |
| **Explanation** | 理解背景与「为什么」 | 读懂概念 |
| **Reference** | 查阅事实与规格 | 扫描查找 |
| **Landing** | 帮读者选对文档类型 | 决定去哪 |

侧栏选项菜单可切换 **中文 / English**。页脚使用 docmd `complete` 样式；`assets/footer.css` 仅修复 sky 主题下页脚被裁切的问题。

## 快速开始

```bash
cd path/to/docmd/template   # 或复制后的目标目录
npm install
npm run dev      # http://localhost:3000
npm run build    # 输出到 site/
npm run validate # 检查内链
```

## GitHub Pages

仓库已附带 `.github/workflows/deploy-docs.yml`（**Node 24** action majors：`checkout@v6`、`setup-node@v6`、`upload-pages-artifact@v5`、`deploy-pages@v5`）。定稿说明见 [`../SKILL.md`](../SKILL.md)。

```bash
# 可选：官方生成器；若输出仍是 @v4，请用本模版 workflow 覆盖
npx @docmd/core deploy --github-pages
```

在 GitHub 仓库 Settings → Pages → Source 选择 **GitHub Actions**。

把 `docmd.config.js` 里的 `url` 改成你的 Pages 地址，例如：

`https://<user>.github.io/<repo>`

## 复制到新项目

1. 复制整个本 `template/` 目录（或按 [`../SKILL.md`](../SKILL.md) 摊到项目根）
2. 改 `package.json` 的 `name`、`docmd.config.js` 的 `title` / `url`
3. 按 Diátaxis 四类目录写内容，保持 Landing 页只做导航
