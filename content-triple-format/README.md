# Content Triple Format · 3F Content v3.2

> **一句话定位**：任何 PPT / 长图 / 知识卡片产出物都按 v3.2 发布：
> - **必填 2 件**：`content.md` 源文字 + `web.html` PPT 演示版
> - **可选 1 件**：`presentation.pptx` 真实 PowerPoint（需要二次编辑时才生成）
>
> 让内容对 AI 和人类同等友好 + 任何场景都能演示 + 不强求 PowerPoint。
>
> 这是 pretty-skills 的核心约定。所有贡献者必读。

> ### ⚠️ 配套 · 生图能力是必须的
>
> 3F Content + 锦绣 范式都依赖 AI 出图。
> **推荐使用 MiniMax 套餐** —— **49 元 Token plan 套餐**就能跑（支持 matrix MCP 多模态生图 + 生视频，月费起步）。
> 没生图能力 = 范式坍塌。

## 为什么做 3F

| 加 `.md` 之前 | 加 `.md` 之后 |
|---|---|
| GitHub diff 看不懂 .pptx 内嵌文字（zip） | ✅ 逐字 diff，文案改动可追溯 |
| AI agent 没法吃你的 PPT（OCR 慢且不准） | ✅ `.md` 直接喂 LLM / 总结 / 翻译 / 二创 |
| 屏幕阅读器 / 搜索引擎爬不动 .pptx | ✅ `.md` 全可读、可索引、可引用 |
| 别人想 fork 只能下载反推文案 | ✅ 拿 `.md` 就能复刻成图，省 80% 工时 |
| 自媒体文章需重新拆 PPT 重写 | ✅ `.md` 直接做推文 / 视频脚本 / Newsletter |
| 只有你自己能消费这些 PPT | ✅ 任何 AI 工具都能消化你的整个仓库 |

> 根因：**`.md` 是数据，`web.html` 是表示（演示场景），`presentation.pptx` 是可选二次编辑载体。数据与表示分离** = 软件工程经典思想应用到内容领域。

## v3.2 必填 + 可选清单

```
<case-name>/
├── content.md            # F1 · 源文字（必填 · 人类 + AI 最高兼容）
├── web.html              # F2 · PPT 演示版 HTML（必填 · 演示场景）
├── presentation.pptx     # F3 · PowerPoint（可选 · 仅二次编辑时生成）
├── images/               # AI 出图原图（必填）
├── prompts/              # 出图 prompt 文件（必填 · 工程可复现）
└── 锦绣/                 # 传播素材（必填 · v3.1 简化：2 封面 + slides/ + readme.md）
```

**v3.2 关键变化**：
- ✅ **`web.html` 是 PPT 演示版**（必填 · 替代 .pptx 作为演示载体）
- ⚠️ **`presentation.pptx` 改为可选**（warning · 不阻止 PR · 加 `--with-pptx` 才生成）

### 为什么 PPTX 改可选

| 维度 | HTML（必填）| PPTX（可选）|
|---|---|---|
| 通用性 | ✅ 任何浏览器 | ❌ 需要 PowerPoint |
| 文件大小 | 几百 KB | 几 MB - 几十 MB |
| 演示场景 | ✅ 中央大图 + 键盘翻页 | ✅ 同样可演示 |
| 二次编辑 | ❌ 需重新生成 | ✅ PowerPoint 友好 |
| AI 友好 | ✅ HTML 可被 AI 解析 | ❌ 二进制 |
| 协作 | ✅ Git diff 友好 | ⚠️ 二进制难 diff |

**90% 用户只看不编辑** → HTML 就够。**10% 用户要二次编辑** → 显式加 `--with-pptx` 标志。

完整 PPT 版 HTML 规范：[ppt-html-spec.md](./ppt-html-spec.md)

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

### F2 · web.html（PPT 演示版 · 必填）

**详细规范**：[ppt-html-spec.md](./ppt-html-spec.md)

**核心功能**：
- 16:9 中央大图全屏
- 键盘翻页（`←` `→` `Space`）
- 缩略图侧栏（可折叠）
- 全屏（`F11` / `F`）
- 演讲者模式（`S` / `P`）
- 黑/白屏（`B` / `W`）
- 进度显示（`1/9`）

**用 `html-ppt-viewer` skill（v3.2 升级版）生成**。

### F3 · presentation.pptx（可选）

- 16:9 宽屏（13.333" × 7.5"）
- 2 种模式（image 纯图 / editable 图+文字框）
- 无任何装饰元素（无 badge / 无边框 / 无 logo）
- 用 `~/.mavis/bin/build_pptx_v2.py` 一键生成
- **仅当用户需要二次编辑时生成**（用 `--with-pptx` 标志）

## 反模式（必避）

- ❌ 只输出 `.pptx` 没有 `.md` → 失去 80% AI 友好性
- ❌ `.md` 是 prompt 元注释（"X 色 强调 Y"）→ 必须真内容
- ❌ 3 件套文件名不匹配 → 必须同名同 case 目录
- ❌ `.md` 跟 `.html` 内文不一致 → 以 `.md` 为准
- ❌ `.pdf` 替代 `.md` → `.pdf` 不是纯文本，diff/搜索/AI 处理弱
- ❌ **web.html 是文字版**（不是 PPT 演示版）→ 必须按 ppt-html-spec.md 规范生成

