# ps doctor · 环境能力体检

`ps doctor` 是个内置体检工具，跑一次能知道你的环境缺什么、缺了体验会差在哪。

## 用法

```bash
ps doctor              # 跑一次体检
ps doctor --explain    # 加一段"缺能力时体验会差在哪"的解释
```

`install.sh` 装完会自动跑一次。如果你之后环境变了（重装 gh / 重新登录 GitHub），随时手跑 `ps doctor` 重新体检。

## 检查项

| 能力 | 关键度 | 缺了后果 | 怎么补 |
|---|---|---|---|
| `bash` ≥ 3.2 | 🔴 关键 | ps 跑不起来 | macOS: `brew install bash` |
| `git` ≥ 2.0 | 🔴 关键 | `ps add` / `ps update` / `ps contribute` 全废 | `brew install git` |
| `curl` | 🔴 关键 | install.sh 一行装脚本不能用 | `brew install curl` |
| `python3` ≥ 3.8 | 🟡 重要 | `ps create` / pretty-skills-creator 不可用 | `brew install python3` |
| `gh` | 🟡 重要 | `ps contribute` 不可用（提 PR 走不通） | `brew install gh` |
| `gh auth` | 🟡 重要 | `ps contribute` 卡在登录 | `gh auth login` |
| `~/.local/bin` 在 PATH | 🟡 重要 | 装完 `ps` 命令找不到 | `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| **生图能力**（matrix MCP） | 🟢 可选 | 创建 image 风格 skill 不自动生图 | 装 matrix MCP / mavis 桌面端 |
| `jq` | 🟢 可选 | manifest 校验降级 | `brew install jq` |

## 3 种结果

### ✅ 完整能力
所有关键 + 重要 + 可选都齐。5 agent 全功能可用，包括 `ps contribute` 提 PR 和 image 风格生图。

### ⚠️ 体验降级
关键 + 重要都齐，可选有缺。能跑但部分体验会缺，强烈建议补。

### ❌ 关键能力缺失
关键项有缺。ps 核心功能跑不起来。

## 样例输出

```
🩺 pretty-skills doctor  环境能力体检

  能力              状态   详情 / 怎么补
  ──────────────────  ──────  ──────────────────────────────────────────
  bash                ✅  v3.2.57(1)-release
  git                 ✅  v2.50.1
  curl                ✅  v8.7.1
  python3             ✅  v3.14.4
  gh                  ✅  v2.92.0
  gh auth             ⚠️   未登录（ps contribute 会卡在登录）
                               → gh auth login
  ~/.local/bin        ✅  在 PATH
  生图能力        ⚠️   matrix MCP 未注册
                               → mavis mcp add matrix ...
  jq                  ✅  v1.8.1

  ⚠️  体验降级 (2 项可选缺失)
     能跑但部分体验会缺，强烈建议补
```

## 为什么先看 doctor

按我们设计的 5 agent 跨平台安装 + 边缘优先开源贡献模型：

1. **装完跑一次** → 知道装得对不对、缺什么
2. **改完环境** → 跑一次确认没退化
3. **遇到 `ps xxx` 失败** → 跑一次定位是环境问题还是命令 bug
4. **提 PR 前** → 跑一次确认 `gh auth` + matrix MCP 都对

这是 pretty-skills 工具的"自检"。
