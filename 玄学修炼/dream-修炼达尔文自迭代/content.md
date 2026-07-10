# dream-修炼达尔文自迭代 · pretty-skills 元库自迭代机制

> [3F Content 范式](../../content-triple-format/) · F1 源文字版

---

## P0 · 封面

- **核心主张**：pretty-skills 30+ case 不能"写完就死"——必须会自我进化
- **双引擎**：dream 修炼（每日 23:00）+ 达尔文 2.0（每周/每月）
- **疗效**：每个 case 持续保持高质量 + 与新论文/新方法同步
- **金句**：会进化的 skill = 杠杆 × 时间

---

## P1 · 痛点 · 静态 skill 的 4 大死亡路径

- 死亡 1：方法论过期（论文 / 工具 / 平台更新）
- 死亡 2：作者离开（无人维护）
- 死亡 3：与其他 skill 冲突（不知道哪个对）
- 死亡 4：从未实战（理论推演无验证）

---

## P2 · 双引擎设计（核心）

```
pretty-skills 自迭代双引擎
├── 引擎 1 · 每日 dream 修炼（v0 已存在）
│   - 每日 23:00 自动化
│   - 沉淀当日对话为 3F Content case
│   - 输出：dream-log.md
│
└── 引擎 2 · 达尔文 2.0（v1 新增 · 本 case 核心）
    - 触发：每周日 / 每月 1 日 / 重要 PR 后
    - 9 维评分 + 多评委 + validation 回滚
    - human-in-loop CHECKPOINT
```

---

## P3 · 9 维评分标准（核心 · 30+ 行详解）

### 维度 1-3（借达尔文 2.0 · 通用）

#### 维度 1 · 失败模式编码
- 10 分：明确"如果 X 就做 Y；否则 Z" 全部主分支
- 5 分：只有 happy path
- 0 分：完全没有错误处理

#### 维度 2 · 可执行具体性
- 10 分：每个动作具体可执行
- 5 分：≤ 2 处软化措辞
- 0 分：3 处以上软化（建议/可以考虑/视情况而定）

#### 维度 3 · 高风险行动黑名单
- 10 分：独立章节 ≥ 5 条
- 5 分：≤ 3 条
- 0 分：完全没有

### 维度 4-9（pretty-skills 专属 · 元库标准）

#### 维度 4 · 4 件套完整度
- 10 分：content.md + PDF + images/ + 锦绣 + check-3f EXIT=0
- 5 分：3 件套
- 0 分：≤ 2 件套

#### 维度 5 · 锦绣素材完整度
- 10 分：2 封面 + 8-12 讲解图 + 融合 md
- 5 分：3 类素材
- 0 分：≤ 2 类素材

#### 维度 6 · 跨 agent 兼容性
- 10 分：5 agent 端（Mavis/Claude/Codex/Cursor/Windsurf）全测试
- 5 分：3 个 agent
- 0 分：1 个 agent

#### 维度 7 · 实战验证
- 10 分：用户实战 + 量化疗效（X 小时/Y%）
- 5 分：作者自验证
- 0 分：理论推演

#### 维度 8 · 内容数据支撑
- 10 分：所有断言有引用 + 来源
- 5 分：关键断言有引用
- 0 分：通篇"我认为"

#### 维度 9 · 维护者活跃度
- 10 分：7 天内 commit
- 5 分：30 天内 commit
- 0 分：> 90 天无更新

---

## P4 · 多评委独立审查协议

### 启动规则
每轮启动 2 个独立 AI 评委：
- 评委 A：GPT-4 class
- 评委 B：Claude 3.5 class
- 评委 C（可选）：Gemini Pro class
- 共识：≥ 2 评委分数差 ≤ 1 分 → 共识分数

### 锚定防御
- 不复用：下一轮启动全新评委
- 不看历史：只公布当前 case 内容
- 基线公布：不公布上次分数

### 早停机制
- 单轮涨幅 < 1 分 → 早停
- 干跑模式 > 30% → 告警
- 连续 2 轮涨幅 < 0.5 → 强制停手

---

## P5 · 反例黑名单（8 条 · 核心防错）

1. **同一个 AI 又改又评**（SkillLens 印证 · 单评委 46.4%）
2. **用 `git reset --hard` 当回滚**（应该用 `git revert`）
3. **为凑分堆冗余**（早停机制防御）
4. **跳过测试提示词直接评分**（必须用真实 case 测试）
5. **一轮内改多个维度**（每轮只改最低维度）
6. **干跑模式 > 30%**（必须实测）
7. **静默跳过异常**（必须显性处理）
8. **忽视维度相关簇**（改一维会带动一簇）

