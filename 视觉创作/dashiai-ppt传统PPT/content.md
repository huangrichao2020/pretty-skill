# dashiai-ppt传统PPT · 真正可编辑的 PPT 生成工具

> [3F Content 范式](../../content-triple-format/) · F1 源文字版

---

## P0 · 封面

- **核心主张**：生成 HTML PPT → 浏览器编辑 → 一键导出真正可编辑的 PPTX
- **疗效**：30 分钟拿到可交付的 .pptx，比纯生图塞 PPTX 的方式多一个编辑环节，交付质量大幅提升
- **金句**：编辑比生成更重要

---

## P1 · 痛点 · 现有 PPT 生成方式的局限

- 生图塞 PPTX：AI 出图 → 截图 → 贴进 PPT → 文字不可编辑、领导没法改
- 模板填充：文字可编辑但视觉单一，缺分析模型和图表
- 在线协作 PPT：依赖网络、隐私风险、交付后无法离线使用

---

## P2 · dashiai-ppt 核心工作流

```
用户需求（自然语言）
  ↓
Mavis 安装并激活 skill（见 P4 安装步骤）
  ↓
整理成 goal.json（结构化需求）
  ↓
bash render_goal_deck.sh → 生成 index.html
  ↓
浏览器打开 → 每一页自带编辑控制台（滑杆/开关/下拉）
  ↓
导出 PPTX / PDF / HTML 单文件
```

---

## P3 · 12 套视觉主题（选一套锁定）

| 主题 | 风格 | 适合场景 | 适合人群 |
|---|---|---|---|
| 轻拟态风 | 白底圆角卡片 | 产品介绍/企业汇报/方案说明 | 产品经理/销售顾问 |
| 炫光紫绿 | 紫绿渐变科技感 | 科技发布会/AI/机器人主题 | 技术负责人 |
| 深浅代码 | 程序员感深色 | 技术方案/系统架构/开发者大会 | 工程师/架构师 |
| 玻璃糖果 | 磨砂玻璃糖果色 | 消费品牌/创意提案/社媒内容 | 品牌团队/设计师 |
| **色谱图表** | **专业数据感** | **数据报告/市场分析/KPI复盘** | **分析师/咨询顾问 ← A股场景首选** |
| 深色图谱 | 深色高密度 | 战略分析/金融报告/产业研究 | 投资人/高管 |
| 冷白调研 | 学术白底 | 调研报告/白皮书/竞品分析 | 研究机构/智库 |
| 黑金实验 | 黑金奢华感 | 高端发布/品牌提案/奢华科技 | 高端品牌/创意总监 |
| 深蓝杂志 | 蓝底杂志风 | 品牌故事/人物访谈/企业形象 | 公关团队/媒体编辑 |
| 金色指数 | 金色金融感 | 金融数据/投资报告/商业榜单 | 投资机构/分析师 |
| 高能增长 | 增长驱动红橙 | 融资路演/商业计划/增长复盘 | 创业者/VC/PE |
| 声波霓虹 | 霓虹色彩感 | 音乐娱乐/潮流活动/直播内容 | 娱乐品牌/活动策划 |

---

## P4 · 安装步骤（Mavis 本地）

### 首次安装（一次性）

```bash
# 克隆到 Mavis skills 目录
mkdir -p ~/.mavis/agents/mavis/skills
cd ~/.mavis/agents/mavis/skills
git clone --depth=1 https://github.com/chuspeeism/dashiAI-ppt-skill dashiai-ppt

# 验证安装成功
ls ~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/
# 应看到：SKILL.md project/ scripts/ assets/ references/
```

### 触发词

用户说以下任意词时激活本 case：
- "做传统 PPT"
- "做正经 PPT"
- "做可编辑 PPT"
- "用 dashiai-ppt"
- "汇报材料"
- "演示文稿"

---

## P5 · 核心使用流程（Mavis 操作员版）

### Step 1：确认需求 + 选风格

激活 skill 后，问用户两个问题（合并为一个）：

> 「这份 PPT 是做什么用的？受众是谁？你偏好哪种视觉风格？」
> 然后展示风格图：`/Users/tingchi/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/assets/skill/theme-style-grid.png`

### Step 2：整理 goal.json

把用户需求整理成结构化 JSON，写入 `<输出目录>/goal.json`。参考 `references/examples/` 下的示例。

