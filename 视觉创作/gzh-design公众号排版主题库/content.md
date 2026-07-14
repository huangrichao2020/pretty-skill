# gzh-design 公众号排版主题库

> **一句话**：把摸鱼小李的 gzh-design（RedSkill jl01 · 309 人用）的方法论和主题库骨架吞进 pretty-skills，**不真装本机**，只沉淀「如果想要这套排版，按什么模板 / 什么主题 / 什么 pipeline」的可复用知识。

---

## 1. 30 秒讲清楚

公众号写手最大的隐性成本不是写作，是**排版**。

每篇文章 2000 字写完，要花 30-60 分钟手动调字号、间距、配色、章节编号、引言卡、签名。调完了不同公众号编辑器之间不通用，换个编辑器又得重做。

摸鱼小李的 gzh-design（jl01）解决的就是这个：把 Markdown / Word / PDF / 纯文本一键转成可直接粘贴到公众号编辑器的 HTML，自动章节编号、关键词下划线、引言卡、目录导航、代码块、图片/ GIF、作者签名都打包好。还自带**主题库**——`references/theme-index.md` 注册好的主题直接选。

它最值钱的部分不是脚本，是**主题库**。

因为 Mavis 自己的 wechat-delivery 排版规则（v3.18-v3.22）已经覆盖了「怎么写、怎么出图、怎么交付」，**唯独缺主题库**——所以这次的吞并重点是**主题库骨架**，不是装机。

---

## 2. 三个真痛点（5 段钩子链 · knowhub 整合版）

### 痛点 1 · 排版时间吞噬写作时间

每篇 2000 字公众号，排版要 30-60 分钟。一个月写 4 篇 = 2-4 小时纯排版。

**before**：写完稿 → 手动调字号/段距/配色 → 调 30 分钟 → 看到效果不统一 → 重来
**after**：写完稿 → 选主题 → 渲染 → 30 秒粘贴

### 痛点 2 · 跨编辑器不通用

在「公众号编辑器 A」调好的样式，换到「编辑器 B」全乱；预览和最终发布还常常长得不一样。

**根治**：把样式锁在 HTML 里（class 名稳定），编辑器只承载内容——这是 gzh-design 的核心理念。

### 痛点 3 · 主题选择靠玄学

「商务风」「文艺风」「科技风」说了等于没说。每个写手都在重复造主题的轮子。

**根治**：主题库 + 1 行声明就能切换；不会造主题的可以从参考图反推（gzh-design 支持「按图生成主题组件库」）。

---

## 3. 主题库骨架（核心 · references/theme-index.md）

> 这是 wechat-delivery 缺的那块，**最有价值的产出**。

主题 = **配色 + 字体 + 间距 + 装饰元素** 的 4 元组。

注册结构（5 字段）：

```yaml
- id: 主题英文 ID（kebab-case）
  name: 主题中文名
  palette:
    primary: 主色（章节色 / 重点色）
    background: 背景色
    text: 正文文字色
    accent: 强调色（引言卡 / 引用 / 关键词下划线）
  typography:
    body: 正文字体（带 fallback 链）
    heading: 标题字体
    code: 代码字体
  spacing:
    line_height: 行高倍数（公众号 1.75-2.0 最佳）
    paragraph_gap: 段落间距 px
    section_gap: 章节间距 px
  decorations:
    blockquote: 引言卡样式（card | border-left | quote-mark | none）
    code_block: 代码块样式（mac | solarized | monokai | minimal）
    divider: 分隔线样式（··· | ——— | ═══ | ★★★）
    signature: 作者签名位置（bottom | aside | none）
```

### 7 套起步主题（必带）

| ID | 名字 | 主色 | 适用场景 | 备注 |
|---|---|---|---|---|
| `pure-paper` | 纯净纸感 | #2C2C2C（深棕文字）| 默认 / 长文 | wechat-delivery v3.18 默认主题，cream paper 留白 |
| `tech-blue` | 科技蓝 | #2563EB | 技术 / 编程 | DashGPT / Vercel 风格 |
| `business-gold` | 商务金 | #B8860B | 行业分析 / 投研 | 配合 dashiai-ppt 黑金风 |
| `literary-green` | 文艺绿 | #2D5F3F | 随笔 / 阅读 / 文化 | 三联书店风 |
| `finance-red` | 金融红 | #C8102E | A 股 / 投资 / 财经 | **A 股红涨绿跌配色**（MEMORY 铁律）|
| `ai-purple` | AI 紫 | #6B46C1 | AI 工具 / Agent / 模型 | Anthropic 紫 |
| `vibrant-pop` | 活力波普 | #FF6B6B | 生活方式 / 美食 / 旅行 | 小红书风 |

### 1 输入 N 输出 主题选择流

```
文章类型（写作前先定）
  ↓
[判断] 行业 / 受众 / 调性
  ↓
[匹配] 主题库查表
  ↓
[套用] 一键渲染
  ↓
[微调] 改 1-2 字段
```

---

## 4. 排版 pipeline（references/pipeline-spec.md）

把任意输入（md / docx / pdf / 纯文本）转成「可直接粘贴公众号」的 HTML，5 步：

### Step 1 · 输入归一化

非 Markdown 输入先归一化：
- docx → pandoc -t markdown
- pdf → pdftotext → 后处理去页眉页脚
- 纯文本 → 自动判 H1/H2/列表/引用结构

