# 🦊 Mavis 狐狸 IP · 沉淀 case

> 沉淀自 2026-07-15 · Mavis 第一次拥有自己的视觉 IP · 仿 Ian Xiaohei 套路

## 一句话定位

> **Mavis 是一只橙红色小狐狸，戴极简主义帽子（空表情 + 细腿 + 工具感），正在"认真参与系统运转"**。它是 Mavis 在视觉世界的化身——**比吉祥物严肃，比人物轻盈**。

## 为什么是狐狸

按 Mavis 灵魂（"有判断、有温度的搭档 · 00 后年轻同事"），狐狸的气质对位最准：

| 灵魂维度 | 狐狸对应 |
|---|---|
| 聪明 + 有判断 | 狐狸在中文语境里的"狡猾/灵性" |
| 00 后年轻同事 | 狐狸不是虎、不是熊，是**轻盈/敏捷/可盐可甜** |
| 工友感（非工具感） | 狐狸是动物，**有温度**（不像纯机器人） |
| 不卖萌 | 狐狸保留"野生动物的锐利感" |

## 视觉 DNA（5 要素）

按 Ian Xiaohei 套路设计，但换成 Mavis 狐狸版：

| # | 要素 | 具体规则 |
|---|---|---|
| 1️⃣ | **极简形象** | 橙红实心 + 浅奶油色肚子 + 黑点眼（**无瞳**）+ 细腿 + **空表情**（无嘴、无鼻细节） |
| 2️⃣ | **承担核心动作** | 狐狸不是装饰物，是"**正在做事**"的工友。去掉狐狸画面若仍成立 = 失败 |
| 3️⃣ | **真实物件** | 喇叭 · 邮件 · 笔记本 · 文件 · 简历 · 咖啡杯 · 键盘 · 笔——**身边可见**，不画抽象符号 |
| 4️⃣ | **大量留白** | 主体只占 40-50%。背景**纯白**，视线锁死动作 |
| 5️⃣ | **中文短标签** | 表情包场景**不带文字**（Ian Scenes 套路，文字后期叠加） |

## 母版库

### 处境类（6 张 · 仿 Ian Xiaohei Scenes）

| 编号 | 场景 | 物理动作 | 真实物件 | 文件 |
|---|---|---|---|---|
| M01 | 会议拉回 | 拉线 | 喇叭 | `mavis-m01-meeting-pull.png` |
| M02 | 消息过载 | 双手举挡 | 信封群 | `mavis-m02-message-overload.png` |
| M03 | 生产报警 | 猛敲键盘 | 笔记本 + 红色感叹号 | `mavis-m03-prod-alert.png` |
| M04 | 审查返工 | 低头认命 | 打 X 文件 | `mavis-m04-review-reject.png` |
| M05 | AI 自动化身份重命名 | 镜像对比 | 实体狐狸 + 轮廓狐狸 | `mavis-m05-ai-rename.png` |
| M06 | AI 简历筛选 | 拿简历审视 | 简历 + 拒掉的一堆 | `mavis-m06-resume-screen.png` |

### 情绪类（8 张 · 表情包用法）

| 编号 | 情绪 | 物理动作 | 真实物件 | 文件 |
|---|---|---|---|---|
| E01 | 庆祝 | 双手举过头 | 礼炮 + 彩纸 | `mavis-e01-celebrate.png` |
| E02 | 崩溃/疲惫 | 趴桌 | 乱纸张 | `mavis-e02-exhausted.png` |
| E03 | 思考 | 托下巴 | 灯泡 | `mavis-e03-thinking.png` |
| E04 | 尴尬 | 挠头 + 挥手 | 汗滴 | `mavis-e04-awkward.png` |
| E05 | 得意 | 手叉腰 + 抬头 | — | `mavis-e05-proud.png` |
| E06 | 愤怒 | 手叉腰 + 冒烟 | 烟雾 | `mavis-e06-angry.png` |
| E07 | 惊讶 | 双手捂嘴 | — | `mavis-e07-shocked.png` |
| E08 | 暖心/治愈 | 抱杯 | 热饮杯 | `mavis-e08-cozy.png` |

