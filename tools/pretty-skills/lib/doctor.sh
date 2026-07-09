#!/usr/bin/env bash
# pretty-skills · doctor（环境能力校验）
# 用法: source this file, call run_doctor
#
# 检查项：
#   关键（缺了 ps 核心功能跑不起来）：
#     - bash >= 3.2
#     - git >= 2.0
#     - curl
#   重要（缺了体验降级）：
#     - python3 >= 3.8       (ps create / pretty-skills-creator 需要)
#     - gh CLI                (ps contribute 需要)
#     - gh auth status        (提 PR 需要登录)
#     - ~/.local/bin in PATH  (装完 ps 找不到)
#   可选（缺了某些风格不可用）：
#     - mavis CLI + matrix MCP  (生图能力 — image 风格 skill 需要)
#     - jq                    (manifest 校验)

set -uo pipefail  # 不开 -e，因为我们要收集所有检查结果

# ===== 颜色 =====
if [ -t 1 ]; then
  RED='\033[0;31m'
  GREEN='\033[0;32m'
  YELLOW='\033[0;33m'
  BLUE='\033[0;34m'
  BOLD='\033[1m'
  DIM='\033[2m'
  RESET='\033[0m'
else
  RED='' GREEN='' YELLOW='' BLUE='' BOLD='' DIM='' RESET=''
fi

# ===== 三个等级 =====
# OK:     ✅   完整能力
# WARN:   ⚠️   体验降级（但能跑）
# MISS:   ❌   关键缺失（核心功能跑不起来）

# 全局结果数组
declare -a DOCTOR_RESULTS=()

# 添加一行结果
# 用法: doctor_add "git" "OK" "2.39.3" "" "..."
doctor_add() {
  local name="$1"
  local status="$2"   # OK / WARN / MISS
  local detail="$3"   # 版本号 / 简短说明
  local fix="${4:-}"  # 怎么补
  DOCTOR_RESULTS+=("$status|$name|$detail|$fix")
}

# ===== 单项检查 =====

check_bash() {
  local version="${BASH_VERSION:-unknown}"
  local major="${version%%.*}"
  if [ "$major" -ge 3 ] 2>/dev/null; then
    doctor_add "bash" "OK" "v$version" ""
  else
    doctor_add "bash" "MISS" "v$version" "升级 bash（macOS: brew install bash）"
  fi
}

check_git() {
  if ! has_cmd git; then
    doctor_add "git" "MISS" "未装" "brew install git"
    return
  fi
  local v
  v=$(git --version 2>/dev/null | sed -E 's/git version //' | sed -E 's/ \(Apple Git-[0-9]+\)$//' | head -1)
  local major="${v%%.*}"
  if [ "$major" -ge 2 ] 2>/dev/null; then
    doctor_add "git" "OK" "v$v" ""
  else
    doctor_add "git" "WARN" "v$v（< 2.0 旧版可能有问题）" "brew upgrade git"
  fi
}

check_curl() {
  if has_cmd curl; then
    local v
    v=$(curl --version 2>/dev/null | head -1 | sed -E 's/curl //' | cut -d' ' -f1)
    doctor_add "curl" "OK" "v$v" ""
  else
    doctor_add "curl" "MISS" "未装" "brew install curl"
  fi
}

check_python3() {
  if ! has_cmd python3; then
    doctor_add "python3" "WARN" "未装（ps create / pretty-skills-creator 不可用）" "brew install python3"
    return
  fi
  local v
  v=$(python3 --version 2>&1 | sed -E 's/Python //')
  local major minor
  major=$(echo "$v" | cut -d. -f1)
  minor=$(echo "$v" | cut -d. -f2)
  if [ "$major" -ge 3 ] && [ "$minor" -ge 8 ] 2>/dev/null; then
    doctor_add "python3" "OK" "v$v" ""
  else
    doctor_add "python3" "WARN" "v$v（< 3.8，部分脚本可能不兼容）" "brew upgrade python3"
  fi
}

check_gh() {
  if ! has_cmd gh; then
    doctor_add "gh" "WARN" "未装（ps contribute 不可用 — 不能提 PR 回主项目）" "brew install gh"
    return
  fi
  local v
  v=$(gh --version 2>/dev/null | sed -E 's/gh version //' | head -1)
  doctor_add "gh" "OK" "v$v" ""

  # 子检查：是否登录
  if gh auth status >/dev/null 2>&1; then
    local user
    user=$(gh api user --jq .login 2>/dev/null || echo "?")
    doctor_add "gh auth" "OK" "已登录 ($user)" ""
  else
    doctor_add "gh auth" "WARN" "未登录（ps contribute 会卡在登录）" "gh auth login"
  fi
}

check_local_bin_path() {
  case ":$PATH:" in
    *":$HOME/.local/bin:"*)
      doctor_add "~/.local/bin" "OK" "在 PATH" ""
      ;;
    *)
      doctor_add "~/.local/bin" "WARN" "不在 PATH（装完 ps 命令找不到）" 'echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> ~/.zshrc && source ~/.zshrc'
      ;;
  esac
}

