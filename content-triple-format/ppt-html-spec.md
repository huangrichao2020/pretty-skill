# PPT 版 HTML 规范 · v3.2

> **TL;DR**：**PPT 版 HTML = 演示场景的网页版 PPT**。
> - **必填**：HTML 是 v3.2 唯一必填的演示载体
> - **可选**：真实 .pptx 文件（需要二次编辑时才生成）

---

## 💡 为什么是"PPT 版 HTML"

### 现状问题

之前的 3F Content 范式（v1-v3.1）把 `.md` + `.pptx` + `.html` 都列为必填 = 3 件套。

但实际场景：
- 90% 用户**只看不编辑** → 不需要 .pptx
- 真实 .pptx 制作复杂（需要 PowerPoint / python-pptx + AI 出图）
- HTML 通用（任何浏览器 + 任何设备 + 任何 OS）
- **HTML 才是"演示场景"的最佳载体**

### v3.2 决策

> **必填**：content.md（数据）+ web.html（PPT 演示版）· **2 件**
> **可选**：presentation.pptx（需要二次编辑时才生成）
> **必填**：images/ + prompts/ + 锦绣/

### 对比

| 维度 | HTML（必填）| PPTX（可选）|
|---|---|---|
| 通用性 | ✅ 任何浏览器 | ❌ 需要 PowerPoint |
| 文件大小 | 几百 KB | 几 MB - 几十 MB |
| 演示场景 | ✅ 中央大图 + 键盘翻页 | ✅ 同样可演示 |
| 二次编辑 | ❌ 需重新生成 | ✅ PowerPoint 友好 |
| AI 友好 | ✅ HTML 可被 AI 解析 | ❌ 二进制 |
| 协作 | ✅ Git diff 友好 | ⚠️ 二进制难 diff |

**HTML 已经能干 PPT 90% 的事**（演示 + 翻页 + 全屏），且更轻量 + 通用。**.pptx 只在需要二次编辑时才生成**。

---

## 📐 PPT 版 HTML 规范

### 核心功能

| 功能 | 快捷键 | 说明 |
|---|---|---|
| 翻页（上/下）| `←` `→` `Space` | 切换上/下一页 |
| 首页/末页 | `Home` `End` | 跳到首页/末页 |
| 全屏 | `F11` 或 `F` | 浏览器全屏（投影必备）|
| 演讲者模式 | `S` 或 `P` | 显示当前页 + 下一页 + 备注 + 计时器 |
| 黑屏 | `B` | 暂时黑屏（演讲停顿）|
| 白屏 | `W` | 暂时白屏 |
| 显示/隐藏备注 | `N` | 切换备注显示 |
| 缩略图侧栏 | `T` | 切换侧栏显示 |
| 进度 | 显示在右上角 | "1 / 9" |

### 界面布局

```
┌──────────────────────────────────────────────┐
│ [缩略图侧栏] │ 中央大图（全屏）        │ 进度  │
│ [可折叠]    │                          │ 1/9  │
│  □ □ □      │                          │       │
│  □ □ □      │      [画面主体]          │       │
│  □ □ □      │                          │       │
│  □ □ □      │                          │       │
│              │                          │       │
│ [首页][上][下][末页]  [全屏][备注][演]     │       │
└──────────────────────────────────────────────┘
```

### 演讲者模式布局

```
┌──────────────────────────────────────────────┐
│ 当前页                       │ 下一页预览      │
│                              │                │
│      [画面]                  │   [缩略图]     │
│                              │                │
│                              │                │
│──────────────────────────────│  备注          │
│ 备注（可滚动）                │  - 重点 1     │
│  - 这是案例的关键论点         │  - 重点 2     │
│  - 数据：xxx                  │                │
│                              │  计时器        │
│                              │  00:15:30     │
└──────────────────────────────────────────────┘
```

### 元素清单

| 元素 | 必填 | 说明 |
|---|---|---|
| 中央大图 | ✅ | 全屏显示对应页图片 |
| 翻页按钮 | ✅ | 上/下/首页/末页 |
| 键盘提示 | ✅ | 第一次访问显示快捷键说明 |
| 缩略图侧栏 | ✅ | 可折叠，显示所有页缩略图 |
| 进度显示 | ✅ | "1 / 9" |
| 标题栏 | 可选 | 半透明覆盖在画面顶部 |
| 演讲者模式 | 可选 | 按 S 进入 |
| 备注 | 可选 | 每页可单独写备注 |
| 计时器 | 可选 | 演讲者模式显示 |
| 全屏快捷键 | ✅ | F11/F |
| 黑/白屏 | 可选 | 演讲时临时用 |
| 自动翻页 | ❌ | 不推荐（演讲者控制） |

---

