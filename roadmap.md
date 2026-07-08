# 路线图

> **💎 再定义**：pretty-skill 是 **agent 的「知识工程中枢」** —— **不是**传统 `SKILL.md` 技能仓。
> **这里不是工具箱，是出版局。**

---

## v3.13 · 2026-07-08 ✨ 当前

### 项目定位

- 仓库定位 = agent 的**知识工程中枢**（v3.12 起正式再定义）
  - 区别传统 `SKILL.md` 技能仓
  - 沉淀可复用的结构化知识产物
- 核心哲学 = 「清晰 > 速度 · 多花 5 分钟讲清楚 = 100 倍可懂性提升」
- 美学 = 手绘叙事 + 马卡龙配色（v3.10 起锁定）
- 用法 = 学一下 XXX + 4 自在（观 / 化 / 照 / 渡）

### 现状交付

- 11 中文领域预设（`AI能力 / 编程开发 / 数据科学 / 产品设计 / 商业运营 / 金融投资 / 内容创作 / 教育学习 / 游戏玩家 / 生活方式 / 思维方法`）
- **3 件套发布范式**（`content.md` 喂 LLM + `web.html` 演示版 + 锦绣 PPT 形态）
- **3 个真实 case**（`cartman-team-ai-agent-collab` / `social-ecom-skill` / `chokepoint-mainboard` · @Kun 贡献）
- **自动化工具**：check-3f.py 校验（含 manifest.json v3.11）+ skill-creator CLI（v0.1 stub · v0.2 计划 + --visibility）
- **agent 接入协议**：INDEX.md（11 领域快查）+ manifest.json（visibility 标识）+ USAGE.md（学一下 / dream / PR 标准协议）
- **README 配图**：v3.10-v3.13 全部统一手绘马卡龙
- **CI**：GitHub Actions 自动校验 PR

**当前核心指标**：
- 3 个 case · 9 领域待全球开发者贡献
- 13+ 个完整文档（README / INDEX / USAGE / STRUCTURE / CONTRIBUTING / FRIENDS-PR-GUIDE / PROMOTION / CONTRIBUTORS / roadmap · 4 个范式 + 11 领域 + skill-creator）

---

## v3.14+ · 1 个月内（2026-08）

### skill-creator 从 stub 到真实

- v0.2 真正实现 `3 件套生成`（content.md + web.html + 锦绣）
  - 解析 `.md` / URL → 4-7 字段/页 content.md
  - 调 matrix MCP 出图（手绘马卡龙 5 色 · 按 pretty-skill 锁定风格）
  - python-pptx 嵌图 → `presentation.pptx`
  - html-ppt-viewer → `web.html`
  - 自动写 manifest.json（用 `--visibility` 参数）

### 公开化

- [ ] 公众号 + 知乎 详细版（PROMOTION.md 草稿已就绪）
- [ ] V2EX + 推特 + 微博 短版
- [ ] 邀请 5-10 个朋友提 PR（触发 GitHub 算法推荐）
- [ ] 知乎周报 + 公众号二推

### agent 真实可用性验证

- 至少 3 个不同 agent（Mavis / Claude Code / Cursor）实测：
  - 读 INDEX.md 启动
  - 「学一下 XXX」标准协议
  - 「每晚 dream 修炼」cron 实现

**目标**：100-300 star · 验证 agent 真实可用

---

## v3.20 · 3 个月内（2026-10）

### 中枢规模化

- 11 领域 × ≥ 5 case = 50+ 真实 case
- 贡献者激励：CONTRIBUTORS.md + 公众号文章推送 + 个人品牌曝光
- 公开 API：第三方工具/agent 可查询 / 拉取 cases
  - `GET /api/cases?domain=金融投资` 风格 REST 接口
  - agent 跨项目复用
- 中文社区合作：腾讯文档 / 飞书文档 / Notion 协作工具提供导出插件

### 中枢智能化

- 自动 skill 提炼 agent：每天 scan 热门 GitHub README + 公众号文章 → 自动出 case
- 跨领域推荐：「你关心 X · 也许关心 Y」基于 tags
- 学习路径建议：从思维方法 → 金融投资 → 数据科学 · 自适应

**目标**：500+ star · agent 元知识领域事实标准

---

## v4.0 · 6 个月内（2027-01）

### 全球化

- 多语言支持：英 / 日 / 韩
  - 每个 case 加 README_en.md（机器翻译起步 + 社区精修）
- 海外 KOL 协作：Stripe Press / Vercel Blog 风格英文案例发布
- 公共 API + Webhooks：让外部 agent 自动同步

### 商业化（可选 · 不影响免费）

- 公益 + 商业双轨：
  - 公益：核心 pretty-skill 开源永久免费
  - 商业：定制 case 服务 / 中小企业知识沉淀咨询 / agent 接入培训
- 「pretty-skill 企业版」：私有部署 + SSO + 审计
- 自媒体矩阵联动：每个新 case 自动转公众号 + 知乎 + 小红书帖 + 视频脚本

**目标**：2000+ star · 全球 agent 元知识底座

---

## 设计原则

> **真用户复利 > 短期 star 数字**

每个版本都先问"用户得到什么"，再问"star 涨多少"。star 是副产物，不是 KPI。

> **清晰 > 速度 · 让人看得懂 > 快速生成**

之前的工具追求"自动化"和"快速生成"——但这恰恰是优秀知识没人用的根因。
pretty-skill **从不追求快速生成 SOP**，各位多花 5 分钟讲清楚 = 100 倍可懂性提升。
