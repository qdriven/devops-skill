# 创建 GitHub Release

配合 GitHub CLI 使用 `gh-create-release` skill。

## 前置条件

- `gh` 已登录且有创建 Release 权限
- 仓库已约定 tag 策略

## 步骤

1. 确认 skill 已安装到你的 Agent。
2. 按 `gh-create-release/SKILL.md` 查看参数，或执行典型发布：

   ```bash
   gh release create v1.0.0 --title "v1.0.0" --notes "Release notes"
   ```

3. Draft / 附件等细节见 `gh-create-release/references/`。
