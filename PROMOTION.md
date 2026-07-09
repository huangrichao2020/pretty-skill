# pretty-skills 宣传文草稿 · v3.13 「知识工程中枢」

> **写作用 3F Content + 锦绣范式 + 量化疗效叙事**：先告诉疗效（你拿到什么）再讲技术细节
> **v3.13 定位**：**agent 的「知识工程中枢」** —— 不是传统 `SKILL.md` 技能仓。沉淀学到的、做过的、提炼过的知识，整理成 AI 能直接读 + 人能看得懂 的结构化产物。
> **一句话**：**这里不是工具箱，是出版局。**

> **⚠️ 前置条件 · 生图能力是必须的** —— 3F Content + 锦绣范式都依赖 AI 出图。
> 推荐使用 MiniMax 套餐（49 元 Token plan 套餐就能跑，支持 matrix MCP 多模态生图 + 生视频，月费起步）。

---

## 📱 公众号版（1800 字）

### 标题备选
- A：《我做了一件事：把 agent 的"知识工程中枢"开源了——不是装工具箱，是出版局》
- B：《pretty-skills v3.13 上线 · 「知识工程中枢」理念 + 12 领域 + 学一下 XXX 协议》
- C：《从 1 个仓库到 agent 元知识底座 · pretty-skills 是怎么变成知识工程中枢的》

### 正文

```
我做了 1 件事：把"agent 的知识工程中枢"做成开源项目。

pretty-skills v3.13 上线：https://github.com/huangrichao2020/pretty-skills

再定义先讲清：本项目**不是**传统带 SKILL.md 的 agent 技能仓
（不是「按此执行 xxx」的预制工具箱）。
本项目是**知识工程中枢** —— 沉淀知识产物，让人看 + 让 LLM 读 + 让下个项目复用。

它解决 3 个真问题：

1. 太多优质知识被锁在 PDF / Word / 二进制里
   - 别人搜不到、diff 不了、AI 爬不动
   - 沉淀一次，到处看不见 = 价值归零

2. AI 不友好的内容 = 没有未来
   - 当 LLM 普及后，只有 AI 友好的内容才能被消化
   - 单向给人看 → 错过 agent 时代的红利

3. 知识无法共享 = 一个人积累，全世界看不到
   - 你写了一篇顶级方法论，没传播 = 等于没写
   - 共享需要：人能看懂 + AI 能读 + PR 流程简单

所以 pretty-skills 做 3 件事：

(1) 3F Content 范式 = AI 能直接读
   每个 case 按 .md + .pptx + .html 三件套发布
   .md 是真相源，LLM 一眼理解
   → 学一下 XXX：agent 不装包，从这里抽知识

(2) 锦绣概念 = 人能看得懂（v3 首次提出）
   每个 case 创建时**自动生成 4 形态**：
   - 锦绣封面（朋友圈 1 张大图）
   - 锦绣 PPT（公众号 12 页完整讲解）
   - 锦绣 9 图（小红书传播）
   - 锦绣视频脚本（30-60 秒讲解）

(3) 16 领域 + skill-creator 工具 = 全局共享
   - 12 个中文领域预设：Agent知识 / 编程开发 / 数据科学 / 产品设计
     / 商业运营 / 金融投资 / 内容创作 / 教育学习 / 游戏玩家
     / 情感领域 / 做事技巧 / 玄学修炼
   - 全球开发者都能 PR 贡献 · 也可 PR 新增领域
   - skill-creator 工具一键把任何知识 → 完整 case 目录
   - v3.13 新增：manifest.json 标识 public / private / draft
     私密标记的不共享，本地仍可用

**v3.13 真正的不同 · 4 个用法**：
1. 看现成的（读）：打开 web.html 翻页就懂
2. 做自己的（创建）：5 分钟复制模板做自己的 case
3. 分享你的（提 PR）：开发者共用非私密部分
4. 元知识底座（学一下 XXX）：agent 不装包，从这里抽

仓库里已经有 3 个真实 case：
- Agent知识/AI狼群战法（团队与 AI 协作 8 页）
- Agent知识/社交电商掘金术（社交电商两层拆解 8 页）
- 金融投资/卡脖子猎手（A 股卡脖子选股 9 页 · @Kun）

9 个领域等待全球开发者贡献。

**怎么贡献？**
- Fork 仓库
- 复制 _模板/案例 到你的领域目录
- 改 content + 出图 + 跑 check-3f.py
- 提 PR · 自动 GitHub Actions 校验（含 manifest.json 必填）
- 仓库主 review · merge · 全球共享

⭐ Star 仓库：https://github.com/huangrichao2020/pretty-skills
📧 联系我：提 Issue / 邮箱 / 评论区

— huangrichao2020
2026-07-08
```

---

## 📝 知乎版（1300 字）

### 标题
- 《pretty-skills v3.13 上线 · 「知识工程中枢」理念 · 不再是 SKILL.md 技能仓》
- 《让 AI 直接读 + 人能看得懂 · pretty-skills 是怎么变成 agent 元知识底座的》

