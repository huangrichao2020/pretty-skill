# oil-cover 小红书 AI 工具封面方法论

> **一句话定位**：把油老师的小红书 AI 工具封面方法论沉淀成可复用范式 · 一次成图 = 流量级

---

## 这个 case 是什么

**作者**：oil 欧呦 · 转录 + 方法论沉淀：Mavis
**生成日期**：2026-07-10
**风格**：手绘科教 · 马卡龙 5 色循环 · 工具类内容适配
**页数**：7 页
**所属领域**：视觉创作

## 核心论点

小红书 AI 工具封面 = 流量入口 · 一次生成真实、清楚、干净、精致 = 用户点击关键。oil-cover 的 5 大方法论支柱 + 2 种执行模式 + 12 项必填件 + 完整 SOP = 任何 AI 工具类内容按这套出封面 = 流量级。

## 适用场景

- 小红书 AI 工具实操内容（视频 / 截图 / 关键帧 → 封面）
- 任何需要"稳定 + 清楚 + 干净 + 精致 + 一次成图"封面的工具类内容
- 跨 agent 平台共享（Claude Code / Codex / Mavis 都能调）
- 想摆脱 AI 编造虚假界面截图 / 后贴字 / 拼贴感 难题的内容创作者

## 3F Content 必填件（v3.20 PDF 时代）

- ✅ `content.md` — 源文字
- ✅ `oil-cover小红书AI封面讲解.pdf` — PDF 讲解版（待生成）
- ✅ `images/` — AI 出图原图（待生成）
- ✅ `prompts/` — 出图 prompt 文件（待生成）
- ✅ `manifest.json` — 必填
- ⚠️ `presentation.pptx` — 可选
- ⚠️ `锦绣/` — v3.1 简化：2 封面 + slides/ + readme.md

## 核心方法论（精华 4 段）

### 1 · 5 大方法论支柱（缺一不可）

| 支柱 | 含义 | 验证问题 |
|---|---|---|
| 稳定 | 选帧 → 提示词 → 生图 全流程有 guard | 不靠运气 = 每次都能成功 |
| 清楚 | 标题措辞 + 主产品 Logo + 真实屏幕证据 | 三件齐全才算清楚 |
| 干净 | 风格克制 · 不堆装饰 · 留白充分 | 不廉价拼贴感 |
| 精致 | 商业品牌级完成度 · 直接可用于发布 | 用户第一眼认可 |
| 一次成图 | 生成完整画面含文字 · 不后贴字 / Logo / 拼图 | 流水线 0 后处理 |

### 2 · 2 种执行模式 + 持久化选择

- **模式一 · 脚本模式**（默认）：generate_oil_cover.py · ZenMux Gemini 选帧 + gpt-image-2 生图 · 需要 Python + ffmpeg + ZenMux key
- **模式二 · Agent 自主执行**：自身多模态视觉选帧 + 自带 image_gen 工具 · 无外部依赖
- 模式选择存 `~/.oil-cover/config.json` 的 `mode` 字段（script / agent-native）
- **设一次，以后不问**

### 3 · 12 项必填件（绝对不能违反）

- 触发 4 项 · 一次成图 3 项 · 内容干净 2 项 · 默认输出 1 项 · 资产保存 1 项 · 安全 1 项
- 任一违反 = 不收

### 4 · 默认入口 + 进阶参数

```
# 默认 90% 场景
python3 ~/.claude/skills/oil-cover/scripts/generate_oil_cover.py \
  --video "<视频路径>" \
  --title "<标题>" \
  --topic "<背景>"

# 默认不传 --aspect = 并行生成 3:4 + 4:3
```

## 跨引用

- [3F Content 范式](../../content-triple-format/)
- [PDF 讲解版规范](../../content-triple-format/case-pdf-spec.md)
- [本案例 prompt](./prompts/)
- [本案例图片](./images/)
- [本案例 PDF](./oil-cover小红书AI封面讲解.pdf)
- [本案例 manifest](./manifest.json)

## 贡献者

- oil 欧呦（原作者 · 封面方法论）
- @huangrichao2020（需求方 · 转化沉淀）
- @Mavis（方法论提炼 · pretty-skills 转化）