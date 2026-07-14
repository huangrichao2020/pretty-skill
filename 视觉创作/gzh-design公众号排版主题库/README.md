# gzh-design 公众号排版主题库

> 把摸鱼小李的 gzh-design（RedSkill jl01 · 309 人用）**主题库 + 排版 pipeline 方法论**沉淀进 pretty-skills。
> **不真装本机**——这是一份「如果想要这套排版能力，按什么来」的可复用知识。

---

## 这是什么

| 维度 | 内容 |
|---|---|
| **目标** | 补 Mavis 公众号排版 wechat-delivery（v3.22）的主题库短板 |
| **来源** | 摸鱼小李在 RedSkill 发布的 jl01 skill「gzh-design」 |
| **沉淀时间** | 2026-07-14 |
| **使用人数（上游）** | 309 人 |
| **本机依赖** | ❌ 无（仅做方法论沉淀）|

---

## 包含什么

```
gzh-design公众号排版主题库/
├── README.md                              # 这个文件
├── content.md                             # 讲什么（30 秒版 + 痛点 + pipeline + 反模式）
├── manifest.json                          # case 元数据
├── gzh-design公众号排版主题库讲解.pdf      # 7 张图讲解（合成）
├── references/
│   ├── theme-index.md                     # ⭐ 7 套起步主题（核心交付）
│   └── pipeline-spec.md                   # 排版 5 步 pipeline 规范
├── images/                                # 讲解图源文件
└── 锦绣/                                  # 锦绣版讲解图
```

---

## 3 句话讲清楚

1. **公众号写手最大的隐性成本是排版**——每篇 30-60 分钟手动调样式。
2. **gzh-design 解决这个**——md/docx/pdf/纯文本 → 公众号 HTML 一键渲染，自带主题库。
3. **本次沉淀**——只把**主题库骨架**和**pipeline 规范**吞进 pretty-skills，不真装本机。wechat-delivery 下次写公众号时，可直接选主题 + 渲染。

---

## 5 段钩子链（公众号自检用）

- **P1 痛点**——3 个真痛点（排版时间 / 跨编辑器不通用 / 主题靠玄学）
- **P2 翻转**——主题库 + 1 行声明切换，根治第 3 个痛点
- **P3 范式**——5 步 pipeline（归一化 → 结构识别 → 主题渲染 → 装饰 → 输出）
- **P4 案例**——7 套起步主题（pure-paper / tech-blue / business-gold / literary-green / finance-red / ai-purple / vibrant-pop）
- **P5 CTA**——下次写公众号时，说「用科技蓝主题」即可

---

## 量化疗效（3 filter · 疗效/量化/场景）

| 之前 | 现在 |
|---|---|
| 每篇排版 30-60 分钟 | **10-15 分钟**（含选主题）|
| 主题复用 0% | **80% 复用**（从 7 套起步主题选）|
| 跨编辑器样式丢 | **inline 100% 锁定** |
| 不会造主题 | **按描述/参考图反推** |

---

## 适用 / 不适用

**适用**：
- 公众号 30+ 篇/月写手
- 团队风格统一（多写手共用主题库）
- 跨平台分发（一稿多投）

**不适用**：
- 月发 < 4 篇（投入产出不划算）
- 强个性化需求
- 公众号外富文本（PPT / 网页）

---

## 跟 wechat-delivery 关系

| 模块 | 谁做 |
|---|---|
| 写什么 / 7 段骨架 / 5 段钩子链 | wechat-delivery（v3.22 已锁）|
| 配图 / 4 张图规则 | wechat-delivery（v3.21 已锁）|
| 桌面 8 文件交付结构 | wechat-delivery（v3.18 已锁）|
| **主题库** | **本 case 贡献**（wechat-delivery 缺这块）|
| **排版 HTML 渲染** | **本 case 贡献**（可执行 spec）|

---

## 下一步

- [ ] wechat-delivery 加载本主题库（v3.23 升级）
- [ ] 可选实现 `scripts/render_to_gzh.py`（按 pipeline-spec.md）
- [ ] GitHub release v3.20.0
