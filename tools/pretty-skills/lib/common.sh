#!/usr/bin/env bash
# pretty-skills 公共安装函数
# 来源: tools/pretty-skills/lib/common.sh
# 所有 agent 安装脚本都 source 这个

set -euo pipefail

# ===== 颜色（只在 TTY 启用）=====
if [ -t 1 ]; then
  RED='\033[0;31m'
  GREEN='\033[0;32m'
  YELLOW='\033[0;33m'
  BLUE='\033[0;34m'
  BOLD='\033[1m'
  RESET='\033[0m'
else
  RED='' GREEN='' YELLOW='' BLUE='' BOLD='' RESET=''
fi

# ===== 路径常量 =====
# 注意：不 export 重新赋值（避免覆盖调用方传进来的 PS_ROOT）
: "${PS_ROOT:=$HOME/.pretty-skills}"
: "${PS_STORE:=$PS_ROOT/store}"
: "${PS_CONFIG:=$PS_ROOT/config.yaml}"
: "${PS_REPO:=huangrichao2020/pretty-skills}"
: "${PS_BRANCH:=main}"
: "${PS_SKILLS_DIR:=$PS_ROOT/bin}"   # 工具自身所在的 bin 目录
export PS_ROOT PS_STORE PS_CONFIG PS_REPO PS_BRANCH PS_SKILLS_DIR

# ===== 工具函数 =====

log_info()  { printf "${BLUE}[ps]${RESET} %s\n" "$*"; }
log_ok()    { printf "${GREEN}[ps]${RESET} %s\n" "$*"; }
log_warn()  { printf "${YELLOW}[ps]${RESET} %s\n" "$*" >&2; }
log_err()   { printf "${RED}[ps]${RESET} %s\n" "$*" >&2; }

# 检测命令是否存在
has_cmd() { command -v "$1" >/dev/null 2>&1; }

# 检测某个 agent 的 skills 目录是否存在
agent_skills_dir() {
  case "$1" in
    claude-code) echo "$HOME/.claude/skills" ;;
    codex)       echo "$HOME/.codex/skills" ;;
    mavis)       echo "$HOME/.mavis/skills" ;;
    cursor)      echo "$HOME/.cursor/skills" ;;
    windsurf)    echo "$HOME/.windsurf/skills" ;;
    *)           log_err "未知 agent: $1"; return 1 ;;
  esac
}

# 列出本机已安装的 agent
detect_agents() {
  local agents=()
  for a in claude-code codex mavis cursor windsurf; do
    local dir
    dir=$(agent_skills_dir "$a" 2>/dev/null) || continue
    [ -d "$dir" ] && agents+=("$a")
  done
  printf '%s\n' "${agents[@]}"
}

# 把 store 里的 skill 软链到某个 agent
link_skill_to_agent() {
  local skill_name="$1"
  local agent="$2"
  local agent_dir
  agent_dir=$(agent_skills_dir "$agent") || return 1
  local src="$PS_STORE/$skill_name"
  local dst="$agent_dir/$skill_name"

  if [ ! -d "$src" ]; then
    log_err "store 里没有 $skill_name"
    return 1
  fi
  mkdir -p "$agent_dir"
  if [ -L "$dst" ] || [ -e "$dst" ]; then
    log_warn "  $agent: $dst 已存在（跳过，ps rm 旧版后再装）"
    return 0
  fi
  ln -s "$src" "$dst"
  log_ok "  $agent: $dst -> $src"
}

# 卸载时反软链
unlink_skill_from_agent() {
  local skill_name="$1"
  local agent="$2"
  local dst
  dst=$(agent_skills_dir "$agent")/$skill_name
  if [ -L "$dst" ]; then
    rm "$dst"
    log_ok "  $agent: 删 $dst"
  elif [ -d "$dst" ]; then
    log_warn "  $agent: $dst 是目录不是软链，跳过（手动处理）"
  fi
}

# 检查依赖是否满足（read manifest.yaml + check 依赖的 skill 在 store 里）
check_dependencies() {
  local skill_name="$1"
  local manifest="$PS_STORE/$skill_name/manifest.yaml"
  if [ ! -f "$manifest" ]; then
    log_warn "$skill_name 没有 manifest.yaml（跳过依赖检查）"
    return 0
  fi
  # 简单解析：找 dependencies: 下的 name: 字段
  local deps
  deps=$(awk '/^dependencies:/{flag=1;next}/^[a-zA-Z]/{flag=0}flag' "$manifest" | grep -E '^[[:space:]]+-?[[:space:]]*name:' | sed -E 's/.*name:[[:space:]]+//' | tr -d '"' || true)
  if [ -z "$deps" ]; then
    return 0
  fi
  local missing=()
  for dep in $deps; do
    if [ ! -d "$PS_STORE/$dep" ]; then
      missing+=("$dep")
    fi
  done
  if [ ${#missing[@]} -gt 0 ]; then
    log_warn "$skill_name 缺依赖: ${missing[*]}"
    log_warn "运行: ps add ${missing[*]}"
    return 1
  fi
  return 0
}
