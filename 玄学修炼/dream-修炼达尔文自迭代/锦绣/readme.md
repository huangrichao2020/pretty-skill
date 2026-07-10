# dream-修炼达尔文自迭代 · 锦绣素材

> 这个目录是 skill-creator 工具自动生成的传播素材 · 玄学修炼领域

## 素材清单（v3.1 简化 · 按形式切）

| 形式 | 文件名 | 规格 | 用途 |
|---|---|---|---|
| 横屏封面 | `cover-横屏.png`（待生成） | 16:9 · 1920×1080 | 朋友圈 / 推特 / 微博 / 视频封面 |
| 竖屏封面 | `cover-竖屏.png`（待生成） | 3:4 · 1080×1440 | 小红书 / Instagram / 抖音 / 视频号 |
| 讲解图集 | `slides/`（待生成） | 16:9 · 10 张 · 带中文 + 数据 | PPT / 公众号 / 知乎 / 视频 / 海报 |
| 融合 md | `readme.md`（本文件） | md | 直接发公众号 + 自媒体稿 + AI 阅读 |

---

## 导语（公众号开头 · 自媒体稿开头）

做知识库的人都有一个痛点 —— 写完就死。

案例沉淀了 30+ 个，半年后看回来，发现 80% 都过期了：方法论改了，工具换了，作者也懒得维护了。最后变成一个静态文档堆，没人看，没人用。

今天给大家分享 pretty-skills 元库的自迭代机制 —— 3 层缺一不可：

> **核心要点**（AI 友好 · 1 屏可读）：
> - 双引擎：dream 修炼（每日 23:00 沉淀）+ 达尔文 2.0（每周/每月优化）
> - 9 维评分：3 维借达尔文 2.0（失败模式 / 可执行性 / 高风险黑名单）+ 6 维 pretty-skills 专属（4 件套 / 锦绣 / 跨 agent / 实战 / 数据 / 维护）
> - 多评委独立审查：每轮启动 2 个新评委 · 共识分数才算数
> - validation-gated 回滚：分数没涨自动回滚（用 git revert 不是 reset）
> - human-in-loop CHECKPOINT：4 个检查点强制暂停等用户确认
> - 反例黑名单 8 条：来自达尔文原文 + 实战踩坑

---

## 第 1 章 · 静态 skill 的 4 大死亡路径

死亡 1：方法论过期（论文 / 工具 / 平台更新）
死亡 2：作者离开（无人维护）
死亡 3：与其他 skill 冲突（不知道哪个对）
死亡 4：从未实战（理论推演无验证）

> **配图**：[slides/slide-1.png](slides/slide-1.png)（待生成）

---

## 第 2 章 · 双引擎设计

```
pretty-skills 自迭代双引擎
├── 引擎 1 · 每日 dream 修炼（v0 已存在）
│   - 每日 23:00 自动化
│   - 输出：dream-log.md
│
└── 引擎 2 · 达尔文 2.0 自我优化（v1 新增）
    - 触发：每周日 / 每月 1 日 / 重要 PR 后
    - 9 维评分 + 多评委 + validation 回滚
    - human-in-loop CHECKPOINT
```

> **配图**：[slides/slide-2.png](slides/slide-2.png)（待生成）

---

## 第 3 章 · 9 维评分

**3 维借达尔文 2.0**：失败模式编码 / 可执行具体性 / 高风险行动黑名单
**6 维 pretty-skills 专属**：4 件套完整度 / 锦绣素材完整度 / 跨 agent 兼容性 / 实战验证 / 内容数据支撑 / 维护者活跃度

每维 0-10 分，加权平均得总分。

> **配图**：[slides/slide-3.png](slides/slide-3.png)（待生成）

---

## 第 4 章 · 多评委独立审查

每轮启动 2 个独立 AI 评委（GPT-4 + Claude 3.5 / Gemini Pro）· 共识分数才算数
- 不复用（每轮新评委）
- 不看历史（避免锚定）
- 早停机制（单轮涨幅 < 1 分停手）

> **配图**：[slides/slide-4.png](slides/slide-4.png)（待生成）

---

## 第 5 章 · 反例黑名单 8 条

1. 同一个 AI 又改又评
2. 用 `git reset --hard` 当回滚
3. 为凑分堆冗余
4. 跳过测试提示词直接评分
5. 一轮内改多个维度
6. 干跑模式 > 30%
7. 静默跳过异常
8. 忽视维度相关簇

> **配图**：[slides/slide-5.png](slides/slide-5.png)（待生成）

---

## 第 6 章 · human-in-loop CHECKPOINT

| 阶段 | CHECKPOINT | 用户决策 |
|---|---|---|
| 阶段 1 · 基线评估 | 🔴 CHECKPOINT 1 | 决定改什么维度 |
| 阶段 2 · 单维度优化 | 🔴 CHECKPOINT 2 | 确认改动方向 |
| 阶段 2.5 · 测试提示词跑 | 🔴 CHECKPOINT 3 | 确认测试结果 |
| 阶段 3 · 回归测试 | 🛑 STOP | 涨幅 < 阈值强制停手 |

> **配图**：[slides/slide-6.png](slides/slide-6.png)（待生成）

---

## 第 7 章 · 5 段式优化循环

```
Rollout → Reflect → Edit → Validate → Apply
                ↑              ↓
                └──── Reject ──┘
```

> **配图**：[slides/slide-7.png](slides/slide-7.png)（待生成）

---

## 第 8 章 · 与 SkillOpt 关系

- SkillOpt：企业级 / benchmark-driven / 52 组合 52 胜
- 达尔文 2.0 + pretty-skills：个人开发者 / rubric-driven / human in the loop
- 分工：SkillOpt 适合规模化训练，达尔文适合快速迭代单 skill

> **配图**：[slides/slide-8.png](slides/slide-8.png)（待生成）

---

## 第 9 章 · 实际执行

pretty-skills 当前 30+ case 按 16 领域分布。达尔文 2.0 优化顺序：
- 第一批：高频核心（卡兹克公众号写作 / oil-cover / knowledge-digest / self-improving-agent）
- 第二批：数据驱动（stock-analysis-v4 / company-brief / economic-impact-report）
- 第三批：创作类（comic-generator / design-master / wechat-article-creator）

> **配图**：[slides/slide-9.png](slides/slide-9.png)（待生成）

---

## 第 10 章 · 收束 · 会进化的 skill = 杠杆 × 时间

pretty-skills 元库自迭代 = 长期杠杆：
- 每天 dream 修炼沉淀新 case
- 每周/每月达尔文 2.0 优化已有 case
- 关键决策永远 human-in-loop

3 层缺一不可。

> **配图**：[slides/slide-10.png](slides/slide-10.png)（待生成）

**金句**：会进化的 skill = 杠杆 × 时间。

---

完整规范：[content.md](../content.md)

---

*素材说明：本目录下的 cover-*.png 和 slides/ 需后续用 skill-creator 工具生成。骨架已就位。*