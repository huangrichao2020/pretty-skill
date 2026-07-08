# 仓库目录结构 · Structure Decision v3

> **TL;DR**：v3 结构 = **11 个中文领域一级目录** + **3F Content + 锦绣范式** + **skill-creator 自动化工具**。
>
> 一句话：**面向中文开发者 + 玩家 + 开发者PR共建** 的开源项目。

---

## ✅ v3 推荐结构

```
pretty-skill/
├── AI能力/                          ← 11 领域（中文一级目录）
│   ├── cartman-team-ai-agent-collab/
│   └── social-ecom-skill/
├── 编程开发/                        ← 全球开发者 PR 用
├── 数据科学/
├── 产品设计/
├── 商业运营/
├── 金融投资/
│   └── chokepoint-mainboard/
├── 内容创作/
├── 教育学习/
├── 游戏玩家/                        ← 玩家专属领域
├── 生活方式/
├── 思维方法/
│
├── _模板/                           ← case 模板
│   ├── 案例/                        ← 单 case 模板
│   └── 锦绣/                        ← 锦绣 PPT 模板
│
├── skill-creator/                   ← 🆕 自动化工具
│   ├── create.py                    ← 主脚本
│   ├── templates/                   ← 内部模板
│   └── README.md
│
├── content-triple-format/           ← 范式文档
│   ├── README.md
│   ├── 3F-content.md                ← 旧范式（保留）
│   ├── 锦绣.md                      ← 🆕 新范式
│   ├── check-3f.py                  ← PR 自动校验
│   ├── onboarding-guide.md
│   ├── before-after-example.md
│   ├── methodology.md
│   └── deep-themes.md               ← 视觉风格预设
│
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md     ← 11 领域下拉
│   └── workflows/check-3f.yml
│
├── README.md                        ← 项目总览（重写）
├── STRUCTURE.md (本文件)
├── CONTRIBUTING.md
├── FRIENDS-PR-GUIDE.md
├── PROMOTION.md
├── CONTRIBUTORS.md
├── LICENSE
└── roadmap.md
```

---

## 🎯 11 领域分类（v3 预设 · 开发者PR共建）

| # | 领域（一级目录）| 范围 |
|---|---|---|
| 1 | **AI能力** | LLM / Agent / 提示工程 / 机器学习 |
| 2 | **编程开发** | 通用编程 / 架构 / 模式 / 最佳实践 / 前后端 / 移动 |
| 3 | **数据科学** | 数据分析 / 可视化 / 统计 / BI / 量化研究 |
| 4 | **产品设计** | 产品方法论 / UX / UI / 用户研究 / 需求管理 |
| 5 | **商业运营** | 营销 / 增长 / 用户运营 / 商业模式 / 私域 |
| 6 | **金融投资** | A 股 / 港美股 / 加密货币 / 量化 / 财务规划 |
| 7 | **内容创作** | 视频 / 写作 / 直播 / 摄影 / 短视频 |
| 8 | **教育学习** | 学科教育 / 语言学习 / 知识管理 / 学习方法 |
| 9 | **游戏玩家** | 游戏攻略 / 角色养成 / 副本流程 / MOD 制作 / 二创 |
| 10 | **生活方式** | 健康 / 时间管理 / 关系 / 旅行 / 美食 / 家居 |
| 11 | **思维方法** | 决策框架 / 思维模型 / 心理学 / 认知科学 |

### 命名逻辑（为什么这么命名）

| 领域 | 命名理由 |
|---|---|
| AI能力（不是 AI培训）| 能力是双向的（既给 AI 学，又用人学 AI）|
| 编程开发（不是 开发）| 含"编程"= 强调实践 |
| 金融投资（不是 金融分析）| "投资"强调价值导向，"分析"偏方法论 |
| 内容创作（不是 创作）| "内容"强调输出形式（视频 / 文字 / 图片）|
| 思维方法（不是 认知）| "方法"更实用 = 学了能用 |
| 游戏玩家（不是 游戏）| "玩家"强调身份认同 = 这就是为玩家做的方法论 |

### 为什么是 11 个

- **认知心理学 7±2 极限的扩展版** = 覆盖广 + 不超载
- **全球开发者 PR 时能一眼选对领域** = 0 沟通成本
- **可扩展**：可以 PR 新领域（验证 + 审核）

