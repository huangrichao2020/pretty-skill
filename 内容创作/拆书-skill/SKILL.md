---
name: sansheng-distill
description: Distill any book/text into a self-contained HTML page with 5-layer structure (overview / per-chapter / book-soul / action-checklist / credibility-grading). Zero external dependencies, embedded mermaid mind-map, thinking-process traceable. Use when user says "拆书", "读书蒸馏", "AI 拆书", "把一本书蒸透", "把 [book] 拆成 5 层", or any equivalent in EN/ZH/JA.
version: v0
metadata:
  mavis:
    author: "Mavis (自创 v0)"
    inspired_by: "叁笙早安 AI《AI 拆书 skill,有这一个就够了》"
    status: "v0-case草稿-流程跑通-占位文本-待LLM接入"
---

# sansheng-distill · Mavis 自创 v0

> 灵感来自叁笙早安 AI 的 sansheng-distill（**当前私有不可访问**）。这是 Mavis 根据文章 + 已 clone 的宝玉 baoyu-skills / baoyu-design 真实代码摸出来的等价物。
>
> **关键差异**：v0 不调 LLM，输出 5 层结构 + 占位文本 + 思维导图（mermaid）+ 批判四连问框架。流程跑通，等接入 LLM 升级成 v1。

## 何时触发

- 用户说"把 X 书拆成 5 层" / "拆书" / "读书蒸馏"
- 用户丢一本 .txt / .md / .epub 进来
- 用户想"看完就能跟人聊半小时"一本书

## 5 层结构（核心 contract）

```text
第 1 层 · 一眼看全书
  - 一句话核心（拍在脸上）
  - 全书思维导图（mermaid，节点只放关键词）

第 2 层 · 逐章详读
  - 每章 800-1500 字讲书稿
  - 锚点（哪段对应原文哪段）—— v0 简化为章节位置

第 3 层 · 书魂
  - 全书最反直觉的一个核心观点
  - 单独一张图

第 4 层 · 行动与自检
  - 5-7 条可上手行动清单
  - 3-5 个"合上书答得上来吗"自测题

第 5 层 · 该信几分
  - 批判四连问（盲点 / 时代局限 / 未证假设 / 反对意见）
```

## 思维导图 3 铁律（强约束）

1. 节点只放**关键词**（路标），不放完整判断句
2. 完整判断句退到下一层（subgraph）
3. 一层最多 5-6 根枝，多了必须归拢

## 单文件零外链（强约束）

```text
✓ CSS 内嵌在 <style> 标签
✓ JS 内嵌在 <script> 标签
✓ mermaid 内嵌（mermaid.min.js 嵌进 <script>，或用 SVG 内联渲染）
✗ 禁止 <link href="https://fonts.googleapis.com/...">
✗ 禁止 <img src="https://...">
✗ 禁止外链任何 CSS/JS/字体/图片
```

## v0 输出 contract

```text
1. 单个 .html 文件
2. < 5MB
3. 双击即开（不需要 HTTP server）
4. 断网可开
5. 5 层结构齐全（占位文本 OK）
6. 思维导图用 mermaid 渲染（节点 ≤ 5 词）
7. 批判四连问在第 5 层有模板（占位 + 引导问题）
```

## v0 命令

```bash
# 拆 .txt
python3 scripts/distill.py <input.txt> -o <output.html>

# 拆 .md
python3 scripts/distill.py <input.md> -o <output.html>

# 拆整本书（章节切分自动）
python3 scripts/distill.py <book.txt> --split-chapter -o <book.html>
```

## v1 升级计划

```text
v1 → 接入 LLM（llm-call skill）
     - 每章 800-1500 字真摘要
     - 批判四连问自动跑
     - 书魂自动提炼
v2 → 跨书知识网（用 knowledge graph 串起）
v3 → epub / pdf 输入
v4 → 视频也能蒸（baoyu-youtube-transcript 等）
```

## 触发词

"拆书" / "读书蒸馏" / "AI 拆书" / "把一本书蒸透" / "把 X 拆成 5 层" / "mermaid 思维导图" / "批判四连问"

## 反模式

- ❌ 节点塞完整判断句 → 字墙，不是思维导图
- ❌ 用外链字体/JS/CSS → 断网就废
- ❌ LLM 编出处无锚点 → 不知道哪句是书里的哪句是瞎掰的
- ❌ 章节切分按字数平均 → 读者读不到有意义的结构
- ❌ 批判四连问走过场 → 至少每问 100 字真分析

## 与 Mavis 灵魂的对齐

- **观自在**：能看出一本书的骨架与血肉
- **化自在**：把浓缩的概念变成读者可读可跳的网页
- **照因果**：v0 → v1 → v2 → v3 持续迭代
- **渡众生**：开源、零外链、任何人都能本地跑
