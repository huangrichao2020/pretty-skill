# 反例对照 · 文字 PPT vs 图 PPT

> **这个文件存在的目的**：让 pretty-skill 仓库的贡献者一眼看懂"为什么必须出图"。

---

## ❌ 反例 · 文字 PPT（agent 偷懒走的最短路径）

**生成方式**：
```python
# agent 偷懒代码（这就是朋友 agent 实际跑过的）
from pptx import Presentation
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])
tf = slide.shapes.add_textbox(...)
tf.text_frame.text = "团队协作 5 原则\n1. 透明\n2. 反馈\n3. 共担..."  # ← 全部文字
prs.save("presentation.pptx")  # 文件大小 ≈ 200 KB
```

**视觉结果**：
```
┌─────────────────────────────────┐
│                                 │
│  团队协作 5 原则                 │
│                                 │
│  1. 透明                        │
│  2. 反馈                        │
│  3. 共担                        │
│  4. 试错                        │
│  5. 复盘                        │
│                                 │
│         （白底纯文字）            │
└─────────────────────────────────┘
```

**问题**：
- 文件 ≈ 200 KB（无图证据）
- 视觉冲击力 = 0（一眼看上去是"提纲"，不是"设计稿"）
- AI 不友好（没有可消费的视觉信息）
- **3F Content 80% 价值丧失**

---

## ✅ 正例 · 图 PPT（3F Content 范式要求）

**生成方式**：
```python
# 正确路径
from pptx import Presentation
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[6])

# 关键：用 add_picture() 嵌入 AI 出图
slide.shapes.add_picture(
    "images/p3_teamwork_5_principles.png",  # matrix AI 生成的图
    left=Emu(0), top=Emu(0),
    width=prs.slide_width, height=prs.slide_height,
)
prs.save("presentation.pptx")  # 文件大小 ≈ 5 MB
```

**视觉结果**：
```
┌─────────────────────────────────┐
│  [精美设计稿]                     │
│                                  │
│   团队协作 5 原则                  │
│   ╱ ╱ ╱ ╱ ╱                      │
│                                  │
│  透明 ↔ 反馈 ↔ 共担 ↔ 试错 ↔ 复盘 │
│  (每个原则配图标 + 视觉化)         │
│                                  │
│         （背景渐变 + 图标）         │
└─────────────────────────────────┘
```

**优势**：
- 文件 ≈ 5 MB（含图证据）
- 视觉冲击力强（一眼看上去是"设计稿"）
- AI 友好（图嵌入 .pptx 的同时 .md 是真相源）
- **3F Content 价值完整**

---

## 直观对比

| 维度 | ❌ 文字 PPT | ✅ 图 PPT |
|---|---|---|
| 文件大小 | ~200 KB | ~5 MB |
| 视觉冲击力 | 0 | 强 |
| AI 可消费 | 部分（文字可 OCR） | 完全（.md + 图） |
| 3F Content 价值保留 | 20% | 100% |
| GitHub diff 可读 | ✅（文字） | ✅（.md 是真相） |
| 朋友看到会 | 觉得是"提纲" | 觉得是"PPT" |

---

## 为什么 agent 会走错路径

**根因**：3F Content README 列了 3 个文件要求 —— `.md` + `.pptx` + `.html`。**没说 F2/F3 必须是图**。

Agent 的最短路径：
```
写 .md → 用 text_frame 铺文字生成 .pptx → 完成
（绕开"调 AI 出图 API"这个重活）
```

**修复**：把所有"必须生图"写进 SKILL 头部 + CONTRIBUTING 拒绝标准 + 反例对照。

---

## 对贡献者说

如果你 PR 进来一份 200 KB 的 .pptx 全是文字 → **自动退 PR**。

不是我们苛刻 —— 是因为：
1. 文字 PPT 在仓库里 = 别人 fork 时也会偷懒复制 = 仓库质量崩盘
2. AI agent 看 pretty-skill 时 = 看到文字 PPT = 学到错误范式 = 全员传染
3. 用户的预期是"对 AI 友好的视觉稿" = 必须含图

**5 MB 图 PPT vs 200 KB 文字 PPT = 25 倍文件大小 = 100 倍视觉价值**。

按 3F Content 走完整流程（matrix AI 出图 → add_picture 嵌入）= **你的 PR 一定通过**。

---

**对照样本**：
- ❌ 反例：朋友 agent 跑出的丑文字 PPT（2026-07-08 已拒）
- ✅ 正例：`domains/ai-training/cartman-team-ai-agent-collab/presentation.pptx`（5.4 MB，含图）