# 生图能力检测
check_image_gen() {
  local mavis_cmd="$HOME/.mavis/bin/mavis"

  # 1. mavis CLI 在不在
  if [ ! -x "$mavis_cmd" ]; then
    # 试一下 PATH 里有没有
    if ! has_cmd mavis; then
      doctor_add "生图能力" "WARN" "无 mavis CLI（image 风格 skill 创建时不会自动生成预览图）" "装 Mavis / Mavis 桌面端"
      return
    fi
    mavis_cmd="mavis"
  fi

  # 2. mavis mcp ls 看 matrix 注册没
  local mcp_ls_out
  mcp_ls_out=$("$mavis_cmd" mcp ls 2>/dev/null || true)
  if echo "$mcp_ls_out" | grep -q "matrix"; then
    # 3. 试调一个 matrix 工具，确认能用
    if "$mavis_cmd" mcp call matrix matrix_get_voice_list '{}' >/dev/null 2>&1; then
      doctor_add "生图能力" "OK" "matrix MCP 已注册 + 可用" ""
    else
      doctor_add "生图能力" "WARN" "matrix MCP 已注册但调用失败" "检查 mavis mcp call matrix 详情"
    fi
  else
    doctor_add "生图能力" "WARN" "matrix MCP 未注册（image 风格 skill 创建时不会自动生成预览图）" "mavis mcp add matrix ..."
  fi
}

check_jq() {
  if has_cmd jq; then
    local v
    v=$(jq --version 2>/dev/null | sed -E 's/jq-//')
    doctor_add "jq" "OK" "v$v" ""
  else
    doctor_add "jq" "OK" "未装（可选 — manifest 校验会降级到 Python）" "brew install jq（可选）"
  fi
}

# ===== 跑全部 + 输出 =====

run_doctor() {
  DOCTOR_RESULTS=()

  echo
  echo "${BOLD}🩺 pretty-skills doctor${RESET}  ${DIM}环境能力体检${RESET}"
  echo

  check_bash
  check_git
  check_curl
  check_python3
  check_gh
  check_local_bin_path
  check_image_gen
  check_jq

  # 统计
  local ok_count=0 warn_count=0 miss_count=0
  for r in "${DOCTOR_RESULTS[@]}"; do
    case "$r" in
      OK\|*)  ((ok_count++)) || true ;;
      WARN\|*) ((warn_count++)) || true ;;
      MISS\|*) ((miss_count++)) || true ;;
    esac
  done

  # 打印表格
  printf "  ${BOLD}%-18s  %-7s  %-50s${RESET}\n" "能力" "状态" "详情 / 怎么补"
  printf "  ${DIM}%-18s  %-7s  %-50s${RESET}\n" "──────────────────" "──────" "──────────────────────────────────────────"
  for r in "${DOCTOR_RESULTS[@]}"; do
    local status="${r%%|*}"
    local rest="${r#*|}"
    local name="${rest%%|*}"
    local detail_fix="${rest#*|}"
    local detail="${detail_fix%%|*}"
    local fix="${detail_fix#*|}"

    local icon color
    case "$status" in
      OK)   icon="✅"; color="$GREEN" ;;
      WARN) icon="⚠️ "; color="$YELLOW" ;;
      MISS) icon="❌"; color="$RED" ;;
    esac

    printf "  %-18s  ${color}%s${RESET}  %s\n" "$name" "$icon" "$detail"
    if [ -n "$fix" ]; then
      printf "  ${DIM}%-18s  %-7s  %s${RESET}\n" "" "" "→ $fix"
    fi
  done

  # 总结
  echo
  if [ "$miss_count" -gt 0 ]; then
    printf "  ${RED}${BOLD}❌ 关键能力缺失 (%d 项)${RESET}\n" "$miss_count"
    printf "  ${RED}   ps 核心功能跑不起来，请先补${RESET}\n"
  elif [ "$warn_count" -gt 0 ]; then
    printf "  ${YELLOW}${BOLD}⚠️  体验降级 (%d 项可选缺失)${RESET}\n" "$warn_count"
    printf "  ${YELLOW}   能跑但部分体验会缺，强烈建议补${RESET}\n"
  else
    printf "  ${GREEN}${BOLD}✅ 完整能力${RESET}\n"
    printf "  ${GREEN}   5 agent 全功能可用，包括 ps contribute 提 PR 和 image 风格生图${RESET}\n"
  fi
  echo

  return 0
}

# ===== 体验降级场景说明（被打 doctor.md / 错误时引用）=====

explain_degraded_experience() {
  cat <<EOF
${BOLD}📉 缺能力时体验会差在哪？${RESET}

${YELLOW}❌ 缺 git / curl${RESET}
   → ps add / ps update / 一键装脚本全部不能用
   → 装 pretty-skills 走手工 cp 流程

${YELLOW}❌ 缺 gh CLI${RESET}
   → ps contribute 不能用（提 PR 给主项目走不通）
   → 退路：手动 git fork + push + 用网页提 PR

${YELLOW}❌ 缺 gh auth（未登录 GitHub）${RESET}
   → ps contribute 会卡在 gh auth login 提示
   → 补：gh auth login

${YELLOW}❌ 缺 python3${RESET}
   → ps create 不能用（pretty-skills-creator 全部功能停摆）
   → 退路：手动用 4 风格 HTML 模板 + 提 PR

${YELLOW}❌ 缺 matrix MCP / mavis CLI${RESET}
   → 创建 image 风格 skill 时，封面/配图不会自动生图
   → 退路：手动用其他 AI 生图工具（Midjourney / 即梦），再回填图片 URL

${YELLOW}❌ ~/.local/bin 不在 PATH${RESET}
   → 装完 ps 命令找不到
   → 补：export PATH="\$HOME/.local/bin:\$PATH" 到 ~/.zshrc

EOF
}
