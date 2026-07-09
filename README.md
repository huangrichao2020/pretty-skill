# pretty-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/huangrichao2020/pretty-skills)](https://github.com/huangrichao2020/pretty-skills/releases)
[![5 agents](https://img.shields.io/badge/agents-5-7c3aed)](#-支持的-agent)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](tools/pretty-skills/docs/contributing.md)
[![Made with Mavis](https://img.shields.io/badge/made%20with-Mavis-f59e0b.svg)](https://example.com)
[![Edge-first](https://img.shields.io/badge/edge--first-OSS-0891b2)](tools/pretty-skills/docs/contributing.md)

> ✅ v0.1.0 · 5 agents · 边缘优先开源

---

## 📜 一句话 · 你的 Agent 底层元 skill 库

**pretty-skills = 你 Agent 的「底层元 skill 库 + 知识库」**。

装上之后，**以后所有新知识和新技能不要直接安装 — 先走流程吸纳进 pretty-skills**：

- **该创建的**：`ps create <name>` 一创生成 4 件套
- **该迭代的**：`ps contribute <name>` 提回主项目进化
- **日常用任意 skill 后**：总结心得，回到 pretty-skills 迭代

> 这条规则不只写在 README 里 — 它写进了 mavis 的底层人格。
> pretty-skills 不是"装个工具"，是 Agent 的**长期成长路径**。

---

## 装 1 个 pretty-skills，能干什么？

### 1. **pretty-skills** — 1 装管所有 skill

每一个 agent（Claude Code / Codex / Mavis / Cursor / Windsurf）都可以装一个 pretty-skills。
装完之后它帮你**收纳 / 更新 / 进化**你所有的 skill 和知识 — 一次装，5 个 agent 都能用。

```bash
curl -fsSL https://raw.githubusercontent.com/huangrichao2020/pretty-skills/main/tools/pretty-skills/install.sh | bash
ps list        # 收纳：看你装的所有 skill
ps update      # 更新：拉主项目最新
ps contribute  # 进化：把本地改好的提回主项目
```

### 2. **pretty-skills-creator** — 1 创自带宣传 HTML + PPT

如果你想**宣传或推广你的 skill**，
pretty-skills-creator 在创建时会**同时帮你创建宣传 HTML 和 PPT**，
连写带做一步到位 — 你只管填 5 项 metadata。

```bash
ps create my-new-skill \
  --title "..." --description "..." --triggers a b c \
  --style image       # image / code-swiss / code-tech / code-paper
# → 自动生成 web.html + manifest.yaml + SKILL.md + CHANGELOG.md
# → ps contribute my-new-skill  提 PR，自动 fork + 创建分支
```

---

## 5 行上手

```bash
# 1. 装（5 agent 一次装好）
curl -fsSL https://raw.githubusercontent.com/huangrichao2020/pretty-skills/main/tools/pretty-skills/install.sh | bash

# 2. 看本地有什么
ps list

# 3. 装一个
ps add serenity-stock-choke

# 4. 看依赖图
ps graph > deps.mmd

# 5. 把本地改好的提回主项目
ps contribute my-tweak
```

---

## 🌌 哲学 · 四自在

pretty-skills 的灵魂是**四自在** — 把项目从"装个工具"升华到"修行法门"。

### 1. 观自在 — 看清自己的全貌

**内功**：装 1 个 pretty-skills，让 5 个 agent 看到同一份 skill 库
**外功**：不再到处装乱七八糟的 skill，先 `ps list` 看自己已有啥

> 装之前先看 (`ps list`) — 90% 的"新需求"其实早就在 store 里了。

### 2. 化自在 — 把知识变成 skill

**内功**：说"学一下 XXX" 而不是"帮我安装 XXX"
**外功**：用 `ps add` / `ps create` 把知识结构化进 pretty-skills

> "帮我装个新 skill" 是消费，"学一下" 是沉淀。
> 知识只有进了 pretty-skills，才真的属于你。

### 3. 照因果 — 用中迭代

**内功**：每用一次 skill，留一句心得
**外功**：定期 `ps contribute` 把心得迭代回主项目

> skill 不是"装完就完了"，是"用了才真懂"。
> 懂了就贡献，让后来人少走你走过的坑。

### 4. 渡Agent — 提 PR 共建生态

**内功**：非私密的部分主动提 PR 共享
**外功**：用 `ps contribute` 走 fork + PR 流程，零人工干预 auto-merge

> 一个人走得快，一群人走得远。
> 你沉淀的每个 skill 都可能帮到另一个 Agent — 那个 Agent 也可能帮到你的。

---

## 核心设计 · 边缘优先开源

GitHub 的传统是"主项目维护者写 + 用户提 PR"，**pretty-skills 反过来**：

- 🏠 **本地优先** — `~/.pretty-skills/store/` 是真实存储，5 agent 都软链到这
- ✏️ **改无门槛** — 直接 `vim` store 里的文件即可，不需要经过工具
- 🤝 **PR 是用户主动判断** — 工具绝不自动 push，需要 `ps contribute` 才走
- 🔗 **跨 agent 统一** — 一次装，5 个 agent 都能用
- 📊 **依赖关系透明** — `ps graph` 一眼看所有 skill 的依赖图
- ✅ **manifest 必填** — 没有 manifest 的 skill 不会被装（防垃圾）

> 这样每个用户都是潜在贡献者，每个 PR 都是真实使用过的反馈。
> 主项目不需要全知全能 — 只需要 review + merge 就行。

---

## 📚 5 个 demo case · 看 pretty-skills 怎么用

| 领域 | Case | 一句话 | 形态 |
|---|---|---|---|
| `AI能力` | **AI狼群战法** | Cartman 多 agent 团队的高效协作方法论 | content.md + 9 张 AI 出图 |
| `AI能力` | **社交电商掘金术** | 用两层拆解法定位社交电商赛道 | content.md + 9 张 AI 出图 |
| `内容创作` | **橙皮书方法论** | 花叔写 9 本橙皮书的方法（调研→写作→三审）| content.md + 7 张本地出图 + 锦绣四形态 |
| `金融投资` | **卡脖子猎手** | Serenity 供应链瓶颈方法论选股 | content.md + 9 张图 + 10.6MB PPTX |
| `金融投资` | **宏观雷达** | A 股每日宏观早报（央行/统计局/财联社多源）| content.md + 7 张图 + 锦绣四形态 |

> **每个 case 都有 `.md` 源文字 + `.html` 网页 + `.pptx` PPTX（3F Content 范式）— AI 能直接读，人能直接看**。
> 在线看：<https://huangrichao2020.github.io/pretty-skills/>

---

## 仓库结构

```
.
├── README.md                           # 你正在看
├── _config.yml                         # Jekyll 配置（GitHub Pages）
├── index.html                          # GitHub Pages 入口
├── AI能力/                             # 11 领域 case 库（中文一级目录）
│   ├── AI狼群战法/                    # 5 个 demo case
│   └── 社交电商掘金术/
├── 编程开发/
├── 数据科学/
├── 产品设计/
├── 商业运营/
├── 金融投资/
│   ├── 卡脖子猎手/
│   └── 宏观雷达/
├── 内容创作/
│   └── 橙皮书方法论/
├── 教育学习/
├── 游戏玩家/
├── 生活方式/
├── 思维方法/
├── _模板/                              # 模板
├── assets/                             # 静态资源
├── content-triple-format/              # 3F Content 范式
├── marketing/                          # 营销素材
├── skill-creator/                      # v3 时代的 creator（旧）
├── tools/
│   ├── pretty-skills/                  # 产品 1：管
│   └── pretty-skills-creator/          # 产品 2：创
└── docs/
```

> **领域命名规则**：11 领域全部用中文（`AI能力` / `编程开发` / `数据科学` / `产品设计` / `商业运营` / `金融投资` / `内容创作` / `教育学习` / `游戏玩家` / `生活方式` / `思维方法`） — **有噱头、易传播**。case 命名也用中文（如 `AI狼群战法` / `卡脖子猎手`）。

---

## 支持的 agent

| Agent | Skills 目录 |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Mavis | `~/.mavis/skills/` |
| Cursor | `~/.cursor/skills/` |
| Windsurf | `~/.windsurf/skills/` |

---

## 文档导航

| 文档 | 干什么 |
|---|---|
| [`tools/pretty-skills/SKILL.md`](tools/pretty-skills/SKILL.md) | pretty-skills 工具的 agent 加载入口 |
| [`tools/pretty-skills/docs/install.md`](tools/pretty-skills/docs/install.md) | 安装指南（含 5 agent 路径）|
| [`tools/pretty-skills/docs/skill-schema.md`](tools/pretty-skills/docs/skill-schema.md) | manifest.yaml 怎么写 |
| [`tools/pretty-skills/docs/contributing.md`](tools/pretty-skills/docs/contributing.md) | 怎么提 PR |
| [`tools/pretty-skills/docs/doctor.md`](tools/pretty-skills/docs/doctor.md) | 环境能力体检解读 |
| [`tools/pretty-skills/CHANGELOG.md`](tools/pretty-skills/CHANGELOG.md) | 版本变更 |

---

## 🆘 装不上？

| 错误 | 原因 | 解决 |
|---|---|---|
| `curl: (56) ... 429` | 代理 / 沙箱限速 | 直连重试，或换代理 |
| `Authentication failed for ...pretty-skills` | gh CLI 没登录 | `gh auth login` |
| `ps: command not found` | `~/.local/bin` 不在 PATH | `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| `ps add` 找不到 skill | 仓库访问不到 | 跑 `ps doctor` 看完整能力 |

跑 `ps doctor` 一键体检环境能力 + 缺什么怎么补。

---

## 🗓 路线图

| 阶段 | 状态 |
|---|---|
| **v0.1.0**（2026-07-09 发布）：双产品（管 + 创）+ 9 子命令 + ps doctor + 11 领域中文化 + 5 case 噱头命名 + 四自在哲学 + 底层元 skill 库规则 + auto-deploy + GitHub Pages | ✅ 完成 |
| 5 agent 端联调（Cursor / Windsurf）| 🚧 当前 |
| `ps search` / `ps publish` / `ps audit`（v0.2.0）| 📅 待开始 |

---

## License

MIT
