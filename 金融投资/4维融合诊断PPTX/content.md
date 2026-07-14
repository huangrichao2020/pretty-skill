# 4 维融合诊断 PPTX · 复盘 + 出图 + 拼装一站式

> [3F Content 范式](../../../content-triple-format/) · F1 源文字版 · v3.23（7 段骨架 + 认知锚点 + Shot List 必填）
>
> 把 A 股复盘工作流沉淀为可复用 case：拉数据 → 出图 → 拼 PPTX → 8 页深度报告

---

## P0 · 封面

- **标题**：4 维融合诊断 PPTX · 复盘 + 出图 + 拼装一站式
- **副标**：从 daily-market-review 到 macaron 5 色手绘 .pptx · 30 分钟
- **副副标**：3 步流程 + 8 段骨架 + 9 维 rubric
- **作者小字**：Mavis · 2026-07-14 · 金融投资 / #复盘 / #4维融合 / #PPTX
- **章节类型**：封面
- **核心主张**：复盘 PPTX = 1 套可复用的"诊断 + 可视化 + 装订"三件套
- **认知锚点**：「4 维数据看板 + 8 段 P0-P7 骨架」—— 任何复盘 30 分钟出深度 PPTX
- **关键要点**：
  - 3 步流程：拉数据 (5 min) + 出图 (10 min) + 拼 PPTX (15 min)
  - 8 段骨架 P0-P7 = 封面 + 概览 + 4 维 + 下期 + 风险
  - 调用 3 个 skill：daily-market-review + matrix MCP + python-pptx
  - macaron 5 色手绘风格 · 16:9 2K · 红涨绿跌（A 股配色）
- **数据 / 数字**：3 步 / 8 段 / 8 图 / 21 MB PPTX
- **金句**：复盘不是数据堆砌，是 4 维讲清楚 1 天的市场。

---

## P1 · 钩子 · 为什么复盘只写 markdown 不够

- **标题**：复盘 markdown ≠ 复盘 PPTX · 1 张图 vs 8 段深度
- **副标**：3 个真实痛点 + 1 个 PPTX 解药
- **章节类型**：钩子
- **核心主张**：markdown 复盘只能给"读"的人，PPTX 能给"看"的人
- **认知锚点**：「复盘 PPTX = 1 份能讲 1 小时的材料」—— markdown 是笔记，PPTX 是演示
- **关键要点**：
  - **痛点 1**：markdown 复盘 30 分钟看完，PPTX 30 分钟讲完（含问答）
  - **痛点 2**：markdown 是文字密集型，PPTX 是图 + 字混合，传播效率 5x
  - **痛点 3**：markdown 没人主动翻，PPTX 可发群 / 客户 / 二次加工
  - **解药**：4 维融合诊断 PPTX = 8 段 P0-P7 + 8 张 macaron 5 色手绘图
- **数据 / 数字**：传播效率 5x / 8 段 P0-P7 / 8 张图 / 21 MB
- **金句**：数据是死的，解读是活的，PPTX 让解读看得见。

---

## P2 · 总纲 · 3 步流程 + 8 段骨架

- **标题**：3 步流程 + 8 段骨架 · 30 分钟出深度 PPTX
- **副标**：拉数据 → 出图 → 拼 PPTX · P0-P7 8 段不重不漏
- **章节类型**：总纲
- **核心主张**：3 步流程 = 工作流，8 段骨架 = 内容框架
- **认知锚点**：「3 步 × 8 段 = 24 个工作单元」—— 30 分钟完成
- **关键要点**：
  - **Step 1 拉数据（5 min）**：调 `daily-market-review` skill 拉 4 维数据
  - **Step 2 出图（10 min）**：调 matrix MCP（image_synthesize）出 8 张图
  - **Step 3 拼 PPTX（15 min）**：用 python-pptx 模板拼 8 页
  - **8 段骨架 P0-P7**：封面 + 概览 + 4 维 (L0/L1/L2/L3) + 下期 + 风险
- **数据 / 数字**：3 步 / 8 段 / 30 分钟 / 8 张图
- **金句**：流程是骨架，骨架对了 PPTX 自己长出来。

---

## P3 · Step 1 拉数据 · 调 daily-market-review skill

