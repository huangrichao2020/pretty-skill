---
name: dashiai-ppt
description: |
  制作传统 PPT / 汇报材料 / 可编辑 PPTX 时使用。
  dashiai-ppt = 生成 HTML PPT → 浏览器编辑（控制台/滑杆/换布局）→ 一键导出真正可编辑的 PPTX。
  比 ai-image-to-pptx（生图塞PPT）多了编辑环节，交付质量更高。
  适合：正经汇报 / 分析模型（SWOT/波特五力/雷达图） / 需要交付可编辑 PPTX 的场景。
  不适合：知识讲解/可视化长图（用 ai-image-to-pptx）/ 公众号配图（用 oil-cover）。
triggers:
  - 做传统PPT
  - 做正经PPT
  - 做可编辑PPT
  - 汇报材料
  - 演示文稿
  - dashiai-ppt
  - 传统ppt
---

# dashiai-ppt · 真正可编辑的 PPT 生成工具

## 一句话定位

HTML PPT 生成 → 浏览器编辑控制台改稿 → 一键导出真正可编辑的 .pptx。

## 三段式工作流（借鉴 CyberPPT）

**段1: 证据链** → **段2: 视觉蓝图** → **段3: PPTX 重建**

```
用户需求（自然语言）
  ↓
段1: 写证据链
  → 每页 slides[].evidence.conclusion：这页凭什么成立
  → evidence_ids[]：引用 text 字段中的数据 key
  → conflicts[]：需回避或说明的矛盾（可选）
  ↓
段2: 选 layout 填视觉蓝图
  → layout:query 选页
  → inspect:layout + props:safe 填 props
  → bash render_goal_deck.sh → index.html
  ↓
段3: 浏览器编辑 + 导出
  → 控制台改稿（文字/布局/图表/配色）
  → 导出 PPTX / PDF / HTML
```

> **核心原则**: 先过"证据关"再进"视觉关"——如果某页说不出"凭什么成立"，先补 evidence 再选 layout。

## Step 1：选风格（先问用户）

**必须先问用户选哪种风格，不要跳过这一步。**

展示 12 套主题预览图：
`/Users/tingchi/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/assets/skill/theme-style-grid.png`

A股/金融场景推荐：**色谱图表风（theme05）** 或 **深色图谱风（theme06）**

## Step 2：生成 HTML

```bash
SKILL_ROOT="/Users/tingchi/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt"
mkdir -p <输出目录> && cd <输出目录>
bash "$SKILL_ROOT/scripts/render_goal_deck.sh"
```

首次运行自动 npm install（约 30-60 秒）。

## Step 3：给用户预览链接

生成完成后输出预览 URL，用户在浏览器里翻页 + 用控制台改稿。

## Step 4：导出 PPTX

用户点右上角「导出」→ 选 PPTX，或用命令行：

```bash
SKILL_ROOT="/Users/tingchi/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt"
npm --prefix "$SKILL_ROOT/project" run export:pptx -- <输出目录>/ppt output.pptx
```

## 环境要求

- Node.js 18+ ✅
- Chrome/Chromium/Edge（导出 PPTX 用）

## Skill 根目录

`/Users/tingchi/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/`

## ⚠️ 反模式（已踩坑）

1. **不要跳过选风格** — 必须先问用户选哪种风格，展示主题预览图，用户确认后再生成
2. **讲解图不要出现页码标记** — 图里不要有"P1"/"P2"等标注；标题和内容直接表达，页码只在 PDF 合成时标注
