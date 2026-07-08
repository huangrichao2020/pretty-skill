# 朋友 PR 指南 · 5 分钟贡献流程

> **目标**：让你不需要仓库主的 GitHub token，也能给 pretty-skill 提 PR。
> **核心理念**：PR 流程应该**去 token 化** —— 任何人 fork 仓库就能贡献。

---

## ⚠️ 重要：你不需要仓库主的 token

之前朋友拿 token 提 PR = **token 共享反模式**：

- ❌ 仓库主 token 离开本机 = 安全风险（token 可能在第三方设备被记录 / 截屏 / 泄露）
- ❌ 一旦 token 泄露 = 攻击者可读写整个 GitHub 账号
- ✅ **正确做法**：每个贡献者用自己的 GitHub 账号 fork + 提 PR

这个仓库已经设了 GitHub Actions 校验脚本（`.github/workflows/check-3f.yml`），你提 PR 后系统会自动跑校验。**完全不需要主仓库 token**。

---

## 5 分钟标准流程

### Step 1 · Fork 仓库（一次性 · 用你自己 GitHub 账号）

1. 打开 https://github.com/huangrichao2020/pretty-skill
2. 点右上角 **Fork** 按钮 → 选你的 GitHub 账号
3. 完成后你有了 `https://github.com/<你的用户名>/pretty-skill`

### Step 2 · Clone 你自己的 fork 到本机

```bash
git clone https://github.com/<你的用户名>/pretty-skill.git
cd pretty-skill
```

### Step 3 · 加主仓库为 upstream（拉最新用）

```bash
git remote add upstream https://github.com/huangrichao2020/pretty-skill.git
git fetch upstream
git checkout main
git merge upstream/main
```

### Step 4 · 创建新 case

```bash
# 复制模板
cp -r domains/_template/case domains/<领域>/<你的-case-名称>

# 编辑文件
cd domains/<领域>/<你的-case-名称>
# 1. 改 content.md（用你的真实内容，每页 4-7 字段）
# 2. 改 README.md
# 3. 准备 images/（用 matrix / DALL-E / Midjourney 出 N 张图）
# 4. 生成 presentation.pptx（用 python-pptx add_picture 嵌图）
# 5. 生成 web.html（用 html-ppt-viewer 嵌图）
```

完整 onboarding：[content-triple-format/onboarding-guide.md](./content-triple-format/onboarding-guide.md)

### Step 5 · 本地校验（必跑）

```bash
# PR 提交前必跑这一行（GitHub Actions 也会跑，但本地先跑发现问题更快）
python3 content-triple-format/check-3f.py domains/<领域>/<你的-case-名称>

# 退出码：
#   0 = 全部通过（可提 PR）
#   1 = 有检查项失败（按错误提示修复）
```

### Step 6 · Commit + Push 到你的 fork

```bash
git add domains/<领域>/<你的-case-名称>
git commit -m "feat(<领域>): add <你的-case-名称> case (3F Content)"
git push origin main
```

### Step 7 · 在 GitHub 网页开 PR

1. 访问 https://github.com/<你的用户名>/pretty-skill
2. 看到 **"Compare & pull request"** 按钮 → 点
3. 选 base = `huangrichao2020/pretty-skill:main`，compare = `<你的用户名>/pretty-skill:main`
4. 填 PR 模板（自动填充）
5. 点 **Create pull request**

**PR 提完后**：
- GitHub Actions 自动跑 `check-3f.py` → 30 秒出结果
- 如果 ❌ 失败 → 看 GitHub Actions 日志修复
- 如果 ✅ 通过 → 等仓库主 review

---

## 🚨 如果你之前用仓库主的 token 提过 PR

**立刻做的事**：

1. **告诉仓库主 rotate token**（删除旧 token + 生成新 token）
   - 仓库主路径：https://github.com/settings/tokens
   - 找到泄露的 PAT → 点 **Revoke** → 删掉
   - 生成新 PAT（如果还需要）

2. **你之前的 PR 不会失效**（PR 是基于代码 diff，不依赖 token 权限）

3. **之后按本指南用你自己的 GitHub 账号操作**

---

## ❓ 常见问题

### Q: 我没有 GitHub 账号怎么办？

去 https://github.com/signup 注册一个（免费，5 分钟）。

### Q: 我不熟悉 git 命令怎么办？

装 GitHub Desktop（https://desktop.github.com）—— 图形界面 fork + commit + PR 都点点鼠标就行。

### Q: 我不会用 python-pptx 生成 PPT？

看 [onboarding-guide.md](./content-triple-format/onboarding-guide.md) Step 4 的代码示例，复制粘贴改改路径即可。

### Q: 我没装 matrix MCP 出图怎么办？

随便用 DALL-E / Midjourney / Stable Diffusion / 即梦 / 文心一言 **任何一个 AI 出图工具**都行。只要最后把 PNG 图放到 `images/` 目录 + 用 `add_picture()` 嵌入 PPTX。

### Q: PR 失败被 check-3f 拒绝了怎么办？

读 Actions 日志，会告诉你是哪项检查失败。常见 3 种：
- `.pptx` < 1 MB → 用 `add_picture()` 嵌图（不是 text_frame 铺文字）
- `.html` 不含 `<img>` → 用图嵌进 HTML（不是 .md 转 HTML）
- `images/` 缺失 → 调 AI 出图 API 把 PNG 放进去

---

## ✅ 你贡献后拿到什么

| 你做了什么 | 你拿到什么 |
|---|---|
| Fork + 提 PR | GitHub 个人页 + 1 个「贡献者」标记 |
| 你的 case 被合并 | pretty-skill 仓库 README 收录你的名字 |
| 贡献了 3F Content | 任何 AI 工具都能消化你的 PPT（自动化的未来资产） |
| 教了 1 个 agent 不偷懒 | 真实帮助中文 AI 友好内容生态 |

---

**记住**：你**永远不需要**仓库主的 token。GitHub 的 PR 流程本来就设计成"分布式协作"—— fork + PR 是 GitHub 的核心约定，**比任何 token 共享方案都安全**。

---

参考：
- [CONTRIBUTING.md](./CONTRIBUTING.md) —— 完整贡献指南
- [content-triple-format/onboarding-guide.md](./content-triple-format/onboarding-guide.md) —— 5 步标准流程
- [content-triple-format/check-3f.py](./content-triple-format/check-3f.py) —— PR 自动校验脚本
- [GitHub 官方 Fork 文档](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks)