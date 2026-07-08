# 仓库目录结构 · Structure Decision

> **TL;DR**：**新结构用中文领域一级目录 = `<领域>/<case>/`**。
>
> 理由一句话：**面向中文开发者，目录名就该用中文**。打开 GitHub 看到 `金融分析/chokepoint-mainboard/` 一眼就知道这是金融类 case。

---

## ✅ 推荐结构 · 中文领域一级目录（v2 起的所有新 case）

```
pretty-skill/
├── AI培训/                      ← 中文领域（一级）
│   ├── cartman-team-ai-agent-collab/  ← case（case 名可英文/中文）
│   └── social-ecom-skill/
├── 金融分析/                    ← 中文领域（一级）
│   └── chokepoint-mainboard/
├── 教育/                        ← 占位（未来扩展）
│   └── (空)
├── _模板/                      ← 案例模板
│   └── 案例/
├── content-triple-format/      ← 范式文档
├── .github/                    ← CI/CD + PR 模板
├── README.md
├── STRUCTURE.md (本文件)
└── ...
```

**为什么用中文领域目录**：

1. **面向中文开发者**：仓库主明确说"面向中文开发者"——目录名用中文是基本盘
2. **一眼懂**：打开 `金融分析/` 不用想"这是干啥的"，直接进
3. **GitHub / 终端 / IDE 全兼容**：现代系统都支持 UTF-8 路径，没有兼容性问题
4. **跨领域对比直观**：`AI培训/ vs 金融分析/ vs 教育/` 直接列，扁平 2 层
5. **case 名可灵活**：case 内部名 `cartman-team-ai-agent-collab` / `chokepoint-mainboard` 可以英文（方便搜索 + GitHub 友好），**只有领域目录必须中文**

---

## ❌ Deprecated 结构

### 1. `domains/<area>/<case>/`（v0 旧结构，2026-07-07 用过）

```
domains/
├── ai-training/                  ← 英文
│   ├── cartman-team-ai-agent-collab/
│   └── social-ecom-skill/
└── financial-analysis/          ← 英文
    └── chokepoint-mainboard/
```

**为什么 deprecated**：
- ❌ 英文目录名对中文用户不友好
- ❌ 路径长 3 层
- ❌ 领域是英文，与仓库"面向中文开发者"定位不符

**v2 迁移**：2026-07-08 已经全部迁到中文结构（`AI培训/`、`金融分析/`），`domains/` 目录已删。

### 2. `cases/<case>/`（v1 临时结构，2026-07-08 短暂用过）

```
cases/
└── chokepoint-mainboard/
```

**为什么 deprecated**：
- ❌ 抹掉了"领域"分类信息
- ❌ 所有 case 混在一起，跨领域对比难
- ❌ 我（mavis）之前推这个结构没尊重用户"中文领域一级目录"的需求——已纠正

**v2 迁移**：`cases/chokepoint-mainboard/` → `金融分析/chokepoint-mainboard/`，`cases/` 目录已删。

---

## 📐 v2 结构约定

### 一级目录（领域）—— 100% 中文

| 目录 | 状态 | 说明 |
|---|---|---|
| `AI培训/` | 已有 case | 第 1 个领域，2 个 v0 seed cases |
| `金融分析/` | 已有 case | 第 2 个领域，1 个 case（@Kun 卡脖子选股） |
| `教育/` | 空目录（占位）| 未来扩展 |
| `_模板/` | 模板 | case 模板，非领域 |

**领域命名规范**：
- ✅ 2-6 个汉字：`AI培训` / `金融分析` / `教育` / `产品设计` / `运营增长` / `技术研发`
- ❌ 不加 `/`：用 `金融分析` 不用 `金融/分析`
- ❌ 不加前缀：用 `金融分析` 不用 `领域-金融分析`
- ❌ 不用拼音：用 `金融分析` 不用 `jinrongfenxi`

### 二级目录（case）—— 英文/中文都可

| 推荐 | 例子 |
|---|---|
| ✅ 英文 kebab-case | `chokepoint-mainboard` / `cartman-team-ai-agent-collab` |
| ✅ 中文 kebab-case | `小红书爆款拆解` / `抖音起号方法论` |
| ❌ 大写字母 | `CHOKEPOINT` |
| ❌ 下划线 | `chokepoint_mainboard`（grep 不友好） |
| ❌ 空格 | `chokepoint mainboard`（URL 编码会乱） |

