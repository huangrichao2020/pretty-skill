# cinema-dna-21x9x3 电影感三联 · case

> **沉淀时间**：2026-07-22
> **来源**：[dacnay816y62-hub/cinema-dna-21x9x3](https://github.com/dacnay816y62-hub/cinema-dna-21x9x3) · 39 stars · 2026-07-20
> **方法论作者**：梵想美学（小红书）· 拆 300 个电影镜头提炼
> **沉淀者**：Mavis（按 pretty-skills 完整 case 流程 · 2026-07-22）
> **类型**：重度学习 · 完整 3F Content + 锦绣 + cinema-dna 完整方法论

## 这是什么

cinema-dna-21x9x3 = **3 镜头叙事合同**的电影感 AI 提示词设计 skill。**不是堆提示词，是先判断镜头为什么成立**（镜头/光线/空间/叙事 4 维）→ 才生成 3 张 21:9 横向 triptych 图。

**核心心法**：
- 3 镜头功能差异：建立世界（24-28mm）→ 建立关系（32-50mm）→ 留下余韵（50-85mm）
- 现场摄影语言 5+ 参数（焦段/机位/距离/比例/遮挡/光源/焦点/视线/信息位置）
- Anti-AI 电影画面纪律（禁用 rich detail / epic / masterpiece 等 8 词）
- 光学缺陷 + 受控 dirt（每张选 1 胶片介质 + 1 dirt 家族）
- Triptych 节奏（1.25:0.9:0.85 强调首镜头，黑色 8px 间隔作剪辑呼吸）

## 文件结构

```
cinema-dna-21x9x3电影感三联/
├── README.md                  # 本文件
├── SKILL.md                   # 触发词 + 一句话定位
├── content.md                 # 9 段深度方法论（5字段/段）
├── cinema-dna-21x9x3电影感三联讲解.pdf  # PDF 讲解版
├── images/                    # 15 张 cinema-dna example + 1 张 triptych 示范
│   ├── *.jpg / *.png          # cinema-dna 自带 15 张 example
│   └── triptych-demo.jpg      # 1 张实际 triptych 拼接示范（3 张按 1.25:0.9:0.85 + 8px 黑色间隔）
├── prompts/                   # 9 段出图 prompt
│   ├── README.md
│   └── p0_cover.md ~ p8.md
├── 锦绣/                      # 多平台素材
│   ├── cover-横屏.png
│   ├── cover-竖屏.png
│   ├── slides/                # 3 张 triptych example（hotel-pink + venice + journey-west）
│   └── readme.md              # 融合 md（公众号 + 自媒体稿 + AI 阅读）
└── manifest.json
```

## 核心心法（9 段详见 content.md）

| 段 | 主题 |
|---|---|
| P0 | 封面 · 4 个判断（镜头/光线/空间/叙事）|
| P1 | 3 镜头叙事合同（建立世界/建立关系/留下余韵）|
| P2 | 现场摄影语言 5+ 参数（10 摄影参数全栈）|
| P3 | Anti-AI 电影画面纪律（禁用 8 词 + 故事线索上限）|
| P4 | 光学缺陷 + 受控 dirt（7 胶片 + 7 dirt）|
| P5 | Triptych 节奏（5 比例分配）|
| P6 | 导演风格转译（学"为什么"不学"滤镜"）|
| P7 | Mavis 工具栈适配（matrix_generate_image × 3 + PIL）|
| P8 | 工具对比（vs 普通配图 / scroll-world / dashiai-ppt / 公众号 7 段）|

## 实战示例

**3 张 triptych 示范**（images/triptych-demo.jpg）：

| 镜头 | 主题 | 焦段 | 功能 |
|---|---|---|---|
| Shot 1 (1.25x) | hotel-pink-ritual | 24-28mm | 建立世界：环境 > 人物 |
| Shot 2 (0.9x) | venice-palace | 32-50mm | 建立关系：人物 20-35% |
| Shot 3 (0.85x) | green-water-memory | 50-85mm | 留下余韵：背影/空/未完成 |

**PIL 拼接代码**（prompts/p8.md 完整版）：

```python
# Triptych 比例 1.25:0.9:0.85 + 8px 黑色间隔
gap = 8
total_w = w1 + w2 + w3 + gap * 2
canvas = Image.new("RGB", (total_w, target_h), (0, 0, 0))
x = 0
canvas.paste(img1, (x, 0))
x += w1 + gap
canvas.paste(img2, (x, 0))
x += w2 + gap
canvas.paste(img3, (x, 0))
```

## 适用场景

- 公众号配图（3 张电影感三联，21:9 横向 + 黑色间隔）
- 小红书封面（高 3 张或横 3 张）
- 视频号封面（视频开始前后的关键帧）
- 报告插图（高级感主题转译）
- 产品发布 / 旅行记录 / 人物故事 / 空间转译

## 用户拿到后

- 拿到任何主题 → **30 min 出 3 张电影感三联图**（不用 AI 套词）
- 3 镜头功能差异 + 至少 4 维变化 → 不再 3 张同 wide shot
- 镜头为什么成立（5+ 摄影参数）→ 不用 "电影感滤镜"
- Triptych 节奏（1.25:0.9:0.85）→ 黑色 8px 间隔 = 剪辑呼吸
- 整体：1 个主题 → 3 张高级感图（不是 1 张 AI 精修大图）

## 沉淀版本

v1.0 · 2026-07-22

## 引用

- pretty-skills：[huangrichao2020/pretty-skills](https://github.com/huangrichao2020/pretty-skills)
- 原项目：[dacnay816y62-hub/cinema-dna-21x9x3](https://github.com/dacnay816y62-hub/cinema-dna-21x9x3)
- 小红书：codex 电影感 skill
