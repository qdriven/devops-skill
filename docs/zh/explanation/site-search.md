# 本站搜索是如何工作的

文档站点内置了 **离线全文搜索**（docmd `@docmd/plugin-search` + MiniSearch）。它不依赖外部搜索 API，构建时生成索引，在浏览器里本地查询——适合 GitHub Pages、内网与离线预览。

## 为什么需要单独说明

搜索看起来像「侧边栏上的一个框」，但实际行为与常见在线文档站不同：

- 索引是 **构建产物**，不是实时抓取
- 中英文各有一份索引，跟当前语言相关
- 用 `file://` 打开本地 HTML 时搜索会失败（需要 HTTP 服务）

把这些写清楚，能减少「搜不到 / 搜不到英文 / 本地打不开」这类误判。

## 怎么用

1. 打开侧边栏顶部 **选项菜单** 里的搜索入口（放大镜 / Search）
2. 或使用快捷键 **⌘K**（macOS）/ **Ctrl+K**（Windows / Linux）打开搜索框
3. 输入关键词，用方向键移动结果，**Enter** 跳转，**Esc** 关闭

搜索框出现后会加载当前语言对应的索引；首次打开可能有短暂加载。

## 它索引了什么

构建时，docmd 会把 `docs/` 下的 Markdown 页面打进搜索索引，主要包括：

| 字段 | 说明 |
|------|------|
| `title` | 页面标题（权重较高） |
| `headings` | 各级标题 |
| `text` | 正文文本 |

本站开启了中英双语（`zh` / `en`）：

- 默认语言（中文）索引：`site/_docmd-search/search-index.json`
- 英文索引：`site/_docmd-search/en/search-index.json`

切换语言后，搜索会加载对应 locale 的索引，因此中文页主要命中中文文档，英文页主要命中英文文档。

## 工作原理（简要）

```mermaid
flowchart LR
  MD[docs Markdown] --> Build[docmd build]
  Build --> Index[search-index.json]
  Index --> Browser[浏览器 MiniSearch]
  Browser --> UI[搜索结果列表]
```

1. `npm run docs:build`（或 `docmd build`）解析 Markdown，生成静态站点与搜索索引
2. 用户打开搜索时，前端 `fetch` 索引 JSON，用 MiniSearch 做前缀 / 模糊匹配
3. 结果在客户端渲染，无需后端

插件默认启用；本站在 `docmd.config.js` 的 `plugins.search: {}` 中保持开启。

## 限制与注意

- **需要构建**：改文档后必须重新 build，搜索索引才会更新
- **客户端搜索**：索引随站点一起下载；文档很多时体积会变大
- **不要用 file://**：必须通过本地 HTTP（如 `npm run docs:dev`）或已部署的 Pages 访问
- **`--offline` 构建**：若使用 docmd 的 offline 相关标志，搜索可能被禁用
- **非语义搜索**：默认是关键词 / 模糊匹配，不是 LLM 语义理解（除非另行配置 semantic 模式）
- **按语言隔离**：在中文站搜英文专有名词，可能不如切到 English 后再搜

## 相关页面

- [构建文档站点](../how-to/build-docs.md) — 本地预览与生成索引
- [docmd 搜索插件说明](https://docs.docmd.io)（上游文档）
