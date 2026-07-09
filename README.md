# pretty-skills

> ✅ **v0.1.0 已发布**（2026-07-09）· 仓库名 `pretty-skill` → `pretty-skills`。
> **README 顶部先说一件事**：这是一次产品重塑，定位从"内容案例仓库" → "双产品工具生态"。

---

## 一句话

**pretty-skills = 让每个 agent 都能装、每个用户都能改、每个贡献都被看见。**

它是一个**双产品**仓库：

| 产品 | 干什么 | 安装 |
|---|---|---|
| **pretty-skills**（管） | 跨 agent 统一管理你的所有 skill 和知识 | `curl -fsSL .../install.sh \| bash` |
| **pretty-skills-creator**（创） | 创建 skill 时自动带 4 风格 HTML 占位 + 可选 PPT | `ps create my-skill` |

> "管"和"创"是父子关系：装好 pretty-skills 后，`ps create` 就把 pretty-skills-creator 调起来。

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

## 支持的 agent

| Agent | Skills 目录 |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Mavis | `~/.mavis/skills/` |
| Cursor | `~/.cursor/skills/` |
| Windsurf | `~/.windsurf/skills/` |

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
