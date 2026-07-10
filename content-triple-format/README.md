# Content Triple Format · 3F Content v3.20

> **一句话定位**：任何 PPT / 长图 / 知识卡片产出物都按 v3.20 发布：
> - **必填 2 件**：`content.md` 源文字 + `xxx讲解.pdf` PDF 讲解版
> - **可选 1 件**：`presentation.pptx` 真实 PowerPoint（需要二次编辑时才生成）
>
> 让内容对 AI 和人类同等友好 + GitHub 原生 PDF 预览 + 不强求 PowerPoint。
>
> **v3.20 重大变更**：PPT 相关流程去掉 html 阅读器兜底，默认 `.pptx` 输出（按 `ppt-best-practice.md`）。详细背景见 mavis agent MEMORY.md · PPT 任务用户偏好 v2。
>
> 这是 pretty-skills 的核心约定。所有贡献者必读。

> ### ⚠️ 配套 · 生图能力是必须的
>
> 3F Content + 锦绣 范式都依赖 AI 出图。
> **推荐使用 MiniMax 套餐** —— **49 元 Token plan 套餐**就能跑（支持 matrix MCP 多模态生图 + 生视频，月费起步）。
> 没生图能力 = 范式坍塌。

## 为什么 v3.20 从 PPT 路线去掉 html 兜底

按 **PPT 任务用户偏好 v2（2026-07-10 用户强烈反馈后固化）**：

| 维度 | 旧（v3.18-19 含 html 兜底）| 新（v3.20 默认 .pptx） |
|---|---|---|
| PPT 默认输出 | ❌ HTML 阅读器中间步骤（"先 HTML 验收再 PPTX" 范式） | ✅ 直接 `.pptx` 真实文件 |
| AI 出图内容 | ❌ 文字用 HTML 数据卡叠加 | ✅ 讲解图本身带中文 + 数据（AI 直接出）|
| PowerPoint 打开 | ⚠️ 走 PPTX 流程才能编辑 | ✅ `.pptx` 双击打开即编辑 |
| 分享体验 | ⚠️ HTML 浏览器打开 / PPTX 双击 | ✅ PPTX 双击打开（统一）|

**根因**（用户反馈 2026-07-10）：
> "以后 pretty-skills 也好，knowhub 也好，里面的 ppt 相关技能都去掉 html，然后这次我要你做的是按 knowhub 里的 ppt 技能，生成讲解长电科技的 pptx，懂吗，pptx 直接合并图片生成。"

> **v3.20 切换总结**：
> - 删除 PPT 相关技能里的 html 兜底步骤
> - 默认 `presentation.pptx`（不是 HTML 阅读器）
> - 讲解图本身带中文 + 数据（不依赖 HTML 数据卡）
> - 新增 `ppt-best-practice.md`（v3.20 完整 PPT 流程最佳实践）

## v3.20 必填 + 可选清单

```
<case-name>/
├── content.md            # F1 · 源文字（必填 · 人类 + AI 最高兼容）
├── xxx讲解.pdf            # F3 · PDF 讲解版（必填 · GitHub 原生预览）
├── presentation.pptx     # F2 · PowerPoint（可选 · 仅二次编辑时生成 · v3.20 默认不依赖 HTML）
├── images/               # AI 出图原图（必填 · 讲解图带中文 + 数据）
├── prompts/              # 出图 prompt 文件（必填 · 工程可复现）
└── 锦绣/                 # 传播素材（必填 · v3.1 简化：2 封面 + slides/ + readme.md）
```

### 为什么 PDF 是必填

| 场景 | PDF | HTML（已废止）|
|---|---|---|
| GitHub 仓库浏览 | ✅ 直接预览 | ❌ 不能预览 |
| 邮件 / IM 分享 | ✅ PDF 阅读器都能开 | ⚠️ 浏览器 + 依赖外部 CSS |
| 打印 / 演示 | ✅ 原生支持 | ❌ 需特殊设置 |
| 长期归档 | ✅ ISO 标准 | ⚠️ 浏览器兼容性差 |
| PPT 任务交付 | ❌ 不算 .pptx 交付 | ❌ 不算 .pptx 交付 |

### 为什么 PPTX 是默认（可选 → 默认升级）