---

## 🌟 "锦绣"概念（v3 首次提出）

> **锦绣（Jinxiu）= 把任何知识 / skill 在创建时就"绣"成易传播的视觉作品**

类比：原材料知识 → 刺绣工艺 → 锦（华丽展示品）

### 4 种形态

| 形态 | 用途 | 平台 |
|---|---|---|
| **锦绣封面** | 1 张 16:9 大图 | 朋友圈 / 推特 / 微博 |
| **锦绣 PPT** | 8-12 页完整讲解 | 小红书 / 公众号 / 知乎 / 演讲 |
| **锦绣网页版** | 移动友好 | 微信 / 推友 |
| **锦绣视频脚本** | 30-60 秒讲解 | 短视频平台（抖音 / 视频号 / B 站）|

### 1 次创作 = 1 套多平台素材

`skill-creator` 工具一键生成 4 种形态，开发者 / 玩家拿到就能传播。

### 完整规范

[content-triple-format/锦绣.md](./content-triple-format/锦绣.md)

---

## 📐 完整 case 内部结构

```
<领域>/<case>/
├── README.md                  ← case 说明（必填）
├── content.md                 ← 源文字（**必填** · 每页 4-7 字段）
├── web.html                   ← PPT 演示版（**必填** · 中央大图 + 键盘翻页 + 全屏 + 演讲者模式）
├── presentation.pptx          ← 真实 PowerPoint（**可选** · 仅二次编辑时生成 · 加 --with-pptx）
├── build_pptx.py              ← PPTX 生成脚本（推荐 · 可选时使用）
├── images/                    ← AI 出图原图（**必填** · ≥ 1 张/页）
│   ├── p0_cover.png
│   ├── p1_hook.png
│   └── ...
├── output/                    ← PPTX 输出（**可选** · ≥ 1 MB · 二次编辑时生成）
│   └── <case_name>.pptx
├── prompts/                   ← 出图 prompt（**必填** · 60 行/页）
│   ├── README.md
│   ├── p0_cover.md
│   └── ...
│
└── 锦绣/                      ← 🆕 锦绣素材（**必填** · v3.1 简化）
    ├── cover-横屏.png          # 1 张横屏封面（16:9）
    ├── cover-竖屏.png          # 1 张竖屏封面（3:4 或 9:16）
    ├── slides/                 # 8-12 张讲解图（16:9 · creator 自行决定）
    │   ├── slide-1.png
    │   ├── slide-2.png
    │   └── ...
    └── readme.md               # 1 份融合 md（公众号 + 自媒体稿 + AI 阅读）
```

---

## 🛠️ skill-creator 工具（v3 新增）

### 是什么

CLI 工具，把任意知识一键变成 pretty-skill 完整目录（3F Content + 锦绣）

### 输入

- 任意 `.md` 文件
- 任意 URL（博客 / 知乎 / 公众号）
- 视频脚本 / 笔记 / 你脑子里想的

### 输出

- 完整 skill 目录：`content.md` + `images/` + `presentation.pptx` + `web.html` + **锦绣 PPT**
- 多平台素材：朋友圈 1 图 + 小红书 9 图 + 公众号 12 页 + 视频脚本

### 安装 + 使用

```bash
# 未来
pip install pretty-skill
pretty-skill create --input my-knowledge.md --domain "金融投资"
```

完整使用：[skill-creator/README.md](./skill-creator/README.md)

---

## 🛠️ 现有 case 迁移路径

### 新 case（用 v3 结构）

```bash
# 1. 复制模板
cp -r _模板/案例 "<11 领域之一>/<你的-case-名>"

# 2. 编辑文件
cd "<11 领域之一>/<你的-case-名>"
# 改 content.md / build_pptx.py / web.html ...

# 3. 跑 check-3f.py 验证
python content-triple-format/check-3f.py "<领域>/<case>"

# 4. 提 PR
git add "<领域>/<case>"
git commit -m "feat(<领域>): add <case> case (3F Content + 锦绣)"
git push
```

### 改路径 / 改领域

直接 `git mv` + 改 README 跨引用 + 改 PR 模板里的"所属领域"段。

---

## 📂 各路径约定

