# skill-creator · pretty-skill 自动化工具

> **任何知识 → 1 键生成完整 pretty-skill 目录（3F Content + 锦绣）**
>
> v3 核心工具。全球开发者 / 玩家都能用。

> ### ⚠️ 前置条件 · 生图能力是必须的
>
> skill-creator 默认调 matrix MCP 出图。
> **推荐使用 MiniMax 套餐** —— **49 元 Token plan 套餐**就能跑（月费起步，支持多模态生图 + 生视频）。
> 没生图 = skill-creator 只能生成「骨架」，不是真视觉化。

---

## 💡 这是什么

CLI 工具，把任意知识（.md / URL / 笔记 / 你脑子里想的）一键变成 pretty-skill 完整目录：

- `content.md`（4-7 字段/页 · **必填**）
- `web.html`（PPT 演示版 · **必填**）
- `output/<case_name>.pptx`（**可选** · 加 `--with-pptx` 才生成）
- `images/`（N 张 AI 出图 · **必填**）
- `锦绣/`（v3.1 简化：横屏封面 + 竖屏封面 + 8-12 讲解图 + 1 融合 md · **必填**）

**意义**：让"贡献一个 skill"和"创建 1 个 GitHub repo"一样简单。

---

## 🛠️ 安装

```bash
# 未来发布到 PyPI
pip install pretty-skill

# 现在用 git clone
git clone https://github.com/huangrichao2020/pretty-skill.git
cd pretty-skill
pip install -e skill-creator/
```

---

## 🚀 5 分钟上手

### 输入：任意 .md

```bash
python skill-creator/create.py \
  --input my-knowledge.md \
  --domain "金融投资" \
  --style "深色科技风" \
  --output ./output/

# 自动生成：
# output/<domain>/<case-name>/
# ├── content.md
# ├── images/        # 9 张 AI 出图
# ├── output/        # PPTX
# ├── web.html
# ├── prompts/       # 9 个 prompt 文件
# └── 锦绣/          # v3.1 简化（按形式 · 不锁死平台）
#     ├── cover-横屏.png
#     ├── cover-竖屏.png
#     ├── slides/    # 8-12 张讲解图
#     └── readme.md  # 1 份融合 md（公众号 + 自媒体稿 + AI 阅读）
```

### 输入：URL（博客 / 知乎 / 公众号）

```bash
python skill-creator/create.py \
  --url https://zhuanlan.zhihu.com/p/xxxxxx \
  --domain "思维方法" \
  --style "马卡龙"
```

### 输入：视频脚本

```bash
python skill-creator/create.py \
  --input video-script.md \
  --domain "内容创作" \
  --style "深色科技风" \
  --pages 8
```

---

## 📋 命令行参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `--input` | 是* | 输入 .md 文件路径 |
| `--url` | 是* | 输入 URL（与 --input 二选一）|
| `--domain` | 是 | 11 预设领域之一（AI能力 / 编程开发 / ...）|
| `--style` | 否 | 视觉风格（马卡龙 / 古铜金 / 蓝白灰 / 深色科技风 / 城市插画 / 真实生活感）· 默认蓝白灰 |
| `--pages` | 否 | PPT 页数（默认 9）|
| `--output` | 否 | 输出目录（默认 ./output/）|
| `--no-jinxiu` | 否 | 跳过锦绣 3 样生成（仅生成 3F Content）|
| `--with-pptx` | 否 | 生成真实 .pptx（v3.2 默认不生成）|
| `--api-key` | 否 | AI 出图 API key（默认读环境变量 `MATRIX_API_KEY`）|

---

## 🎯 工作流（v3 推荐）

```
1. 用户准备知识（任意形式）              ← 0 分钟
   ↓
2. skill-creator create               ← 5 分钟
   ├─ 解析输入 → content.md（4-7 字段/页）
   ├─ 调 matrix AI 出图（9 张）
   ├─ python-pptx 嵌图 → presentation.pptx
   ├─ html-ppt-viewer（v3.2 升级） → web.html（PPT 演示版 · 必填）
   ├─ （可选）python-pptx → presentation.pptx
   └─ 锦绣 3 样生成（横屏封面 + 竖屏封面 + 8-12 讲解图 + 1 融合 md）
   ↓
3. 人类编辑 / 调优视觉（30 分钟）        ← 30 分钟
   ↓
4. check-3f.py 跑过                    ← 10 秒
   ↓
5. 提 PR → GitHub Actions 自动跑 → merge  ← 1 分钟
```

**关键**：
- 步骤 2 = 机器做（80% 自动化）
- 步骤 3 = 人做（20% 调优）
- 步骤 4-5 = 工具做（100% 自动化）

