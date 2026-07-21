# Git Worktree 命令与约束

## 心智模型

一个仓库（`.git`）可挂多个工作目录：每个目录各自检出不同分支，共享对象库与历史，互不影响对方的未提交改动。

```
repository（一份 .git）
├── main worktree      ← clone / init 时的目录
└── linked worktrees   ← git worktree add
    ├── /path/to/wt-b  → branch B
    └── /path/to/wt-c  → branch C（或 detached HEAD）
```

| 概念 | 含义 |
|------|------|
| Main worktree | `git clone` / `git init` 得到的主工作树 |
| Linked worktree | `git worktree add` 挂上的额外工作树 |
| 共享 | commits、blobs、refs、仓库级 config |
| 不共享 | 每个 worktree 的 `HEAD`、index、未跟踪文件、部分 per-worktree 配置 |

约束：**同一分支不能同时被两个 worktree 检出**。并行时用 `-b` 新分支或 `--detach`。

## 常用命令

### 查看

```bash
git worktree list
git worktree list -v
```

### 新增

```bash
# path 末段作默认分支名
git worktree add ../hotfix

# 检出已有分支
git worktree add ../feature-foo feature-foo

# 显式新分支
git worktree add -b experiment ../experiment main

# 临时实验：detached HEAD
git worktree add --detach ../scratch
```

### 移动 / 删除 / 清理

```bash
git worktree move <worktree> <new-path>
git worktree remove <worktree>
git worktree remove -f <worktree>   # 有未提交改动时强制

# 目录已被手动删除时清理元数据
git worktree prune
```

### 锁定（外置盘等）

```bash
git worktree lock ../portable-wt --reason "on USB drive"
git worktree unlock ../portable-wt
```

## 磁盘布局

主仓库：

```
.git/worktrees/<id>/
  ├── HEAD
  ├── gitdir
  └── ...
```

Linked worktree 内通常是一个 `.git` **文件**：

```
gitdir: /path/to/main-repo/.git/worktrees/<id>
```

直接 `rm -rf` 工作目录而不 `remove`/`prune`，会留下过期管理条目。

## 与再 clone 对比

| | 再 clone | worktree |
|--|----------|----------|
| 对象库 | 各一份（或偏重） | 共享一份 |
| 分支可见性 | 需分别 fetch | 同一仓库立刻可见 |
| 并行检出 | 可以 | 可以 |
| 清理 | 删整个目录 | `remove` + 必要时 `prune` |
| 适用 | 机器/权限边界 | 本机并行、临时实验、Agent 隔离 |

## 注意点

1. **分支独占**：已在某 worktree 的分支不能再 `add` 到另一棵树。
2. **删目录走命令**：手动删目录后记得 `prune`。
3. **依赖**：`node_modules` 等通常各自安装。
4. **bare 仓库**：可以只有 linked worktrees。
5. **Agent / IDE**：隔离实验优先 worktree，优于在主树 stash 再切分支。

## 延伸阅读

- `git worktree --help`
- [Git Tools - Multiple Working Trees](https://git-scm.com/docs/git-worktree)
