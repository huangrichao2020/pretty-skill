# Pretty Skill · 全球优质技能与知识集合

> **这是一个开源项目**：集合**全世界开发者与玩家**贡献的优质**技能 / 知识** —— 每个 skill 在创建时就**自动生成锦绣讲解 PPT**（"锦绣"概念），方便传播和分享。
>
> **3 件套发布** = `.md` 源文字（给 AI 读）+ `.pptx` 演示稿（给人演示）+ `.html` 网页版（浏览器直接看）。

[English](./README_en.md) · 简体中文（本页）

---

## 💡 是什么

太多的优质技能 / 知识 / 方法论被锁在：
- **个人笔记** —— 别人看不到
- **PDF / Word** —— AI 爬不动，diff 不了
- **.pptx 二进制** —— 搜不到、复刻成本高

**pretty-skill** 做一件事：**让任何知识都能被 AI 消化 + 给人传播**。任何开发者 / 玩家 / 研究者都可以把自己做好的 skill 或知识贡献到这个项目，按统一的"3F Content + 锦绣"范式发布。

### 与传统开源项目的不同

| 维度 | 传统开源项目 | pretty-skill |
|---|---|---|
| **代码友好** | ✅ | ✅ |
| **AI 友好**（能被 LLM 直接消化）| ❌ | ✅ **3F Content 范式** |
| **人易传播**（一眼懂 + 视觉冲击）| ❌ | ✅ **锦绣范式**（创建时自动生成）|
| **多平台分发**（朋友圈 / 小红书 / 公众号）| ❌ | ✅ 1 次创作 = 1 套多平台素材 |
| **全球共建**（任何人都能贡献 skill）| ✅ | ✅ + 11 领域预设 + 允许扩展 |

---

## 🎯 项目愿景

> **让全世界任何优质技能 / 知识都能被 AI 消化、被人传播、让开发者 + 玩家共同贡献。**

任何人都可以：
1. 把自己做好的 skill / 方法论 / 知识沉淀按 pretty-skill 范式发布
2. 用 **skill-creator** 工具一键把任意知识变成"3F Content + 锦绣"
3. 提 PR 进 11 个领域之一（也可以 PR 新领域）
4. 仓库主审核 → merge → 全球共享

---

## 📚 11 个领域（v3 预设 · 全球共建）