---

## P6 · human-in-loop CHECKPOINT 协议

| 阶段 | CHECKPOINT | 用户决策 |
|---|---|---|
| 阶段 1 · 基线评估 | 🔴 CHECKPOINT 1 | 决定改什么维度 |
| 阶段 2 · 单维度优化 | 🔴 CHECKPOINT 2 | 确认改动方向 |
| 阶段 2.5 · 测试提示词跑 | 🔴 CHECKPOINT 3 | 确认测试结果 |
| 阶段 3 · 回归测试 | 🛑 STOP | 涨幅 < 阈值强制停手 |

每个 CHECKPOINT 强制暂停等用户确认——关键决策永远交回人。

---

## P7 · 5 段式优化循环

```
Rollout（跑任务）→ Reflect（复盘）→ Edit（提议改动）→ Validate（验证）→ Apply（应用）
                ↑                                                    ↓
                └────────────────── Reject（回滚） ←──────────────────┘
                                         ↑
                                分数没涨或破坏
```

---

## P8 · 与 SkillOpt 关系

- **SkillOpt**：企业级 / benchmark-driven / 52 组合 52 胜
- **达尔文 2.0 + pretty-skills**：个人开发者 / rubric-driven / human in the loop / 主观评估为主
- **分工**：SkillOpt 适合规模化训练，达尔文适合快速迭代单 skill

---

## P9 · 实际执行（pretty-skills 当前 30+ case）

### 已沉淀 30+ case
按 16 领域分布：金融投资 5（company-brief / economic-impact-report / event-driven-analyzer / marginal-tracker / stock-analysis-v4）/ 视觉创作 9（comic-generator / design-master / finance-cartoon-creator / gif-sticker-generator / nano-banana-pro / oil-cover / product-visual-creator / remotion-video / wan2.7-image-skill / xiaohongshu-image-creator）/ 内容创作 5（卡兹克公众号写作 / wechat-article-creator / wechat-viral-article-creator / 橙皮书方法论 / 公众号爆款操盘术）/ 社交主导 2（persona-lab / sales-powermap）/ 商业运营 1（social-media-insights）/ 做事技巧 10（agent-browser / auto-vlog-editor / computer-interface-controller / doc-reader / folder-cleanup-assistant / ima-skill / markdown-converter / meoo-cli / office-document-specialist-suite / pdf-reader / project-manager-expert / web-access）/ Agent知识 2（browser-act / self-improving-agent）/ 教育学习 1（knowledge-digest）/ 玄学修炼 2（占星入门12星座 / dream-修炼达尔文自迭代）/ 视觉创作 1（oil-cover小红书AI封面）。

### 达尔文 2.0 优化顺序
- 第一批：高频核心（卡兹克公众号写作 / oil-cover / knowledge-digest / self-improving-agent）· v0.1 baseline
- 第二批：数据驱动（stock-analysis-v4 / company-brief / economic-impact-report）
- 第三批：创作类（comic-generator / design-master / wechat-article-creator）

---

## P10 · 收束 · pretty-skills 元库自迭代 = 长期杠杆

pretty-skills 不能是"写完就死"的静态仓库。30+ case 必须会自我进化：
- 每天 dream 修炼沉淀新 case
- 每周/每月达尔文 2.0 优化已有 case
- 关键决策永远 human-in-loop

3 层缺一不可。这就是 pretty-skills 元库的长期杠杆——会进化的 skill × 进化本身的方法论 × 人类卡口。

**金句**：会进化的 skill = 杠杆 × 时间。

---

## 元信息

- **案例来源**：微信文章 达尔文 2.0（花叔）+ pretty-skills 元库设计原则
- **作者**：huangrichao2020（设计）+ Mavis（沉淀）
- **生成日期**：2026-07-10
- **风格**：手绘科教 + 玄学修炼特有风格
- **页数**：10 页
- **疗效**：pretty-skills 30+ case 长期自迭代 · 不再"写完就死"

---

## 跨引用

- **PDF 讲解版**（必填 · GitHub 原生预览）：`./dream-修炼达尔文自迭代讲解.pdf`
- **配套 prompt**：`./prompts/`
- **视觉资源**：`./images/`
- **锦绣素材**：`./锦绣/`
- **关联 case**：[pretty-skills/dream-log.md](../../dream-log.md)（引擎 1 每日沉淀）· [content-triple-format/](../content-triple-format/)（4 件套范式）