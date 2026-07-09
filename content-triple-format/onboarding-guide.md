# Agent Onboarding Guide

> **谁该读这个**：你是 agent，接到 PPT 任务，要给 pretty-skills 仓库或任何 3F Content 范式交付物做贡献。
> **读完这个你拿到**：一个**不能偷懒**的标准流程，照着做就能交付合格 PPT。

---

## ❗ 第一句话最重要

> **你接到 PPT 任务，第一步不是写 `.pptx`，也不是用代码铺文字。**
> **第一步是写 `.md`（content.md）。**

如果你跳过"AI 出图"步骤直接生成文字 PPT —— **结果是丑文字框**，仓库主会拒绝。

---

## 5 步标准流程（每步都不能跳）

### Step 1 · 写 content.md（必做 · 第一步）

每一页用 4-7 字段：

```markdown
## P{n} · {章节类型}-{主题}

- **标题**：
- **副标**：
- **章节类型**：（钩子 / 总纲 / 核心解法 / 深化 / 角色升级 / 收束）
- **核心主张**：
- **关键要点**：3-5 bullets
- **数据 / 数字**：
- **金句**：
- **童趣图标**：（出图用）
```

**每页 5-10 行。** 这是"数据"——AI 出图时 prompt 会基于它生成。

### Step 2 · 写 prompt（每页 60 行）

每页对应一个 prompt 文件，60 行内：
- 风格锁（必填）—— 马卡龙 / 古铜金 / 蓝白灰 / 自选
- 画面要点（自由布局）—— 不要堆字体铁律
- 中文用语
- 约束（16:9 / 2K / 无错字）

**反模式**：
- ❌ 在 prompt 里写 "X 色 强调 Y"（AI 会当文案画进去！）
- ❌ 锁死布局（让 AI 自由发挥）
- ❌ 超过 100 行（堆字体铁律禁锢 AI）

### Step 3 · 调 image_gen API 出图（**关键步骤**）

```bash
# matrix MCP example (or any image_gen: DALL-E / Midjourney / Stable Diffusion)
mavis mcp call matrix matrix_generate_image '{"prompt": "...", "aspect_ratio": "16:9", "resolution": "2K"}' 2>&1 | tail -10
```

**这一步不能跳** —— 跳了你只能出文字 PPT。

**出图后必做**：
- 保存 PNG 到 `images/p{n}_{name}.png`
- 记录 prompt 文件到 `prompts/p{n}_{name}.md`
- 这两份就是"图嵌入"的证据

### Step 4 · 用 python-pptx 嵌图生成 `.pptx`

```python
from pptx import Presentation
from pptx.util import Inches, Emu

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

blank = prs.slide_layouts[6]

for page in pages:
    slide = prs.slides.add_slide(blank)
    slide.shapes.add_picture(
        page["file"],
        left=Emu(0), top=Emu(0),
        width=prs.slide_width, height=prs.slide_height,
    )

prs.save("presentation.pptx")
```

**关键**：`add_picture()` 嵌图，**不是** `text_frame.add_paragraph()` 铺文字。

完整脚本：`~/.mavis/bin/build_pptx_v2.py`（支持 image / editable 双模式）

### Step 5 · 用 html-ppt-viewer 包图生成 `.html`

不要直接用 .md 转 HTML！必须用图：

```html
<div class="slide-thumb">
  <img src="images/p0_cover.png" />
</div>
```

完整模板：`domains/_template/case/` 或 `~/.mavis/skills/html-ppt-viewer/`

---

## ❌ 反模式清单（任何一条 = PR 退回）

| 反模式 | 结果 | 怎么修 |
|---|---|---|
| 跳过 step 3（不出图直接写 .pptx） | 文字 PPT（丑） | 必须调 image_gen API |
| 直接用 .md 转 .html | 纯文字网页（无图） | 必须用图嵌进 HTML |
| .pptx 内嵌图但用 .md 改文案没同步 | 3 件套文案不一致 | 以 .md 为唯一真相源 |
| 3 件套文件名不匹配（如 `case.pptx` + `index.html`） | 难以检索 | 必须同名同目录 |
| 提交 .pdf 替代 .md | PDF 不是纯文本，diff / 搜索 / AI 处理弱 | 必须用 .md |
| prompt 写满元注释（"X 色 强调 Y"） | AI 把元注释当文案画进去 | 元注释放进【风格锁】段，【画面要点】只描述内容 |

---

## ✅ 完整 checklist（PR 前必查）

```
□ Step 1: content.md 每页 4-7 字段齐全
□ Step 2: prompts/ 下有对应 prompt 文件
□ Step 3: images/ 下有 8 张 PNG（每页 1 张）
□ Step 4: presentation.pptx 用 add_picture() 嵌图
□ Step 5: web.html 用 <img src="..."> 嵌图
□ 3 件套齐全且文件名一致
□ README.md 写完
```

**任一项打 ✗ → 退回。**

---

## 你拿到什么（疗效）

按这个流程做完：
- **你交付**：3 件套完整 + AI 出图证据 + 工程可复现
- **仓库主拿到**：质量稳定的 PR，star 自然涨
- **LLM 拿到**：可消费的 .md（任何 AI agent 都能消化你的 PPT）
- **人类拿到**：视觉冲击力强的 PPT（不是文字框）

---

## 看到这一步你做到什么

1. **你不会偷懒成文字 PPT**（因为你已经知道丑）
2. **你交付更快**（流程已经清楚，不重复想"先做什么"）
3. **你 PR 通过率 100%**（流程符合 pretty-skills 标准）

---

## 详细规范

- [content-triple-format/README.md](./README.md) —— 完整范式
- [CONTRIBUTING.md](../CONTRIBUTING.md) —— PR 流程
- [README.md](../README.md) —— 项目总览

---

**记住：流程不可跳。第一步写 .md，第二步 prompt，第三步调 API 出图。**  
**不按这个流程 = 文字 PPT = 仓库主拒绝。**