## 🎨 视觉风格

### 演示场景配色（默认）

- **画布背景**：`#000`（黑）让大图最突出
- **侧栏**：`#1a1a1a`（深灰）半透明
- **文字**：`#fff`（白） + `#aaa`（次文字）
- **进度/页码**：`#00d4aa`（青绿高亮）

### 演讲者模式

- **背景**：`#0a0a0a`（近黑）
- **当前页边框**：`#00d4aa`（青绿高亮）
- **下一页**：`#333`（暗）
- **文字**：`#fff` + `#aaa`
- **备注**：`#ddd`

---

## 💻 最小实现模板

参考 `_模板/案例/web.html`（v3.2 升级版）：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{案例标题} · PPT 演示版</title>
  <style>
    /* 演示场景 CSS（黑底 + 中央大图 + 侧栏） */
  </style>
</head>
<body>
  <div class="app">
    <aside class="sidebar"><!-- 缩略图 --></aside>
    <main class="stage">
      <div class="slide"><img></div>
      <div class="overlay"><!-- 进度 + 标题 --></div>
      <div class="controls"><!-- 翻页按钮 --></div>
    </main>
  </div>
  <div class="presenter-mode"><!-- 演讲者模式 --></div>
  <script>
    // 键盘事件：翻页 / 全屏 / 演讲者模式 / 黑/白屏
    // 鼠标事件：点击翻页 / 缩略图切换
  </script>
</body>
</html>
```

完整实现见 `html-ppt-viewer` skill（v3.2 升级版）。

---

## 🤖 自动生成（skill-creator v0.2）

```bash
pretty-skills create \
  --input my-knowledge.md \
  --domain "trading-review"

# 自动生成（v3.2）：
# 1. content.md（必填）
# 2. web.html（必填 · PPT 演示版 · 自动应用 PPT 版 HTML 规范）
# 3. images/（必填 · AI 出图）
# 4. 锦绣/（必填 · v3.1 简化）
# 5. presentation.pptx（可选 · 加 --with-pptx 才生成）
```

```bash
# 加 --with-pptx 才生成真实 PPTX
pretty-skills create \
  --input my-knowledge.md \
  --domain "trading-review" \
  --with-pptx
```

---

## ✅ 校验（check-3f.py v3.2）

| 项 | 必填/可选 | 校验 |
|---|---|---|
| `content.md` | **必填** | exit 1 if 缺失 |
| `web.html` | **必填**（PPT 演示版）| exit 1 if 缺失 |
| `images/` | **必填** | exit 1 if 缺失 |
| `prompts/` | **必填** | warning if 缺失 |
| `presentation.pptx` | **可选** | warning if 缺失 |
| `output/*.pptx` | **可选** | warning if 缺失 |
| `锦绣/` | **必填** | exit 1 if 缺失（v3.1 软警告 → v3.2 改硬要求）|

**v3.2 关键变化**：
- ✅ `web.html` = **PPT 演示版**（必填 · 替代 .pptx 作为演示载体）
- ⚠️ `presentation.pptx` = **可选**（warning · 不阻止 PR）

---

## 🎯 真实场景工作流

### 场景 A · 用户只看不编辑（90% 场景）

```
content.md + web.html + images/ + 锦绣/ = 完整交付
  ↓
用户双击 web.html → 浏览器打开 → 键盘翻页 → 全屏投影
```

**不需要 .pptx**。

### 场景 B · 用户要二次编辑（10% 场景）

```
内容同上 + presentation.pptx
  ↓
用户用 PowerPoint / Keynote / WPS 打开 .pptx
  ↓
改文字 / 改布局 / 改图 → 保存
```

**需要 .pptx**（用 `--with-pptx` 标志生成）。

### 场景 C · AI 训练 / 数据集

```
content.md（纯净文本）+ images/（图片数据）= AI 友好
```

**只需要 content.md + images/**。

---

## 💯 设计原则

> **范式的"必填项"应该是真正的核心需求**。
>
> 之前我把 .pptx 列为"必填"是错的——90% 用户不需要二次编辑。
> 真正的核心需求是"演示"——HTML 已经能干 90% 的事。
> PPTX 只在"二次编辑"场景下需要，列为可选。
>
> 范式**只锁核心 + 留弹性**：
> - 必填 = 90% 场景都需要
> - 可选 = 10% 场景额外需求
> - 不锁平台 = creator 自适配

---

参考：
- [content-triple-format/README.md](./README.md) · 3F Content 范式总览
- [content-triple-format/锦绣.md](./锦绣.md) · 锦绣范式
- [skill-creator/README.md](../../skill-creator/README.md) · 自动生成工具
- [STRUCTURE.md](../../STRUCTURE.md) · 仓库结构决策