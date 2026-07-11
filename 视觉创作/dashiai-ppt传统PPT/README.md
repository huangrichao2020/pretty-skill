# dashiai-ppt传统PPT · 真正可编辑的 PPT 生成工具

> **一句话定位**：生成 HTML PPT → 浏览器编辑控制台改稿 → 一键导出真正可编辑的 .pptx

---

## 这个 case 是什么

把用户的自然语言需求变成一份正经 PPT：不是生图塞 PPTX，而是先生成带控制台的 HTML，翻页确认、调整布局/图表/配色，满意后一键导出可编辑 PPTX。

**作者**：chuspeeism（主项目）+ Mavis（沉淀为 pretty-skills case）
**生成日期**：2026-07-11
**页数**：9 页

---

## 核心论点

传统 PPT 生成有两个问题：AI 生图塞 PPTX → 文字不可编辑、领导没法改；模板填充 → 视觉单一、缺图表分析模型。dashiai-ppt 的核心解决思路是：**生成是起点，编辑才是终点**。每一页都带控制台，生成后可以继续改，改完再导出交付。

---

## 适用场景

- ✅ 行业研究 / 融资复盘 / 竞品分析 / 趋势报告
- ✅ 项目汇报 / 方案展示 / 内部培训
- ✅ 数据报告（含图表：雷达/瀑布/趋势/SWOT/波特五力等）
- ✅ 需要交付**可编辑 PPTX**给领导/同事继续改的场景
- ❌ 纯知识讲解/可视化长图（用 ai-image-to-pptx）
- ❌ 公众号配图/小红书封面（用 oil-cover）

---

## 触发词

"做传统 PPT" / "做正经 PPT" / "做可编辑 PPT" / "汇报材料" / "演示文稿" / "用 dashiai-ppt"

---

## 使用流程

1. **激活 skill** → 安装路径：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/`
2. **确认需求 + 选风格** → 展示 12 套主题预览图
3. **整理 goal.json** → 结构化需求写入输出目录
4. **生成 HTML** → `bash render_goal_deck.sh`
5. **给用户预览链接** → 用户在浏览器里翻页 + 用控制台改
6. **导出 PPTX** → 用户点导出，或 Mavis 用命令行导出

---

## 12 套视觉主题

| 主题 | 适合场景 | A股适配度 |
|---|---|---|
| 轻拟态风 | 产品介绍/企业汇报 | ⭐⭐⭐ |
| 炫光紫绿 | 科技发布会/AI主题 | ⭐⭐⭐⭐ |
| 深浅代码 | 技术方案/系统架构 | ⭐⭐⭐ |
| 玻璃糖果 | 消费品牌/创意提案 | ⭐⭐ |
| **色谱图表** | **数据报告/KPI复盘** | **⭐⭐⭐⭐⭐ A股首选** |
| 深色图谱 | 战略分析/金融报告 | ⭐⭐⭐⭐ |
| 冷白调研 | 调研报告/白皮书 | ⭐⭐⭐ |
| 黑金实验 | 高端发布/品牌提案 | ⭐⭐⭐ |
| 深蓝杂志 | 品牌故事/人物访谈 | ⭐⭐ |
| 金色指数 | 金融数据/投资报告 | ⭐⭐⭐⭐ |
| 高能增长 | 融资路演/增长复盘 | ⭐⭐⭐ |
| 声波霓虹 | 音乐娱乐/潮流活动 | ⭐⭐ |

---

## 跨引用

- **GitHub 仓库**：https://github.com/chuspeeism/dashiAI-ppt-skill
- **Skill 主文件**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/SKILL.md`
- **主题预览图**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/assets/skill/theme-style-grid.png`
- **版式库清单**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/references/layout-pool.md`
- **导出引擎（MIT）**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/project/packages/html-deck-to-pptx`
