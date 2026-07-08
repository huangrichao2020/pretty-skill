# 贡献指南 · pretty-skill v3

> **欢迎全球开发者 / 玩家贡献 skill 或知识！**
> pretty-skill 是一个**开源项目** —— 集合全世界优质技能与知识，按 **3F Content + 锦绣** 范式发布，让任何知识都能被 AI 消化 + 给人传播。

---

## 💡 为什么贡献

1. **你的知识永久价值化** —— 一份 `.md` + 1 套多平台素材 = 全网共享
2. **AI 友好** —— LLM 能直接消化你的内容（不像 PDF / Word）
3. **人易传播** —— 锦绣 PPT 让分享到朋友圈 / 小红书有视觉冲击
4. **全球共享** —— 仓库公开 = 任何人都能 fork / 复刻 / 翻译
5. **社区贡献者** —— 自动加入 [CONTRIBUTORS.md](./CONTRIBUTORS.md) 榜

---

## 🎯 贡献什么

| 类型 | 例子 | 领域 |
|---|---|---|
| **方法论** | 决策框架 / 思考模型 / 最佳实践 | 思维方法 / 编程开发 / 产品设计 |
| **案例分析** | 真实项目复盘 / 案例拆解 | 商业运营 / 金融投资 / 数据科学 |
| **技能教程** | 工具使用 / 编程技巧 / 制作流程 | 编程开发 / 内容创作 / 游戏玩家 |
| **知识沉淀** | 学科总结 / 概念解释 / 历史复盘 | 教育学习 / 思维方法 / 生活方式 |
| **攻略 / 指南** | 游戏攻略 / 旅行指南 / 工具评测 | 游戏玩家 / 生活方式 / 内容创作 |
| **可视化** | 信息图 / 数据可视化 / 思维导图 | 数据科学 / 思维方法 / 编程开发 |

---

## 🚀 5 分钟贡献流程

### Step 1 · Fork 仓库（一次性 · 用你 GitHub 账号）

1. 打开 https://github.com/huangrichao2020/pretty-skill
2. 点右上角 **Fork** 按钮 → 选你的 GitHub 账号
3. 完成后你有了 `https://github.com/<你的用户名>/pretty-skill`

### Step 2 · Clone 你的 fork

```bash
git clone https://github.com/<你的用户名>/pretty-skill.git
cd pretty-skill
```

### Step 3 · 加主仓库为 upstream

```bash
git remote add upstream https://github.com/huangrichao2020/pretty-skill.git
git fetch upstream
git checkout main
git merge upstream/main
```

### Step 4 · 创建新 case

```bash
# 1. 复制模板
cp -r _模板/案例 "<11 领域之一>/<你的-case-名>"

# 2. 编辑文件
cd "<11 领域之一>/<你的-case-名>"
# - 改 content.md（用你的真实内容，每页 4-7 字段）
# - 改 README.md（用例说明）
# - 准备 images/（用 matrix / DALL-E / Midjourney 出 N 张图）
# - 跑 build_pptx.py 生成 output/<case_name>.pptx
# - 改 web.html（用 html-ppt-viewer 模板）
# - 生成 锦绣/（4 形态：cover + 9图 + PPT + 视频脚本）
```

**推荐用 skill-creator 自动化**（未来 v3.1）：

```bash
pip install pretty-skill
pretty-skill create --input my-knowledge.md --domain "金融投资" --style "深色科技风"
# 自动生成 content.md + images/ + presentation.pptx + web.html + 锦绣 4 形态
```

完整 onboarding：[content-triple-format/onboarding-guide.md](./content-triple-format/onboarding-guide.md)

### Step 5 · 本地校验（必跑 · 退出码 0 才能提）

```bash
# 校验 3F Content + 锦绣层
python content-triple-format/check-3f.py "<11 领域>/<你的-case-名>"

# 退出码：
#   0 = 全部通过（PR 可提）
#   1 = 有检查项失败（按错误提示修复）
```

