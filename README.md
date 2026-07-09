# pretty-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/huangrichao2020/pretty-skills)](https://github.com/huangrichao2020/pretty-skills/releases)
[![5 agents](https://img.shields.io/badge/agents-5-7c3aed)](#-支持的-agent)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](tools/pretty-skills/docs/contributing.md)
[![Made with Mavis](https://img.shields.io/badge/made%20with-Mavis-f59e0b.svg)](https://example.com)
[![Edge-first](https://img.shields.io/badge/edge--first-OSS-0891b2)](tools/pretty-skills/docs/contributing.md)

> ✅ **v0.1.0 已发布**（2026-07-09）· 仓库名 `pretty-skill` → `pretty-skills`。

---

## 装 1 个 pretty-skills，能干什么？


### 1. **pretty-skills**  管理你所有 skill

每一个 agent（Claude Code / Codex / Mavis / Cursor / Windsurf）都可以装一个 pretty-skills。
装完之后它帮你**收纳 / 更新 / 进化**你所有的 skill 和知识 — 一次装，5 个 agent 都能用。

```bash
curl -fsSL https://raw.githubusercontent.com/huangrichao2020/pretty-skills/main/tools/pretty-skills/install.sh | bash
ps list        # 收纳：看你装的所有 skill
ps update      # 更新：拉主项目最新
ps contribute  # 进化：把本地改好的提回主项目
```

### 2. **pretty-skills-creator** 帮你创建skill时同步生成知识讲解HTML 或 PPT

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

## 仓库结构

```
.
├── README.md                           # 你正在看
├── _config.yml                         # Jekyll 配置（GitHub Pages）
├── index.html                          # GitHub Pages 入口
├── cases/                              # 案例库（演示 pretty-skills 怎么用）
│   └── ...
├── docs/                               # 总文档
│   ├── 4-installation.md
│   ├── 5-skill-schema.md
│   └── 6-contributing.md
└── tools/
    ├── pretty-skills/                  # 产品 1：管
    │   ├── SKILL.md                    # agent 加载入口
    │   ├── install.sh                  # 一键装 5 agent
    │   ├── cli/ps                      # 主命令
    │   ├── cli/ps-list / info / add / rm / update / graph / contribute / create
    │   ├── lib/common.sh
    │   ├── manifest-schema.json
    │   ├── CHANGELOG.md
    │   └── docs/                       # 工具自己的文档
    └── pretty-skills-creator/          # 产品 2：创（待迁移）
        └── ...
```

---

## 文档导航

| 文档 | 干什么 |
|---|---|
| [`tools/pretty-skills/SKILL.md`](tools/pretty-skills/SKILL.md) | pretty-skills 工具的 agent 加载入口（agent 读这个） |
| [`tools/pretty-skills/docs/install.md`](tools/pretty-skills/docs/install.md) | 安装指南（含 5 agent 路径） |
| [`tools/pretty-skills/docs/skill-schema.md`](tools/pretty-skills/docs/skill-schema.md) | manifest.yaml 怎么写 |
| [`tools/pretty-skills/docs/contributing.md`](tools/pretty-skills/docs/contributing.md) | 怎么提 PR |
| [`tools/pretty-skills/CHANGELOG.md`](tools/pretty-skills/CHANGELOG.md) | 版本变更 |

---

## 🆘 装不上？

| 错误 | 原因 | 解决 |
|---|---|---|
| `curl: (56) ... 429` | 代理 / 沙箱限速 | 直连重试，或换代理 |
| `Authentication failed for ...pretty-skills` | gh CLI 没登录 | `gh auth login` |
| `ps: command not found` | `~/.local/bin` 不在 PATH | `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| `ps add` 找不到 skill | 仓库还在过渡期（旧名） | 跑 `ps doctor` 看完整能力 |

跑 `ps doctor` 一键体检环境能力 + 缺什么怎么补。

---

## 🗓 路线图

| 阶段 | 时间 | 状态 |
|---|---|---|
| 重塑方案 + 草稿 | 2026-07-09 | ✅ 完成 |
| 工具核心（CLI + install + manifest） | Day 1-3 | ✅ 完成 |
| pretty-skills-creator 迁移 | Day 4-5 | ✅ 完成 |
| ps doctor 环境能力体检 | Day 5 | ✅ 完成 |
| PR #3 合到 main | 2026-07-09 | ✅ 完成 |
| GitHub 改名 + v0.1.0 release | 2026-07-09 | ✅ 完成 |
| 5 agent 端联调 | Day 5-6 | 🚧 当前 |
| 撤回 PR #2 + 调整 auto-deploy workflow | 待定 | 📅 待开始 |

---

## 旧 `pretty-skill` 单数版的说明

旧 README（含四自在哲学、案例展示）在 git history 里。改名后旧 URL 会被 GitHub 自动重定向到新仓库。

如果你是从旧 URL 跳过来的：
- "四自在"哲学保留在 `docs/soul.md`（待写）
- 所有 case 演示会在 `cases/` 目录（待迁移）
- 旧 `pretty-skill` skill 名 → 新 `pretty-skills` skill 名（自动）

---

## License

MIT
