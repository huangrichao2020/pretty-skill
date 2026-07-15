# IP 形象 + 表情包 · prompt 模板

> 完整 prompt 模板 + 填法示例。
> 改 prompt 时只改 `SCENE: ...` 部分，**BASE 别动**。

---

## 1️⃣ 标准形象 prompt

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

### 填法示例

| 角色 | 动物名 | 主色 | 辅色 |
|---|---|---|---|
| Mavis 狐狸 | `fox` | `orange-red` | `cream beige` |
| 通用小猫 | `cat` | `soft yellow` | `white` |
| 通用小熊 | `bear` | `warm brown` | `cream` |
| AI 机器人 | `small robot` | `silver-grey` | `cyan glow` |

---

## 2️⃣ 处境类母版 prompt（6 张）

```python
# 母版库：6 张处境
M01_MEETING  = BASE + "SCENE: pulling a megaphone back with a long stretchy string"
M02_OVERLOAD = BASE + "SCENE: surrounded by dozens of falling speech bubble envelopes, paws up"
M03_ALERT    = BASE + "SCENE: at a laptop, big red exclamation mark warning, paws on keyboard"
M04_REJECT   = BASE + "SCENE: holding stack of papers with a big red X, head slightly tilted"
M05_RENAME   = BASE + "SCENE: two identical characters side by side, one solid, one ghost outline"
M06_SCREEN   = BASE + "SCENE: at a desk, one paper in paw, stack of rejected papers on the floor with X marks"
```

### 改法

保留 BASE，**只改 SCENE 部分**。例如：
- 改动物（狐狸 → 猫）：保持 BASE 的 `{动物名}` 占位
- 加新母版 M07 = `BASE + "SCENE: sleeping face-down on keyboard at desk"`

---

## 3️⃣ 情绪类母版 prompt（8 张）

```python
# 母版库：8 张情绪
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

## 4️⃣ Matrix MCP 调用示例

```bash
mavis mcp call matrix matrix_generate_image '{
  "prompt": "<BASE + SCENE 拼接后字符串>",
  "aspect_ratio": "1:1",
  "num_images": 1
}'
```

### 完整调用（Mavis 狐狸 E01 庆祝）

```bash
mavis mcp call matrix matrix_generate_image '{"prompt": "A minimalist line-drawing fox character. Solid orange-red silhouette with cream beige belly. Two tiny black dots for eyes, no pupils, no mouth. SCENE: both arms raised up high holding party poppers, confetti and ribbons flying. Pure white background, character 40-50% of canvas, abundant whitespace. Simple clean black outlines, no shading, no gradients. Quirky absurd professional energy, NOT cute, NOT childish. NO text, NO labels, NO watermark. 1:1 square aspect ratio, digital illustration.", "aspect_ratio": "1:1", "num_images": 1}'
```

---

## 5️⃣ Prompt 调优 tips

| 现象 | 加什么 |
|---|---|
| AI 加文字 | `NO text, NO labels, NO watermark` |
| AI 卖萌 | `NOT cute, NOT childish, NOT anthropomorphic smile` |
| AI 给表情 | `no mouth, completely empty expression` |
| 主体太大 | `character occupies 40-50% of canvas` |
| 颜色杂 | `no shading, no gradients, no color details` |
| 风格漂移 | 严格保留 BASE，只改 SCENE |
| 不像动物 | `animal name in prompt + tail visible` |

---

## 6️⃣ 进阶：批量出图脚本（Python）

```python
import subprocess
import json

BASE = """A minimalist line-drawing fox character. ..."""

# 14 张母版
SCENES = {
    "M01_meeting": "SCENE: pulling a megaphone back with a long stretchy string",
    "M02_overload": "SCENE: surrounded by dozens of falling speech bubble envelopes, paws up",
    "M03_alert": "SCENE: at a laptop, big red exclamation mark warning, paws on keyboard",
    "M04_reject": "SCENE: holding stack of papers with a big red X, head slightly tilted",
    "M05_rename": "SCENE: two identical characters side by side, one solid, one ghost outline",
    "M06_screen": "SCENE: at a desk, one paper in paw, stack of rejected papers on the floor with X marks",
    "E01_celebrate": "SCENE: both arms raised up high holding party poppers, confetti and ribbons flying",
    "E02_exhausted": "SCENE: face-down collapsed on a stack of papers at a desk, completely exhausted",
    "E03_thinking": "SCENE: one paw under chin in a classic thinking pose, a glowing lightbulb floating above",
    "E04_awkward": "SCENE: scratching the back of head with one paw, embarrassed wave with the other, a single sweat drop",
    "E05_proud": "SCENE: standing with both paws on hips in a proud stance, head tilted up slightly, looking smug",
    "E06_angry": "SCENE: standing with both paws on hips, steam or smoke wisps rising from the top of head",
    "E07_shocked": "SCENE: both paws covering mouth, eyes wide, in a shocked expression",
    "E08_cozy": "SCENE: sitting comfortably holding a steaming cup of hot drink with both paws, looking cozy",
}

for name, scene in SCENES.items():
    prompt = BASE + scene
    subprocess.run([
        "mavis", "mcp", "call", "matrix", "matrix_generate_image",
        json.dumps({"prompt": prompt, "aspect_ratio": "1:1", "num_images": 1})
    ])
    print(f"✓ Generated {name}")
```

---

## 7️⃣ 推荐 MCP 工具

- **matrix_generate_image**：主图生成（必须）
- **matrix_upload_to_cdn**：图床上 CDN（公开链接用）
- **bash + curl**：图下载到本地
