# IP 形象 + 表情包设计方法论

> **一句话**：用 **5 要素设计哲学** + **3 步流程** + **prompt 模板**，1 周内做出像样的个人 IP 形象 + 表情包库。

> **沉淀自**：2026-07-15 · 仿 Ian Xiaohei 系列 + Mavis 狐狸 IP 实战
> **位置**：`内容创作/ip-character-design/`
> **实战 case**：[`../mavis-fox-ip/`](../mavis-fox-ip/)（14 张母版）

---

## 📐 5 要素设计哲学（核心）

任何 IP 形象 + 表情包都按这 5 条设计。**违反任一条，效果立刻拉胯**。

| # | 要素 | 具体规则 | 反例（违反后会怎样） |
|---|---|---|---|
| 1️⃣ | **极简形象** | 单一实心色 + 2-3 个固定特征（眼/嘴/身材） | 复杂花纹 = 难复用 + 难记忆 |
| 2️⃣ | **承担核心动作** | 角色不是装饰物，**正在做事** | 站着不动的吉祥物 = 没人记得 |
| 3️⃣ | **真实物件** | 用身边可见的物件承载隐喻（咖啡杯/键盘/文件/灯） | 抽象符号 = "看不懂" |
| 4️⃣ | **大量留白** | 主体只占 40-50%，背景纯白/近白 | 满屏 = 视线散 + 印刷贵 |
| 5️⃣ | **空表情原则** | 角色脸永远是"空"（无嘴无鼻细节） | 笑/哭/怒画脸上 = 情绪定死，难复用 |

> **Why 5 要素**：Ian Xiaohei 实战验证过的，**5 条同时满足 = 像"工友"；违反任一 = 沦为吉祥物**。

---

## 🪜 3 步流程（按时间排）

### 步骤 1：调研 · 1-2 天

**目标**：找 1-2 个参考 IP（不要从 0 想象）。

**动作清单**：
- [ ] GitHub / Pinterest / 微博 / 小红书搜 `[关键词] illustrations` / `[关键词] scenes`
- [ ] 选 1 个**风格最像**的（不一定要完美）
- [ ] 拆解 5 要素，看对方怎么落
- [ ] 列出 3-5 个**母版场景**（借鉴对方的母版思路）

**推荐起点**：
- 极简怪诞：`helloianneo/ian-xiaohei-illustrations` + `ian-xiaohei-scenes`
- 国民 IP：小绿、小蓝（Line Friends）
- 公众号风：吾皇猫、巴扎黑

**输出物**：1 页调研笔记（参考 IP + 5 要素拆解 + 母版清单）

---

### 步骤 2：设计 · 1-2 天

**目标**：3-5 套形象候选 → 选 1 套定稿。

**动作清单**：
- [ ] 选动物/拟人/抽象类型（狐狸/猫/熊猫/机器人/工具人）
- [ ] 定核心特征（颜色 + 身材 + 表情 + 标志动作）
- [ ] 用 `matrix_generate_image` 出 3-5 套候选
- [ ] 对比 → 选 1 套（最像"工友"那套，不是最"可爱"那套）
- [ ] 锁定 standard prompt（下面有模板）

**关键决策**（直接给推荐）：
| 角色类型 | 调性 | 推荐场景 |
|---|---|---|
| 🦊 狐狸 | 聪明/工友感 | 内容创作者/独立开发者 |
| 🐱 猫 | 陪伴/独立 | 情感/生活类 |
| 🐼 熊猫 | 国宝/可盐可甜 | 国民向 |
| 🤖 机器人 | 工具/未来 | 极客/AI 类 |
| 🐻 熊 | 温暖/可靠 | 教育/儿童 |

**输出物**：`standard.png` + `standard-prompt.md`

---

### 步骤 3：母版化 · 2-3 天

**目标**：6 张处境 + 8 张情绪 = 14 张母版库。

**3.1 处境类母版（6 张必出）**：

适合"工作场景 + 处境表达"——公众号/PPT 配图。

| 编号 | 场景 | 物理动作 | 真实物件 |
|---|---|---|---|
| M01 | 会议拉回 | 拉线 | 喇叭 |
| M02 | 消息过载 | 双手举挡 | 信封群 |
| M03 | 生产报警 | 猛敲键盘 | 笔记本 + 红感叹号 |
| M04 | 审查返工 | 低头认命 | 打 X 文件 |
| M05 | AI 自动化身份 | 镜像对比 | 实体 + 轮廓 |
| M06 | 简历/任务筛选 | 拿审视 | 简历堆 + 拒掉堆 |

