---
name: pretty-skills-creator
description: |
  创建新 skill 的入口，自动带 4 风格 HTML 占位 + 可选 PPT。
  Use when 用户说"创建 skill / 做个新 skill / 做 skill / 沉淀到 pretty-skills / 提个新 skill"。
  流程: ps create <name> → 填 metadata → 选 4 风格之一 → 自动生成 4 件套 → 提 PR。
triggers:
  - 创建 skill
  - 做个新 skill
  - 做 skill
  - 沉淀到 pretty-skills
  - 提个新 skill
  - ps create
---

# pretty-skills-creator

> **创** — 让创建新 skill 像"填一个表"一样简单。

## 一句话

**pretty-skills-creator = 创建 skill 的 5 步流水线。**

```
ps create <name>  --title "..." --description "..." --triggers a b c [--style image]
  → 校验输入（name / title / description / triggers）
  → 生成 4 件套：web.html + manifest.yaml + SKILL.md + CHANGELOG.md
  → 装到本地 store（ps create 自动软链 5 agent）
  → 你填细节 → ps contribute → 提 PR
```

## 4 风格

| 风格 | 适合什么 | 例子 |
|---|---|---|
| **image**（生图式默认） | 视觉类 case / 故事 | 案例展示 / 训练营介绍 |
| **code-swiss**（瑞士风） | 工具说明 / 文档型 | API 文档 / 配置说明 |
| **code-tech**（技术深色） | 技术类 case | 调试案例 / 性能分析 |
| **code-paper**（学术 paper） | 论文 / 研究 | 研究报告 / 白皮书 |

## 必备参数

| 参数 | 校验 | 说明 |
|---|---|---|
| `--title` | ≥ 5 字 | Skill 标题（中文 / 英文都行） |
| `--description` | ≥ 100 字 | 一句话定位 + 详细说明（多行用 `\|` 或 `\n`） |
| `--triggers` | ≥ 3 个 | 触发词（用户自然语言） |

## 可选参数

| 参数 | 默认 | 说明 |
|---|---|---|
| `--style` | `image` | 4 风格之一 |
| `--contributor` | `@anonymous` | 你的标识 |
| `--cover-image` | （无） | 封面图 URL（仅 image 风格） |
| `--tags` | （无） | 标签列表 |
| `--related` | （无） | 关联资源描述 |
| `--out-dir` | （必填） | 输出目录 |

## 完整流程

### Step 1 · 写参数

```bash
ps create my-new-skill \
  --title "我的新 skill 标题" \
  --description "$(cat <<EOF
这是一个非常厉害的新 skill，解决了 XXX 问题。
它的核心思路是 YYY，用法是 ZZZ。
适用场景：AAA / BBB / CCC。
EOF
)" \
  --triggers 触发词1 触发词2 触发词3 触发词4 \
  --style code-tech \
  --contributor "huangrichao2020" \
  --tags "tag1" "tag2" \
  --related "knowhub 路径 / 关联 skill" \
  --out-dir "$HOME/.pretty-skills/store"
```

### Step 2 · 校验

脚本会自动校验：
- ✅ name 合法（kebab-case，2-64 字符）
- ✅ title ≥ 5 字
- ✅ description ≥ 100 字
- ✅ triggers ≥ 3 个
- ✅ style 在 4 选 1

### Step 3 · 生成 4 件套

```
~/.pretty-skills/store/my-new-skill/
├── web.html              # 4 风格之一（image/code-swiss/code-tech/code-paper）
├── manifest.yaml         # 符合 pretty-skills manifest schema
├── SKILL.md              # agent 加载入口
└── CHANGELOG.md          # 变更记录
```

### Step 4 · 软链到 5 agent

`ps create` 会自动把 `~/.pretty-skills/store/my-new-skill/` 软链到：
- `~/.claude/skills/my-new-skill`
- `~/.codex/skills/my-new-skill`
- `~/.mavis/skills/my-new-skill`
- `~/.cursor/skills/my-new-skill`
- `~/.windsurf/skills/my-new-skill`

### Step 5 · 提 PR

```bash
cd ~/.pretty-skills/store/my-new-skill
# 改 SKILL.md / manifest.yaml 补细节
ps contribute my-new-skill
```

`ps contribute` 会：
1. fork 主项目
2. clone fork → 创建分支
3. copy 4 件套 → commit
4. push 分支
5. 提 PR with `auto-deploy-placeholder` + `skill-status:placeholder` 标签
6. 主项目自动 merge + 部署 Git Pages

## 跟 pretty-skills（管）的关系

- **pretty-skills（管）**：管理所有 skill 的增删改查
- **pretty-skills-creator（创）**：创建新 skill 的入口
- 二者是父子：装好 pretty-skills 后，`ps create` 就调 pretty-skills-creator

## 缺能力时体验会差

- ❌ 没 `python3` → `ps create` 整个不能用
- ❌ 没 `gh` / `gh auth` → `ps contribute` 不能用 → 退路：手动用 `bash scripts/push.sh` 或网页提 PR
- ❌ 没 matrix MCP → image 风格不会自动生图 → 退路：手动用 Midjourney/即梦，再回填 `--cover-image`

跑 `ps doctor` 看完整体检。
