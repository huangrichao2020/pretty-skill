# pretty-skills 安装指南

> 5 大 agent 一次装好，自动软链到所有 skills 目录。

## 一键安装（推荐）

```bash
curl -fsSL https://raw.githubusercontent.com/huangrichao2020/pretty-skills/main/tools/pretty-skills/install.sh | bash
```

它会做：
1. 创建 `~/.pretty-skills/store/` 公共存储
2. 把 pretty-skills 工具自身装到 store
3. 把 `ps` 命令软链到 `~/.local/bin/ps`
4. 软链到所有检测到的 agent（Claude Code / Codex / Mavis / Cursor / Windsurf）

## 高级选项

### 只装到指定 agent

```bash
bash install.sh --agents claude-code,mavis
```

支持的 agent：
- `claude-code` — `~/.claude/skills/`
- `codex` — `~/.codex/skills/`
- `mavis` — `~/.mavis/skills/`
- `cursor` — `~/.cursor/skills/`
- `windsurf` — `~/.windsurf/skills/`

### 只装 store，不软链

```bash
bash install.sh --no-symlink
```

之后手动软链：
```bash
ln -s ~/.pretty-skills/store/pretty-skills ~/.claude/skills/pretty-skills
```

## 验证安装

```bash
ps list
```

应该看到：

```
📦 本地已装 skill

  pretty-skills                       v0.1.0
    跨 agent 统一管理你的所有 skill 和知识。
    agents: claude-code,codex,mavis,cursor,windsurf
```

## PATH 提示

`ps` 命令装在 `~/.local/bin/ps`。如果 shell 找不到：

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 升级

工具自身的升级走 `install.sh`（不是 `ps update`，避免循环依赖）：

```bash
curl -fsSL https://raw.githubusercontent.com/huangrichao2020/pretty-skills/main/tools/pretty-skills/install.sh | bash
```

它会检测 store 里已存在并跳过。

## 卸载

```bash
rm -rf ~/.pretty-skills
find ~/.claude/skills ~/.codex/skills ~/.mavis/skills ~/.cursor/skills ~/.windsurf/skills \
  -name 'pretty-skills*' -exec rm {} \;
```
