# Content Triple Format · 3F Content v3.19

> **一句话定位**：任何 PPT / 长图 / 知识卡片产出物都按 v3.19 发布：
> - **必填 2 件**：`content.md` 源文字 + `xxx讲解.pdf` PDF 讲解版
> - **可选 1 件**：`presentation.pptx` 真实 PowerPoint（需要二次编辑时才生成）
>
> 让内容对 AI 和人类同等友好 + GitHub 原生 PDF 预览 + 不强求 PowerPoint。
>
> 这是 pretty-skills 的核心约定。所有贡献者必读。

> ### ⚠️ 配套 · 生图能力是必须的
>
> 3F Content + 锦绣 范式都依赖 AI 出图。
> **推荐使用 MiniMax 套餐** —— **49 元 Token plan 套餐**就能跑（支持 matrix MCP 多模态生图 + 生视频，月费起步）。
> 没生图能力 = 范式坍塌。

## 为什么 v3.19 从 web.html 改 PDF

| 维度 | web.html（旧）| xxx讲解.pdf（v3.19）|
|---|---|---|
| GitHub 预览 | ❌ **不能**（只下载）| ✅ **原生预览**（内嵌 PDF 阅读器）|
| 文件大小 | 几 KB - 几十 KB | 80-200 KB |
| 演示场景 | ✅ 中央大图 + 键盘翻页 | ✅ 翻页 + 全屏 + 打印 |
| 离线分享 | ✅ 单 HTML | ✅ 单 PDF（更通用）|
| AI 友好 | ⚠️ 可被 AI 解析 HTML | ❌ PDF 二进制 |
| 二次编辑 | ❌ 需改 HTML/CSS | ❌ 需改源 + 重生成 |

**根因**：HTML 演示虽好，但 GitHub 不能预览 → 用户看到的是"白板+乱码"。改 PDF 后，README 里贴 PDF 链接，GitHub 直接渲染。

> **v3.19 切换总结**：
> - 删除 `_模板/案例/web.html` 模板
> - 新增 `_模板/案例/case_pdf.html`（PDF 渲染源）
> - 新增 `tools/build_case_pdf.py`（playwright + chromium 渲染 PDF）
> - 删除 `tools/build_ppt_html.py`（旧 HTML 生成脚本）
> - `check-3f.py` F3 检测改：`*讲解.pdf` 存在 + ≥ 50KB + magic bytes 合法 + 含 image object
> - `manifest.json` 字段 `format.web_html` 改 `format.case_pdf`

## v3.19 必填 + 可选清单

```
<case-name>/
├── content.md            # F1 · 源文字（必填 · 人类 + AI 最高兼容）
├── xxx讲解.pdf            # F3 · PDF 讲解版（必填 · GitHub 原生预览）
├── presentation.pptx     # F2 · PowerPoint（可选 · 仅二次编辑时生成）
├── images/               # AI 出图原图（必填）
├── prompts/              # 出图 prompt 文件（必填 · 工程可复现）
└── 锦绣/                 # 传播素材（必填 · v3.1 简化：2 封面 + slides/ + readme.md）
```

### 为什么 PDF 是必填

| 场景 | PDF | HTML |
|---|---|---|
| GitHub 仓库浏览 | ✅ 直接预览 | ❌ 不能预览 |
| 邮件 / IM 分享 | ✅ PDF 阅读器都能开 | ⚠️ 浏览器 + 依赖外部 CSS |
| 打印 / 演示 | ✅ 原生支持 | ❌ 需特殊设置 |
| 长期归档 | ✅ ISO 标准 | ⚠️ 浏览器兼容性差 |

### 为什么 PPTX 改可选

| 维度 | PDF（必填）| PPTX（可选）|
|---|---|---|
| 通用性 | ✅ 任何 PDF 阅读器 | ❌ 需要 PowerPoint |
| 文件大小 | 80-200 KB | 几 MB - 几十 MB |
| 演示场景 | ✅ 翻页 + 全屏 | ✅ 同样可演示 |
| 二次编辑 | ❌ 需重新生成 | ✅ PowerPoint 友好 |
| AI 友好 | ❌ 二进制 | ❌ 二进制 |
| 协作 | ✅ Git diff 友好 | ⚠️ 二进制难 diff |

**90% 用户只看不编辑** → PDF 就够。**10% 用户要二次编辑** → 显式加 `--with-pptx` 标志。

## 完整工作流

```bash
# 1. 写 content.md（必备 · 数据源）
vim content.md

# 2. 出图（必备 · images/p*.png）
# 用 matrix MCP · 或 skill-creator 自动

# 3. 生成 xxx讲解.pdf（v3.19 必备）
python3 tools/build_case_pdf.py <case_dir>

# 4. 校验 3F 合规
python3 content-triple-format/check-3f.py <case_dir>

# 5. 提交 PR
git add . && git commit -m "feat(<domain>): <case title>" && git push
```

## 字段说明

### content.md（必备 · 数据源）
- 每页 1 个 `## ` 标题 + 4-7 个字段（每字段 1 行 · 80-200 字）
- 喂 LLM / 做素材 / 复刻成图

### xxx讲解.pdf（v3.19 必备 · 表示层）
- 命名规范：`<case name>讲解.pdf`（例：`公众号内容交付方法论讲解.pdf`）
- A4 横版 · 每页 1 张大图 + 标题 + 页码
- 由 `tools/build_case_pdf.py` 自动从 images/ + manifest.json 生成
- 字号大 · 信息密度低 · 一眼能 get

### presentation.pptx（可选 · 二次编辑载体）
- 仅当需要 PowerPoint 二次编辑时才生成
- `python3 tools/build_pptx.py <case_dir> --with-pptx`

### images/（必备 · AI 出图原图）
- 每页 1 张 PNG（≥ 1MB · 2K · 16:9 优先）
- `p0_cover.png`, `p1_xxx.png`, ... 按页顺序

### prompts/（必备 · 工程可复现）
- 每页 1 个 `.md` 文件，含完整出图 prompt
- 可重新跑出图（matrix MCP / 其它生图工具）

### 锦绣/（必备 · 传播素材）
- v3.1 简化：`横屏封面.png` + `竖屏封面.png` + `slides/*.png` (8-12 张) + `readme.md` 融合稿

## 完整规范

- [onboarding-guide.md](./onboarding-guide.md) · 5 步上手
- [methodology.md](./methodology.md) · 设计哲学
- [deep-themes.md](./deep-themes.md) · 风格字典
- [before-after-example.md](./before-after-example.md) · 正反面对照
- [锦绣.md](./锦绣.md) · 4 形态传播素材