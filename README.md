# Pretty Skill

> **看完这篇 README 你会知道**：这是一个开源的中文 **skill 沉淀仓库**，每个 skill 都按 **「3 件套」** 发布 = **`.md` 源文字 + `.pptx` 演示 + `.html` 网页**。让你的内容**对 AI 和人类同等友好**。

[English](./README_en.md) · 简体中文（本页）

## 为什么做这个

太多 AI 培训 / 业务方法论 / 课件都被锁在 `.pptx` 二进制里 —— **搜不到、diff 不了、AI 爬不动、复刻成本高**。这是一个巨大的浪费。

**pretty-skill** 做一件事：把任何 skill / 课件 / 知识沉淀都按 **3F Content** 范式发布（`.md` + `.pptx` + `.html`）。

### 为什么 3F 不能偷懒（文字直转 PPT）

`.md` + `.pptx` + `.html` 不是「任选其一」的格式，是**必须严格按 3F 流程**：

```
content.md（数据）  →  prompt × N  →  matrix AI 出图  →  图嵌入 .pptx + .html（视觉）
```

❌ **直接拿 `.md` 文字转 `.pptx`** → 文字 PPT（丑、缺图、信息密度低）。已经有人试过这种偷懒，**拒绝接受**。

✅ **正确路径** —— 完整流程：[content-triple-format/README.md](./content-triple-format/README.md)

📊 **正反面对照**（文字 PPT vs 图 PPT 直观对比）：[before-after-example.md](./content-triple-format/before-after-example.md)

🤖 **自动校验脚本**（推荐 · 提交 PR 前必跑）：

```bash
python3 content-triple-format/check-3f.py <你的 case 目录>
# 退出码 0 = 通过；1 = PR 会被自动退回
```

## 你拿到什么

| 加 3F 之前 | 加 3F 之后 |
|---|---|
| GitHub diff 看不懂 .pptx 内嵌文字（zip） | ✅ 逐字 diff，文案改动可追溯 |
| AI agent 没法吃你的 PPT（图 OCR 慢且不准） | ✅ `.md` 直接当 prompt 喂 LLM / 总结 / 翻译 / 二创 |
| 屏幕阅读器 / 搜索引擎爬不动 .pptx | ✅ `.md` 全可读、可索引、可引用 |
| 别人想 fork 你的 PPT 只能下载反推文案 | ✅ 拿 `.md` 就能复刻成图，省 80% 工时 |
| 自媒体文章需重新拆 PPT 重写 | ✅ `.md` 直接做推文 / 视频脚本 / Newsletter |
| 只有你自己能消费这些 PPT | ✅ 任何未来 AI 工具都能消化整个仓库 |

## 1 分钟上手

```bash
git clone https://github.com/huangrichao2020/pretty-skill
cd pretty-skill
open AI培训/cartman-team-ai-agent-collab/web.html
# → 看 8 页 PPT 真实案例（Context × Observation 双引擎）
```

## 当前内容

### `AI培训/`（领域 1 · 2 个 cases）

| Case | 主题 | 大小 | 数据 |
|---|---|---|---|
| **cartman-team-ai-agent-collab** | 团队如何与 AI Agent 高效协作 | 21.8 MB | 8 页 PPT · 0 返工 |
| **social-ecom-skill** | 社交电商 × 两层拆解法 | 19.3 MB | 8 页 PPT · 0 返工 |

### `金融分析/`（领域 2 · 1 个 case）

| Case | 主题 | 大小 | 贡献者 | 数据 |
|---|---|---|---|---|
| **chokepoint-mainboard** | A 股卡脖子选股报告 · 主板专版 | ~28 MB | @Kun 🎉 第 1 个真 case | 9 页 PPT · 深色科技风 · 真实 A 股数据 |

每个 case 都有：
- `content.md` —— 人类 + AI 都读的源文字（用 grep / diff / IDE 全文搜索 / LLM prompt 喂）
- `presentation.pptx` —— PowerPoint / Keynote / WPS 可编辑演示（含图）
- `web.html` —— 浏览器直接看，键盘 ← → 翻页（含图）
- `images/` —— AI 出图原图（≥ 1 张 / 页）
- `prompts/` —— 每页 prompt 文件（工程可复现）
- `build_pptx.py` —— 模板化 PPTX 生成脚本

### `content-triple-format/`（核心范式文档）

- 完整 3F Content 规范 + 反模式 + 模板
- **`check-3f.py` 自动校验脚本**（PR 提交前必跑）
- **`deep-themes.md` 视觉风格预设**（手绘马卡龙 + 深色科技风）
- 是这个仓库的核心约定，所有贡献者必读

## 如何贡献

1. **Fork 这个仓库**
2. **新建 case**（参考 `domains/_template/case/` 模板）
3. **3 件套齐全**：`.md` + `.pptx` + `.html`
4. **提 PR** —— 自动加入贡献者榜 [CONTRIBUTORS.md](./CONTRIBUTORS.md)

详细流程：[CONTRIBUTING.md](./CONTRIBUTING.md)

## 路线图

| 版本 | 时间 | 目标 |
|---|---|---|
| **v0** ✨ 已完成 | 2026-07-07 | 第 1 个领域「ai-training」+ 2 个 seed cases + 范式文档 |
| **v1** ✨ 当前 | 2026-07-08 | 第 1 个真 case `chokepoint-mainboard`（@Kun）+ check-3f.py 自动校验 + GitHub Actions + PR 模板 + STRUCTURE 决策 |
| v2 | 1 个月内 | 3-5 个领域（business-pitch / tech-product / education / 等） |
| v3 | 3 个月内 | 10+ 领域 + 自动贡献者榜 + 周更 star 增长 |

[完整路线图](./roadmap.md)

## Star 增长史

- 2026-07-07 ✨ 仓库诞生（README + 2 seed cases + 3F Content 范式）
- 2026-07-08 🎉 **PR #1 合并** · 第 1 个真 case `chokepoint-mainboard`（@Kun）· v1 多领域扩展启动
- 2026-07-08 ✅ 范式升级 4 重防御（SKILL.md 硬约束 + CONTRIBUTING 拒绝标准 + before-after 直观对照 + onboarding 5 步流程）
- 2026-07-08 ✅ check-3f.py 自动校验脚本 + GitHub Actions 集成
- 2026-07-08 ✅ STRUCTURE.md 决策文档（cases/ vs domains/ 路径约定）

## License

[MIT](./LICENSE) —— 内容可商用可改编，只保留原作者署名

## 联系方式

- 提 Issue：[github.com/huangrichao2020/pretty-skill/issues](https://github.com/huangrichao2020/pretty-skill/issues)
- 提 PR：直接 fork 后 push

---

**为什么叫 pretty-skill**：「pretty」= 漂亮 + 易用 + 人人都能读；「skill」= 这个仓库沉淀的都是可复用的「skill」（课件 + 方法论 + skill 沉淀）。**对 AI 友好的中文 skill 仓库** = pretty-skill。

---

<sub>README 自身也按 [3F Content 范式](./content-triple-format/) 写：先告诉疗效（你拿到什么），再讲技术细节。</sub>