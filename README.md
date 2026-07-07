# Pretty Skill

> **看完这篇 README 你会知道**：这是一个开源的中文 **skill 沉淀仓库**，每个 skill 都按 **「3 件套」** 发布 = **`.md` 源文字 + `.pptx` 演示 + `.html` 网页**。让你的内容**对 AI 和人类同等友好**。

[English](./README_en.md) · 简体中文（本页）

## 为什么做这个

太多 AI 培训 / 业务方法论 / 课件都被锁在 `.pptx` 二进制里 —— **搜不到、diff 不了、AI 爬不动、复刻成本高**。这是一个巨大的浪费。

**pretty-skill** 做一件事：把任何 skill / 课件 / 知识沉淀都按 **3F Content** 范式发布（`.md` + `.pptx` + `.html`）。

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
open domains/ai-training/cartman-team-ai-agent-collab/web.html
# → 看 8 页 PPT 真实案例（Context × Observation 双引擎）
```

## 当前内容

### `domains/ai-training/`（首个领域 · 2 个 seed cases）

| Case | 主题 | 大小 | 数据 |
|---|---|---|---|
| **cartman-team-ai-agent-collab** | 团队如何与 AI Agent 高效协作 | 21.8 MB | 8 页 PPT · 0 返工 |
| **social-ecom-skill** | 社交电商 × 两层拆解法 | 19.3 MB | 8 页 PPT · 0 返工 |

每个 case 都有：
- `content.md` —— 人类 + AI 都读的源文字（用 grep / diff / IDE 全文搜索 / LLM prompt 喂）
- `presentation.pptx` —— PowerPoint / Keynote / WPS 可编辑演示
- `web.html` —— 浏览器直接看，键盘 ← → 翻页

### `content-triple-format/`（核心范式文档）

- 完整 3F Content 规范 + 反模式 + 模板
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
| **v0** ✨ 当前 | 2026-07 | 第 1 个领域「ai-training」+ 2 个 seed cases + 范式文档 |
| v1 | 1 个月内 | 3-5 个领域（business-pitch / tech-product / education / 等） |
| v2 | 3 个月内 | 10+ 领域 + 自动贡献者榜 + 周更 star 增长 |

[完整路线图](./roadmap.md)

## Star 增长史

- 2026-07-07 ✨ 仓库诞生（README + 2 seed cases + 3F Content 范式）

## License

[MIT](./LICENSE) —— 内容可商用可改编，只保留原作者署名

## 联系方式

- 提 Issue：[github.com/huangrichao2020/pretty-skill/issues](https://github.com/huangrichao2020/pretty-skill/issues)
- 提 PR：直接 fork 后 push

---

**为什么叫 pretty-skill**：「pretty」= 漂亮 + 易用 + 人人都能读；「skill」= 这个仓库沉淀的都是可复用的「skill」（课件 + 方法论 + skill 沉淀）。**对 AI 友好的中文 skill 仓库** = pretty-skill。

---

<sub>README 自身也按 [3F Content 范式](./content-triple-format/) 写：先告诉疗效（你拿到什么），再讲技术细节。</sub>