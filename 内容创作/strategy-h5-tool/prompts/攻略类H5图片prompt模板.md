# 攻略类 H5 图片 Prompt 模板

> matrix 生图统一规范 · v2.0（2026-07-14，v1 升级加封面 prompt）

**v2 升级**：
- 加封面 prompt 模板（运营阶段 3 视觉包装必备）
- 加 4K 源图升级选项（避免小红书发图压缩失真）
- 加 SVG 路径地图底图（v1 已有）→ 升级用 viewBox 1600×900 真实像素感

---

## 通用规则

```yaml
resolution: 2K (默认) / 4K (小红书发图压缩无损，建议)
aspect_ratio: 16:9 (攻略内) / 1:1 (logo) / 3:4 (小红书封面，v2 新增)
format: jpeg 80% (sips 后)
max_size: 500KB
style: "Traditional Chinese ink painting" + "Jiangnan scenery"
forbidden:
  - "text" / "watermark" / "logo" / "caption"
  - "letters" / "characters"
  - "modern graphics"
  - "English text"
```

**v2 关键升级**：
- 源图分辨率从 2K → **4K**（避免小红书发图压缩失真）—— 杭州烟雨 v1 教训：1000px 源图在小红书压成 1080 宽后细节丢失
- sips 处理：`sips -Z 2048`（2K 缩图保留 4K 源的细节）

---

## 1. 9 张景点图模板

### 通用 prompt 模板

```
Traditional Chinese ink painting,
<SCENE_DESCRIPTION>,
<xuan paper texture, soft mist, minimalist composition>,
<COLOR_PALETTE>,
<SEASONAL_OR_TIME>,
no text, no watermark, no logo, no characters anywhere in the frame,
cinematic 16:9
```

### 9 张景点 prompt（杭州烟雨实战版）

**01 断桥**
```
Traditional Chinese ink painting, classic Broken Bridge at West Lake Hangzhou
in early morning mist, soft white fog, distant Leifeng Pagoda silhouette,
weeping willows along lake shore, minimalist composition, xuan paper texture,
muted teal and gold palette, no text, no watermark, cinematic 16:9
```

**02 三潭印月**
```
Traditional Chinese ink painting, Three Pools Mirroring the Moon at West Lake,
three small stone pagodas rising from calm jade water, full moon reflection,
lotus leaves floating, minimalist composition, xuan paper texture,
muted teal and gold palette, no text, no watermark, cinematic 16:9
```

**03 雷峰塔**
```
Traditional Chinese ink painting, Leifeng Pagoda at sunset, ancient five-story
brick pagoda glowing golden in evening light, dramatic orange and gold sky,
Su Causeway silhouette, minimalist composition, xuan paper texture,
muted teal and gold palette, no text, no watermark, cinematic 16:9
```

**04 灵隐寺**
```
Traditional Chinese ink painting, Lingyin Temple Hangzhou, ancient Buddhist
temple with incense smoke rising, majestic banyan tree, stone steps,
prayer flags in soft breeze, mountain backdrop with mist, minimalist,
xuan paper texture, muted teal and gold palette, no text, no watermark, 16:9
```

**05 龙井茶园**
```
Traditional Chinese ink painting, Longjing tea plantations Hangzhou,
terraced green tea fields rolling over hills, misty mountain valley,
tea pickers in conical hats, dreamy atmosphere, minimalist composition,
xuan paper texture, muted teal and gold palette, no text, no watermark, 16:9
```

**06 九溪烟树**
```
Traditional Chinese ink painting, Jiuxi Yanshu creek path, babbling stream
through green forest, stone stepping stones, dappled sunlight, autumn maple
leaves, peaceful valley trail, minimalist, xuan paper texture,
muted teal and gold palette, no text, no watermark, cinematic 16:9
```

**07 西溪湿地**
```
Traditional Chinese ink painting, Xixi Wetland Hangzhou, golden reed marshes
at sunset, wooden boardwalk path, water reflections, white egrets in flight,
dreamy warm light, minimalist composition, xuan paper texture,
muted teal and gold palette, no text, no watermark, cinematic 16:9
```

**08 拱宸桥**
```
Traditional Chinese ink painting, Gongchen Bridge over Grand Canal,
ancient three-arch stone bridge reflected in still water, traditional Chinese
architecture along canal, soft morning mist, minimalist composition,
xuan paper texture, muted teal and gold palette, no text, no watermark, 16:9
```

**09 满觉陇**
```
Traditional Chinese ink painting, Manjuelong village, autumn osmanthus
flowers blooming along tea plantations, traditional white-walled village
houses, misty morning, stone path, dreamy atmosphere, minimalist composition,
xuan paper texture, muted teal and gold palette, no text, no watermark, 16:9
```

---

## 2. 1 张地图底图模板

```
Top-down bird's eye view traditional Chinese ink wash style stylized map
of <CITY>, China. Layout:
- <CENTRAL_FEATURE> as <SHAPE> in <POSITION>
- <AREA_1> in <POSITION>
- <AREA_2> in <POSITION>
- <AREA_3> in <POSITION>
- <AREA_4> in <POSITION>
- <WATERWAY/RIVER> flowing from <DIRECTION>
- subtle gray mountain contour lines
- soft blue water ribbons
- NO TEXT OR LABELS, NO numbers, NO English, completely clean map
- white xuan paper background
- elegant Chinese brushstroke style
- muted teal green and gold accents
- minimalist composition
- 16:9 aspect ratio
- suitable as map base layer
```