### Case 内部结构

```
<领域>/<case>/
├── README.md              ← case 说明（必填）
├── content.md             ← 源文字（必填，每页 4-7 字段）
├── build_pptx.py          ← PPTX 生成脚本（推荐）
├── web.html               ← 浏览器翻页版（必填，含 <img> 标签）
├── images/                ← AI 出图原图（必填，≥ 1 张/页）
│   ├── p0_cover.png
│   ├── p1_hook.png
│   └── ...
├── output/                ← PPTX 输出（必填，≥ 1 MB）
│   └── <case_name>.pptx
└── prompts/               ← 出图 prompt（推荐，60 行/页）
    ├── README.md
    ├── p0_cover.md
    └── ...
```

---

## 🛠️ 现有 case 迁移路径

### 新 case（用 v2 结构）

```bash
# 复制模板
cp -r _模板/案例 "中文领域/<你的-case>"

# 编辑
cd "中文领域/<你的-case>"
# 改 content.md / build_pptx.py / web.html ...
```

### 修改已存在的 case

直接改，不需要迁移。

---

## 📂 各路径约定（v2 终态）

| 路径 | 用途 | 谁应该写 |
|---|---|---|
| `<中文领域>/` | **新 case 主目录**（领域） | 所有贡献者（新 PR） |
| `<中文领域>/<case>/` | **case 目录** | 贡献者（PR 改这个） |
| `_模板/案例/` | **case 模板** | 仓库主（不要 PR 改这个） |
| `content-triple-format/` | **范式文档** | 仓库主（范式升级） |
| `.github/workflows/` | **CI/CD** | 仓库主 |
| `.github/PULL_REQUEST_TEMPLATE.md` | **PR 模板** | 仓库主 |
| `CONTRIBUTING.md` | **贡献指南** | 仓库主 |
| `FRIENDS-PR-GUIDE.md` | **5 分钟 PR 流程** | 仓库主 |
| `STRUCTURE.md` | **本文件 · 目录结构决策** | 仓库主 |

---

## 🚨 提 PR 时路径检查

**PR 提之前必查**：

```bash
# 1. 跑 check-3f.py（自动校验）
python content-triple-format/check-3f.py "<中文领域>/<你的-case>"
# 退出码 0 = OK；1 = 失败 + 错误原因

# 2. 确认路径规范
ls "<中文领域>/<你的-case>/"
# 应该有：content.md + web.html + images/ + output/<case_name>.pptx + prompts/
```

**PR 模板**（`.github/PULL_REQUEST_TEMPLATE.md`）会强制你声明：
- [ ] 我把 case 放在 `<中文领域>/<case>/`（推荐结构）
- [ ] 领域目录名是中文
- [ ] case 名是英文 kebab-case 或中文 kebab-case

---

## 🗓️ 历史时间线

| 时间 | 结构 | 备注 |
|---|---|---|
| 2026-07-07 v0 | `domains/ai-training/<case>/` | 仓库主首次公开时的结构 |
| 2026-07-08 v1.0 | `cases/<case>/`（尝试扁平）| @Kun 提 PR #1 时改用，但抹掉领域分类 |
| 2026-07-08 v1.1 | **`<中文领域>/<case>/`** | 用户纠正"面向中文开发者" → 改用中文领域一级目录 ✅ |
| v2（未来） | 可能按"内容形式"分类（PPT / 长图 / 视频脚本）| 暂未规划 |

---

## 💯 设计原则

> **目录结构必须尊重用户语言/文化偏好**。中文项目 = 中文目录 = 中文体验。
> 不要套用"通用最佳实践"（英文扁平）忽略用户实际需求。

---

参考：
- [CONTRIBUTING.md](./CONTRIBUTING.md) · 完整贡献指南
- [FRIENDS-PR-GUIDE.md](./FRIENDS-PR-GUIDE.md) · 5 分钟 PR 流程
- [content-triple-format/README.md](./content-triple-format/README.md) · 3F Content 范式
- [roadmap.md](./roadmap.md) · 仓库路线图