- **标题**：Step 1 · 拉数据（5 min）· 调 daily-market-review
- **副标**：4 维融合框架 = L0 人性 / L1 情绪 / L2 产业 / L3 证据
- **章节类型**：核心解法
- **核心主张**：1 个 skill 拉 4 维数据，30 秒出当日诊断
- **认知锚点**：「daily-market-review = 4 维体检」—— 像看医生一样看市场
- **关键要点**：
  - **调哪个 skill**：`daily-market-review`（Mavis 端 L0-L3 4 维融合框架）
  - **触发词**：用户说"复盘大盘/今天大盘怎么样/复盘今日行情"自动触发
  - **数据源**：
    - 5 大指数 → 腾讯 qt.gtimg.cn
    - 涨停/跌停/成交额 → 东方财富 / 同花顺
    - 板块资金流 → akshare
    - 政策催化 → 公开新闻
  - **输出**：1 份 daily log（feishuclaw/daily/YYYY-MM-DD.md）+ 4 维判定
- **数据 / 数字**：5 大指数 / 4 维框架 / L0-L3 4 层 / 30 秒
- **金句**：4 维融合 = 给市场做日度体检，比单纯看涨跌深 10x。

### 4 维融合框架（daily-market-review skill 输出）

| 层 | 名字 | 看什么 | 权重 |
|---|---|---|---|
| L0 | 人性层 | 住相信号链（5 维）| 否决权最高 |
| L1 | 情绪层 | STW 周期（冰点/复苏/高潮/退潮）| 高 |
| L2 | 产业层 | 政策/业绩/供需（三层齐全=真主线）| 中 |
| L3 | 证据层 | Tier A/B/C/D（证据硬度）| 中 |

**否决权层级**：L0 > L1 > L3 > L2

---

## P4 · Step 2 出图 · 调 matrix MCP（image_synthesize）

- **标题**：Step 2 · 出图（10 min）· 调 matrix MCP
- **副标**：8 张 macaron 5 色手绘图 · 16:9 2K · 一键出图
- **章节类型**：核心解法
- **核心主张**：1 套风格 = 8 张图 = 1 个 PPTX 视觉系统
- **认知锚点**：「macaron 5 色 = 视觉指纹」—— 一眼识别 = 品牌一致
- **关键要点**：
  - **调哪个工具**：`image_synthesize`（matrix MCP · MiniMax Token plan 套餐）
  - **风格锁定**：手绘科教 + macaron 5 色循环（粉 #F8C8DC + 薄荷 #B8E0D2 + 淡黄 #FFE5B4 + 淡蓝 #B4D4E1 + 薰衣草 #D5C5E0）
  - **A 股配色**：红涨绿跌（虽然 macaron 5 色是 pretty-skill 美学，但 A 股图表元素用 A 股配色）
  - **每张图 prompt 必含**：
    1. 主体内容（认知锚点对应的视觉）
    2. macaron 5 色
    3. cream paper #FFF7E8 背景
    4. 顶部 30% 留标题
    5. 16:9 比例
    6. "NO watermark"（反 AI 味）
- **数据 / 数字**：5 色 / 2K / 16:9 / 1 prompt / 8 张图
- **金句**：1 套配色 = 1 套品牌 = 1 套可识别。

### 8 张图 prompt 模板（每页 1 张）

```python
# P0 封面
prompt = f"Hand-drawn educational style illustration. {core_subject}. 
  Macaron pastel colors (pink #F8C8DC + mint #B8E0D2 + yellow #FFE5B4 + 
  blue #B4D4E1 + lavender #D5C5E0). Cream paper #FFF7E8 background. 
  Top 30% reserved for title. 16:9. Title: {P0_title}. NO watermark."
```

8 段图分别对应：
- P0 封面：5 大指数 + 同步性
- P1 概览：4 维数据看板
- P2 L0：5 个信号全亮
- P3 L1：情绪温度计
- P4 L2：6 板块 × 3 维矩阵
- P5 L3：4 Tier 等级金字塔
- P6 下期：3 方向 × 5 维
- P7 风险：1 警告三角 + 3 风险

---

## P5 · Step 3 拼 PPTX · 用 python-pptx 模板

