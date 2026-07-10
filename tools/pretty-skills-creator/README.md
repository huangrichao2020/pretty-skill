# pretty-skills-creator（创）

> **创** — 让创建新 skill 像"填一个表"一样简单。
>
> v3.20 PDF 时代 — 去 web.html + 去 4 风格 HTML 模板 + 去 --style picker

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
  --out-dir "$HOME/.pretty-skills/store"

# 3. 改 SKILL.md / manifest.yaml 补细节
cd ~/.pretty-skills/store/my-new-skill
vim SKILL.md

# 4. 准备图 + 跑 build_case_pdf.py 生成真 PDF
mkdir images
# 把 AI 出图放到 images/slide-01.png / slide-02.png / ...
python3 ../../tools/build_case_pdf.py "my-new-skill"
# 工具路径：pretty-skill/tools/build_case_pdf.py · v3.20 极简版

# 5. 提 PR
ps contribute my-new-skill
```

## 4 件套

| 文件 | 干什么 |
|---|---|
| `xxx讲解.pdf.placeholder.md` | PDF 占位说明（跑 build_case_pdf.py 生成真 PDF）|
| `manifest.yaml` | 符合 pretty-skills schema，ps 工具用它发现 / 装 / 校验 |
| `SKILL.md` | agent 加载入口，agent 读这个决定要不要触发这个 skill |
| `CHANGELOG.md` | 变更记录（用户后续 PR 时维护）|

## v3.20 改造（**对比 v3.18**）

| v3.18（PPT 时代）| v3.20（PDF 时代）|
|---|---|
| `web.html` 必填（4 风格之一）| ❌ 删 |
| 4 风格 HTML 模板（image/code-swiss/code-tech/code-paper）| ❌ 删 |
| `--style` 参数（PPT picker）| ❌ 删 |
| `xxx讲解.pdf` 可选 | ✅ 必填（GitHub 原生预览）|
| `presentation.pptx` 兜底 | ✅ 仍可选（已有的 .pptx 保留）|

## 目录结构

```
tools/pretty-skills-creator/
├── SKILL.md                          # agent 加载入口
├── README.md                         # 你正在看
├── manifest.yaml                     # 工具自己的 manifest
├── scripts/
│   ├── create_skill.py               # 主脚本（被 ps create 调用）· v3.20
│   └── push.sh                       # 提 PR helper
└── docs/
    └── (待写)
```

> v3.18 的 `templates/` 目录（4 个 .html）已删 · 用户说"创建流程里不要 PPT/HTML"

## 校验规则

| 参数 | 校验 | 缺了 |
|---|---|---|
| `name` | 2-64 字符 / 全小写 / kebab-case | 报错 |
| `title` | ≥ 5 字 | 报错 |
| `description` | ≥ 100 字 | 报错 |
| `triggers` | ≥ 3 个 | 报错 |

## 跟 pretty-skills（管）的关系

- **pretty-skills（管）**：管理所有 skill
- **pretty-skills-creator（创）**：创建新 skill
- 二者是父子：装好 pretty-skills 后，`ps create` 就调 pretty-skills-creator
- pretty-skills-creator 的 manifest 里 declare 依赖 pretty-skills（`>=0.1.0`）

## 缺能力时退路

| 缺 | 体验降级 | 退路 |
|---|---|---|
| `python3` | `ps create` 整个不能用 | 手动用 4 件套模板 + 提 PR |
| `gh` / `gh auth` | `ps contribute` 不能用 | 手动 `bash scripts/push.sh` 或网页提 PR |
| matrix MCP / AI 出图 | 跑不出真 PDF | 手动用 DALL-E / 即梦 出图，再回填 |
| `pyyaml` | `ps create` 报错 | `pip install pyyaml` |

跑 `ps doctor` 看完整体检。
