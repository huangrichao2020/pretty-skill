# 主题库索引（Theme Index · 起步 7 套）

> **用途**：wechat-delivery 公众号写手配主题用。每个主题 = 配色 + 字体 + 间距 + 装饰 4 元组。
> **加载方式**：wechat-delivery Step 2 写完后，从这里选 1 个主题 → 调 1-2 字段 → 渲染。
> **如何扩展**：照这个 YAML 格式往下加 1 段即可。

---

## 7 套起步主题

### 1. `pure-paper` · 纯净纸感（**默认 · 长文必选**）

```yaml
id: pure-paper
name: 纯净纸感
palette:
  primary: '#8B6F47'        # 深棕主色
  background: '#FAF7F2'     # cream paper
  text: '#2C2C2C'           # 深棕文字
  accent: '#D4A574'         # 浅棕强调
typography:
  body: '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif'
  heading: '"Source Han Serif SC", "Noto Serif CJK SC", serif'
  code: '"SF Mono", "Menlo", "Consolas", monospace'
spacing:
  line_height: 1.9
  paragraph_gap: 20
  section_gap: 32
decorations:
  blockquote: card
  code_block: mac
  divider: '···'
  signature: bottom
```

**适用**：默认 / 长文 / 知识科普 / 个人观点。**最安全**。
**反例**：金融 / 科技 / 二次元主题文章会显得太「佛」。

---

### 2. `tech-blue` · 科技蓝

```yaml
id: tech-blue
name: 科技蓝
palette:
  primary: '#2563EB'        # Tailwind blue-600
  background: '#FFFFFF'
  text: '#1F2937'           # gray-800
  accent: '#3B82F6'         # blue-500
typography:
  body: '"Inter", "PingFang SC", sans-serif'
  heading: '"Inter", -apple-system, sans-serif'
  code: '"JetBrains Mono", monospace'
spacing:
  line_height: 1.75
  paragraph_gap: 18
  section_gap: 28
decorations:
  blockquote: border-left
  code_block: solarized-light
  divider: '———'
  signature: aside
```

**适用**：技术 / 编程 / AI 工具 / 模型介绍。
**反例**：金融分析（蓝绿色彩不够「权威」）。

---

### 3. `business-gold` · 商务金

```yaml
id: business-gold
name: 商务金
palette:
  primary: '#B8860B'        # 深金（暗金）
  background: '#F8F5F0'     # 浅米
  text: '#1A1A1A'
  accent: '#DAA520'         # 金色 goldenrod
typography:
  body: '"Source Han Serif SC", "Georgia", serif'
  heading: '"Source Han Serif SC", serif'
  code: '"SF Mono", monospace'
spacing:
  line_height: 1.85
  paragraph_gap: 22
  section_gap: 36
decorations:
  blockquote: quote-mark
  code_block: minimal
  divider: '═══'
  signature: bottom
```

**适用**：行业分析 / 投研报告 / 商业评论 / 财富类。
**反例**：生活方式 / 美食（太正式）。

---

### 4. `literary-green` · 文艺绿

```yaml
id: literary-green
name: 文艺绿
palette:
  primary: '#2D5F3F'        # 三联书店绿
  background: '#F5F2E8'     # 旧纸色
  text: '#1F2D24'
  accent: '#6B8E23'         # 橄榄绿
typography:
  body: '"Source Han Serif SC", "KaiTi", serif'
  heading: '"Source Han Serif SC", serif'
  code: '"Menlo", monospace'
spacing:
  line_height: 2.0
  paragraph_gap: 24
  section_gap: 40
decorations:
  blockquote: quote-mark
  code_block: minimal
  divider: '★★★'
  signature: bottom
```

**适用**：随笔 / 阅读 / 文化 / 历史 / 哲学。
**反例**：快讯 / 教程 / 商业（太慢）。

---

### 5. `finance-red` · 金融红（A 股配色铁律）