- **标题**：Step 3 · 拼 PPTX（15 min）· python-pptx 模板
- **副标**：每页 = 左图 + 右深度文字（标题/副标/核心/锚点/要点/数据/金句）
- **章节类型**：核心解法
- **核心主张**：1 套模板 = 8 页深度版 PPTX · PowerPoint 可编辑
- **认知锚点**：「左图右文 = 杂志风排版」—— 跟 pretty-skill 美学一致
- **关键要点**：
  - **调哪个工具**：`python-pptx`（标准库 + 1 个脚本）
  - **PPT 模板（每页）**：
    - 左 50% = 1 张 16:9 图（占满）
    - 右 50% = 6 块文字（标题/副标/核心/锚点/要点/数据/金句）
  - **每页文字结构**（按 pretty-skill v3.23 7 段骨架）：
    - 标题（22pt 加粗深棕 #6B4423）
    - 副标（13pt 斜体）
    - 核心主张（14pt 加粗深红 #C0392B）
    - 认知锚点（11pt 斜体）
    - 5 关键要点（11pt · 加粗关键短语）
    - 数据/数字（10pt 斜体）
    - 金句（12pt 加粗）
  - **输出**：1 个 21 MB .pptx · PowerPoint 双击可编辑
- **数据 / 数字**：8 页 / 21 MB / 16:9 / 0 HTML
- **金句**：PPTX 不是 HTML 阅读器，是 PowerPoint 能直接打开的文件。

### python-pptx 模板代码

```python
from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

for i, (img, title, core, anchor, points, data, quote) in enumerate(pages):
    slide = prs.slides.add_slide(blank)
    slide.shapes.add_picture(img, Inches(0), Inches(0), Inches(6.5), Inches(7.5))
    # 右半边文字（6 块 textbox）...
    # 详见 tools/build_diagnosis_pptx.py
prs.save("诊断-YYYY-MM-DD.pptx")
```

---

## P6 · 实战示范 · 2026-07-13 全市场崩盘

- **标题**：实战示范 · 2026-07-13 全市场崩盘
- **副标**：4 维判定 = 系统性风险 + 资金防御切换
- **章节类型**：深化
- **核心主张**：实战验证 3 步流程 = 30 分钟出深度版 PPTX
- **认知锚点**：「4 维判定 → 8 段 PPTX → 21 MB 交付」—— 流水线 1 次跑通
- **关键要点**：
  - **当日数据**：上证 -2.06% / 深成 -3.48% / 创 -3.10%（5 大同步下跌）
  - **L0 判定**：5/5 信号全亮 = 减仓信号生效（最高优先级）
  - **L1 判定**：退潮阶段确立（涨停 32 / 跌停 400 = 0.08 比例）
  - **L2 判定**：0 真主线（中药/银行/燃气都 < 2 层齐全）
  - **L3 判定**：半导体 Tier D（短期承压） + 中药/银行 Tier C
  - **PPT 交付**：21 MB · 8 页 · 8 张 macaron 5 色手绘图 · 桌面
- **数据 / 数字**：5/5 信号 / 0.08 比例 / 0 真主线 / 21 MB
- **金句**：3 步流程跑通 1 次 = 30 分钟搞定 1 天复盘。

### 实战对照

| 阶段 | 之前（markdown）| 现在（PPTX）| 改进 |
|---|---|---|---|
| 数据 | 30 行文字 | 5 指数 + 4 维 = 9 数据点 | 1.5x 信息密度 |
| 解读 | 文字段落 | 8 段 P0-P7 + 5 关键要点/页 | 3x 结构化 |
| 传播 | 文字群发 | PPTX 群发 + 客户分享 | 5x 传播力 |
| 复用 | 写完就过 | 模板可复用 + 案例可学习 | 10x 复利 |

---

## P7 · 收束 · 3 步开始 + 反 AI 味 7 问自检

- **标题**：3 步开始 + 7 问自检 · 复制即用
- **副标**：从今天复盘开始 · 30 分钟出 PPTX
- **章节类型**：收束
- **核心主张**：复制 3 步流程 + 复制 8 段骨架 = 任何复盘 30 分钟出深度 PPTX
- **认知锚点**：「模板 = 杠杆 · 复制 1 次 = 节省 2 小时」—— 流水线思维
- **关键要点**：
  - **第 1 步 · 抄模板**：复制本 case 的 P0-P7 8 段骨架 + Step 1-3 流程
  - **第 2 步 · 调数据**：daily-market-review skill 拉 4 维数据
  - **第 3 步 · 出图 + 拼 PPTX**：matrix MCP 出 8 张图 + python-pptx 拼 8 页
