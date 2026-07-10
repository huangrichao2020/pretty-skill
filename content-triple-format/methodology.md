# 3F Content 方法论

## 起源

2026-07-07 Mavis 在 huangrichao2020 提问「上传的每个 PPT 都应该有 .md」之后，把这个想法正式命名为：

**Triple-Format Content Skill（3F Content / 3FCS）**

## 核心思想

**数据与表示分离** —— 软件工程经典思想应用到内容领域。

```
        单源真相（spec）
              │
              ↓
   ┌─────────┬─────────┐
   │         │         │
 .md        .pptx     .html
   │         │         │
   └─────────┼─────────┘
              │
       3 个不同表示
```

- **`.md` 是数据**（纯文本 / 可 diff / 可 grep / 可被 LLM 消费）
- **`.pptx` / `.html` 是表示**（视觉演示）
- **以 `.md` 为单一真相源**：任何 3 件套文案有出入，`.md` 为准

## 类比

- **SDR (Software Defined Radio)** —— 数据 vs 表示分离 → 内容 vs 模板分离
- **spec-driven development** —— 写 spec → generate code → 同样 spec → 同样 code
- **JAMStack** —— Markdown / 数据当 source of truth + 静态生成为多种输出
- **headless CMS** —— 内容是数据，前端是表现

## 真实案例

### AI狼群战法（团队 AI Agent 协作）

- 8 页 PPT
- **`.md`**：人类 + AI 都读的源文字（每页 4-7 字段）
- **`.pptx`**：21.8 MB · PowerPoint 双击打开
- **`.html`**：浏览器直接看，键盘 ← → 翻页
- **疗效**：0 返工 · 内容能被任何 AI 工具消化

### 社交电商掘金术（社交电商 × 两层拆解法）

- 8 页 PPT
- **`.md`**：含 41 场景 / 6 板块 / 3 类型 / 90 天落地的全部信息
- **`.pptx`**：19.3 MB
- **`.html`**：浏览器阅读
- **疗效**：skill 升级实战验证（vs 修复前的 25% 返工）

## 反模式 vs 正例

### ❌ 反例 1：`.md` 是 prompt 装饰指令

```markdown
## P1 · 破局钩子
（珊瑚粉 #FF6B9D 强调 X）
（wobbly outlines 涂鸦线）
（童趣图标：链条断裂）
```

→ 这不是 `.md`，是出图指令。

### ✅ 正例 1：`.md` 是真内容

```markdown
## P1 · 破局钩子 — 3 大症状

- **标题**：「每个人都在用 AI，但团队效能提升了吗？」
- **章节类型**：破局钩子
- **核心主张**：单点效率提升 ≠ 团队效能
- **关键要点**：
  - 上下文断裂：每次对话割裂、信息无法共享
  - 零资产沉淀：每次新建对话 AI 都是「出厂设置」
  - 1+1<2：个人加法、团队摩擦
- **数据 / 数字**：1 个工程师至少 4-5 轮 ChatGPT 对话
- **金句**：「一个上午过去了，又来了一个需求。」
- **童趣图标**：断裂链条 / 空白工厂 / 反向箭头 / 叹气小人
```

→ 这是真内容。AI 读这段能直接复述 / 翻译 / 改写。

### ❌ 反例 2：3 件套不齐全

```
<case>/
├── content.md
└── presentation.pptx    ← 缺 .html
```

→ 不收。3 件套必须齐全。

### ✅ 正例 2：3 件套齐全

```
<case>/
├── content.md           ← F1
├── presentation.pptx    ← F2
└── xxx讲解.pdf          ← F3（v3.19 替代 web.html）
```

## 工程流程

```
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
6. build_case_pdf.py 渲染 → xxx讲解.pdf
   ↓
7. 用 content.md 反查 .pptx/.html（如有出入以 .md 为准）
   ↓
8. 3 件套归档 → domains/<area>/<case>/
```

## 适用范围

- ✅ 培训课件 / 知识沉淀 / 卡脖子分析长图
- ✅ 往公开仓库贡献内容
- ✅ 自媒体内容素材源
- ✅ 任何"要让别人再看"的内容
- ⚠️ 内部演示草稿 → 可选
- ❌ 时间不允许三件套的临时草稿
- ❌ 内容完全不能公开（合规/隐私）

## 触发词

| 用户说 | 触发 |
|---|---|
| "做 PPT / 课件 / 演示稿" | ppt-orchestrator → 3 件套输出 |
| "上传到 xxx 仓库" | content-triple-format |
| "AI 友好 / LLM 友好" | content-triple-format |
| "把 PPT 转 markdown" | content-triple-format (F1 reverse) |

## 来源

- 2026-07-07 huangrichao2020 提出想法 → Mavis 命名 3F Content
- 实战：AI狼群战法 + 社交电商掘金术 同时升级为 3 件套
- 类比：SDR / spec-driven development / JAMStack / headless CMS