| 维度 | PDF（必填）| PPTX（默认 · 可选）|
|---|---|---|
| 通用性 | ✅ 任何 PDF 阅读器 | ✅ PowerPoint / Keynote / WPS |
| 文件大小 | 80-200 KB | 几 MB - 几十 MB |
| 演示场景 | ✅ 翻页 + 全屏 | ✅ 同样可演示 |
| 二次编辑 | ❌ 需重新生成 | ✅ PowerPoint 友好 |
| AI 友好 | ❌ 二进制 | ❌ 二进制 |
| 协作 | ✅ Git diff 友好 | ⚠️ 二进制难 diff |

**v3.20 升级**：PPTX 从「可选」升级为「默认交付物」—— 讲解图本身带中文 + 数据，python-pptx 嵌入即可生成真实 .pptx，PowerPoint 双击打开即用。

## 完整工作流（v3.20 · PPT 默认 .pptx 路线）

```bash
# 1. 写 content.md（必备 · 数据源）
vim content.md

# 2. 出图（必备 · images/p*.png · 讲解图带中文 + 数据）
# 用 matrix MCP · 或 skill-creator 自动
# 共享 [4 STYLE] 段 + 5 段式 prompt · 每页 ≤ 60 行
# 4 并发跑 / 3 轮搞定 12 张图

# 3. 生成 xxx讲解.pdf（v3.20 必备 · 展示用）
python3 tools/build_case_pdf.py <case_dir>

# 4. （可选 · 二次编辑时）生成 presentation.pptx
python3 tools/build_pptx.py <case_dir> --with-pptx
# v3.20 不再依赖 HTML 阅读器 · 直接走 ai-image-to-pptx

# 5. 校验 3F 合规
python3 content-triple-format/check-3f.py <case_dir>

# 6. 提交 PR
git add . && git commit -m "feat(<domain>): <case title>" && git push
```

## 字段说明

### content.md（必备 · 数据源）
- 每页 1 个 `## ` 标题 + 4-7 个字段（每字段 1 行 · 80-200 字）
- 喂 LLM / 做素材 / 复刻成图

### xxx讲解.pdf（v3.20 必备 · 表示层）
- 命名规范：`<case name>讲解.pdf`
- A4 横版 · 每页 1 张大图 + 标题 + 页码
- 由 `tools/build_case_pdf.py` 自动从 images/ + manifest.json 生成
- 字号大 · 信息密度低 · 一眼能 get

### presentation.pptx（v3.20 默认 · 二次编辑载体）
- **v3.20 升级**：从"可选"升级为"默认交付"
- 直接走 `ai-image-to-pptx` 技能：讲解图（带中文 + 数据）→ python-pptx 嵌入 → .pptx
- `python3 tools/build_pptx.py <case_dir> --with-pptx`
- 完整 PPT 流程最佳实践：`ppt-best-practice.md`

### images/（必备 · AI 出图原图 · 讲解图带中文 + 数据）
- 每页 1 张 PNG（≥ 1MB · 2K · 16:9 优先）
- `p0_cover.png`, `p1_xxx.png`, ... 按页顺序
- **关键**：讲解图本身带中文 + 量化数据，不需要 HTML 数据卡叠加

### prompts/（必备 · 工程可复现）
- 每页 1 个 `.md` 文件，含完整出图 prompt
- 共享 [4 STYLE] 段 + 5 段式 prompt 模板
- 可重新跑出图（matrix MCP / 其它生图工具）

### 锦绣/（必备 · 传播素材）
- v3.1 简化：`横屏封面.png` + `竖屏封面.png` + `slides/*.png` (8-12 张) + `readme.md` 融合稿

## 完整规范

- [onboarding-guide.md](./onboarding-guide.md) · 5 步上手
- [methodology.md](./methodology.md) · 设计哲学
- [deep-themes.md](./deep-themes.md) · 风格字典
- [before-after-example.md](./before-after-example.md) · 正反面对照
- [锦绣.md](./锦绣.md) · 4 形态传播素材
- [ppt-best-practice.md](./ppt-best-practice.md) · ⭐ v3.20 新增 · PPT 流程最佳实践（共享风格段 + 5 段式 prompt + python-pptx 嵌入）