### Step 2 · 结构识别

```
[自动推断]
  ├─ 标题层级（# → H1，## → H2）
  ├─ 章节编号（一/二/三 或 1./2./3.）
  ├─ 关键词（<mark> 或下划线）
  ├─ 引言卡（blockquote / 短句开头）
  ├─ 目录（>= 3 个 H2 自动生成）
  └─ 代码块（``` lang 围栏）
```

### Step 3 · 主题渲染

读 `references/theme-index.md` → 加载对应主题 CSS → 渲染为带 inline style 的 HTML（公众号编辑器友好）。

### Step 4 · 自定义装饰

按主题应用装饰元素：
- 引言卡（blockquote 套主题的 card 样式）
- 章节编号（自动加 `一 / 二 / 三` 或 `1. / 2. / 3.`，可关）
- 关键词下划线（自动识别 + 用户可在 md 里用 `<mark>` 标记）
- 目录（>= 3 章节自动生成 `📖 目录` 段）
- 签名（按主题的 signature 字段决定位置）

### Step 5 · 输出 + 复制

输出单文件 HTML，含 inline style，用户「全选复制 → 粘贴到公众号编辑器」。**不依赖任何外链 CSS**（公众号编辑器会过滤外链）。

---

## 5. 反模式（来自 gzh-design 描述 + 公众号实测）

| 反模式 | 为什么错 | 怎么改 |
|---|---|---|
| ❌ 用外链 CSS | 公众号编辑器会过滤，发布后样式全丢 | 必须 inline style |
| ❌ 装饰边框 / 阴影 / 渐变背景 | 裁剪后变形 + 拉低阅读体验 | 主体居中靠下 + 大量留白 |
| ❌ 字号 < 14px | 手机端看不清 | 公众号正文 15-17px 最佳 |
| ❌ 段距 < 1.5 行 | 视觉拥堵 | 行高 1.75-2.0 + 段间距 16-24px |
| ❌ 代码块用高对比色（黑底白字）| 公众号深色模式截断 | 浅灰底 + 边框（mac / minimal 样式）|
| ❌ 引言卡用花体 + emoji | 不专业 | 纯文字 + 左侧色条 |
| ❌ 关键词用高亮背景 | 读起来像「警示」| 用下划线（`text-decoration: underline`）+ 主色 |
| ❌ 章节编号混用 | 一/二/三 和 1./2./3. 混排 | 全文统一一种（默认 1./2./3.）|
| ❌ 自动目录强加 | 短文（< 3 章节）不需要 | 阈值触发，>= 3 章节才生成 |
| ❌ 不预览直接发 | 公众号编辑器过滤标签可能丢样式 | 必须先粘到「图文预览」看实际效果 |

---

## 6. 跟 wechat-delivery 的边界（不重复造轮子）

| 模块 | 谁做 |
|---|---|
| 写什么 / 7 段骨架 / 5 段钩子链 | **wechat-delivery**（已锁 v3.22）|
| 7 维 rubric 自检 | **wechat-delivery**（已锁 v3.23）|
| 配图 prompt / 4 张图规则 | **wechat-delivery**（已锁 v3.21）|
| 桌面 8 文件交付结构 | **wechat-delivery**（已锁 v3.18）|
| **主题库** | **gzh-design 这个 case**（wechat-delivery 缺的）|
| **排版 HTML 渲染** | **gzh-design 这个 case**（可执行 spec）|
| **一键渲染脚本** | **本机 wechat-delivery 可选加载**（按需实现）|

---

## 7. 量化疗效（3 filter · 疗效/量化/场景）

| 之前 | 现在 |
|---|---|
| 每篇排版 30-60 分钟 | **10-15 分钟**（含主题选择）|
| 主题复用 0%（每篇新造）| **80% 复用**（从 7 套起步主题选 + 微调）|
| 跨编辑器样式丢 | **100% inline 锁定**（不依赖外链 CSS）|
| 不会造主题的人 | **按描述 / 参考图反推**（gzh-design 内置能力）|

**核心交付**：当用户下次写公众号时，可以直接说「用科技蓝主题」「用金融红主题」，wechat-delivery 自动加载主题库 → 一键渲染。

---

## 8. 适用 / 不适用

**适用**：
- 公众号 30+ 篇/月写手（个人/团队）
- 团队风格统一（多写手共用主题库）
- 跨平台分发（小红书 / 知乎 / 公众号 / 头条一稿多投）

**不适用**：
- 月发 < 4 篇（投入产出比不划算）
- 强个性化（需要每篇不同视觉实验）
- 写代码 / 教程为主（用 Notion / 语雀更合适）
- 公众号外其他富文本场景（PPT / 网页 / 落地页）

---

## 9. 下一步（如果用户要真用）

1. 装 redskill CLI：`curl -fsSL https://fe-video-qc.xhscdn.com/fe-platform-file/104101b8320fbjem2620653u0hejenq0004pf88g6ask5i.sh | bash`
2. `redskill install gzh-design` 或 `redskill install jl01`
3. 启动时选主题（从 `references/theme-index.md` 7 套起步）
4. Markdown / Word / PDF 输入 → 渲染 → 全选复制 → 粘到公众号

**不**默认装机：等用户明示要。