**总时间**：从知识到合并 = ~40 分钟

---

## 🔧 实现细节

### 输入解析

- `.md` 文件 → 按 `## P{n}` 自动切页
- URL → 调 browser-act skill 抓取 + 转 .md
- 视频脚本 → 按时间戳切分

### 内容生成（content.md）

每页 4-7 字段：
- 标题 / 副标
- 章节类型（钩子 / 总纲 / 核心解法 / 深化 / 收束）
- 核心主张（1 句话）
- 关键要点（3-5 bullets）
- 数据 / 数字
- 金句
- 童趣图标

### AI 出图

默认调 matrix MCP：
```python
mavis mcp call matrix matrix_generate_image '{"prompt": "...", "aspect_ratio": "16:9", "resolution": "2K"}'
```

也支持：
- DALL-E
- Midjourney
- Stable Diffusion
- 即梦 / 文心一言

### 锦绣 3 样生成（v3.1 简化）

| 形态 | 模板 | 实现 |
|---|---|---|
| 横屏封面 | 1 张 16:9 大图 | matrix 出图 + 1 句话金句叠加 |
| 竖屏封面 | 1 张 3:4 或 9:16 大图 | matrix 出图 + 1 句话金句叠加 |
| 讲解图集 slides/ | 8-12 张 16:9 | matrix 出图 × 8-12 + 标题叠加 |
| 锦绣视频脚本 | 30-60 秒 | 模板文案 + 用户填实 |

---

## 🛣️ Roadmap

| 版本 | 状态 | 目标 | 进度 |
|---|---|---|---|
| v0.1 | ✅ 已完成 | CLI 框架 + 命令行参数 + 11 领域 / 6 风格 + visibility 参数 | ✅ |
| v0.2 | ✅ **v3.15 完成** | 真分页 · 真写 4 件套骨架（content.md + manifest.json + web.html + 锦绣 4 形态）+ prompts/ | ✅ 实测通过 |
| v0.3 | 计划 | 真调 matrix 出图 · 嵌图到 PPTX · 跑 check-3f.py 自动验证 |
| v0.4 | 计划 | URL 输入支持（browser-act 集成）+ 自动 fetch + 转 .md |
| v1.0 | 计划 | 完整 3F Content + 锦绣 + PR 模板 + CI 自动提 PR |
| v2.0 | 计划 | Web UI（拖拽 .md / 输入 URL → 一键生成）|

### v0.2 真实成果

跑 v0.2 后，骨架自动生成：

```text
output/<domain>/<case-name>/
├── content.md          (4-7 字段/页 · 按 H2 自动分页)
├── manifest.json       (含 --visibility 字段 · v3.11 PR 必填)
├── web.html            (PPT 演示版骨架 · 用 _模板/案例/web.css)
├── NEXT_STEPS.md       (5 步清单：编辑 → 出图 → 校验 → 提 PR)
├── prompts/            (每页 1 个 matrix prompt 模板 · 手绘马卡龙风)
└── 锦绣/                (4 形态占位 + .gitignore)
    ├── cover-横屏.png.placeholder
    ├── cover-竖屏.png.placeholder
    ├── readme.md       (融合稿 · 公众号 + 自媒体 + AI 阅读三用)
    └── slides/         (N 张 PNG 占位 · placeholder 形式)
```

**实测结果**（2026-07-08）：

```bash
$ python skill-creator/create.py \
    --input sample-knowledge.md \
    --domain "金融投资" \
    --case-name "chokepoint-test"
✅ manifest.json (public)
✅ content.md (6 页 · 自动分页)
✅ web.html (PPT 演示版骨架)
✅ 锦绣/ 4 形态骨架 (cover × 2 + 6 slides + readme.md)
✅ prompts/ 6 个 (matrix prompt 模板)
✅ NEXT_STEPS.md (接下来做什么)
```

---

## 🤝 贡献

skill-creator 本身欢迎全球开发者贡献：
- 新增出图 API（DALL-E / Midjourney / 即梦 / ...）
- 新增视觉风格预设
- 新增内容解析器（PDF / URL / 视频）
- 新增锦绣模板

参考 [CONTRIBUTING.md](../CONTRIBUTING.md) 提 PR。

---

参考：
- [README.md](../README.md) · 项目总览
- [CONTRIBUTING.md](../CONTRIBUTING.md) · 完整贡献指南
- [content-triple-format/README.md](../content-triple-format/README.md) · 3F Content 范式
- [content-triple-format/锦绣.md](../content-triple-format/锦绣.md) · 锦绣范式