**3.2 情绪类母版（8 张必出）**：

适合"表情包 + 公众号小插图"。

| 编号 | 情绪 | 物理动作 | 真实物件 |
|---|---|---|---|
| E01 | 庆祝 | 双手举过头 | 礼炮 + 彩纸 |
| E02 | 崩溃/疲惫 | 趴桌 | 乱纸张 |
| E03 | 思考 | 托下巴 | 灯泡 |
| E04 | 尴尬 | 挠头 + 挥手 | 汗滴 |
| E05 | 得意 | 手叉腰 + 抬头 | — |
| E06 | 愤怒 | 手叉腰 + 冒烟 | 烟雾 |
| E07 | 惊讶 | 双手捂嘴 | — |
| E08 | 暖心/治愈 | 抱杯 | 热饮杯 |

**输出物**：`mavis-m0X-*.png`（6 张）+ `mavis-e0X-*.png`（8 张）

---

## 📝 Prompt 模板

### Base Prompt（标准形象）

```python
BASE_PROMPT = """
A minimalist line-drawing {动物名} character. 
Solid {主色} silhouette with {辅色} belly. 
Two tiny black dots for eyes, no pupils, no mouth, no nose detail, completely empty expression. 
Standing upright on thin stick legs, tail behind. 
Pure white background, character occupies 40-50% of canvas, abundant whitespace. 
Simple clean black outlines, no shading, no gradients, no color details. 
Quirky, slightly absurd working professional energy - NOT cute, NOT childish, NOT anthropomorphic smile. 
NO text, NO labels, NO watermark. 
1:1 square aspect ratio, digital illustration, character design.
"""
```

**填法示例**（Mavis 狐狸）：
- 动物名 = `fox`
- 主色 = `orange-red`
- 辅色 = `cream beige`

---

### 处境 SCENE 模板

```python
M01_MEETING  = BASE + "SCENE: pulling a megaphone back with a long stretchy string"
M02_OVERLOAD = BASE + "SCENE: surrounded by dozens of falling speech bubble envelopes, paws up"
M03_ALERT    = BASE + "SCENE: at a laptop, big red exclamation mark warning, paws on keyboard"
M04_REJECT   = BASE + "SCENE: holding stack of papers with a big red X, head slightly tilted"
M05_RENAME   = BASE + "SCENE: two identical characters side by side, one solid, one ghost outline"
M06_SCREEN   = BASE + "SCENE: at a desk, one paper in paw, stack of rejected papers on the floor with X marks"
```

**改法**：把 `SCENE: ...` 里的物件/动作换掉就行，BASE 别动。

---

### 情绪 SCENE 模板

```python
E01_CELEBRATE = BASE + "SCENE: both arms raised up high holding party poppers, confetti and ribbons flying"
E02_EXHAUSTED = BASE + "SCENE: face-down collapsed on a stack of papers at a desk, completely exhausted"
E03_THINKING  = BASE + "SCENE: one paw under chin in a classic thinking pose, a glowing lightbulb floating above"
E04_AWKWARD   = BASE + "SCENE: scratching the back of head with one paw, embarrassed wave with the other, a single sweat drop"
E05_PROUD     = BASE + "SCENE: standing with both paws on hips in a proud stance, head tilted up slightly, looking smug"
E06_ANGRY     = BASE + "SCENE: standing with both paws on hips, steam or smoke wisps rising from the top of head"
E07_SHOCKED   = BASE + "SCENE: both paws covering mouth, eyes wide, in a shocked expression"
E08_COZY      = BASE + "SCENE: sitting comfortably holding a steaming cup of hot drink with both paws, looking cozy"
```

---

## ✅ QA Checklist（出图后逐项检查）

| 项 | 检查点 | 不通过就 |
|---|---|---|
| 眼睛 | 黑点眼 + 无瞳 + 无嘴 | 重出 |
| 留白 | 主体 ≤ 50% 画面 | 重出 |
| 线条 | 单色黑线 + 无渐变 | 重出 |
| 表情 | 角色脸空（无嘴/鼻细节） | 重出 |
| 物件 | 真实可见物件（不抽象） | 重出 |
| 文字 | NO 文字标签 | 重出 |
| 比例 | 1:1 方形 | 调整 |
| 一致性 | 14 张同角色（颜色/身材/眼睛统一） | 漂移大就重出 |

