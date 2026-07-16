# scroll-world · matrix MCP Pipeline

> **作用**：完整 MCP 调用 sequence（替代原 higgsfield pipeline.md）
> **工具**：`mavis mcp call matrix matrix_generate_image` + `mavis mcp call matrix matrix_gen_videos` + ffmpeg
> **核心约束**：seam frame-identical（matrix 限制 → 2 段拼接 + crossfade 500ms）

---

## Step 0 · Bootstrap

```bash
# 准备目录
WORK=/tmp/scroll-world
ASSETS=./assets
mkdir -p "$WORK/stills" "$WORK/clips" "$ASSETS/vid"

# 检查工具
which ffmpeg ffprobe  # 必须都在
mavis mcp tools matrix matrix_generate_image  # 检查 MCP 可用
mavis mcp tools matrix matrix_gen_videos      # 检查 MCP 可用
```

## Step 1 · Interview（收集 8 字段）

```text
SUBJECT:           bubble tea 品牌 / 一句话定位
BRAND_NAME:        Pearl & Co.
PALETTE:           taro #9B7EBD, cream #F5EDE0, caramel #C88A5A, matcha #8FB98A, plum #3A2E48
BG_HEX:            #F5EDE0       (PALETTE 中最浅的那个)
TONE:              cozy / premium
SECTIONS[]:        [farm, kitchen, shop, delivery, finale]   (5 段)
MOBILE:            yes            (影响 2× 信用成本)
```

## Step 2 · 出 N 张场景图（matrix_generate_image 并行）

**Style preamble**（byte-for-byte 一致，N 段都复用）：

```text
Isometric low-poly 3D diorama floating as a small rounded island on a plain solid
[BG_HEX] background with a soft contact shadow beneath it. Soft matte clay 3D render,
rounded toy-model shapes, gentle warm studio lighting, soft long shadows, tilt-shift
miniature look. Cohesive color palette of [PALETTE]. Highly detailed, centered
composition, absolutely no text, no letters, no numbers, no logos.
```

**单段 prompt**：

```text
${STYLE_PREAMBLE}

Section: ${SECTION_NAME}
Subject: ${SECTION_SUBJECT}
```

**MCP 调用**（批量并行）：

```bash
# 为每段写 prompt 文件
for n in ${NAMES}; do
  cat > "$WORK/stills/${n}.txt" <<EOF
${STYLE_PREAMBLE}

Section: ${n}
Subject: ${SECTION_SUBJECTS[$n]}
EOF
done

# 批量出图（matrix 一次最多 5 个 request）
mavis mcp call matrix matrix_generate_image "$(python3 -c "
import json, sys
names = '${NAMES}'.split()
requests = []
for n in names:
    with open(f'$WORK/stills/{n}.txt') as f:
        prompt = f.read()
    requests.append({
        'prompt': prompt,
        'aspect_ratio': '3:2',
        'resolution': '2K'
    })
print(json.dumps({'requests': requests}))
")"
```

## Step 3 · 出 2N-1 段视频（matrix_gen_videos 串行）

**关键**：matrix 一次只能锁 1 端（first_frame / last_frame / subject）。

**Dive clip**（N 段，每段 8s，锁 last_frame = 场景内部帧）：

```bash
# 单段
mavis mcp call matrix matrix_gen_videos "$(cat <<EOF
{
  "requests": [{
    "prompt": "Camera flying INTO the [${SECTION}] interior, smooth cinematic motion, diorama view",
    "input_image": {
      "file": "$WORK/stills/${SECTION}.png"
    },
    "reference_type": "last_frame",
    "duration": 8,
    "resolution": "768P"
  }]
}
EOF
)"
```

**Connector clip**（N-1 段，每段 8s，锁 first_frame = 上一段 dive 末帧）：

```bash
# 提取每段 dive 末帧（作为 connector 首帧）
for i in $(seq 0 $((N-2))); do
  ffmpeg -sseof -0.1 -i "$WORK/clips/dive_${i}.mp4" \
    -frames:v 1 -y "$WORK/clips/dive_${i}_end.png"
done

# 出 connector clip
for i in $(seq 0 $((N-2))); do
  NEXT=$((i+1))
  mavis mcp call matrix matrix_gen_videos "$(cat <<EOF
{
  "requests": [{
    "prompt": "Camera flying THROUGH the [transition ${i} to ${NEXT}], smooth cinematic motion, continuous flight",
    "input_image": {
      "file": "$WORK/clips/dive_${i}_end.png"
    },
    "reference_type": "first_frame",
    "duration": 8,
    "resolution": "768P"
  }]
}
EOF
)"
done
```

## Step 4 · ffmpeg 拼接（crossfade 500ms）

**为什么用 crossfade**：matrix 限制只能锁 1 端 → 拼接处可能不完全 frame-identical → crossfade 500ms 视觉上近似无缝（人类感知阈值 100ms）。

