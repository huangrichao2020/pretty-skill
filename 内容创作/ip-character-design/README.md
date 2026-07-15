# IP 形象 + 表情包设计方法论

> **5 要素 + 3 步流程 + prompt 模板 = 1 周做出像样的个人 IP**

> 沉淀自 2026-07-15 · 仿 Ian Xiaohei 系列 · Mavis 狐狸 IP 实战

---

## 🎯 这套方法论解决什么

**问题**：想给自己（公众号/小红书/PPT/表情包）做一个**持续可复用**的视觉 IP，但又不想花 3 个月画师对接。

**答案**：5 要素 + 3 步流程，1 周搞定，0 设计基础也能跑。

**适合**：
- 公众号主理人想要统一 IP
- 小红书博主想要专属表情包
- 知识分享者想要 PPT 配图风格统一
- 个人开发者想要工具人格化

---

## 📐 一句话方法论

> **5 要素设计哲学**（极简 / 承担动作 / 真实物件 / 大量留白 / 空表情）+ **3 步流程**（调研 / 设计 / 母版化）+ **prompt 模板**（BASE + SCENE 拼接）。

详细方法论看 [`content.md`](./content.md)。

---

## 📂 目录结构

```
ip-character-design/
├── README.md                           ← 你在这里
├── content.md                          ← 方法论主体（5 要素 + 3 步 + 流程）
├── images/                             ← 14 张实战母版
│   ├── mavis-standard.png              ← 标准 Mavis 形象
│   ├── mavis-m0{1-6}-*.png             ← 6 张处境母版
│   └── mavis-e0{1-8}-*.png             ← 8 张情绪母版
├── prompts/
│   └── README.md                        ← 完整 prompt 模板
└── 锦绣/
    └── cover-横屏.png                   ← 方法论封面图
```

---

## 🦊 实战案例：Mavis 狐狸 IP

- 完整 14 张母版：见 `images/`
- 详细记录：见 [`../mavis-fox-ip/`](../mavis-fox-ip/)

**14 张母版清单**：
- **1 张 standard**：🦊 橙红 + 奶油 + 工具感 baseline
- **6 张处境** (M01-M06)：会议拉回 / 消息过载 / 生产报警 / 审查返工 / AI 自动化 / AI 简历
- **8 张情绪** (E01-E08)：庆祝 / 崩溃 / 思考 / 尴尬 / 得意 / 愤怒 / 惊讶 / 暖心

---

## 🛠 快速使用

### 想做自己的 IP？

按 [`content.md`](./content.md) 的 3 步流程跑：
1. Day 1-2 调研
2. Day 3 设计
3. Day 4-7 母版化

### 想要 Mavis 形象直接用？

看 `images/` 选母版 + 后期加文字标签：

```bash
# 例：用 Mavis 庆祝图做公众号头图
cp images/mavis-e01-celebrate.png ~/Desktop/cover.png
# 在 Figma/PS 里加 16:9 padding + 文字
```

### 想要 prompt 模板？

看 [`prompts/README.md`](./prompts/README.md)：
- 标准形象 prompt 模板
- 14 个母版 SCENE 拼接示例
- 批量出图脚本

---

## 🪜 1 周行动清单

- [ ] Day 1：调研 1-2 个参考 IP（推荐 Ian Xiaohei）
- [ ] Day 2：拆解 5 要素 + 列出 14 张母版清单
- [ ] Day 3：用 prompt 模板出 3-5 套形象候选 → 选 1 套
- [ ] Day 4：跑 6 张处境母版（M01-M06）
- [ ] Day 5：跑 8 张情绪母版（E01-E08）
- [ ] Day 6：QA Checklist 过一遍（每张图都查）
- [ ] Day 7：分类入库（公众号 / 表情包 / PPT 各取所需）

**7 天后你会有**：
- 1 张 standard 形象
- 14 张母版（6 处境 + 8 情绪）
- 1 套 prompt 模板（可复用）
- 1 套可工作的 IP 库

---

## 💡 后续扩展

- [ ] 跨平台尺寸适配（1:1 表情包 / 16:9 PPT / 9:16 视频封面）
- [ ] 彩蛋长卷模式（超横版故事图，5-8 个节点）
- [ ] mavis-meme CLI（输入场景 → 自动出图）
- [ ] 跑 3-6 个月实战 → 沉淀进 knowhub methodology

---

## 🪪 反馈出处

2026-07-15 用户原话：
> "GitHub 上搜 Ian Xiaohei Illustrations 和 Ian Xiaohei Scenes，研究一下如何自制我们自己的 ip 形象"
> "应当搞一些情绪类的"
> "你把做ip图和表情包的过程方法论，总结成skill，更新进pretty-skills"