---

## 🎯 实战案例

### 借鉴：Ian Xiaohei（小白 IP + 真实物件 + 物理动作）

- 仓库 1：[`helloianneo/ian-xiaohei-illustrations`](https://github.com/helloianneo/ian-xiaohei-illustrations) — 白板手绘风（1.0）
- 仓库 2：[`helloianneo/ian-xiaohei-scenes`](https://github.com/helloianneo/ian-xiaohei-scenes) — 真实物件风（2.0）
- 核心：小黑 IP = 黑色实心 + 白点眼 + 细腿 + 空表情 + 大量留白

### 落地：Mavis 狐狸 IP

- 标准形象：橙红狐狸 + 奶油肚子 + 黑点眼 + 工具感（手拿咖啡杯 + 一手叉腰）
- 14 张母版：6 张处境 + 8 张情绪
- 文件位置：[`../mavis-fox-ip/`](../mavis-fox-ip/)

### Mavis 14 张母版清单

| 编号 | 类型 | 情绪/场景 |
|---|---|---|
| standard | 标准 | 标准形象 baseline |
| M01 | 处境 | 会议拉回 |
| M02 | 处境 | 消息过载 |
| M03 | 处境 | 生产报警 |
| M04 | 处境 | 审查返工 |
| M05 | 处境 | AI 自动化身份重命名 |
| M06 | 处境 | AI 简历筛选 |
| E01 | 情绪 | 庆祝 |
| E02 | 情绪 | 崩溃/疲惫 |
| E03 | 情绪 | 思考 |
| E04 | 情绪 | 尴尬 |
| E05 | 情绪 | 得意 |
| E06 | 情绪 | 愤怒 |
| E07 | 情绪 | 惊讶 |
| E08 | 情绪 | 暖心/治愈 |

---

## 🔁 复用流程

下次做新 IP 时（任何角色类型），按这个方法论 1 周内跑完：

```
Day 1-2  调研：找 1-2 个参考 IP，拆解 5 要素
Day 3    设计：3-5 套形象候选 → 选 1 套
Day 4-5  处境母版：6 张必出
Day 6-7  情绪母版：8 张必出
```

**14 张母版完成后**：以后每次需要配图/表情包，**直接选母版改 prompt**，5 分钟出图。

---

## ⚠️ 踩坑记录

| 坑 | 表现 | 解决 |
|---|---|---|
| 风格漂移 | 6 张处境里有的偏可爱有的偏怪诞 | 严格锁 BASE prompt，不动 |
| 多余文字 | AI 自动加 "REF SHEET" / "v1.0" | prompt 里强写 "NO text, NO labels, NO watermark" |
| 卖萌失控 | AI 画"小可爱"而非"工友" | 加 "NOT cute, NOT childish, NOT anthropomorphic smile" |
| 表情失控 | AI 给角色画笑/哭/怒 | 加 "no mouth, completely empty expression" |
| 满屏失控 | 主体占 80%+ 画面 | 加 "character occupies 40-50% of canvas" |
| 颜色失控 | AI 用红/绿/蓝混杂 | 限制主色/辅色 + "no gradients, no color details" |

---

## 💡 下一步扩展

- [ ] 彩蛋长卷模式（超横版故事图，5-8 个节点串联）
- [ ] mavis-meme CLI（输入场景 → 自动调用 matrix 出图）
- [ ] 跨平台尺寸适配（1:1 表情包 / 16:9 PPT / 9:16 视频封面）
- [ ] 跑 3-6 个月实战，验证 IP 接受度

---

## 🪪 反馈出处

2026-07-15 用户原话：
> "GitHub 上搜 Ian Xiaohei Illustrations 和 Ian Xiaohei Scenes，研究一下如何自制我们自己的 ip 形象，然后看看怎么像表情包一样做成我们的素材 cli"
> "应当搞一些情绪类的"
> "你把做ip图和表情包的过程 方法论，总结成skill，更新进pretty-skills"

**关键决策**：
- 借鉴：Ian Xiaohei 系列（5 要素 + 真实物件套路）
- 动物：🦊 狐狸（气质对位 Mavis 灵魂）
- 情绪：8 张必出（庆祝/崩溃/思考/尴尬/得意/愤怒/惊讶/暖心）
- 沉淀：pretty-skills case `ip-character-design`
