# PDF 讲解版规范 · v3.19

> **TL;DR**：**PDF 讲解版 = GitHub 原生预览的演示载体**。
> - **必填**：PDF 是 v3.19 唯一必填的演示载体（替代 v3.18 的 web.html）
> - **可选**：真实 .pptx 文件（需要二次编辑时才生成）

---

## 💡 为什么 v3.19 从 web.html 改 PDF

### 现状问题（v3.18 web.html）

web.html 作为 PPT 演示版非常出色（中央大图 + 键盘翻页 + 全屏），但在 GitHub 仓库浏览时**无法预览**：

- GitHub 把 HTML 当作**代码文件**，不渲染
- 用户看到的是「白板+乱码」或「双击下载」
- 仓库 README 里贴 HTML 链接 → 没有吸引力

### v3.19 决策

> **必填**：content.md（数据）+ `<case_name>讲解.pdf`（PDF 讲解版）· **2 件**
> **可选**：presentation.pptx（需要二次编辑时才生成）
> **必填**：images/ + prompts/ + 锦绣/

### 对比

| 维度 | PDF（必填）| web.html（已废）| PPTX（可选）|
|---|---|---|---|
| GitHub 预览 | ✅ **原生 PDF 阅读器** | ❌ 只下载 | ❌ 不能预览 |
| 文件大小 | 80-200 KB | 10-20 KB | 几 MB - 几十 MB |
| 演示场景 | ✅ 翻页 + 全屏 | ✅ 翻页 + 全屏 + 演讲者模式 | ✅ 同样可演示 |
| 二次编辑 | ❌ 需重新生成 | ❌ 需重新生成 | ✅ PowerPoint 友好 |
| AI 友好 | ❌ 二进制 | ✅ HTML 可被 AI 解析 | ❌ 二进制 |
| 协作 | ✅ Git diff 友好（图像识别） | ✅ Git diff 友好 | ⚠️ 二进制难 diff |

**PDF 是 GitHub 演示场景的最佳载体** + 任何 PDF 阅读器都能开 + 邮件/IM 分享友好。

---

## 📐 PDF 规格

### 命名规范

```
<case_name>讲解.pdf
```

例：`公众号内容交付方法论讲解.pdf`

**规则**：
- 文件名严格 = `<case_name>讲解.pdf`
- `<case_name>` 从 `manifest.json.name` 字段读
- 中英名都可（manifest 里是什么就用什么）

### 页面规格

- **页面大小**：A4 横版（297 × 210 mm）
- **页面方向**：landscape（横版）
- **背景色**：#FFF7E8（cream paper · pretty-skills 美学锁定）
- **文字色**：#6B4423（深棕色）
- **主色**：#B8E0D2（薄荷绿，用于页码徽章）

### 单页布局

```
┌──────────────────────────────────────────────┐
│ [P1/13]              公众号内容交付方法论 · 讲解│
│ ─────────────────────────────────────────────│
│                                              │
│         ┌─────────────────────────────┐      │
│         │                             │      │
│         │      [P1 大图]               │      │
│         │                             │      │
│         └─────────────────────────────┘      │
│                                              │
│ ─────────────────────────────────────────────│
│ by Mavis             pretty-skills · v3.19   │
└──────────────────────────────────────────────┘
```

### 多页合并

- 每个 PNG 占 1 页
- `page-break-after: always` 控制分页
- 页面间无空隙（A4 满版）

---

## 🔧 生成工具

### tools/build_case_pdf.py

```bash
# 完整用法
python3 tools/build_case_pdf.py <case_dir> [title] [--output <pdf_name>] [--open]

# 示例（自动模式）
python3 tools/build_case_pdf.py "Agent知识/公众号内容交付方法论/"

# 示例（自定义输出名）
python3 tools/build_case_pdf.py "Agent知识/公众号内容交付方法论/" \
                                --output "公众号交付手册.pdf"

# 示例（生成后自动打开）
python3 tools/build_case_pdf.py "Agent知识/公众号内容交付方法论/" --open
```

### 依赖

- **playwright** Python 包（已装）
- **chromium-1223**（ms-playwright 缓存里）
- 路径：`~/Library/Caches/ms-playwright/chromium-1223/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing`

### 自动识别

`build_case_pdf.py` 自动从以下位置读：

- **`manifest.json`** → `title` 字段（`name` 字段作 fallback）
- **`images/`** → `p*.png` 按文件名排序
- **manifest.format.case_pdf** → 输出文件名（默认 `<name>讲解.pdf`）

不需要传图片列表参数。

---

## ✅ check-3f.py F3 检测（v3.19 新增）

F3 检测 4 个维度：

| 检查项 | 通过条件 | 失败原因 |
|---|---|---|
| 文件存在 | `*讲解.pdf` 在 case_dir 下 | 缺 PDF |
| 文件大小 | ≥ 50 KB | 纯文字 PDF |
| Magic bytes | `%PDF-` 开头 | 不是合法 PDF |
| 嵌图证据 | 含 `/Subtype /Image` | 纯文字 PDF |

退出码 `0` = 全部通过，`1` = 至少 1 项失败（PR 会被退）。

---

## 📜 历史

- **v3.2 - v3.18**：web.html 是必填的 PPT 演示版
- **v3.19**：改 PDF 必填，web.html 废弃

**为什么一次性切换**：web.html 在 GitHub 不能预览 → 演示场景价值为 0。PDF 同时支持 GitHub 原生预览 + 邮件分享 + 离线阅读，全面胜出。

---

## 🔗 相关规范

- [README.md](./README.md) · 3F 总览
- [methodology.md](./methodology.md) · 设计哲学
- [onboarding-guide.md](./onboarding-guide.md) · 5 步上手
- [锦绣.md](./锦绣.md) · 4 形态传播素材