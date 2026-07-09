# Changelog

所有 notable 的变更都记在这里。格式参照 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [Unreleased]

### 计划中
- `ps search` — 搜索主项目所有 skill
- `ps publish` — 把本地 skill 发布成独立仓库
- `ps audit` — 检查 manifest 是否合法 / 依赖是否完整
- 自更新机制（`ps self update` 升级工具自身）

## [0.1.0] - 2026-07-09

### 新增
- 工具第一版，从单数 pretty-skill 重塑为复数 pretty-skills
- 8 个子命令：`ps list / info / add / rm / update / graph / contribute / sync / create / help`
- 跨 5 agent 安装（Claude Code / Codex / Mavis / Cursor / Windsurf）
- 公共 store + 软链架构（`~/.pretty-skills/store/` → 各 agent skills 目录）
- manifest.yaml 必填 + JSON Schema 验证
- `ps graph` 输出 Mermaid 依赖图
- `ps contribute` 自动 fork + 提 PR
- `ps create` 调 pretty-skills-creator
- 安装脚本 install.sh（支持 `--agents` / `--no-symlink`）
- 4 个文档：install.md / contributing.md / skill-schema.md / changelog.md

### 设计原则
- 边缘优先开源（本地增删改无门槛）
- PR 是用户主动判断，不是自动同步
- 跨 agent 一次装
- 依赖关系透明

[Unreleased]: https://github.com/huangrichao2020/pretty-skills/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/huangrichao2020/pretty-skills/releases/tag/v0.1.0