```bash
# 拼接所有视频
INPUTS=""
for i in $(seq 0 $((N-1))); do
  INPUTS="$INPUTS -i $WORK/clips/dive_${i}.mp4"
  if [ $i -lt $((N-1)) ]; then
    INPUTS="$INPUTS -i $WORK/clips/conn_${i}.mp4"
  fi
done

# 用 xfade filter 拼接
FILTER=""
OFFSET=0
PREV="[0:v]"
for i in $(seq 0 $((2*N-2))); do
  NEXT_IDX=$((i+1))
  if [ $i -lt $((2*N-2)) ]; then
    NEW_OFFSET=$(echo "$OFFSET + 7.5" | bc -l)  # 8s 视频 - 0.5s crossfade
    FILTER="${FILTER}${PREV}[${NEXT_IDX}:v]xfade=transition=fade:duration=0.5:offset=${NEW_OFFSET}[v${NEXT_IDX}];"
    PREV="[v${NEXT_IDX}]"
    OFFSET=$NEW_OFFSET
  fi
done
FILTER="${FILTER%?};"  # 去掉最后一个分号
FINAL_LABEL="[v${NEXT_IDX}]"

# 输出最终视频
ffmpeg $INPUTS \
  -filter_complex "$FILTER" \
  -map "$FINAL_LABEL" -c:v libx264 -crf 23 -preset medium -pix_fmt yuv420p \
  "$ASSETS/vid/final.mp4"
```

## Step 5 · 编码（web 优化）

```bash
# Web 友好的 h264 mp4
ffmpeg -i "$WORK/raw_final.mp4" \
  -c:v libx264 -crf 23 -preset medium \
  -movflags +faststart \
  -pix_fmt yuv420p \
  "$ASSETS/vid/final.mp4"
```

## Step 6 · 落地页（index-template.html + scrub-engine.js）

```bash
# 下载 scrub engine + template
curl -fsSL https://raw.githubusercontent.com/oso95/scroll-world/main/skills/scroll-world/references/scrub-engine.js -o scrub-engine.js
curl -fsSL https://raw.githubusercontent.com/oso95/scroll-world/main/skills/scroll-world/references/index-template.html -o index-template.html

# 复制 stills + clips
cp $WORK/stills/*.png $ASSETS/
for i in $(seq 0 $((N-1))); do
  cp $WORK/clips/dive_${i}.mp4 $ASSETS/vid/
done

# 改 index-template.html 替换主题/品牌/视频路径
sed -i.bak \
  -e "s/BRAND/${BRAND_NAME}/g" \
  -e "s/SUBJECT/${SUBJECT}/g" \
  -e "s/'\#top'/'#top'/g" \
  -e "s|assets/sceneA.webp|assets/stills/dive_0.mp4|g" \
  index-template.html

# 启动 http server 测试
python3 -m http.server 8000
```

## Step 7 · QA seams

```bash
# 提取每个 dive 末帧 + 每个 connector 首帧，对比
for i in $(seq 0 $((N-2))); do
  ffmpeg -sseof -0.1 -i "$WORK/clips/dive_${i}.mp4" -frames:v 1 -y "$WORK/qa/dive_${i}_end.png"
  ffmpeg -ss 0 -i "$WORK/clips/conn_${i}.mp4" -frames:v 1 -y "$WORK/qa/conn_${i}_start.png"
  # 用 image diff 对比
  compare -metric AE "$WORK/qa/dive_${i}_end.png" "$WORK/qa/conn_${i}_start.png" "$WORK/qa/diff_${i}.png"
done
```

如果差异 > 阈值（5-10% 像素差）→ 重出 connector。

## 完整时间预估（5 段 + mobile）

| 步骤 | 工具 | 段数 | 单段时间 | 总时间 |
|---|---|---|---|---|
| 出场景图 | matrix_generate_image | 5 | 1 min | 1 min（并行） |
| 出 dive 视频 | matrix_gen_videos | 5 | 3-5 min | 15-25 min |
| 出 connector 视频 | matrix_gen_videos | 4 | 3-5 min | 12-20 min |
| 拼接 + 编码 | ffmpeg | - | 1 min | 1 min |
| 落地页 | 模板 | - | 5 min | 5 min |
| QA seams | ffmpeg + image diff | - | 5 min | 5 min |
| **总** | - | - | - | **40-60 min** |

mobile 多 1 倍视频量 → +30-40 min。

## Gotchas

1. **matrix 1 次最多 5 request** — 多段场景图分批出
2. **video duration 限制**：duration=10 必须 resolution=768P；duration=6 任意；1080P 必须 duration=6
3. **reference_type 限制**：只能锁 1 端（first_frame / last_frame / subject）
4. **macOS bash 3.2**：不要用 `declare -A`（关联数组）
5. **video 等待时间**：matrix 出视频 3-5 min/段，串行不要并行（5+ 个 video 并行可能超时）
6. **Higgsfield credit** 比 matrix 便宜 5-10×，但 Mavis 主环境没有 higgsfield，所以必须用 matrix

## 参考

- 原项目：https://github.com/oso95/scroll-world
- scrub engine：https://github.com/oso95/scroll-world/blob/main/skills/scroll-world/references/scrub-engine.js
- index template：https://github.com/oso95/scroll-world/blob/main/skills/scroll-world/references/index-template.html
- matrix MCP 文档：mavis mcp tools matrix