## 工程流程（**不可跳过任一步**）

```text
┌────────────────────────────────────────────────────┐
│ 1. 列 N 页章节清单                                   │
│   ↓                                                │
│ 2. 写 content.md（每页 4-7 字段 · 先！）             │ ← 必填
│   ↓                                                │
│ 3. 写 60 行 prompt × N（每页）                       │
│   ↓                                                │
│ 4. matrix 生成 N 张图（PNG）                          │ ← 必须这一步！
│   ↓                                                │
│ 5. html-ppt-viewer（v3.2 升级）套壳 → web.html        │ ← 必填 · PPT 演示版
│   ↓                                                │
│ 6. （可选）python-pptx 嵌入图 → presentation.pptx   │ ← 加 --with-pptx 才跑
│   ↓                                                │
│ 7. 用 content.md 反查 web.html（以 .md 为准）        │
│   ↓                                                │
│ 8. 锦绣 自动生成（v3.1 简化：2 封面 + slides/ + readme.md）
│   ↓                                                │
│ 9. 完整 case 归档到 <领域>/<case>/                  │
└────────────────────────────────────────────────────┘
```

⚠️ 关键反模式 · 必避
════════════════════════════════════════════════════════════

❌ 「直接拿 content.md 转 PPT」
   → 文字 PPT（丑、缺图、信息密度低）
   → 朋友试了一次，结果就是一堆丑文字框
   
❌ 「跳过步骤 4，直接用 .md 文字拼 .pptx」
   → 失去视觉冲击 = 失去 3F 范式 80% 价值
   
❌ 「步骤 5 用代码生成 HTML 文字 PPT 而不出图」
   → HTML 必须是 PPT 演示版（中央大图 + 键盘翻页 + 演讲者模式）
   → 不是把 .md 转 HTML 文字

✅ 正确路径（必须严格按这个流程）
   → content.md（数据）
     ↓ 写 prompt
   → AI 出图（PNG）
     ↓ embed into
   → web.html（PPT 演示版 · 必填）
   → presentation.pptx（可选 · 加 --with-pptx）
```

**为什么流程不可跳**：
- `.md` 是「数据」
- `web.html` / `presentation.pptx` 是「视觉表示」
- 没有中间的「AI 出图」，数据无法变成有视觉冲击的表示
- **文字直转 = 数据自己说自己，没有视觉化 = 失去 80% 价值**

## 流程校验清单（PR 前必查）

```
□ 步骤 1: 章节清单写好
□ 步骤 2: content.md 每页 4-7 字段齐全
□ 步骤 3: 60 行 prompt × N
□ 步骤 4: 实际调 matrix API 出图 · 截图存 images/
□ 步骤 5: html-ppt-viewer（v3.2）生成 web.html · PPT 演示版
□ 步骤 6: （可选）跑 build_pptx.py 生成 .pptx
□ 步骤 7: 用 .md 反查 web.html · 内文一致
□ 步骤 8: 锦绣 自动生成（4 形态齐全）
□ 步骤 9: 归档到 <领域>/<case>/ 目录

任一项打 ✗ → PR 退回
```

## 给 Agent 的 onboarding（必读）

如果你是 agent 接任务做 PPT，**先看完下面这一段再动手**：

```text
你接到一个 PPT 任务。第一步不是写 .pptx，也不是用代码铺文字。
第一步是：
  1. 写 content.md（每页 4-7 字段）
  2. 写 prompt
  3. 调 image_gen API 出图（matrix / DALL-E / Midjourney）
  4. 把图嵌进 web.html（PPT 演示版 · 必填）
  5. （可选）把图嵌进 .pptx（加 --with-pptx 标志）

如果跳过第 3 步直接生成文字 PPT，结果会很丑，
仓库主会拒绝接受。
```

完整 onboarding：[onboarding-guide.md](./onboarding-guide.md)

## 完整规范 vs 简化版

- **完整版**（推荐）：按上面的工程流程
- **简化版**（PPT 临时草稿 / 内部使用）：可只输出 `.md` + `web.html`（无 `.pptx`），但 `.md` 永远不能省

## 完整方法论

[methodology.md](./methodology.md) —— 详细背景 + 类比 SDR / spec-driven development

## 模板

[templates/content.md.template](./templates/content.md.template) —— 新 case 的 content.md 起步模板

## 30 秒起步

1. **Fork** pretty-skills
2. **复制** `_模板/案例/` 到 `<领域>/<你的-case>/`
3. **填** `content.md`（每页 4-7 字段）
4. **生成** `web.html`（PPT 演示版）
5. **（可选）生成** `presentation.pptx`（用 `--with-pptx`）
6. **提 PR**

[完整 CONTRIBUTING 流程](../CONTRIBUTING.md)

---

**命名传统**：3F Content / Triple-Format Content Skill / 3FCS  
**来源**：2026-07-07 Mavis / huangrichao2020 讨论沉淀  
**v3.2 升级**（2026-07-08）：PPT 版 HTML 强制 + 真实 .pptx 可选