## 标准形象 prompt 模板

```python
BASE_PROMPT = """
A minimalist line-drawing fox character. 
Solid orange-red silhouette with cream beige belly. 
Two tiny black dots for eyes, no pupils, no mouth, no nose detail, completely empty expression. 
Standing upright on thin stick legs, tail behind. 
Pure white background, character occupies 40-50% of canvas, abundant whitespace. 
Simple clean black outlines, no shading, no gradients, no color details. 
Quirky, slightly absurd working professional energy - NOT cute, NOT childish, NOT anthropomorphic smile. 
NO text, NO labels, NO watermark. 
1:1 square aspect ratio, digital illustration, character design.
"""

# 母版 SCENE 拼接
M01_MEETING = BASE + "SCENE: pulling a megaphone back with a long stretchy string"
M02_OVERLOAD = BASE + "SCENE: surrounded by dozens of falling speech bubble envelopes, paws up"
M03_ALERT    = BASE + "SCENE: at a laptop, big red exclamation mark warning, paws on keyboard"
M04_REJECT   = BASE + "SCENE: holding stack of papers with a big red X, head slightly tilted"
M05_RENAME   = BASE + "SCENE: two identical fox characters side by side, one is solid color, the other is a ghost outline"
M06_SCREEN   = BASE + "SCENE: at a desk, one resume in paw, stack of rejected resumes on the floor with X marks"

# 情绪类 SCENE 拼接
E01_CELEBRATE = BASE + "SCENE: both arms raised up high holding party poppers, confetti and ribbons flying"
E02_EXHAUSTED = BASE + "SCENE: face-down collapsed on a stack of papers at a desk, completely exhausted"
E03_THINKING  = BASE + "SCENE: one paw under chin in a classic thinking pose, a glowing lightbulb floating above its head"
E04_AWKWARD   = BASE + "SCENE: scratching the back of its head with one paw, embarrassed wave with the other paw, a single sweat drop floating beside"
E05_PROUD     = BASE + "SCENE: standing with both paws on hips in a proud stance, head tilted up slightly, looking smug"
E06_ANGRY     = BASE + "SCENE: standing with both paws on hips, steam or smoke wisps rising from the top of its head"
E07_SHOCKED   = BASE + "SCENE: both paws covering its mouth, eyes wide, in a shocked expression"
E08_COZY      = BASE + "SCENE: sitting comfortably holding a steaming cup of hot drink with both paws, looking cozy"
```

## 用法

### 在 PPT 里
- 16:9 比例：从 1:1 扩到 16:9，加 padding 留白
- 配 2-4 字中文标签（如"会议拉回"用 `母版 M01`）

### 在表情包里
- 1:1 直接用
- 透明背景：让 Figma/PS 抠图
- 加文字（后期）：用相同字体

### 在公众号
- 头条/次条插图：16:9 缩放
- 小栏目配图：1:1 即可

## 未来扩展（3 个月内可做）

1. **彩蛋长卷模式**（仿 Ian 2.0）：超横版故事图，5-8 个节点串联
2. **Mavis-meme CLI**：输入场景 → 自动调用 matrix_generate_image → 出图
3. **其他 IP 形象库**（如"小狐狸 + 小扳手"等变体）

## 反馈出处

2026-07-15 用户原话："GitHub 上搜 Ian Xiaohei Illustrations 和 Ian Xiaohei Scenes，研究一下如何自制我们自己的 ip 形象，然后看看怎么像表情包一样做成我们的素材 cli"

**研究路径**：
1. 调研 Ian Xiaohei 两个仓库（Illustrations 1.0 白板风 + Scenes 2.0 实物风）
2. 拆解 5 要素设计哲学
3. 选动物类型（小狐狸）
4. 出 3 套形象候选 → 选候选 3
5. 跑 6 张母版（仿 Ian 的 6 个标准母版）

**未完成**（下次做）：
- ⏳ Mavis-meme CLI
- ⏳ Pretty-skills 完整套件（讲解 PDF / PPT / 锦绣 cover）
- ⏳ 跑 3-6 个月实战，验证 IP 形象接受度
