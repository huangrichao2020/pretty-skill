#!/usr/bin/env bash
# pretty-skills · 一键安装
# 用法: curl ... | bash   或   bash install.sh [--agents claude-code,mavis] [--no-symlink]
#
# ╔══════════════════════════════════════════════════════════════╗
# ║  📜 装上之后 · 你 Agent 的底层元 skill 库 + 知识库            ║
# ║                                                              ║
# ║  以后所有新知识和新技能：                                       ║
# ║    • 该创建的：ps create <name>  → 4 件套自动生成             ║
# ║    • 该迭代的：ps contribute <name>  → 提回主项目进化         ║
# ║    • 日常用任意 skill 后：总结心得 → ps contribute 迭代回去   ║
# ║                                                              ║
# ║  这条规则写进了 mavis 的底层人格 — 沉淀型 Agent 的长期路径。   ║
# ╚══════════════════════════════════════════════════════════════╝
#
# 步骤:
#   1. 创建 ~/.pretty-skills/store 公共存储
#   2. 从主项目下载 pretty-skills 工具本身（store 里的第一个 skill）
#   3. 把 ps 主命令软链到 ~/.local/bin/ps
#   4. 软链到各 agent 的 skills 目录
#   5. 装完跑 ps doctor 体检环境能力

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 解析参数
AGENTS="all"
NO_SYMLINK=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agents)  AGENTS="$2"; shift 2 ;;
    --no-symlink) NO_SYMLINK=1; shift ;;
    -h|--help)
      cat <<EOF
用法: install.sh [选项]
  --agents <list>    要装到哪些 agent（逗号分隔，默认 all，all = claude-code,codex,mavis,cursor,windsurf）
  --no-symlink       只装 store，不软链到 agent
  -h, --help         看这个帮助
EOF
      exit 0
      ;;
    *) echo "未知参数: $1"; exit 1 ;;
  esac
done

# 加载公共库
# shellcheck source=lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

echo
echo "${BOLD}╔════════════════════════════════════════════╗${RESET}"
echo "${BOLD}║   pretty-skills · 跨 agent skill 管理器     ║${RESET}"
echo "${BOLD}╚════════════════════════════════════════════╝${RESET}"
echo

# === Step 1: 创建 store ===
log_info "Step 1/4 · 创建 store 公共存储: $PS_STORE"
mkdir -p "$PS_STORE"
log_ok "store 就绪"

# === Step 2: 拉 pretty-skills 工具自身到 store ===
log_info "Step 2/4 · 拉 pretty-skills 工具自身到 store"
TOOL_SRC="$SCRIPT_DIR"
TOOL_DST="$PS_STORE/pretty-skills"
if [ -d "$TOOL_DST" ] || [ -L "$TOOL_DST" ]; then
  log_warn "$TOOL_DST 已存在，跳过（手动删了再装）"
else
  # 复制整个 pretty-skills 目录（包括 cli/ lib/ agents/ install.sh SKILL.md）
  cp -R "$TOOL_SRC" "$TOOL_DST"
  log_ok "工具已装到: $TOOL_DST"
fi

# === Step 3: ps 主命令放进 PATH ===
log_info "Step 3/4 · 装 ps 主命令到 ~/.local/bin/ps"
mkdir -p "$HOME/.local/bin"
PS_CMD_SRC="$PS_STORE/pretty-skills/cli/ps"
PS_CMD_DST="$HOME/.local/bin/ps"
if [ -e "$PS_CMD_DST" ] && [ ! -L "$PS_CMD_DST" ]; then
  log_warn "$PS_CMD_DST 已存在且不是软链（保留旧版）"
elif [ -L "$PS_CMD_DST" ]; then
  rm "$PS_CMD_DST"
fi
ln -s "$PS_CMD_SRC" "$PS_CMD_DST"
log_ok "ps -> $PS_CMD_SRC"

# 提示 PATH
case ":$PATH:" in
  *":$HOME/.local/bin:"*) ;;
  *) log_warn "~/.local/bin 不在 PATH 里，加这一行到 ~/.zshrc: export PATH=\"\$HOME/.local/bin:\$PATH\"" ;;
esac

# === Step 4: 软链到 agent ===
if [ "$NO_SYMLINK" -eq 1 ]; then
  log_info "Step 4/4 · --no-symlink 跳过"
else
  log_info "Step 4/4 · 软链到 agent"

  # 解析 AGENTS
  if [ "$AGENTS" = "all" ]; then
    detected=$(detect_agents)
    if [ -z "$detected" ]; then
      log_warn "没检测到任何 agent 的 skills 目录（手动检查 ~/.claude/skills 等）"
    else
      AGENTS=$(echo "$detected" | tr '\n' ',' | sed 's/,$//')
    fi
  fi

  IFS=',' read -ra AGENT_LIST <<< "$AGENTS"
  for agent in "${AGENT_LIST[@]}"; do
    link_skill_to_agent "pretty-skills" "$agent"
  done
fi

echo
log_ok "🎉 pretty-skills 装好了"
echo

# === Step 5: 体检环境能力 ===
log_info "Step 5/5 · 体检环境能力（缺什么会提示怎么补）"
DOCTOR_LIB="$TOOL_DST/lib/doctor.sh"
if [ -f "$DOCTOR_LIB" ]; then
  # shellcheck source=/dev/null
  source "$DOCTOR_LIB"
  run_doctor
else
  log_warn "找不到 doctor.sh，跳过体检"
fi

echo
echo "试一下："
echo "  ${BOLD}ps list${RESET}          # 看本地所有 skill"
echo "  ${BOLD}ps info pretty-skills${RESET}   # 看详情"
echo "  ${BOLD}ps add serenity-stock-choke${RESET}   # 装一个"
echo "  ${BOLD}ps graph${RESET}        # 看依赖图"
echo "  ${BOLD}ps doctor --explain${RESET}  # 体检 + 缺能力时体验会差在哪"
echo
