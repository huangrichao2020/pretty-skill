# zhongguose-ppt-skill · 中国色汇报演示体系

> **一句话定位**：用中国传统色彩为气韵、原稿章法为骨架，构建可交互、可迁移的中式汇报体系。

---

## 这个 case 是什么

**页数**：5 页 · **领域**：视觉创作
**作者**：木渡川 (Muduchuan)
**产品思路参考**：归藏 (guizang) 的 `guizang-ppt-skill`
**封面字体**：令東 (Lingdong Huang) 的 `qiji-font`（齊伋體，OFL 1.1）
**安装渠道**：RedSkill 商店（小红书）
**安装路径**：`~/.minimax/.../workspace/skills/zhongguose-ppt-skill/`
**状态**：✅ v1.0.0 已装 · pretty-skills case 草稿沉淀

## 核心论点

构建一套**中国色汇报演示体系**，两种交付模式：
1. **HTML 模式**：自包含交互式 HTML deck（`index.html` + `assets/`）
2. **PPT 模式**：为 PPT 制作提供汇报逻辑、页级架构与版式设计参考（不直接生成 .pptx）

**两种模式都遵循 5 个统一原则**：
- 单一中国传统色
- 中式文化气质
- 克制的网格秩序
- 中文主导的中英双语层级
- 逻辑优先的叙事结构

## 6 个主题色（选择 1 个/份演示）

| 名称 | accent | 气质 |
|---|---|---|
| **飞泉绿** Feiquan Green | `#497568` | 沉静青绿（默认）|
| **藕丝秋** Lotus Silk Autumn | `#D9C6B3` | 温润浅茶 |
| **湘蓝** Xiang Blue | `#4A76A8` | 沉稳青蓝 |
| **绛缨** Crimson Tassel | `#9E3B3B` | 深绛有力 |
| **鸦黄** Crow Yellow | `#E6C24D` | 明亮秋黄 |
| **山岚** Mountain Mist | `#B2C9B2` | 雾霭青绿 |

> **浅色主题必须用墨色 accent-on**（不得继续用白字）

选色前打开 `assets/theme-cover-gallery.html` 对照封面示例。

## 12 步工作流

```text
0  确认主题色 + 文稿状态 + 润色尺度（必问）
1  建立源文档逻辑地图
2  制定页级结构合同
3  保留文案与层级
4  从 assets/template-zhongguose/ 模板开始
5  替换页面内容（保留演示外壳）
6  选版式（参考 layout-patterns.md）
7  应用视觉系统（参考 visual-system.md）
8  重建逐稿封面字体（subset-cover-font.py）
9  校验（validate-deck.js / quality-checklist.md）
10 预览（preview-deck.js / browser-qa.js）
11 交付（HTML 单文件 / PPT 框架合同）
+  12 反馈迭代
```

## 3 种润色模式

- **大调** —— 重组段落顺序、强化转场、优化表达（保留事实/意图/已确认观点）
- **微调** —— 优化措辞/节奏/重点/重复（保留结构与论述）
- **近原文** —— 只修正错别字/标点/明显语病（不改变含义与结构）

## 中英双语层级

- **中文主导**：主标题、章节扉页标题、卡片标题、核心陈述保持**纯中文**
- **英文辅助**：导航、元信息、小标签、图注、辅助正文（**更小字号，不与中文等大并列**）
- 英文必须保留原意/名称/数字/因果/顺序，**不得新增观点**

## 6 个 scripts（已装）

| 脚本 | 作用 |
|---|---|
| `validate-deck.js` | 校验 deck |
| `extract-deck-outline.js` | 抽取大纲 |
| `check-cover-glyphs.py` | 检查封面字符（缺失的拉丁/标点回退到下一字体）|
| `browser-qa.js` | 浏览器 QA |
| `subset-cover-font.py` | 重建封面字体子集（Qiji font → WOFF2 subset）|
| `preview-deck.js` | 预览 deck |

## 4 个 references（已装）

| 文件 | 内容 |
|---|---|
| `references/visual-system.md` | 主题色 / 变量合同 / 字体层级 / 色彩使用 / 素材 / 可访问性 |
| `references/layout-patterns.md` | 模式库（封面/章节扉页/正文/对比/数据/收尾等）|
| `references/content-architecture.md` | 文稿锁定 / 源逻辑地图 / 分组提炼 / 页面合同 / 中英双语 / 禁止事项 |
| `references/quality-checklist.md` | 6 维度 30+ 检查项（内容/结构/主题/资源/交互/交付）|

## 跟 pretty-skills 现有 PPT skill 的关系

| Pretty-skills 现有 | 风格 | 触发词 |
|---|---|---|
| `PPT证据链战法`（web.html）| CyberPPT · 蓝/黑 · 证据链 + 三段式 | "证据链" / "三段式" / "CyberPPT" |
| `dashiai-ppt传统PPT` | 大狮 · 通用传统 PPT | "传统PPT" / "通用" / "汇报" |
| **`zhongguose-ppt-skill`** | **中国色 · 中式 · 6 主题色** | **"中国色" / "中国风" / "国风" / "zhongguose" / "中式"** |

**3 个 skill 不互斥**——按内容气质挑风格：
- 科技/产品/数据 → PPT证据链战法
- 通用商务 → dashiai-ppt
- 文化/历史/品牌/中式 → **zhongguose**

## 升级路线（pretty-skills 整活用）

```text
v1  (现在)    → case 草稿沉淀 + 6 主题色 + 12 步工作流速查
v2  (下一步)  → 跑 1 份中国色演示稿实战（拿一篇已知文章做 5-10 页 deck）
v3  (远期)    → 给 PPT证据链战法 web.html 加 6 主题色切换
v4  (终)      → 实战 3-6 个月后升 knowhub methodology
```

## 触发词

"中国色" / "中国风" / "中式" / "东方审美" / "国风PPT" / "zhongguose" / "传统色" / "木渡川" / "归藏" / "中式汇报" / "中国色演示"

---

## 关联沉淀

- `视觉创作/PPT证据链战法/` —— 现有 PPT skill（CyberPPT 风格，不互斥）
- `视觉创作/dashiai-ppt传统PPT/` —— 大狮 PPT（通用商务风格，不互斥）
- 安装路径：`~/.minimax/.../workspace/skills/zhongguose-ppt-skill/`（已装，pretty-skills 仓库**不重复 copy**，只沉淀 case 草稿）
