# AI 自进化技能 · 锦绣素材（dream 修炼达尔文 v2）

> 这个目录是 skill-creator 工具自动生成的传播素材 · Agent知识领域

## 素材清单（v3.1 简化 · 按形式切）

| 形式 | 文件名 | 规格 | 用途 |
|---|---|---|---|
| 横屏封面 | `cover-横屏.png`（待生成） | 16:9 · 1920×1080 | 朋友圈 / 推特 / 微博 / 视频封面 |
| 竖屏封面 | `cover-竖屏.png`（待生成） | 3:4 · 1080×1440 | 小红书 / Instagram / 抖音 / 视频号 |
| 讲解图集 | `slides/`（待生成） | 16:9 · 10 张 · 带中文 + 数据 | PPT / 公众号 / 知乎 / 视频 / 海报 |
| 融合 md | `readme.md`（本文件） | md | 直接发公众号 + 自媒体稿 + AI 阅读 |

---

## 导语（公众号开头 · 自媒体稿开头）

做 AI 代理的人都有一个痛点 —— 同样的错误每天犯 3-5 次，每次用户都要重复纠正。

今天给大家分享 self-improving-agent 的完整方法论 —— **5 项能力 + 5 步工作流 + 8 条反例黑名单**。让 AI 代理从"静态工具"变成"自我进化系统"，每次失败都变下次更好。

> **核心要点**（AI 友好 · 1 屏可读）：
> - 5 项能力：捕获学习 / 错误纠正 / 性能优化 / 知识积累 / 自主成长
> - 5 步工作流：错误发生 → 5 Why 根因 → 分类 → 记录 memory → 更新 skill → 下次预防
> - 8 条反例黑名单：重复犯 / 不记录 / 不更新 / 不学习 / 静默异常 / git reset hard / 同 AI 改评 / 一轮多改
> - dream 修炼 v2 真实优化：9 维评分 4.0 → 7.7（+3.7 涨分）

---

## 第 1 章 · AI 代理的 4 大浪费

- 浪费 1：同样错误犯 N 次
- 浪费 2：不记录失败原因
- 浪费 3：不更新 skill
- 浪费 4：不主动学习

> AI 不进化 = 不会发光的电灯泡

> **配图**：[slides/slide-1.png](slides/slide-1.png)（待生成）

---

## 第 2 章 · 失败模式与兜底树

4 类失败 + 5 Why SOP：

| 失败模式 | 触发 | 一线修复 | 兜底 |
|---|---|---|---|
| 命令执行失败 | 工具调用错 | 重试 1 次 | 切备用工具 |
| 输出质量低 | 用户纠正 | 记录 memory | 反例黑名单 |
| 理解偏差 | 反馈"不是这个" | 反问澄清 | 历史 case 模式 |
| 系统故障 | daemon 崩 | 等待检查 | fallback 模式 |

5 Why 流程：Why 1 → Why 2 → Why 3 → Why 4 → Why 5（挖到根因）→ 写 memory + 更新 skill

> **配图**：[slides/slide-2.png](slides/slide-2.png)（待生成）

---

## 第 3 章 · 5 项核心能力

1. 捕获学习（错误 / 纠正 / 心得 → 记录）
2. 错误纠正（下次自动避开）
3. 性能优化（识别低效 → 重写）
4. 知识积累（沉淀到 knowledge）
5. 自主成长（自动应用）

5 项能力 = AI 代理的肌肉记忆。

> **配图**：[slides/slide-3.png](slides/slide-3.png)（待生成）

---

## 第 4 章 · 5 步工作流（深化）

```
错误发生
  ↓
Step 1 · 根因分析（5 Why）
  ↓
Step 2 · 分类（4 类失败）
  ↓
Step 3 · 记录（memory 3 层）
  ↓
Step 4 · 更新 skill（Edit tool 不重写）
  ↓
Step 5 · 下次预防（共识检查）
```