### Step 3：生成 HTML

```bash
SKILL_ROOT="/Users/tingchi/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt"
cd <输出目录>
bash "$SKILL_ROOT/scripts/render_goal_deck.sh"
# 首次运行会自动 npm install，约 30-60 秒
# 完成后输出预览 URL（本地 http://127.0.0.1:端口/）
```

### Step 4：给用户预览链接

生成完成后，给用户本地预览 URL，让用户在浏览器里：
1. 翻页看效果
2. 用控制台改文字/布局/图表/配色
3. 满意后点右上角「导出」→ 选 PPTX

### Step 5：导出 PPTX

用户点导出，或 Mavis 用命令行导出：

```bash
SKILL_ROOT="/Users/tingchi/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt"
npm --prefix "$SKILL_ROOT/project" run export:pptx -- <输出目录>/ppt output.pptx
```

**环境要求**：
- Node.js 18+ ✅（已验证本机 v23.11.0）
- Chrome/Chromium/Edge（用于导出 PPTX）✅

---

## P6 · 内置版式库（1020 个版式 × 12 主题）

### 图表类型（开箱即用）
折线/柱状/瀑布/雷达/矩形树图/漏斗/热力/桑基/哑铃/气泡/散点/玫瑰/帕累托/旭日/华夫/坡度……

### 分析模型（现成页面）
SWOT / 波特五力 / PEST / 商业模式画布 / 波士顿矩阵 / 双钻模型 / AARRR / RFM / 飞轮 / 技术成熟度曲线 / 甘特排期

### 页面角色（20 种）
封面 / 摘要 / 目录 / 章节分隔 / 背景 / 指标 / 趋势 / 对比 / 比例 / 关系 / 案例 / 图片 / 流程 / 风险 / 展望 / 氛围 / 行动 / 要点 / 团队 / 结尾

---

## P7 · A股场景适配

**选色谱图表风（theme05）或深色图谱风（theme06）**，因为：
- A股配色：红涨绿跌（dashiai 支持部分配色自定义）
- 内置雷达图/瀑布图/趋势图适合盘面分析
- SWOT/波特五力适合板块/个股诊断
- KPI指标页适合展示信心指数/风险评级

**与 ai-image-to-pptx 的分工**：
- **dashiai-ppt**：需要图表/分析模型/可编辑文字的正经汇报 PPT
- **ai-image-to-pptx**：需要 AI 生图讲解、知识可视化、视觉冲击强的内容

---

## P8 · 与现有 skill 的关系

| 场景 | 工具 |
|---|---|
| 知识讲解/可视化长图 | ai-image-to-pptx（matrix 生图） |
| 正经汇报/分析模型/可编辑 PPTX | **dashiai-ppt（本 case）** |
| 公众号配图/小红书封面 | oil-cover / matrix 生图 |

---

## P9 · 常见问题

**Q：导出 PPTX 后文字不可编辑？**
A：dashiai 的导出引擎逐节点还原，文字保持可编辑；确实无法映射的区块会转成图片，但文字仍从 DOM 抽回可编辑。

**Q：生成一套 PPT 大概多久？**
A：10 页实测约 20 万 token + 1-2 分钟渲染；Node.js 依赖首次自动安装。

**Q：内容隐私安全吗？**
A：零上传——文档内容不发送任何服务器，全部本地处理；只有 npm 安装依赖和版本检查会联网。

---

## 元信息

- **案例来源**：GitHub chuspeeism/dashiAI-ppt-skill（AGPL-3.0）
- **作者**：chuspeeism（主项目）+ Mavis（沉淀为 pretty-skills case）
- **生成日期**：2026-07-11
- **页数**：9 页
- **疗效**：30 分钟交付可编辑 PPTX，比纯生图方式多编辑环节，大幅提升交付质量
- **更新日志**：待补充

---

## 跨引用

- **Skill 主文件**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/SKILL.md`
- **主题预览图**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/assets/skill/theme-style-grid.png`
- **版式库清单**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/references/layout-pool.md`
- **导出引擎（MIT）**：`~/.mavis/agents/mavis/skills/dashiai-ppt/skills/dashiai-ppt/project/packages/html-deck-to-pptx`
- **github**：https://github.com/chuspeeism/dashiAI-ppt-skill
