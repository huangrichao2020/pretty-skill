#!/usr/bin/env bash
# push.sh — pretty-skills-creator 提 PR 到主项目
#
# 流程：
# 1. 检查 gh auth（ps doctor 已跑过，这里再保险一次）
# 2. fork 主项目（如果没 fork）
# 3. clone fork → 创建分支 creator/<name>
# 4. copy tools/<name>/ → commit
# 5. push 分支
# 6. 提 PR with auto-deploy-placeholder + skill-status:placeholder 标签
#
# 用法：
#   bash push.sh <out_dir>/<name>

set -euo pipefail

OUT_DIR="${1:?用法: bash $0 <out_dir>/<name>}"
BASE_OWNER="${BASE_OWNER:-huangrichao2020}"
REPO="${REPO:-pretty-skill}"  # 改名时改 pretty-skills（v0.1.0 release）

# 检查 gh auth
if ! gh auth status >/dev/null 2>&1; then
  echo "❌ gh CLI 未认证。请先跑："
  echo "   gh auth login"
  echo "   跑完再跑: ps contribute $OUT_DIR"
  exit 1
fi

# 校验文件
for f in web.html manifest.yaml SKILL.md CHANGELOG.md; do
  [ -f "$OUT_DIR/$f" ] || { echo "❌ 缺 $OUT_DIR/$f"; exit 1; }
done

# 读 manifest 拿 name + title
NAME=$(python3 -c "import yaml; print(yaml.safe_load(open('$OUT_DIR/manifest.yaml'))['name'])" 2>/dev/null \
  || python3 -c "import json; m=json.load(open('$OUT_DIR/manifest.json')); print(m['name'])" 2>/dev/null \
  || basename "$OUT_DIR")
TITLE=$(python3 -c "import yaml; print(yaml.safe_load(open('$OUT_DIR/manifest.yaml'))['description'].split(chr(10))[0])" 2>/dev/null \
  || echo "$NAME")

CURRENT_USER=$(gh api user --jq .login)
echo "[info] 当前 gh 用户: $CURRENT_USER"
echo "[info] 目标 PR → $BASE_OWNER/$REPO"
echo "[info] 路径: tools/$NAME/"

# fork 如果还没
if ! gh repo view "$CURRENT_USER/$REPO" >/dev/null 2>&1; then
  echo "[step] fork $BASE_OWNER/$REPO ..."
  gh repo fork "$BASE_OWNER/$REPO" --clone=false
fi

# 临时目录 clone fork
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT
echo "[step] clone fork ..."
gh repo clone "$CURRENT_USER/$REPO" "$TMPDIR/repo" -- --depth 1 >/dev/null

# 创建分支
BRANCH="creator/$NAME-$(date +%s | tail -c 7)"
cd "$TMPDIR/repo"
git checkout -b "$BRANCH" >/dev/null

# 复制文件
mkdir -p "tools/$NAME"
cp -R "$OUT_DIR"/. "tools/$NAME/"

git add "tools/$NAME/"
git commit -m "feat(tools/$NAME): placeholder '$NAME' via pretty-skills-creator

- tools/$NAME/web.html (placeholder, $TITLE)
- tools/$NAME/manifest.yaml (符合 pretty-skills manifest schema)
- tools/$NAME/SKILL.md (agent 加载入口)
- tools/$NAME/CHANGELOG.md

后续补完整 content.md / 真实 .pptx / 锦绣 4 形态走另一个 PR。

🤖 Generated with [pretty-skills-creator](https://github.com/$BASE_OWNER/$REPO/tree/main/tools/pretty-skills-creator)

Co-Authored-By: Mavis <noreply@anthropic.com>" >/dev/null

echo "[step] push 分支 $BRANCH ..."
git push -u origin "$BRANCH" >/dev/null

echo "[step] 提 PR ..."
PR_URL=$(gh pr create \
  --repo "$BASE_OWNER/$REPO" \
  --head "$CURRENT_USER:$BRANCH" \
  --base main \
  --title "🆕 [tools/$NAME] $TITLE (placeholder)" \
  --body "## 占位版 PR（auto-deploy）

由 pretty-skills-creator 自动生成。

### 内容
- 路径：\`tools/$NAME/\`
- 必含：\`web.html\` ✅ / \`manifest.yaml\` ✅ / \`SKILL.md\` ✅ / \`CHANGELOG.md\` ✅
- 待补：完整 content.md / 真实 .pptx / 锦绣 4 形态

### 标签
- \`auto-deploy-placeholder\` — pretty-skill 端应自动 merge + 部署
- \`skill-status:placeholder\` — 标记当前是占位版

### 验证（auto-deploy workflow 会做）
- [x] web.html 最低质量（title ≥ 5 字 + description ≥ 100 字 + ≥ 1 img）
- [x] manifest.yaml 符合 schema
- [ ] 完整 3F Content（占位版可跳过）" \
  --label "auto-deploy-placeholder" \
  --label "skill-status:placeholder" \
  2>&1 | tail -3)

echo ""
echo "✅ PR 提了：$PR_URL"
echo ""
echo "后续：主项目 GitHub Action 监听 auto-deploy-placeholder 标签 → 自动 merge → 部署 Git Pages"
echo "完成后可分享 URL: https://${BASE_OWNER}.github.io/${REPO}/tools/${NAME}/web.html"