| 领域（一级目录）| 范围 | 当前 case |
|---|---|---|
| **AI能力/** | LLM / Agent / 提示工程 / 机器学习 | 2 个 |
| **编程开发/** | 通用编程 / 架构 / 模式 / 最佳实践 / 前后端 | 0 |
| **数据科学/** | 数据分析 / 可视化 / 统计 / BI | 0 |
| **产品设计/** | 产品方法论 / UX / 用户研究 / 需求 | 0 |
| **商业运营/** | 营销 / 增长 / 用户运营 / 商业模式 | 0 |
| **金融投资/** | A 股 / 港美股 / 加密货币 / 量化 / 财务 | 1 个 |
| **内容创作/** | 视频 / 写作 / 直播 / 摄影 / 短视频 | 0 |
| **教育学习/** | 学科教育 / 语言学习 / 知识管理 / 学习方法 | 0 |
| **游戏玩家/** | 游戏攻略 / 角色养成 / 副本流程 / MOD 制作 | 0 |
| **生活方式/** | 健康 / 时间管理 / 关系 / 旅行 / 美食 | 0 |
| **思维方法/** | 决策框架 / 思维模型 / 心理学 / 认知科学 | 0 |

**为什么是 11 个不是更多**：
- 认知心理学 **7±2 极限的扩展版** = 覆盖广 + 不超载
- 全球开发者 PR 时能**一眼选对领域** = 0 沟通成本
- **可扩展**：可以 PR 新领域（11 + 验证 + 审核）

完整说明：[STRUCTURE.md](./STRUCTURE.md)

---

## 🌟 "锦绣"概念（首次提出）

> **锦绣（Jinxiu）= 把任何知识 / skill 在创建时就"绣"成易传播的视觉作品**

核心：
- **创建时就生成**（不是事后补救）
- **专门给人看**（不是给 AI）
- **一眼懂 + 一眼觉得有价值**（易传播）
- **多平台适配**：1 次生成 = 朋友圈 1 张 + 小红书 9 张 + 公众号 PPT

形态：
- **锦绣封面**：1 张 16:9 大图，朋友圈 / 推特传播
- **锦绣 PPT**：8-12 页完整讲解（小红书 / 公众号 / 知乎 / 演讲）
- **锦绣网页版**：手机也能看（微信 / 推友）
- **锦绣视频脚本**：30-60 秒讲解（短视频平台）

为什么叫"锦绣"：锦（丝绸织成的华丽布料）+ 绣（刺绣工艺）= 把原材料知识"绣"成华丽展示品。锦绣前程 = 前途光明。**价值感 + 视觉冲击 = 易传播**。

完整规范：[content-triple-format/锦绣.md](./content-triple-format/锦绣.md)

---

## 🛠️ skill-creator 工具（v3 新增）

> **任何知识 → 1 键生成 pretty-skill 完整目录（3F Content + 锦绣）**

`skill-creator/` 是个 CLI 工具，输入：
- 任意 `.md` 文件
- 任意 URL（博客 / 知乎 / 公众号）
- 视频脚本 / 笔记 / 你脑子里想的

输出：
- 完整 skill 目录：`content.md` + `images/` + `presentation.pptx` + `web.html` + **锦绣 PPT**
- 多平台素材：朋友圈 1 图 + 小红书 9 图 + 公众号 12 页

意义：**让"贡献一个 skill"和"创建 1 个 GitHub repo"一样简单**。

完整使用：[skill-creator/README.md](./skill-creator/README.md)

---

## 📂 1 分钟上手

```bash
git clone https://github.com/huangrichao2020/pretty-skill
cd pretty-skill
open 金融投资/chokepoint-mainboard/web.html
# → 看 9 页 PPT 真实案例（A 股卡脖子选股报告 · 深色科技风）
```

或看 v0 seed case：
```bash
open AI能力/cartman-team-ai-agent-collab/web.html
# → 8 页 PPT · 团队如何与 AI Agent 高效协作
```

---

## 🚀 如何贡献（开发者 + 玩家）

### 3 步贡献一个 skill

1. **用 skill-creator 生成初稿**（推荐）：
   ```bash
   pip install pretty-skill
   pretty-skill create --input my-knowledge.md --domain "金融投资"
   ```

2. **填实 content.md + 出图 + 跑 check-3f.py**（5 步流程）

3. **提 PR**（PR 模板自动给 11 领域下拉）：
   - Fork 仓库
   - 复制 `_模板/案例/` 到你的领域目录
   - 改 content + 出图 + 跑 check
   - 提 PR → 自动 GitHub Actions 校验

完整流程：[CONTRIBUTING.md](./CONTRIBUTING.md) · [FRIENDS-PR-GUIDE.md](./FRIENDS-PR-GUIDE.md)

### 想新增 1 个领域？

PR 加 `新领域/README.md` + `新领域/<至少 1 个 case>/` = 仓库主审核。**全球开发者可以共建领域清单**。

---

## 📐 范式：3F Content + 锦绣

### 3F Content（AI 友好）

任何 case 必须按 3F Content 范式发布：

```
<领域>/<case>/
├── content.md           # F1 · 源文字（人类 + AI 都读）
├── presentation.pptx    # F2 · 演示稿（PowerPoint / Keynote / WPS 可编辑 · 必须含图）
├── web.html             # F3 · 网页版（浏览器直接看 · 必须含 <img> 标签）
├── images/              # AI 出图原图（≥ 1 张/页）
├── prompts/             # 出图 prompt 文件（工程可复现）
├── build_pptx.py        # 模板化 PPTX 生成脚本
└── README.md            # case 说明
```

完整规范：[content-triple-format/3F-content.md](./content-triple-format/3F-content.md)

### 锦绣（人易传播）

每个 case 在提交时**自动生成**锦绣 PPT：

```
<领域>/<case>/
└── 锦绣/
    ├── cover-朋友圈.png        # 1 张 16:9 大图
    ├── xiaohongshu-9图/        # 9 张图（小红书）
    ├── public-account-ppt/    # 12 页完整讲解
    └── video-script.md         # 30 秒视频脚本
```

完整规范：[content-triple-format/锦绣.md](./content-triple-format/锦绣.md)

---

## 📊 当前内容

### `AI能力/`（领域 1 · 2 个 v0 seed cases）

| Case | 主题 | 数据 |
|---|---|---|
| **cartman-team-ai-agent-collab** | 团队如何与 AI Agent 高效协作 | 8 页 PPT · 马卡龙 |
| **social-ecom-skill** | 社交电商 × 两层拆解法 | 8 页 PPT · 马卡龙 |

### `金融投资/`（领域 6 · 1 个 case）

| Case | 主题 | 贡献者 | 数据 |
|---|---|---|---|
| **chokepoint-mainboard** | A 股卡脖子选股报告 · 主板专版 | @Kun 🎉 第 1 个真 case | 9 页 PPT · 深色科技风 |

### 9 个待开发领域

编程开发 / 数据科学 / 产品设计 / 商业运营 / 内容创作 / 教育学习 / 游戏玩家 / 生活方式 / 思维方法 —— **全球开发者共建**

---

## 🛣️ 路线图

| 版本 | 时间 | 目标 |
|---|---|---|
| **v0** ✅ | 2026-07-07 | 第 1 仓库 + 范式文档 + 2 seed cases |
| **v1** ✅ | 2026-07-08 | 第 1 个真 case 合并 + check-3f.py + GitHub Actions |
| **v2** ✅ | 2026-07-08 | 重构为中文领域 + PR 模板路径检查 |
| **v3** ✨ **当前** | 2026-07-08 | **"锦绣"概念 + 11 领域 + skill-creator 工具 + 全球开源定位** |
| v4 | 1 个月内 | 50+ case · 11 领域全覆盖 · skill-creator 自动化 |
| v5 | 3 个月内 | 200+ case · 社区驱动 · 多语言版本 |

[完整路线图](./roadmap.md)

---

## 🌟 Star 增长史

- 2026-07-07 ✨ 仓库诞生
- 2026-07-08 🎉 PR #1 合并（第 1 个真 case · @Kun）
- 2026-07-08 ✅ 范式升级 4 重防御 + check-3f.py + GitHub Actions
- 2026-07-08 🇨🇳 重构为中文领域一级目录
- 2026-07-08 🌟 **v3 跃迁** · "锦绣"概念首次提出 + 11 领域 + skill-creator 工具 + 全球开源定位

---

## 📜 License

[MIT](./LICENSE) —— 内容可商用可改编，只保留原作者署名。

---

## 🤝 联系

- 提 Issue：[github.com/huangrichao2020/pretty-skill/issues](https://github.com/huangrichao2020/pretty-skill/issues)
- 提 PR：直接 fork 后 push
- 全球开发者：欢迎任何 skill 贡献，按 [CONTRIBUTING.md](./CONTRIBUTING.md) 走流程

---

<sub>**为什么叫 pretty-skill**：「pretty」= 漂亮 + 易用 + 人人都能读；「skill」= 沉淀可复用的「技能 / 知识」。**对 AI 友好 + 人易传播 + 全球共建** = pretty-skill v3。</sub>

<sub>README 自身也按 [3F Content + 锦绣](./content-triple-format/) 范式写：先告诉疗效（你拿到什么），再讲技术细节。</sub>