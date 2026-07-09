# Changelog

所有 notable 的变更都记在这里。格式参照 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [Unreleased]

### 计划中
- `ps search` — 搜索主项目所有 skill
- `ps publish` — 把本地 skill 发布成独立仓库
- `ps audit` — 检查 manifest 是否合法 / 依赖是否完整
- 自更新机制（`ps self update` 升级工具自身）

## [0.1.1] - 2026-07-09

### 新增
- **`ps doctor`** — 环境能力体检（8 项检查）
  - 关键：bash / git / curl
  - 重要：python3 / gh / gh auth / ~/.local/bin in PATH
  - 可选：生图能力（matrix MCP）/ jq
  - `ps doctor --explain` 加一段"缺能力时体验会差在哪"
  - `install.sh` 装完自动跑一次
- **pretty-skills-creator 完整迁移**（4 件套生成器）
  - `scripts/create_skill.py` — 校验输入 + 生成 4 件套（web.html + manifest.yaml + SKILL.md + CHANGELOG.md）
  - `scripts/push.sh` — 提 PR helper（fork + 分支 + 标签）
  - 4 风格 HTML 模板：image / code-swiss / code-tech / code-paper
  - manifest.yaml 符合 pretty-skills schema（不是 json）
  - 路径从 `<domain>/<case>/` 适配为 `tools/<name>/`
- **路径修正**：
  - `ps create` 找 create_skill.py 的路径修对（`scripts/create_skill.py`）
  - `ps create` 转发所有参数给 create_skill.py
  - `ps list` 处理多行 `description: |` 格式
- **新文档** `tools/pretty-skills/docs/doctor.md` — 体检输出解读

### 修复
- BSD sed `\s` 不支持 → 改 `[[:space:]]`
- bash `declare -A` 不支持 → 改纯 awk
- symlink 路径不解析 → ps 主命令用 `readlink -f`

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