```yaml
id: finance-red
name: 金融红
palette:
  primary: '#C8102E'        # A 股红涨
  background: '#FFFFFF'
  text: '#1A1A1A'
  accent: '#1A8F4E'         # A 股绿跌（注意是跌色！）
typography:
  body: '"PingFang SC", "Microsoft YaHei", sans-serif'
  heading: '"Source Han Sans SC", sans-serif'
  code: '"SF Mono", monospace'
spacing:
  line_height: 1.8
  paragraph_gap: 20
  section_gap: 32
decorations:
  blockquote: border-left
  code_block: minimal
  divider: '———'
  signature: bottom
```

**适用**：A 股 / 投资 / 财经 / 行业研报。
**⚠️ 铁律**：**A 股红涨绿跌**（跟欧美相反）—— Mavis MEMORY 铁律第 1 条，错了会扣分。

---

### 6. `ai-purple` · AI 紫

```yaml
id: ai-purple
name: AI 紫
palette:
  primary: '#6B46C1'        # Anthropic 紫
  background: '#FAF8FF'     # 极浅紫
  text: '#1F1B2E'
  accent: '#9333EA'         # purple-600
typography:
  body: '"Inter", "PingFang SC", sans-serif'
  heading: '"Inter", sans-serif'
  code: '"JetBrains Mono", monospace'
spacing:
  line_height: 1.75
  paragraph_gap: 18
  section_gap: 28
decorations:
  blockquote: card
  code_block: monokai
  divider: '╌╌╌'
  signature: aside
```

**适用**：AI 工具 / Agent / 模型评测 / prompt 工程。
**反例**：金融 / 传统行业（紫色容易显「不严肃」）。

---

### 7. `vibrant-pop` · 活力波普

```yaml
id: vibrant-pop
name: 活力波普
palette:
  primary: '#FF6B6B'        # 小红书珊瑚红
  background: '#FFFAF0'     # 浅米黄
  text: '#2D2D2D'
  accent: '#4ECDC4'         # 薄荷绿
typography:
  body: '"PingFang SC", "Microsoft YaHei", sans-serif'
  heading: '"Noto Sans SC", sans-serif'
  code: '"SF Mono", monospace'
spacing:
  line_height: 1.75
  paragraph_gap: 18
  section_gap: 28
decorations:
  blockquote: quote-mark
  code_block: mac
  divider: '✦✦✦'
  signature: bottom
```

**适用**：生活方式 / 美食 / 旅行 / 母婴 / 美妆。
**反例**：技术 / 商业 / 财经（太「活泼」）。

---

## 选择流程（1 输入 N 输出）

```
Step 1 · 问自己 3 个问题
  ├─ 行业是？（技术 / 商业 / 文化 / 金融 / AI / 生活）
  ├─ 受众期待？（专业 / 通俗 / 文艺 / 活泼）
  └─ 文章长度？（< 1000 字 / 1000-3000 字 / > 3000 字）
Step 2 · 查表
  ├─ 行业 = 技术 → tech-blue
  ├─ 行业 = 商业 + 受众 = 专业 → business-gold
  ├─ 行业 = 文化 → literary-green
  ├─ 行业 = A 股 → finance-red（铁律）
  ├─ 行业 = AI → ai-purple
  ├─ 行业 = 生活 → vibrant-pop
  └─ 不确定 → pure-paper（永远不出错）
Step 3 · 微调
  └─ 改 1-2 字段（行高 / 段距 / 装饰）
Step 4 · 渲染
  └─ 输出 HTML
```

---

## 如何扩展主题

照着 YAML 格式往下加 1 段：

```yaml
- id: 你的主题 ID
  name: 你的主题名
  palette: {...}
  typography: {...}
  spacing: {...}
  decorations: {...}
```

**4 元组要一起设计**，不然会出现「金融红色 + 文艺字体 + 波普分隔线」的不和谐组合。

---

## 反模式 · 主题设计踩坑

- ❌ 主色饱和度 > 80% → 刺眼（公众号背景白，纯色块伤眼）
- ❌ 文字和背景对比度 < 4.5:1 → 不达 WCAG AA 标准
- ❌ 中文字体用「Times New Roman」 → 渲染乱
- ❌ 行高 < 1.5 或 > 2.5 → 过密或过疏
- ❌ 装饰超过 3 种 → 视觉嘈杂
- ✅ 主色饱和度 50-70% + 文字对比度 ≥ 7:1 + 行高 1.75-2.0
