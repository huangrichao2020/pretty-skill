# 5 分钟 PR 流程 · pretty-skill v3

> **💎 再定义**：pretty-skill 是 **agent 的「知识工程中枢」** —— **不是**传统 `SKILL.md` 技能仓。
> **这里不是工具箱，是出版局。**

> 给任何开发者 / 玩家看的最简版贡献指南。5 分钟完成 PR。

> **⚠️ 前置条件 · 生图能力是必须的** —— 所有视觉化都靠 AI 出图。
> 推荐 **MiniMax 套餐**，**49 元 Token plan 套餐**就够（matrix MCP 多模态生图 + 生视频）。

---

## 1 分钟选领域

打开 https://github.com/huangrichao2020/pretty-skill/tree/main 看 11 个一级目录，选一个对你的内容最合适的：

```
AI能力/    编程开发/   数据科学/   产品设计/
商业运营/  金融投资/   内容创作/   教育学习/
游戏玩家/  生活方式/   思维方法/
```

**没合适的？** 提 PR 新增（附 README + 至少 1 个 case）。

---

## 4 分钟动手

```bash
# 1. Fork + clone
gh repo fork huangrichao2020/pretty-skill --clone
cd pretty-skill

# 2. 加 upstream
git remote add upstream https://github.com/huangrichao2020/pretty-skill.git
git fetch upstream && git merge upstream/main

# 3. 复制模板
cp -r _模板/案例 "<11 领域之一>/<你的-case-名>"
cd "<11 领域之一>/<你的-case-名>"

# 4. 改 4 个核心文件
# - content.md（4-7 字段/页 · 必填）
# - README.md（case 说明 · 必填）
# - images/（AI 出图 N 张 · 必填）
# - output/<case_name>.pptx（≥ 1 MB · 必填）

# 5. 跑校验
python ../../content-triple-format/check-3f.py .
# 退出码 0 = 通过

# 6. commit + push
git add . && git commit -m "feat(<领域>): add <你的-case-名>"
git push origin main

# 7. 在 GitHub 网页开 PR
gh pr create --web
```

---

## 30 秒看反馈

- ✅ GitHub Actions 跑过 → 等仓库主 review
- ❌ GitHub Actions 失败 → 看 Actions 日志，按 check-3f.py 错误提示修

---

## 必填清单

提交前必查：

```
□ 领域是 11 预设之一 或 PR 新增
□ content.md 每页 4-7 字段
□ presentation.pptx ≥ 1 MB（嵌图）
□ web.html 含 <img> 标签
□ images/ 有 N 张 PNG
□ prompts/ 有 N 个 prompt 文件
□ 锦绣/cover-朋友圈.png
□ 锦绣/xiaohongshu-9图/ 9 张图
□ 锦绣/public-account-ppt/ 12 页 PPT
□ 锦绣/video-script.md
□ check-3f.py 跑过 exit 0
□ 中文无错字
□ 数字 / 时间 / 百分比 ≥ 1 个
□ 金句 ≥ 1 句
```

任何一项 ✗ = 退回。

---

## ❓ 常见 Q

**Q: 我不会用 python-pptx？**
A: 复制 `build_pptx.py` 模板改图片路径。完整示例见 [onboarding-guide.md](./content-triple-format/onboarding-guide.md) Step 4。

**Q: AI 出图用什么工具？**
A: 随便。matrix / DALL-E / Midjourney / 即梦 / 文心一言都行。最后是 PNG 文件 + 嵌进 PPTX。

**Q: 锦绣 PPT 怎么生成？**
A: v3 推荐用 skill-creator 工具（即将开源）。手动：准备 9 张图 + 12 页 PPT + 1 张大图 + 视频脚本。

**Q: 我贡献了会被 AI 训练用吗？**
A: 不会被训练用。但 AI agent 可以消费你的 `.md`（这是 3F Content 的核心价值，类似 Wikipedia）。

**Q: 我的英文 / 中文都不太好？**
A: 用中文就好，仓库主都懂。

---

参考：
- [CONTRIBUTING.md](./CONTRIBUTING.md) · 完整版
- [STRUCTURE.md](./STRUCTURE.md) · 11 领域
- [content-triple-format/README.md](./content-triple-format/README.md) · 3F Content
- [content-triple-format/锦绣.md](./content-triple-format/锦绣.md) · 锦绣范式