### 正文

```
最近把 pretty-skills 升级到 v3.13，先讲清再定义：

本项目**不是**传统 SKILL.md 技能仓（那是 Anthropic Claude Skills 那种"按此执行 xxx"）。
本项目是 agent 的**知识工程中枢** —— 沉淀可复用的结构化知识产物。
**这里不是工具箱，是出版局。**

[Github 链接 + 1 张仓库首页截图 + 知识工程中枢配图]

v3.13 核心跃迁：从「对 AI 友好的中文内容仓」→ 「agent 的知识工程中枢」。

3 件关键升级：

1. 范式升级：3F Content + 锦绣
   - 3F Content（v1-v2）：给 AI 看（.md + .pptx + .html）
   - 锦绣（v3）：给人看（4 形态：封面 + 9图 + PPT + 视频脚本）
   - 一起 = 知识既能被 AI 消化又能被人传播

2. 领域升级：2 → 11 中文领域
   - v3：Agent知识 / 编程开发 / 数据科学 / 产品设计 / 商业运营
     / 金融投资 / 内容创作 / 教育学习 / 游戏玩家
     / 情感领域 / 做事技巧 / 玄学修炼
   - 全球开发者都能 PR 新增领域

3. 元知识接入升级（v3.11+）：
   - INDEX.md · 16 领域快查（agent RAG 友好）
   - manifest.json · visibility 标识（public / private / draft）
   - USAGE.md · agent 接入协议（学一下 XXX / dream 修炼 / 提 PR）
   - 4 自在哲学（观 / 化 / 照 / 渡）

[展示 3 个 seed case 的 3 件套结构 + 1 张锦绣封面示例]

价值：未来 AI 时代，**只有一个项目**（pretty-skills）需要维护，agent 从这里抽知识就够。
不需为每个新知识「装」新工具，直接「学」就好。

GitHub：https://github.com/huangrichao2020/pretty-skills
```

---

## 🐦 推特 / X 版（280 字符）

```
v3.13 上线：agent 的「知识工程中枢」开箱

不是工具箱，是出版局。
不是装，是学。

INPUT: 学一下 XXX
OUTPUT: 人能看 + LLM 能读 + 项目能复用

GitHub: https://github.com/huangrichao2020/pretty-skills

16 领域 + skill-creator + 中文圈首个
```

---

## 🔥 V2EX 版（450 字）

### 标题
- 《[开源] pretty-skills v3.13 · agent 的知识工程中枢 · 不是 SKILL.md 仓》

### 正文

```
[Project] pretty-skills v3.13 · 知识工程中枢 · 12 领域 + skill-creator + 学一下 XXX 协议

[Github 链接 + 1 张知识工程中枢配图]

再定义先讲：本项目**不是**传统 SKILL.md 技能仓（不是"按此执行 xxx"的预制工具箱）。
本项目是 agent 的**知识工程中枢** —— 沉淀可复用的结构化知识产物。

v3.13 关键升级：
1. 「知识工程中枢」再定义（区别于 SKILL.md 仓）
2. INDEX.md + manifest.json（agent RAG + 私密标识）
3. USAGE.md（学一下 XXX / dream 修炼 / 提 PR 协议）
4. 4 自在哲学（观 / 化 / 照 / 渡）
5. 13 个真实 case · 4 个 case 共享

之前 v1-v3 是「3F Content（给 AI 看）+ 锦绣（给人看）」
v3.13 加了「INDEX + manifest + USAGE」让 agent 能真正把它当元知识库用。

技术栈：matrix MCP 出图 + python-pptx 嵌图 + html-ppt-viewer 套壳 + check-3f.py 校验

欢迎 star + PR + fork。
```

---

## 📋 通用发布 checklist

发送前必查：
- [ ] 链接是对的（https://github.com/huangrichao2020/pretty-skills）
- [ ] 描述具体到「你拿到什么」（不是「我做了什么」）
- [ ] 至少 1 张仓库首页截图
- [ ] 至少 1 张「知识工程中枢」配图（v3.13 新出）
- [ ] 至少 1 张 seed case 的 PPT 缩略图
- [ ] 至少 1 张锦绣封面示例
- [ ] 不说「刷 star」「跪求 star」（要真实质量 + 自然增长）
- [ ] 中文社区平台（公众号 / 知乎 / V2EX / 微博 / 推特）各发一份
- [ ] **再加**：每篇宣传文都包含「本项目不是 SKILL.md 仓，是知识工程中枢」的明确定义（v3.13 必带）

---

## 推广节奏建议

| 时间 | 动作 | 目标 |
|---|---|---|
| 第 1 天 | 公众号 + 知乎（详细版） | 100-200 阅读 |
| 第 2 天 | V2EX + 推特 + 微博 | 50-100 star |
| 第 3-7 天 | 邀请 5-10 个朋友提 PR | 触发 GitHub 算法推荐 |
| 第 2 周 | 知乎周报 + 公众号二推 | 500+ star |
| 第 1 月 | 行业 KOL 互推 / 公众号投稿 | 1000+ star |