- **数据 / 数字**：3 步 / 8 段 / 30 分钟 / 21 MB
- **金句**：复盘 PPTX 不是炫技，是给市场 1 份能讲 1 小时的材料。

### 反 AI 味 7 问自检（写完 1 份 PPTX 跑一遍 · 1 分钟）

1. 标题加粗 22pt？✓ 通过
2. 核心主张 1 句话（≤ 30 字）？✓ 通过
3. 认知锚点 ≤ 20 字？✓ 通过
4. 5 关键要点 = 加粗 + 普通混合？✓ 通过
5. 数据/数字单独 1 行？✓ 通过
6. 金句加粗居底？✓ 通过
7. 16:9 + 2K + 顶部 30% 留标题？✓ 通过

**判定**：7/7 = 杂志风 PPTX · 5-6 = 微调 · < 5 = 重做

### 模板文件清单

```
金融投资/4维融合诊断PPTX/
├── content.md                                # 本文件（7 段骨架 + 流程）
├── images/                                   # 8 张示范图
│   ├── p0_cover.png
│   ├── p1_overview.png
│   ├── p2_L0_humanity.png
│   ├── p3_L1_sentiment.png
│   ├── p4_L2_industry.png
│   ├── p5_L3_evidence.png
│   ├── p6_next.png
│   └── p7_risk.png
├── 锦绣/readme.md                            # 4 形态说明
└── 4维融合诊断PPTX讲解.pdf                   # 案例 PDF 讲解版
```

---

## 元信息

- **案例来源**：2026-07-13 A 股复盘实战 + daily-market-review skill 升级
- **作者**：Mavis（从 Mavis 工作流沉淀为公共 case）
- **生成日期**：2026-07-14
- **风格**：手绘 macaron 5 色 + 4 维融合
- **页数**：8 页（P0-P7）
- **9 维评分**：v1 7.5/10（按 9 维评分预估）
- **疗效**：1 份 PPTX = 30 分钟（原 3 小时 + markdown 1 小时 + 改稿 2 小时）

---

## 跨引用（v3.20 PDF 时代）

- **PDF 讲解版**（必填 · GitHub 原生预览）：`./4维融合诊断PPTX讲解.pdf`
- **配套 prompt**：`./prompts/`
- **视觉资源**：`./images/`
- **PPTX**（可选 · 仅二次编辑）：`./output/4维融合诊断.pptx`
- **公开方法论源头**：`pretty-skills/内容创作/杂志风公众号品鉴/`（16 条铁律）
- **Mavis 端 skill**：`~/.minimax/agents/mavis/skills/daily-market-review/`（4 维融合框架源头）

---

## 📸 v3.23 Shot List（防"画册"陷阱）

### Shot List

| 优先级 | 页码 | 认知锚点 | 是否必画 | 推荐比例 |
|---|---|---|---|---|
| 必画 | P0 | 5 大指数 + 同步性 | ✅ | 16:9 |
| 必画 | P1 | 4 维数据看板 | ✅ | 16:9 |
| 必画 | P2 | L0 5 信号全亮 | ✅ | 16:9 |
| 必画 | P6 | 下期 3 方向 × 5 维 | ✅ | 16:9 |
| 选画 | P3 | L1 情绪温度计 | ⬜ | 16:9 |
| 选画 | P4 | L2 6 板块 × 3 维矩阵 | ⬜ | 16:9 |
| 选画 | P5 | L3 4 Tier 等级金字塔 | ⬜ | 16:9 |
| 选画 | P7 | 风险警告三角 | ⬜ | 16:9 |
| 跳过 | P 段文字 | 文字说明为主 | ❌ | — |

**规则**：8 段 → 4 必画 + 4 选画 = 总图数 ≤ 6 张（防画册）。
**判断 3 问**：① 去掉图后文字费劲吗？费劲 = 必画  ② 纯流程/数据表？= 选画  ③ 封面/钩子/总纲/案例/收束？= 必画

**来源**：小克碎碎谈「1个skill把长文变配图」(2026-06-13)
