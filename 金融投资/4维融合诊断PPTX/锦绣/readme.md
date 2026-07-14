# 4 维融合诊断 PPTX · 锦绣 / 4 形态

> 4 形态：cover-横屏 (2.35:1) + cover-竖屏 (1:1) + slides (8 张) + readme.md
> 用途：① 在 GitHub 看 case 一眼明白工作流 ② 复用到自己的复盘 ③ 训练 AI 出图 prompt 参考

## 文件清单

```
4维融合诊断PPTX/
├── content.md                          # F1 源文字版（7 段骨架 + 3 步流程 + 8 段认知锚点）
├── manifest.json                       # v3.11 必填（含 visibility=public）
├── images/
│   ├── p0_cover.png                    # 5 大指数 + 同步性
│   ├── p1_overview.png                 # 4 维数据看板
│   ├── p2_L0_humanity.png              # 5 信号全亮
│   ├── p3_L1_sentiment.png             # 情绪温度计
│   ├── p4_L2_industry.png              # 6 板块 × 3 维矩阵
│   ├── p5_L3_evidence.png              # 4 Tier 等级金字塔
│   ├── p6_next.png                     # 3 方向 × 5 维评估
│   └── p7_risk.png                     # 风险警告三角
└── 锦绣/
    ├── cover-横屏.png                  # 2.35:1 公众号首图
    ├── cover-竖屏.png                  # 1:1 小红书/朋友圈
    ├── slides/                          # 8 页讲解图（同 images/）
    └── readme.md                       # 本文件
```

## 4 形态

### 1. cover-横屏 (2.35:1)
- 公众号首图 / 视频号封面
- 待生成

### 2. cover-竖屏 (1:1)
- 小红书 / 朋友圈
- 待生成

### 3. slides (8 张讲解图)
- 8 张图，对应 P0-P7 8 段
- 必画 4 张（P0 封面 / P1 概览 / P2 L0 / P6 下期）
- 选画 4 张（P3 L1 / P4 L2 / P5 L3 / P7 风险）
- 已在 images/ 目录

### 4. readme.md (本文件)
- 4 形态说明
- 3 步流程
- 跨工具引用

## 3 步流程（30 分钟出 PPTX）

### Step 1 · 拉数据（5 min）
- 调 `daily-market-review` skill
- 触发词：用户说"复盘大盘/今天大盘怎么样"
- 数据源：5 大指数 + 涨停/跌停/成交额 + 板块资金流
- 输出：daily log + 4 维判定

### Step 2 · 出图（10 min）
- 调 `image_synthesize`（matrix MCP）
- 风格：手绘 macaron 5 色循环
- 8 张图 = P0-P7 每段 1 张
- 2K + 16:9 + cream paper 背景

### Step 3 · 拼 PPTX（15 min）
- 调 `python-pptx` 库
- 模板：左 50% 图 + 右 50% 6 块文字
- 8 页 = 8 段 P0-P7
- 输出：21 MB .pptx（PowerPoint 可编辑）

## 跨工具引用

| 步骤 | 工具 | 路径 |
|---|---|---|
| Step 1 拉数据 | daily-market-review skill | `~/.minimax/agents/mavis/skills/daily-market-review/` |
| Step 2 出图 | image_synthesize（matrix MCP）| 工具调用 |
| Step 3 拼 PPTX | python-pptx 库 | `pip install python-pptx Pillow` |

## 反 AI 味 7 问自检

1. 标题加粗 22pt？✓
2. 核心主张 1 句话（≤ 30 字）？✓
3. 认知锚点 ≤ 20 字？✓
4. 5 关键要点 = 加粗 + 普通混合？✓
5. 数据/数字单独 1 行？✓
6. 金句加粗居底？✓
7. 16:9 + 2K + 顶部 30% 留标题？✓

**判定**：7/7 = 杂志风 PPTX · 5-6 = 微调 · < 5 = 重做

## 复用步骤

1. **复制本 case** 的 P0-P7 8 段骨架
2. **调 daily-market-review** 拉当日 4 维数据
3. **填入 8 段内容**（核心主张/认知锚点/5 要点/数据/金句）
4. **image_synthesize** 出 8 张图（macaron 5 色）
5. **python-pptx 拼 8 页**（左图右文）
6. **跑 7 问自检**（1 分钟）
7. **输出**：`4维融合诊断-YYYY-MM-DD.pptx`

## 实战案例

- **2026-07-13**：全市场崩盘 5/5 信号 · 21 MB · 8 页
- 路径：原 PPTX `~/Desktop/A股复盘-2026-07-13-深度版.pptx`

## 来源

- Mavis 端：daily-market-review skill（L0-L3 4 维融合框架）
- 公共方法论：pretty-skills/内容创作/杂志风公众号品鉴/（16 条铁律）
- pretty-skill v3.23 范式
