# baoyu-skills · 宝玉的内容创作 skill 矩阵

> **一句话定位**：21 个 sub-skill 一把抓 · 风格×布局二维选择 · 配置化 Prompt 工程 · 强制 prompt 文件 + 批量 + confirm 三件套。

---

## 这个 case 是什么

**页数**：5 页 · **领域**：内容创作
**作者**：宝玉 xp（@jimliu）
**仓库**：`github.com/JimLiu/baoyu-skills`
**clone 状态**：✅ 已 clone 到 `pretty-skills/内容创作/baoyu-skills/baoyu-skills/`
**实战笔记**：✅ 已读 3 个核心 sub-skill 的 SKILL.md

## 核心论点

Prompt 工程的终局是 **"消失"**——不让你写"你是一个资深设计师,请用…风格…",而是用 `--style notion` / `--layout dense` 这种参数代替。**审美的事交给 skill,用户只管选参数**。

## 21 个 sub-skill（实测 · 2026-07-15）

### 内容生成（核心矩阵）

| Skill | 风格 | 布局 | 适用 | 核心命令 |
|---|---|---|---|---|
| **baoyu-xhs-images** | 12 视觉风格 | 8 布局 | 小红书 / 微信图文 / 知识卡片 | `--style notion --layout dense` |
| **baoyu-infographic** | 22 视觉风格 | 21 布局 | 高密度信息大图 / 可视化 | `--layout bento-grid` |
| **baoyu-cover-image** | 5 维度定制 | — | 博客/公众号封面 | `--quick` |
| **baoyu-slide-deck** | — | — | PPT/汇报 | `--style blueprint` |
| **baoyu-comic** | — | — | 故事漫画/分镜 | `--art manga` |
| **baoyu-diagram** | — | — | 架构图/流程图 | — |
| **baoyu-article-illustrator** | — | — | 技术文章配图 | — |

### 内容转换

| Skill | 作用 |
|---|---|
| **baoyu-markdown-to-html** | Markdown → 含 Mermaid 的单文件 HTML |
| **baoyu-format-markdown** | 格式化/美化 |
| **baoyu-translate** | 翻译 |
| **baoyu-url-to-markdown** | URL → Markdown |
| **baoyu-wechat-summary** | 公众号文章摘要 |
| **baoyu-electron-extract** | Electron 应用内容提取 |
| **baoyu-compress-image** | 图片压缩 |
| **baoyu-image-gen** | 通用图片生成 |

### 内容发布

| Skill | 作用 |
|---|---|
| **baoyu-post-to-wechat** | 公众号发布 |
| **baoyu-post-to-weibo** | 微博发布 |
| **baoyu-post-to-x** | X/Twitter 发布 |

### 实验性

| Skill | 作用 |
|---|---|
| **baoyu-danger-gemini-web** | Gemini Web 抓取（高风险） |
| **baoyu-danger-x-to-markdown** | X 抓转 md（高风险） |
| **baoyu-youtube-transcript** | YouTube 字幕 |

## 实战笔记（看真实代码学到的 · 关键约束）

### 1. 三件套（所有生成类 skill 都有）

```text
a) 强制 prompt 文件（prompt-NN-{type}-{slug}.md）—— reproducibility 记录
b) 批量生成（默认 4 张/组，可调 1-8）—— 用 backend 原生 batch 或 parallel tool calls
c) 默认 confirm（不跳过）—— 必须用 --yes / "直接生成" 才跳过
```

### 2. 风格×布局矩阵

**baoyu-xhs-images** 12 风格：
`cute` / `fresh` / `warm` / `bold` / `minimal` / `retro` / `pop` / `notion` / `chalkboard` / `study-notes` / `screen-print` / `sketch-notes`

8 布局：
`sparse` / `balanced` / `dense` / `list` / `comparison` / `flow` / `mindmap` / `quadrant`

**baoyu-infographic** 22 风格 + 21 布局（覆盖范围更广，包括 `linear-progression` / `bento-grid` / `iceberg` / `story-mountain` 等长尾场景）

### 3. Preferences 系统（EXTEND.md）

```text
优先级 1: .baoyu-skills/<skill>/EXTEND.md  (项目级)
优先级 2: ${XDG_CONFIG_HOME:-$HOME/.config}/baoyu-skills/<skill>/EXTEND.md
优先级 3: $HOME/.baoyu-skills/<skill>/EXTEND.md  (用户级)
```

支持：preferred layout/style / default aspect ratio / language / preferred image backend / custom style definitions。

### 4. Reference image 3 种用法

| Usage | 作用 |
|---|---|
| `direct` | 文件直接传给 backend 作参考图 |
| `style` | 提取风格特征（线条/质感/氛围）拼到 prompt |
| `palette` | 提取 hex 颜色拼到 prompt |

### 5. 不允许的事（反模式）

- ❌ 用 SVG/HTML/CSS 假装生成位图 → 必须 raster
- ❌ 用 ImageMagick/Pillow 在生成的图上"修"文字 → 重生成
- ❌ 用 subagent 单纯为并行渲染图 → subagent 只用于 prompt 探索

### 6. 跨 harness 适配

支持 Claude Code（`AskUserQuestion` / `SendUserFile`） / Cursor（`AskQuestion` / `cursor-ide-browser`） / Codex Agent（`functions.*`）— 每个跑哪个 image backend 是动态决策（Codex `imagegen` > Cursor `GenerateImage` > Hermes `image_generate` > 非 native backend）。

## 安装（已验证）

```bash
# 走 npx 一键安装
npx skills add jimliu/baoyu-skills
# 全局
npx skills add jimliu/baoyu-skills -g
```

需要 Claude Code / Trae / Cursor / Codex Agent 这类"能动手"的 AI 工具。

## 触发词

"封面" / "小红书配图" / "信息图" / "PPT" / "故事漫画" / "宝玉" / "baoyu" / "技术配图" / "排版" / "公众号文章配图" / "高密度信息大图"

---

## 关联沉淀

- 视觉设计相关 → `pretty-skills/视觉创作/baoyu-design/`（本地化 Claude Design）
- 中文排版 + AI 审美黑名单 → `Mavis memory/distillation-review.md` 第 3 条
- sansheng-distill 提到的"12 家前人绝活"之一 → `pretty-skills/内容创作/拆书-skill/`
