# 出图 prompt 合集 · 公众号爆款操盘术

> 本 case 的 4 张配图 prompt（已实际生成并落地）。
> 复用自 pretty-skills 推广文战役，prompt 首词刻意各异以避免并行生图文件名碰撞。

---

## p0 · 封面（知识中枢）

**Hero cover illustration, hand-drawn storybook style, macaron pastel palette...**
中央发光知识中枢 + 机器人图书管理员，书变成分享卡，四周浮空卡片 / 灯泡。16:9，留白。

## p1 · 痛点图（被文件淹没）

**A lonely person sitting looking overwhelmed...**
人被高高倾斜的文件塔 / PDF 图标 / PPT 图标淹没，一张发光卡片想浮起却被压住。奶油粉底，略忧伤但可爱。

## p2 · 范式图（一次创作变多形态）

**A cozy bright publishing bureau scene...**
左侧手写笔记从拱门流入，右侧变成四种输出：网页 / PPT / 手机卡 / 视频按钮，曲线箭头展示一进多出。

## p3 · 案例花园图（共建生态）

**A vibrant growing garden where many small glowing booklets...**
发光小册子像植物长在弯茎上，各标小图标（狼头 / 蜡烛图 / 橙书），小人种植照料，中央暖阳。开源共建感。

---

## ⚠️ 生图红线（来自实战）

1. **并行生图必须 prompt 首词各异** —— 否则工具用 prompt 前缀当文件名，互相覆盖成 1 张。
2. **平台水印去不掉** —— 当前 ImageGen（腾讯混元）默认右下角加水印，prompt 无效；发布前 `sips -c 874 W --cropOffset 0 0` 裁底 ~150px，或换无平台水印生图源。
3. **分辨率合规** —— 单张 ≥ 1024×576，纵横比 16:9 / 3:4 / 9:16 / 1:1，否则被「代码生图」校验误伤。
