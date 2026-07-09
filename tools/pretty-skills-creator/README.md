# pretty-skills-creator（创）

> **创** — 让创建新 skill 像"填一个表"一样简单。

## 一句话

**pretty-skills-creator = 5 步流水线，把"我有个 skill 想法"变成"提了 PR 的新 skill"。**

## 快速开始

```bash
# 1. 装 pretty-skills（前置）
curl -fsSL https://raw.githubusercontent.com/huangrichao2020/pretty-skills/main/tools/pretty-skills/install.sh | bash

# 2. 创建新 skill
ps create my-new-skill \
  --title "我的新 skill 标题" \
  --description "这是一个非常厉害的新 skill，解决了 XXX 问题..." \
  --triggers 触发词1 触发词2 触发词3 \
  --style image \
  --out-dir "$HOME/.pretty-skills/store"

# 3. 改 SKILL.md / manifest.yaml 补细节
cd ~/.pretty-skills/store/my-new-skill
vim SKILL.md

# 4. 提 PR
ps contribute my-new-skill
```

## 4 件套

| 文件 | 干什么 |
|---|---|
| `web.html` | 4 风格之一（image / code-swiss / code-tech / code-paper），用户预览用 |
| `manifest.yaml` | 符合 pretty-skills schema，ps 工具用它发现 / 装 / 校验 |
| `SKILL.md` | agent 加载入口，agent 读这个决定要不要触发这个 skill |
| `CHANGELOG.md` | 变更记录（用户后续 PR 时维护） |

## 4 风格

| 风格 | 适合什么 | 触发 |
|---|---|---|
| **image**（生图式默认） | 视觉类 case / 故事 | `--style image` |
| **code-swiss**（瑞士风） | 工具说明 / 文档型 | `--style code-swiss` |
| **code-tech**（技术深色） | 技术类 case | `--style code-tech` |
| **code-paper**（学术 paper） | 论文 / 研究 | `--style code-paper` |

## 目录结构

```
tools/pretty-skills-creator/
├── SKILL.md                          # agent 加载入口
├── README.md                         # 你正在看
├── manifest.yaml                     # 工具自己的 manifest
├── scripts/
│   ├── create_skill.py               # 主脚本（被 ps create 调用）
│   └── push.sh                       # 提 PR helper
├── templates/
│   ├── image.html                    # 4 风格 HTML 模板
│   ├── code-swiss.html
│   ├── code-tech.html
│   └── code-paper.html
└── docs/
    └── (待写)
```

## 校验规则

| 参数 | 校验 | 缺了 |
|---|---|---|
| `name` | 2-64 字符 / 全小写 / kebab-case | 报错 |
| `title` | ≥ 5 字 | 报错 |
| `description` | ≥ 100 字 | 报错 |
| `triggers` | ≥ 3 个 | 报错 |
| `style` | 4 选 1 | 报错 |

## 跟 pretty-skills（管）的关系

- **pretty-skills（管）**：管理所有 skill
- **pretty-skills-creator（创）**：创建新 skill
- 二者是父子：装好 pretty-skills 后，`ps create` 就调 pretty-skills-creator
- pretty-skills-creator 的 manifest 里 declare 依赖 pretty-skills（`>=0.1.0`）

## 缺能力时退路

| 缺 | 体验降级 | 退路 |
|---|---|---|
| `python3` | `ps create` 整个不能用 | 手动用 4 风格 HTML 模板 + 提 PR |
| `gh` / `gh auth` | `ps contribute` 不能用 | 手动 `bash scripts/push.sh` 或网页提 PR |
| `matrix MCP` | image 风格不会自动生图 | 手动用 Midjourney / 即梦，再回填 `--cover-image` |
| `jinja2` / `pyyaml` | `ps create` 报错 | `pip install jinja2 pyyaml` |

跑 `ps doctor` 看完整体检。