**杭州底图实战版**
```
Top-down bird's eye view traditional Chinese ink wash style stylized map of
Hangzhou, China. Layout:
- West Lake as a large soft blue oval in upper-center
- Lingyin Temple area in upper-left mountains
- Longjing tea plantations in lower-left hills
- Jiuxi creek valley in lower-center-right
- Xixi Wetland as green marshland on the far left
- Gongchen Bridge in upper-right along canal waterway
- Manjuelong village in lower-middle between Longjing and Jiuxi
- Hefang Street area in right side
- subtle gray mountain contour lines
- soft blue water ribbons
- NO TEXT OR LABELS, completely clean map
- white xuan paper background, 16:9
```

---

## 3. 1 张小红书封面模板（v2 新增 · 3:4 比例）

**杭州烟雨 v1 实战版**

```
App poster design, 3:4 vertical ratio, Hangzhou travel guide cover,
top 30% reserved as clean soft misty area for title text overlay,
central visual: classic Broken Bridge silhouette with West Lake
and Leifeng Pagoda in soft morning mist, weeping willow draping
from upper right corner, soft golden sunrise light gradient from
top to bottom, traditional Chinese ink wash aesthetic with modern
flat design elements, muted teal and gold color palette,
NO TEXT OR LETTERS in the image itself (text will be overlaid in post),
cinematic, polished, sharp, high detail, suitable as
Xiaohongshu post cover, 3:4 aspect ratio, 4K resolution
```

**v2 反模式**：
- ❌ 封面在 AI 出图里直接写字（AI 对中文长句渲染不可靠，必须后期叠加）
- ❌ 主体放正中（小红书封面顶部 30% 留给标题，正中放主体容易冲突）
- ❌ 元素太满（封面要"一眼看懂"，元素过多在缩略图看不清）

**v2 修法**：
- ✅ 顶部 30% 留空（mist/sky/transparent area）
- ✅ 主体居中靠下
- ✅ 文字后期用 figma / sketch 叠加（不要靠 AI 渲染中文）

---



### A. 雷峰塔剪影版（推荐）

```
App icon design, perfect 1:1 square ratio, Hangzhou West Lake minimalist logo,
central element: <PAGODA> silhouette reflected in calm teal water, soft misty
mountains in background, willow branches draping from top corner,
traditional Chinese red seal stamp with characters '<SEAL_TEXT>' at bottom right,
modern flat icon design style, elegant Chinese ink wash aesthetic,
clean white or soft cream background, polished, sharp, balanced composition,
simple but memorable, suitable as mobile app icon
```

### B. 拱桥金日版

```
App icon design, 1:1 square, Hangzhou minimalist logo, central element:
arched stone bridge over water with willow reflection, gentle misty mountains,
full moon rising in background, soft teal and warm gold color palette,
modern flat icon design with Chinese ink wash aesthetic, clean background,
polished and sharp, balanced composition, suitable as mobile app icon
```

### C. 印章字版

```
App icon design, 1:1 square, Chinese minimalist logo, central element:
bold stylized Chinese character '<CHAR>' integrated with subtle <CITY> wave
and mountain elements, traditional seal carving style, brushed with red ink,
white or soft cream background, modern flat design with classical Chinese
aesthetic, polished, sharp, balanced composition, suitable as mobile app icon
```

---

## 4. matrix 调用模板

```python
# 9 张景点
image_synthesize(requests=[
    {"prompt": "<景点 prompt>", "output_file_path": "img/01-spot.jpg", "aspect_ratio": "16:9", "resolution": "2K"},
    # ... 8 more
])

# 1 张底图
image_synthesize(requests=[
    {"prompt": "<底图 prompt>", "output_file_path": "img/map-base.jpg", "aspect_ratio": "16:9", "resolution": "2K"}
])

# 1 张 logo（3 选 1）
image_synthesize(requests=[
    {"prompt": "<logo prompt>", "output_file_path": "img/logo.jpg", "aspect_ratio": "1:1", "resolution": "2K"}
])
```

## 5. sips 后处理

```bash
# 缩到 1000px 宽 + 转 jpeg 80
sips -s format jpeg -s formatOptions 80 -Z 1000 img/01-xxx.png --out img/01-xxx.jpg

# 验证单图 < 500KB
ls -la img/
```

## 6. 跨城市适配

把 `Hangzhou` 替换成 `Chengdu/Chongqing/Xi'an/Kyoto/Bangkok`：
- 替换核心地标（如成都换宽窄巷子 / 锦里 / 大熊猫基地）
- 调整色调（成都偏暖棕红，京都偏樱粉金，曼谷偏金顶绿）
- 替换印章文字（如成都 = "蓉城"）
- 替换底图中心地标（如成都换天府广场/春熙路）

## 7. 反模式

- ❌ 加任何文字 / 水印 / logo（除非显式说"印章"）
- ❌ 现代图形（手机/汽车/卡通）
- ❌ 写实摄影风格（不像水墨）
- ❌ 颜色过饱和（保持"muted"色调）
- ❌ 用 picsum/unsplash 占位（国内不稳，必须 AI 生图本地化）
