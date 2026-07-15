# sansheng-distill · Mavis 自创 v0

> **一句话定位**：丢一本电子书进去,吐出一张能点能跳的 HTML 单页,5 层结构 + 思维导图 3 铁律 + 单文件零外链。

---

## 这个 case 是什么

**页数**：5 页 · **领域**：Agent 知识（拆书工具）
**原版作者**：叁笙早安 AI（`github.com/sandypoli-boop/sansheng-distill`，**当前私有无法访问**）
**Mavis 自创 v0**：基于文章 + 已 clone 的 2 个真实 skill 摸出来的等价物
**状态**：v0 · 流程跑通 · 占位文本 · 待接入 LLM

## v0 与原版的差异

| 维度 | 原版 | Mavis v0 |
|---|---|---|
| LLM 接入 | Fable 5 / Anthropic 旗舰 | ❌ 占位文本（标"待 LLM 接入"）|
| 5 层内容质量 | 真人级摘要 | 流程骨架 + 占位 |
| 思维导图 | AI 一笔一笔画 | mermaid 内嵌（合规 3 铁律）|
| 跨书知识网 | 蒸过的书互相印证 | ❌ v0 跳过（v1+）|
| 锚点（出处可翻）| 完整 | v0 简单标注章节位置 |
| 输入格式 | epub / pdf / txt | .txt / .md（v0）|
| 输出 | 自包含 HTML + 字体/JS | 自包含 HTML + mermaid CDN-free |

> 标"非叁笙早安 AI 原版 · Mavis 摸出来的等价物"——区别清楚，等用户哪天能 clone 原版，再按真实代码升级。

## 核心论点

AI 拆书最大的毛病是**编**——一本正经地总结,你不知道哪句是书里的、哪句是它瞎掰的。Mavis v0 解法 = **单文件 HTML + 5 层结构 + 思维导图 3 铁律 + 占位锚点**。

## 5 层结构（5 页内容）

1. **一眼看全书**：一句话拍脸 + 能展开的全书思维导图
2. **逐章详读**：每章 800-1500 字讲书稿（v0 占位）
3. **书魂**：全书最反直觉的核心观点单拎一张图
4. **行动与自检**：可上手行动清单 + "合上书答得上来吗"自测题
5. **该信几分**：作者盲点 / 时代局限 / 未证假设 / 反对意见（**批判四连问**）

## 思维导图 3 铁律

1. 节点只放**关键词**（路标），不放完整判断句
2. 完整判断句退到下一层，想看再点开
3. 一层最多几根枝，多了必须归拢

> 反例：节点塞 51 个字 = "字墙"，不是思维导图

## 硬规则（继承自原版）

- **单文件、零外链、断网可开**
- **HTML < 5MB**（微信/邮件发得出去）
- 产出前用 **批判四连问** 自查"该信几分"
- 锁死版式，AI 只准填内容不准自由发挥

## v0 实操（已跑通）

### 跑通示例

```bash
# 输入: samples/alice-ch1-5.txt (Project Gutenberg 的 Alice in Wonderland 截 5 章)
# 输出: samples/alice-ch1-5.html (单文件, 5 层结构, 内嵌 mermaid 思维导图)
python3 scripts/distill.py samples/alice-ch1-5.txt -o samples/alice-ch1-5.html
```

打开 `samples/alice-ch1-5.html` → 断网也能看 → 双击即用。

### v0 章节切分规则

```text
中文: 第[一二三四五六七八九十百零0-9]+章 / 第[一二三四五六七八九十百零0-9]+节
英文: Chapter X / CHAPTER X / Section X
fallback: 整个文件 = 1 章
```

## 升级路线

```text
v0  (现在)    → 流程跑通 + 占位文本 + 1 个 sample
v1  (下一步)  → 接入 LLM（llm-call skill）+ 真摘要
v2  (远期)    → 跨书知识网 + 锚点(可翻回原文) + 视频也能蒸
v3  (终)      → 实战 3-6 个月后升级 knowhub methodology
```

## 12 家前人绝活（待 v1+ 逐家实现）

| # | 来源 | 状态 |
|---|---|---|
| 1 | 李继刚 xray 拆书 → 三轮认知压缩 | ✅ 已沉 Mavis memory |
| 2 | crayon-ai book-to-webpage | ⏸ v1+ 调研 |
| 3 | 花叔女娲 → 心智模型/决策规则/内在张力 | ⏸ v2+ |
| 4 | 仓颉 → **批判四连问** | ✅ v0 模板已实现 |
| 5 | ebook-to-mindmap → 大部头分组蒸馏 | ⏸ v1+ |
| 6 | deep-reading-coach → 入书诊断 | ⏸ v2+ |
| 7 | reading-pipeline → 质检门 | ⏸ v1+ |
| 8 | wikigraph → 档案为主、网页为投影 | ⏸ v2+ |
| 9 | ai-refinery → 体积纪律 | ✅ v0 HTML < 5MB 约束 |
| 10 | 归藏 → 锁死版式 | ✅ v0 mermaid + CSS 锁死 |
| 11 | Anthropic frontend-design → 两遍设计工序 | ⏸ v1+ 自查 |
| 12 | 宝玉 baoyu-design → 中文排版 + AI 审美黑名单 | ⏸ v1+ |

## 谦逊有立场的收尾

> "v0 跑通流程 · 占位文本 · 待 LLM 接入 · 等你哪天能 clone 原版再升级"——
> 那个"v0"，是我留给自己持续完善的余地；
> 那个"待你 clone 原版"，是我留给叁笙早安 AI 原版的位置。

## 触发词

"拆书" / "读书蒸馏" / "AI拆书" / "sansheng" / "叁笙早安AI" / "知识蒸馏" / "把一本书蒸透" / "5 层结构" / "思维导图 3 铁律"

---

## 关联沉淀

- Mavis agent memory：`distillation-review.md`（三轮认知压缩 / 批判四连问 / 单文件零外链 / 谦逊收尾 · 已沉）
- pretty-skills/内容创作/baoyu-skills：宝玉的 21 个内容创作 sub-skill
- pretty-skills/视觉创作/baoyu-design：宝玉的设计 skill（harness-agnostic + 33 built-in-skill）