| 路径 | 用途 | 谁应该写 |
|---|---|---|
| `<11 领域之一>/` | **case 主目录**（领域）| 全球开发者 / 玩家（PR） |
| `<领域>/<case>/` | **case 目录** | 全球开发者（PR 改这个）|
| `<领域>/<case>/锦绣/` | **锦绣 PPT** | skill-creator 自动生成 |
| `_模板/案例/` | **case 模板** | 仓库主（不要 PR 改）|
| `_模板/锦绣/` | **锦绣 PPT 模板** | 仓库主 |
| `skill-creator/` | **自动化工具** | 仓库主 + 社区贡献 |
| `content-triple-format/` | **范式文档** | 仓库主（范式升级）|
| `.github/` | **CI/CD + PR 模板** | 仓库主 |

---

## 🚨 提 PR 时路径检查

**PR 提之前必查**：

```bash
# 1. 跑 check-3f.py（自动校验）
python content-triple-format/check-3f.py "<领域>/<case>"
# 退出码 0 = OK；1 = 失败 + 错误原因

# 2. 确认路径规范
ls "<领域>/<case>/"
# 应该有：content.md + web.html + images/ + output/<case_name>.pptx + prompts/ + 锦绣/

# 3. 确认领域是 11 预设之一 或 PR 新增
# PR 模板自动给 11 领域下拉
```

**PR 模板**（`.github/PULL_REQUEST_TEMPLATE.md`）会强制你声明：
- [ ] 我把 case 放在 11 领域之一
- [ ] 领域目录名是中文
- [ ] case 名是英文/中文 kebab-case
- [ ] 3 件套 + 锦绣全有
- [ ] check-3f.py 跑过 exit 0

---

## ➕ 新增领域 PR 流程

**全球开发者都可以 PR 新领域**（不只是仓库主预设）：

```bash
# 1. 创建新领域目录
mkdir -p 新领域名称/案例1

# 2. 新领域必须有 README
cat > 新领域名称/README.md <<EOF
# 新领域名称
> 这个领域是什么
> 至少 1 个 case 验证
EOF

# 3. 至少有 1 个 case（否则不接受空领域）

# 4. 提 PR
git add 新领域名称/
git commit -m "feat(领域): add 新领域 + 案例1"
```

**仓库主审核标准**：
- 新领域有清晰定义（不和 11 预设重叠）
- 至少有 1 个高质量 case
- 命名规范（中文 / 2-6 汉字 / 不加 / / 不加前缀）

---

## 🗓️ 历史时间线

| 时间 | 结构 | 备注 |
|---|---|---|
| 2026-07-07 v0 | `domains/ai-training/<case>/` | 仓库主首次公开 |
| 2026-07-08 v1 | `cases/<case>/`（英文扁平）| @Kun PR #1 临时结构 |
| 2026-07-08 v1.1 | `<中文领域>/<case>/`（金融分析 + AI培训）| 用户纠正"面向中文开发者" |
| 2026-07-08 v2 | `<中文领域>/<case>/`（2 领域）| STRUCTURE.md 决策文档化 |
| 2026-07-08 **v3** ✨ | **11 领域 + 锦绣 + skill-creator + 全球开源** | **本次跃迁** |

---

## 💯 设计原则

> **目录结构必须尊重用户语言/文化偏好 + 工具/范式必须服务真实需求。**
> 中文项目 = 中文目录 = 中文体验。
> 范式 = AI 友好（3F Content）+ 人易传播（锦绣）。
> 工具 = skill-creator（让贡献和创建一样简单）。
> 任何"推荐结构"前必问"目标用户语言"和"命名习惯"。

---

参考：
- [README.md](./README.md) · 项目总览
- [CONTRIBUTING.md](./CONTRIBUTING.md) · 完整贡献指南
- [FRIENDS-PR-GUIDE.md](./FRIENDS-PR-GUIDE.md) · 5 分钟 PR 流程
- [content-triple-format/README.md](./content-triple-format/README.md) · 3F Content 范式
- [content-triple-format/锦绣.md](./content-triple-format/锦绣.md) · 锦绣范式
- [skill-creator/README.md](./skill-creator/README.md) · skill-creator 工具
- [roadmap.md](./roadmap.md) · 仓库路线图