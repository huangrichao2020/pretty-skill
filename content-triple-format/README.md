# Content Triple Format · 3F Content

> **一句话定位**：任何 PPT / 长图 / 知识卡片产出物都按 3 件套发布：**`.md` 源文字 + `.pptx` 演示 + `.html` 网页**。让内容对 AI 和人类同等友好。

> 这是 pretty-skill 的核心约定。所有贡献者必读。

## 为什么做 3F

| 加 `.md` 之前 | 加 `.md` 之后 |
|---|---|
| GitHub diff 看不懂 .pptx 内嵌文字（zip） | ✅ 逐字 diff，文案改动可追溯 |
| AI agent 没法吃你的 PPT（OCR 慢且不准） | ✅ `.md` 直接喂 LLM / 总结 / 翻译 / 二创 |
| 屏幕阅读器 / 搜索引擎爬不动 .pptx | ✅ `.md` 全可读、可索引、可引用 |
| 别人想 fork 只能下载反推文案 | ✅ 拿 `.md` 就能复刻成图，省 80% 工时 |
| 自媒体文章需重新拆 PPT 重写 | ✅ `.md` 直接做推文 / 视频脚本 / Newsletter |
| 只有你自己能消费这些 PPT | ✅ 任何 AI 工具都能消化你的整个仓库 |

> 根因：**`.md` 是数据，`.pptx/.html` 是表示。数据与表示分离** = 软件工程经典思想应用到内容领域。

## 3 件套规范

```
<case-name>/
├── content.md            # F1 · 源文字（人类 + AI 最高兼容）
├── presentation.pptx     # F2 · PowerPoint / Keynote / WPS 可编辑
└── web.html              # F3 · 浏览器直接看，sidebar 翻页 + 键盘快捷键
```

### F1 · content.md 模板

每页 4-7 字段：

```markdown
## P{n} · {章节类型}-{主题}

- **标题**：
- **副标**：
- **章节类型**：（钩子/总纲/核心解法/深化/角色升级/收束/演示对照）
- **核心主张**：一句话
- **关键要点**：3-5 bullets
- **数据 / 数字**：
- **金句**：可独立传播的一句话
- **童趣图标**：（出图时用）
```

### F2 · presentation.pptx

- 16:9 宽屏（13.333" × 7.5"）
- 2 种模式（image 纯图 / editable 图+文字框）
- 无任何装饰元素（无 badge / 无边框 / 无 logo）
- 用 `~/.mavis/bin/build_pptx_v2.py` 一键生成

### F3 · web.html

- 左侧 sidebar 缩略图翻页
- 中间大图全屏
- 键盘 ← → 翻页
- 不依赖任何后端

## 反模式（必避）

- ❌ 只输出 `.pptx` 没有 `.md` → 失去 80% AI 友好性
- ❌ `.md` 是 prompt 元注释（"X 色 强调 Y"）→ 必须真内容
- ❌ 3 件套文件名不匹配 → 必须同名同 case 目录
- ❌ `.md` 跟 `.pptx` 内文不一致 → 以 `.md` 为准
- ❌ `.pdf` 替代 `.md` → `.pdf` 不是纯文本，diff/搜索/AI 处理弱

## 工程流程

```text
1. 列 N 页章节清单
   ↓
2. 写 content.md（每页 4-7 字段，先！）
   ↓
3. 写 60 行 prompt × N（每页）
   ↓
4. matrix 生成 N 张图（PNG）
   ↓
5. python-pptx 嵌入 → presentation.pptx
   ↓
6. html-ppt-viewer 套壳 → web.html
   ↓
7. 用 content.md 反查 .pptx/.html（如有出入以 .md 为准）
   ↓
8. 3 件套归档 → domains/<area>/<case>/
```

## 完整规范 vs 简化版

- **完整版**（推荐）：按上面的工程流程
- **简化版**（PPT 临时草稿 / 内部使用）：可只输出 `.md` + `.pptx`（无 `.html`），但 `.md` 永远不能省

## 完整方法论

[methodology.md](./methodology.md) —— 详细背景 + 类比 SDR / spec-driven development

## 模板

[templates/content.md.template](./templates/content.md.template) —— 新 case 的 content.md 起步模板

## 30 秒起步

1. **Fork** pretty-skill
2. **复制** `domains/_template/case/` 到 `domains/<your-area>/<your-case>/`
3. **填** `content.md`（每页 4-7 字段）
4. **生成** `.pptx` + `.html`
5. **提 PR**

[完整 CONTRIBUTING 流程](../CONTRIBUTING.md)

---

**命名传统**：3F Content / Triple-Format Content Skill / 3FCS  
**来源**：2026-07-07 Mavis / huangrichao2020 讨论沉淀