5 步工作流 = 进化 pipeline。

> **配图**：[slides/slide-4.png](slides/slide-4.png)（待生成）

---

## 第 5 章 · 反例黑名单 8 条（核心）

| # | 反例 | 反例描述 | 修复 |
|---|---|---|---|
| 1 | 重复犯同样错误 | 用户每次都纠正 | 每次 → memory append |
| 2 | 不记录失败原因 | 日志只写"失败" | 含 trigger + reason + fix |
| 3 | 不更新 skill | memory 有但 SKILL.md 旧 | 每月 review · Edit 不重写 |
| 4 | 不主动学习 | 等用户纠正才动 | 每日 dream + 达尔文评分 |
| 5 | 静默跳过异常 | catch 错误吞了 | 必须显性记录 + 通知用户 |
| 6 | 用 `git reset --hard` | 改错想回滚 | 用 `git revert` · 保留历史 |
| 7 | 同一个 AI 又改又评 | 评分作弊 | 多评委独立审查 |
| 8 | 一轮内改多个维度 | 不知道哪个有效 | 每轮只改最低维度 |

8 条反例 = AI 代理的"禁止事项"。

> **配图**：[slides/slide-5.png](slides/slide-5.png)（待生成）

---

## 第 6 章 · mavis memory 集成（3 层）

- **agent memory**（`~/.mavis/agents/mavis/memory/`）· 跨 session 持久
- **project memory**（`~/.mavis/knowledge/<project>/`）· 项目专属
- **user memory**（`~/.mavis/memory/user.md`）· 用户偏好

memory 4 字段必填：
- 主题（日期）
- Type：pattern / decision / fact / preference
- Trigger：什么情况下适用
- Content：具体内容

> memory 写入 = 自进化的物理基础

> **配图**：[slides/slide-6.png](slides/slide-6.png)（待生成）

---

## 第 7 章 · 实战案例 2 个

### 案例 1 · pretty-skills 大活清理

**失败**：AI 不知道用户希望什么
**根因**（5 Why）：没问"清理范围"
**修复**：立刻问 1 个关键问题 + 给出 A/B/C 选项

**疗效**：4 commit + 60+ 文件改动 + 用户验收

### 案例 2 · dream 修炼达尔文误解

**失败**：把 dream 修炼做成"元 case 解释"
**根因**（5 Why）：误解 pretty-skill 设计精神
**修复**：用户纠正 + 跑 9 维评分 + 真实优化

**疗效**：4.0 → 7.7（+3.7 涨分）

> 实战案例 = 自进化的"训练数据"

> **配图**：[slides/slide-7.png](slides/slide-7.png)（待生成）

---

## 第 8 章 · 9 维评分应用

按 pretty-skills 元库 9 维评分标准：
- self-improving-agent 每月用 9 维评 1 次
- 多评委协议：mavis + 用户自评
- validation：跑 check-3f.py · 涨分 commit · 跌分 revert

> **配图**：[slides/slide-8.png](slides/slide-8.png)（待生成）

---

## 第 9 章 · 5 + 5 + 8 = 自我进化系统

5 步工作流 + 5 项能力 + 8 条反例 = 完整自我进化系统。

每次失败 → 5 Why → 失败编码 → 反例更新 → memory 沉淀 → 下次避开。

> **配图**：[slides/slide-9.png](slides/slide-9.png)（待生成）

---

## 第 10 章 · 收束 · 会进化的 AI = 杠杆 × 时间 × 自我

AI 代理装了 self-improving-agent 之后会从"静态工具"变成"自我进化系统"。

**金句**：会进化的 AI = 杠杆 × 时间 × 自我。

> **配图**：[slides/slide-10.png](slides/slide-10.png)（待生成）

---

完整规范：[content.md](../content.md)

---

*素材说明：本目录下的 cover-*.png 和 slides/ 需后续用 skill-creator 工具生成。骨架已就位。*