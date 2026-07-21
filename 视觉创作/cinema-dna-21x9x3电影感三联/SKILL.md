---
name: cinema-dna-21x9x3电影感三联
description: |
  电影感不是滤镜，是 4 个判断先成立（镜头/光线/空间/叙事）。
  cinema-dna-21x9x3 = 3 镜头叙事合同（建立世界/建立关系/留下余韵）+ 现场摄影语言 5+ 参数 + Anti-AI 电影画面纪律 + 光学缺陷 + Triptych 节奏。
  拆 300 个电影镜头提炼的纯 prompt 设计 skill，matrix_generate_image × 3 + PIL 拼接直接落地。
  适用：公众号配图 / 小红书封面 / 视频号封面 / 报告插图 / 任何"高级感"主题。
  不适用：纯科普 / 数据展示 / 长文（用其他方法）。
triggers:
  - 电影感
  - 21:9
  - 三联镜头
  - triptych
  - 高级感
  - 镜头语言
  - 电影感 AI 提示词
  - cinema-dna
  - 拍出电影感
  - 镜头为什么成立
---

# cinema-dna-21x9x3 电影感三联

## 一句话定位

**电影感 = 镜头/光线/空间/叙事 4 个判断先成立**，不堆提示词。3 张 21:9 横向 triptych 叙事图（建立世界/建立关系/留下余韵）+ 现场摄影 5+ 参数 + Anti-AI 纪律 + 光学缺陷。matrix_generate_image × 3 + PIL 拼接即可落地。

## 5 步核心工作流

| 步 | 动作 | 关键 |
|---|---|---|
| 1 | 任务分析 | 主题 / 类型 / 受众 / 3 镜头角色分配 |
| 2 | 镜头方案 | Shot 1 建立世界（24-28mm）→ Shot 2 建立关系（32-50mm）→ Shot 3 留下余韵（50-85mm） |
| 3 | 光线 + 色彩脚本 | 选胶片介质（35mm/16mm/VHS/MiniDV 等 7 选 1）+ 光源 + 色彩身体 |
| 4 | 空间组织 | 5+ 摄影参数（焦段/机位/距离/比例/遮挡/空间轴/光源/焦点/视线/信息位置）|
| 5 | 输出完整 prompt + matrix_generate_image × 3 + PIL 拼接 | Triptych 比例 1.25:0.9:0.85（强调首镜头）+ 8px 黑色间隔 |

## 与同类方法对比

| 维度 | 普通 AI 配图 | cinema-dna | scroll-world | dashiai-ppt |
|---|---|---|---|---|
| 输出形式 | 1 张竖图 + AI 套词 | 3 张 21:9 横向叙事 | 2N-1 段视频 | 22 幕讲解 |
| 核心 | "电影感滤镜" | 镜头成立的原因 | seam frame-identical | 横屏适配 |
| 工具 | matrix_generate_image | matrix_generate_image × 3 + PIL | matrix_gen_videos + ffmpeg | matrix_generate_image + PIL |
| 适用 | 配图随手出 | 高级感主题 | 品牌沉浸 landing | 演讲/汇报 |
| 不适用 | 高品质场景 | 纯科普/数据/长文 | 静态图 | 视频/动画 |

## 详细文档

- `content.md` · 9 段深度方法论（建立世界/建立关系/留下余韵/现场摄影/Anti-AI/光学缺陷/Triptych 节奏/导演转译/Mavis 适配/工具对比）
- `images/` · 15 张 cinema-dna 自带 example + 1 张 triptych 示范
- `prompts/` · 9 段出图 prompt（含 triptych 拼接示意）
- `cinema-dna-21x9x3电影感三联讲解.pdf` · PDF 讲解版
- `锦绣/` · 3 张 triptych example + cover + 融合 md

## 关键参考

- 原项目：[dacnay816y62-hub/cinema-dna-21x9x3](https://github.com/dacnay816y62-hub/cinema-dna-21x9x3) · 39 stars
- SKILL.md 771 行（含 v3/v4 全部硬规则 + 14 张 example + 2 份 references）
- 14 张 triptych example（hotel-pink-ritual / venice-palace / journey-west / 等）

## 沉淀版本

v1.0 · 2026-07-22