### Step 6 · Commit + Push 到你的 fork

```bash
git add "<11 领域>/<你的-case-名>"
git commit -m "feat(<11 领域>): add <你的-case-名> case (3F Content + 锦绣)"
git push origin main
```

### Step 7 · 在 GitHub 网页开 PR

1. 访问 https://github.com/<你的用户名>/pretty-skill
2. 点 **"Compare & pull request"** 按钮
3. 选 base = `huangrichao2020/pretty-skill:main`，compare = `<你的用户名>/pretty-skill:main`
4. 填 PR 模板（11 领域下拉 + 3 件套 + 锦绣 全选）
5. 点 **Create pull request**

**PR 提完后**：
- GitHub Actions 自动跑 `check-3f.py` + 锦绣层校验 → 30 秒出结果
- 如果 ❌ 失败 → 看 GitHub Actions 日志修复
- 如果 ✅ 通过 → 等仓库主 review

---

## 🌟 想新增 1 个领域？（v3 全球共建核心）

**全球开发者都可以 PR 新领域**（不只是仓库主预设）：

```bash
# 1. 创建新领域目录
mkdir -p "新领域名称/案例1"

# 2. 新领域必须有 README
cat > "新领域名称/README.md" <<EOF
# 新领域名称

> 这个领域是什么 / 范围 / 适用人群
> 至少有 1 个 case 验证
EOF

# 3. 至少有 1 个 case（否则不接受空领域）
cp -r _模板/案例 "新领域名称/案例1"
cd "新领域名称/案例1"
# 改 content + 出图 + 跑 check ...

# 4. 提 PR
git add "新领域名称/"
git commit -m "feat: add 新领域名称 + 案例1"
```

**仓库主审核标准**：
- ✅ 新领域有清晰定义（不和 11 预设重叠）
- ✅ 至少有 1 个高质量 case
- ✅ 命名规范（中文 / 2-6 汉字 / 不加 / / 不加前缀）
- ✅ content.md 字段齐全
- ✅ 锦绣 4 形态齐全

---

## 🛠️ 11 领域（v3 预设 · 完整列表）

| 领域 | 范围 |
|---|---|
| **AI能力** | LLM / Agent / 提示工程 / 机器学习 |
| **编程开发** | 通用编程 / 架构 / 模式 / 最佳实践 / 前后端 |
| **数据科学** | 数据分析 / 可视化 / 统计 / BI |
| **产品设计** | 产品方法论 / UX / UI / 用户研究 |
| **商业运营** | 营销 / 增长 / 用户运营 / 商业模式 |
| **金融投资** | A 股 / 港美股 / 加密货币 / 量化 |
| **内容创作** | 视频 / 写作 / 直播 / 摄影 |
| **教育学习** | 学科教育 / 语言学习 / 知识管理 |
| **游戏玩家** | 游戏攻略 / 角色养成 / 副本流程 / MOD |
| **生活方式** | 健康 / 时间管理 / 关系 / 旅行 |
| **思维方法** | 决策框架 / 思维模型 / 心理学 |

---

## ✅ 4 条硬规则

1. **3 件套齐全**（content.md + presentation.pptx + web.html）—— 不收不齐的 PR
2. **锦绣 3 样齐全**（横屏封面 + 竖屏封面 + 8-12 讲解图 + 1 融合 md）—— v3.1 简化要求
3. **`.md` 为单一真相** —— `.pptx` / `.html` / `锦绣` 内文以 `.md` 为准
4. **作者署名** —— `content.md` 顶部加作者 / 来源 / 日期

## 🚫 5 个反模式（PR 100% 退回）

