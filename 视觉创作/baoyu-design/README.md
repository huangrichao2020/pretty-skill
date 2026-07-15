# baoyu-design · 本地化 Claude Design 的 Agent skill

> **一句话定位**：把 Claude Design 的设计引擎打包成 harness-agnostic Agent skill · Claude Code / Cursor / Codex 都能跑 · 自包含 HTML 输出。

---

## 这个 case 是什么

**页数**：4 页 · **领域**：视觉创作
**作者**：宝玉 xp（@jimliu）
**仓库**：`github.com/JimLiu/baoyu-design`
**clone 状态**：✅ 已 clone 到 `pretty-skills/视觉创作/baoyu-design/baoyu-design/`
**实战笔记**：✅ 已读 SKILL.md + built-in-skills/ 全部 33 个内置 skill 清单

## 核心论点

Claude Design 在线版很强，但**没法在本地 Agent 里跑**。宝玉把它的设计引擎打包成本地 skill——**不依赖云端 · harness-agnostic · 设计风格一致**。

## 实战笔记（看真实代码学到的）

### 1. Harness-agnostic 模式

入口 SKILL.md 第 2 步就是"识别你的 harness 并加载工具参考"：
- Claude Code（`AskUserQuestion` / `SendUserFile` / Claude Preview MCP）
- Cursor（`AskQuestion` / `cursor-ide-browser` / `user-chrome-devtools` MCP）
- Codex Agent（`functions.*` / `tool_search` / Codex Browser/Chrome plugins）
- Claude Desktop-like / 未知 file-capable → 走通用 workflow

### 2. Single source of truth 模式

```text
system-prompt.md  →  工艺/方法论的 single source of truth
references/<harness>.md  →  harness 工具映射的 single source of truth
SKILL.md  →  只做编排（orchestration），不重复内容
```

**反模式**：把方法论散在多个文件里 → harness 一变就乱。

### 3. 33 个 built-in-skill（实测全清单）

#### 基础工艺（必备）
- `hi-fi-design.md` — 高保真设计
- `interactive-prototype.md` — 交互原型
- `wireframe.md` — 低保真线框图
- `use-design-system.md` — 消费已有设计系统
- `low-level-tweaks-api.md` — 底层微调
- `tweaks-protocol.md` — 微调协议
- `claude-api-in-prototypes.md` — 在原型里调 Claude API

#### 设计系统（建/导）
- `design-system-authoring-guide.md` — 完整 authoring 流程
- `create-design-system.md` — 创建设计系统
- `design-system-preview.md` — 设计系统预览页
- `design-components.md` — 设计组件
- `use-design-system.md` — 消费设计系统

#### 导入
- `import-from-figma.md` — 导入 Figma .fig 文件（**不需要 Figma 账号**）
- `import-from-github.md` — 导入 GitHub 仓库作参考
- `import-from-html.md` — 导入 HTML/CSS 作参考

#### 输出格式
- `export-as-video.md` — 导出动画为 .mp4
- `export-as-pptx-editable.md` — 导出 PPTX（**可编辑**，默认走这个）
- `export-as-pptx-screenshots.md` — 导出 PPTX（**像素级截图**，仅当用户明确要）
- `save-as-standalone-html.md` — 单文件 HTML 输出
- `save-as-pdf.md` — 存 PDF
- `send-to-figma.md` / `send-to-canva.md` — 发到 Figma/Canva

#### 文档
- `make-a-doc.md` — 简历/一页纸/备忘录/信/报告
- `make-a-deck.md` — deck/演示文稿
- `make-tweakable.md` — 可微调的产物
- `speaker-notes.md` — 演讲者备注
- `read-pdf.md` — 读 PDF

#### 移动 / 动画 / 声音
- `mobile-prototype.md` — 移动端原型
- `animated-video.md` — 动画视频
- `sound-effects.md` — 音效

#### 元 / 实验
- `frontend-design.md` — 前端设计
- `generate-images.md` — 图片生成
- `handoff-to-claude-code.md` — 交接给 Claude Code
- `something-cool.md` — 用户明说"想被惊艳"时（opt-in，不默认）

### 4. 强制要求

- **保存位置**：`designs/<descriptive-project-name>/`（默认），不能散到 repo 根
- **设计系统绑定**：用 `glob designs/*/_ds_manifest.json` 发现可用系统 → 多选让用户挑
- **resume 已存在项目**：先读 `_d_meta.json` 找 `designSystems` → 加载每个绑定系统的 prompt 跟做（**不重新问**）
- **资产记录**：用 `agents/record-asset.mjs` 记录每个 UI 产物（会 bootstrap `_d_meta.json`）

### 5. 中文排版硬规矩 + AI 审美俗套黑名单

宝玉的 baoyu-design 里默认带：
- **中文排版硬规矩**：行距 / 字间距 / 标点挤压 / 字体回退
- **AI 审美俗套黑名单**：禁止蓝紫渐变 / 禁止过度圆润 / 禁止统一圆角等

> 已被 sansheng-distill 第 12 条吸收

### 6. Figma 离线支持（强项）

`import-from-figma.md` 走 `agents/import-figma.mjs`：
- `outline` 看结构
- `mount` / `materialize` / `render` 作参考
- `design-system` 完整 emission 进 design-system-authoring-guide

**离线解码 .fig 文件 —— 不需要 Figma 账号 / MCP**。

## 团队协作目录结构

```
team-project/
├── designs/              # 所有设计项目
│   ├── marketing-site/
│   └── mobile-app/
├── design-systems/       # 团队设计系统
│   ├── brand-system/
│   └── component-library/
└── shared-assets/
```

## 安装（已验证）

```bash
npx skills add JimLiu/baoyu-design
# 全局
npx skills add JimLiu/baoyu-design -g
```

**推荐配置**：Claude Opus 4.8（最佳设计效果）

## 触发词

"UI mockup" / "UI 设计" / "本地设计" / "Claude Design" / "Figma 导入" / "设计系统" / "baoyu" / "宝玉" / "自包含 HTML" / "PPT/汇报" / "deck"

---

## 关联沉淀

- 内容创作相关 → `pretty-skills/内容创作/baoyu-skills/`
- AI 审美黑名单 / 中文排版 → `Mavis memory/distillation-review.md` 第 3 条
