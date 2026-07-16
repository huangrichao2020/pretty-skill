# scroll-world 滚动驱动相机 · Mavis 工具栈适配

> **来源**：[oso95/scroll-world](https://github.com/oso95/scroll-world) · 2850 stars · 2026-07-06
> **原项目**：Anthropic/agent 生态 · 适配 Claude Code / Codex / 20+ agent
> **Mavis 改造**：matrix MCP 替代 higgsfield + ffmpeg 编码 + vanilla JS scrub engine 保留
> **沉淀时间**：2026-07-17

---

## 一句话定位

**滚动驱动相机**的着陆页生成 skill —— scroll 位置 = 相机时间，预渲染 N 段场景图 + (2N-1) 段相机视频，**首尾帧锁定**保证无缝飞行。比 H5 翻页更进化的视觉体验（连续飞行 vs 切换幕）。

## 核心机制

```
用户滚动 (scroll position)
  ↓
[scrub-engine.js] 0.0 ~ 1.0
  ↓
映射到 N 张视频 [dive_0, conn_0, dive_1, conn_1, ..., dive_{N-1}]
  ↓
每段视频在 scroll 范围内播放一遍
  ↓
视觉 = 相机在 N 段场景中连续飞行（无切）
```

**2N-1 段视频** = N 段 dive 视频（从外景飞入内景）+ (N-1) 段 connector 视频（内景之间穿越）。

## 核心难点：seam frame-identical

**最关键规则**：相邻视频的接缝必须**首尾帧完全一致**，否则会"跳一下"破坏连续感。

**原 higgsfield 方案**：`seedance_2_0 --start-image --end-image` 同时锁定首尾两帧。

**matrix MCP 限制**：`matrix_gen_videos` 的 `input_image` + `reference_type` **只能锁 1 端**（first_frame / last_frame / subject）。

**Mavis 适配方案**（2 段拼接 + crossfade）：

```
dive_clip 锁 last_frame = 场景 A 内部帧
   ↓
[crossfade 500ms]
   ↓
connector_clip 锁 first_frame = 场景 A 内部帧（同上）
   ↓
[crossfade 500ms]
   ↓
dive_clip 锁 last_frame = 场景 B 内部帧
```

**接受近似的 seam**：matrix 2 段拼接不能保证 100% frame-identical，但 crossfade 500ms 视觉上接近无缝（人类感知阈值 ~100ms 帧间差）。

## 与同类方法对比

| 维度 | 普通 PPT 翻页 | H5 滑动（24 幕切换） | scroll-world 连续飞行 |
|---|---|---|---|
| 视觉感受 | 切换幕 | 切换幕 | 连续飞行 |
| scroll 作用 | 跳到下一幕 | 翻到下一幕 | 驱动相机时间 |
| 视频数 | 0 | 0 | 2N-1 段 |
| 核心难点 | 排版 | 横屏适配 | seam frame-identical |
| 实现工具 | dashiai-ppt | viewport + 触屏滑动 | matrix MCP + ffmpeg + scrub engine |
| 适用 | 静态作品 | 22 幕 talk | 6-8 段品牌沉浸体验 |

## 5 步工作流（Mavis 工具栈版）

| 步 | 名称 | 关键 |
|---|---|---|
| 0 | Bootstrap | ffmpeg / ffprobe on $PATH · MCP matrix 已配置 · 准备 prompts / assets 目录 |
| 1 | Interview | subject + brand_name + palette + tone + N sections 名称 + 是否 mobile（影响 2× 信用成本） |
| 2 | 出 N 张场景图 | `matrix_generate_image` × N 并行 · 同一段 style preamble · aspect 3:2 · 2K |
| 3 | 出 2N-1 段视频 | `matrix_gen_videos` × (2N-1) 串行 · 每段 8s · reference_type=last_frame 或 first_frame |
| 4 | 拼装 + 编码 | ffmpeg concat 拼接 + crossfade 500ms + h264 mp4 web 编码 |
| 5 | 落地页 | 用 `index-template.html` 模板 + `scrub-engine.js`（vanilla JS 不动） |

详细 MCP 调用见 `matrix-pipeline.md`。

## 关键代码

### 1. Style preamble（必填 · byte-for-byte 一致）

```text
Isometric low-poly 3D diorama floating as a small rounded island on a plain solid
[BG_HEX] background with a soft contact shadow beneath it. Soft matte clay 3D render,
rounded toy-model shapes, gentle warm studio lighting, soft long shadows, tilt-shift
miniature look. Cohesive color palette of [PALETTE]. Highly detailed, centered
composition, absolutely no text, no letters, no numbers, no logos.
```

**为什么 byte-for-byte 一致**：是让 N 张场景图视觉连续的关键。任何 prompt 差异都会让场景看起来"不是一个世界"。

### 2. matrix MCP 出图（N 张并行）

```javascript
// Mavis 通过 mavis mcp call matrix matrix_generate_image
{
  "requests": [
    {
      "prompt": "${style_preamble}\n\nSection: ${name}\n${specific_description}",
      "aspect_ratio": "3:2",
      "resolution": "2K"
    }
    // ... × N sections
  ]
}
```

### 3. matrix MCP 出视频（2N-1 段串行）

```javascript
// Dive clip: 锁 last_frame = 场景内部帧
{
  "requests": [{
    "prompt": "Camera flying into the [section] interior, smooth cinematic motion",
    "input_image": { "file": "${still_$N.png}" },  // 场景图作为参考
    "reference_type": "last_frame",  // 锁尾帧
    "duration": 8,
    "resolution": "768P"
  }]
}

// Connector clip: 锁 first_frame = 上一段内部帧
{
  "requests": [{
    "prompt": "Camera flying through the [scene transition]",
    "input_image": { "file": "${dive_$N_last_frame.png}" },  // 上一段尾帧
    "reference_type": "first_frame",  // 锁首帧
    "duration": 8,
    "resolution": "768P"
  }]
}
```

### 4. ffmpeg 拼接（接受近似的 seam）

```bash
# 提取每段视频首尾帧（用于 crossfade）
for i in $(seq 0 $((N-1))); do
  # Dive clip 末帧 → connector clip 首帧
  ffmpeg -sseof -0.1 -i dive_$i.mp4 -frames:v 1 -y dive_${i}_end.png
done

# crossfade 拼接所有视频
ffmpeg \
  -i dive_0.mp4 -i conn_0.mp4 -i dive_1.mp4 -i conn_1.mp4 ... \
  -filter_complex "
    [0:v][1:v]xfade=transition=fade:duration=0.5:offset=7.5[v01];
    [v01][2:v]xfade=transition=fade:duration=0.5:offset=15.5[v012];
    ...
  " \
  -c:v libx264 -crf 23 -preset medium -pix_fmt yuv420p \
  final.mp4
```

### 5. scrub engine 用法（vanilla JS · 不动）

```html
<div id="world"></div>
<script src="scrub-engine.js"></script>
<script>
mountScrollWorld(document.getElementById('world'), {
  brand: { name: 'Pearl & Co.', href: '#top' },
  diveScroll: 1.3,  // 视口高度 / 每段 dive
  connScroll: 0.9,  // 视口高度 / 每段 connector
  sections: [
    { id: 'sceneA', label: 'The Farms',
      still: 'assets/sceneA.webp',
      clip: 'assets/vid/dive_0.mp4',
      eyebrow: '起源', title: 'The Farms', body: '...', tags: [...] },
    // ... × N
  ],
  connectors: [
    'assets/vid/conn_0.mp4',
    'assets/vid/conn_1.mp4',
    // ... × N-1
  ]
});
</script>
```

## 反模式（必避坑）

| 反模式 | 后果 | 正确做法 |
|---|---|---|
| Style preamble 每次改字 | 场景视觉不连续 | byte-for-byte 一致 + 替换 [BG_HEX]/[PALETTE] 占位 |
| N 段场景并行出 prompt 不同 | "不是一个世界" | 同一段 preamble + 段名/描述做差异 |
| 忽略 seam frame-identical | 视觉跳一下破坏连续感 | 2 段拼接 + crossfade 500ms |
| 视频分辨率 1080P + 10s 组合 | matrix 拒绝 | 768P + 8s 或 1080P + 6s |
| 同步等所有出图 | 时间 × N | 并行 5/批（matrix limit） |
| 没用 ffmpeg 拼装直接播放 (2N-1) 段 | 视频间有黑屏/白屏 | ffmpeg xfade crossfade 拼接 |
| 不知道 matrix 一次只能锁 1 端 | 试图同时锁首尾 | 拆 2 段 + crossfade |
| mobile clip 跟 desktop 同 1080P | 流量翻倍 | 单独出 720p mobile 编码 |

## 工具栈对照

| 环节 | 原 higgsfield 方案 | Mavis 适配方案 |
|---|---|---|
| 场景图 | `higgsfield generate create gpt_image_2` | `matrix_generate_image` (3:2, 2K) |
| Dive 视频 | `higgsfield seedance_2_0 --start-image <still> --end-image <internal>` | `matrix_gen_videos` `reference_type=last_frame` + input_image=still |
| Connector 视频 | `higgsfield seedance_2_0 --start-image <dive_end> --end-image <next_dive_start>` | `matrix_gen_videos` `reference_type=first_frame` + input_image=prev_dive_end + 2 段拼接 + crossfade |
| 编码 | ffmpeg 同 | ffmpeg 同（保留） |
| Scrub engine | vanilla JS 同 | vanilla JS 同（保留） |

## 适用 / 不适用

**适用**：
- 6-8 段的品牌沉浸体验（5 段太少没沉浸感，10 段太长疲劳）
- landing page / hero / 1-2 页品牌故事
- 已有品牌调性（颜色 + 视觉）可以稳定出图

**不适用**：
- 单纯 22 幕 talk（用 H5 滑动翻页）
- 静态文档/手册（用 dashiai-ppt）
- 公众号长文（用 wechat-delivery 5 段钩子链）
- 不接受近似 seam 的场景（matrix 限制 — 但 99% 场景 crossfade 都够用）

## 用户拿到后

- 拿到任何品牌/主题 → **1-2h 出 1 个滚动相机飞行 landing page**
- 6-8 段沉浸场景 + 触屏/滚轮/键盘都能飞
- 桌面 1920×1080 + 移动 720p 适配
- 完整代码（matrix pipeline + scrub engine）+ 模板（index-template.html）

## 完整 MCP 调用 sequence

见 `matrix-pipeline.md`（详细步骤 + 5 段小节）。

## 关键参考

- 原项目 README · oso95/scroll-world
- 603 行 SKILL.md（含 10 步 + 4 类 gotcha）
- 448 行 scrub-engine.js（vanilla JS 滚动引擎，可直接用）
- index-template.html（完整 HTML 模板）

## 沉淀版本

v1.0 · 2026-07-17