1. ❌ 直接拿 `.md` 转 `.pptx`（文字 PPT）→ 必须 `add_picture()` 嵌图
2. ❌ 直接用 `.md` 转 `.html`（纯文字网页）→ 必须含 `<img>` 标签
3. ❌ 跳过 AI 出图步骤 → 必须有 `images/` + N 张 PNG
4. ❌ 跳过锦绣 3 样 → 必须有 `锦绣/cover-横屏.png` + `cover-竖屏.png` + `slides/`（8-12 张）+ `readme.md`
5. ❌ case 名称用大写 / 下划线 / 空格 → 必须 kebab-case（英文）或 kebab-case（中文）

---

## ❓ 常见问题

### Q: 我没装 matrix MCP 出图怎么办？

随便用 DALL-E / Midjourney / Stable Diffusion / 即梦 / 文心一言 **任何一个 AI 出图工具**都行。只要最后把 PNG 图放到 `images/` 目录 + 用 `add_picture()` 嵌入 PPTX。

### Q: 我不会用 python-pptx 生成 PPT？

看 [content-triple-format/onboarding-guide.md](./content-triple-format/onboarding-guide.md) Step 4 的代码示例，复制粘贴改改路径即可。

### Q: 锦绣 3 样素材怎么生成？

v3.1 推荐用 skill-creator 工具（即将开源）。手动方式：
1. 准备 **1 张横屏封面**（16:9）+ **1 张竖屏封面**（3:4 或 9:16）+ **8-12 张讲解图**（16:9）+ **1 份融合 md**
2. 按 [content-triple-format/锦绣.md](./content-triple-format/锦绣.md) v3.1 范式排版

### Q: 锦绣要发哪个平台？

**不限定**。creator 拿到素材后自己决定发朋友圈 / 小红书 / 抖音 / 推特 / 微博 / 公众号 / 视频号 / 任何平台。范式只规定"形式"（横/竖/讲解图/md），不规定"平台"。

### Q: PR 失败被 check-3f 拒绝了怎么办？

读 Actions 日志，会告诉你是哪项检查失败。常见：
- `.pptx` < 1 MB → 用 `add_picture()` 嵌图
- `.html` 不含 `<img>` → 用图嵌进 HTML
- `images/` 缺失 → 调 AI 出图 API 把 PNG 放进去
- `锦绣/` 不全 → 按 [锦绣.md](./content-triple-format/锦绣.md) 4 形态补齐

### Q: 中英文 case 名哪个好？

都可以。**英文** (`chokepoint-mainboard`) 更适合 GitHub 搜索；**中文** (`小红书爆款拆解`) 更直观。

### Q: 我贡献的内容会被 AI 训练用吗？

不会被直接训练用。但任何 AI agent 可以消费你的 `.md` 内容（这是 3F Content 的核心价值）。这和 Wikipedia 类似。

### Q: 我是新领域，怎么提 PR？

见上方"🌟 想新增 1 个领域？"段。

---

## 🎯 贡献者福利

- ✅ 你的 GitHub 个人页 + 「pretty-skill 贡献者」标记
- ✅ 每个贡献的 case 永久收录
- ✅ 中文 / 全球 圈的人脉 + 影响力
- ✅ 优先收录你的自媒体内容（按规范审核）
- ✅ 仓库主 1v1 review 反馈（让你下次写得更好）

---

## 📞 任何问题

- 提 Issue
- 或在 PR 评论里讨论

我们优先回复 —— 这是中文圈第一个按 **3F Content + 锦绣** 范式做的开源项目，欢迎全球贡献者共建。

---

参考：
- [README.md](./README.md) · 项目总览
- [STRUCTURE.md](./STRUCTURE.md) · 11 领域结构
- [FRIENDS-PR-GUIDE.md](./FRIENDS-PR-GUIDE.md) · 5 分钟 PR 流程
- [content-triple-format/README.md](./content-triple-format/README.md) · 3F Content 范式
- [content-triple-format/锦绣.md](./content-triple-format/锦绣.md) · 锦绣范式
- [skill-creator/README.md](./skill-creator/README.md) · 自动化工具
- [roadmap.md](./roadmap.md) · 仓库路线图