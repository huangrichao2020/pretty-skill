# 给 pretty-skills 提贡献

> **边缘优先开源** — 你本地增删改无门槛，觉得好就提 PR。

## 贡献流程

### 1. 本地改

```bash
ps list                                # 找到你想改的 skill
vim ~/.pretty-skills/store/<name>/...  # 直接改
```

不用 fork 不用 clone 不需要 main 分支权限。

### 2. 测一下

```bash
ps info <name>                         # 确认改对了
# 或者在某个 agent 里跑一下
```

### 3. 写 changelog

```bash
cd ~/.pretty-skills/store/<name>
# 编辑 CHANGELOG.md，加一行
echo "## 1.0.1 (2026-07-09) · 修了什么" >> CHANGELOG.md
```

### 4. 推回主项目

```bash
ps contribute <name>
```

它会做：
1. 检查本地修改
2. 让你写一句话 PR 描述
3. `gh repo fork` 主项目（一次）
4. clone fork + 建分支
5. 同步 `store/<name>` → `tools/<name>`
6. commit + push + 提 PR

### 5. 维护者 review

PR 进 GitHub 后，主项目维护者会 review：
- ✅ 合并
- 💬 讨论
- ❌ 关闭

## 写新 skill

```bash
ps create my-new-skill
```

它会调 `pretty-skills-creator`，生成：
- 4 风格 HTML 占位（image / code-swiss / code-tech / code-paper）
- `SKILL.md` 模板
- `manifest.yaml` 模板
- `CHANGELOG.md` 空文件

填好之后 `ps contribute my-new-skill` 提 PR。

## 风格要求

### 代码

- bash 脚本顶部带 `set -euo pipefail`
- Python 脚本带 shebang `#!/usr/bin/env python3`
- 不引入新依赖（如必须，先在 PR 描述说明）
- 跨平台（macOS / Linux 都跑得动）

### SKILL.md

- 一句话定位 ≤ 100 字符
- 触发词清单（agent 用这个判断要不要加载）
- "快速开始"小节（让用户 5 分钟能跑起来）
- 例子：`<skill>/SKILL.md`

### manifest.yaml

- 必填字段填齐
- version 遵循 semver
- 依赖用 `>=` 范围

## 决策原则

### 主项目维护者保留什么？

- **API 设计决策** — `ps` 子命令的命名 / 参数 / 行为
- **manifest schema** — 字段的语义和类型
- **风格规范** — 上面这些

### 贡献者保留什么？

- **每个 skill 的内容** — 你写什么就是什么
- **本地使用方式** — 你怎么用都行
- **changelog** — 你的改动你记录

## Code of Conduct

- 主项目维护者 7 天内必回 PR
- 不友好 → 直接 close
- 重大变更 → 先开 issue 讨论
