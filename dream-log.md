# dream-log · pretty-skill 每日修炼记录

> 由「每日 dream 修炼」自动化每日 23:00 回顾当日对话，把可复用知识沉淀为 3F Content case。
> 格式：日期 → 沉淀了什么 → 新建/更新了哪些 case → check-3f 结果。

---

## 2026-07-08

**沉淀了什么**
- 把 WorkBuddy 已有的两个能力正式迁移进 pretty-skill 作为 3F Content 案例：
  1. `macro-monitor`（A股宏观数据监控技能）—— 已适配 WorkBuddy 环境（用 WebFetch/WebSearch+Read 替代原 openclaw 的 browser/message 工具）。
  2. `橙皮书方法论`（花叔写 9 本橙皮书的方法：调研→规划→并行写作→三审三校+事实核查→构建）。

**新建/更新了哪些 case**
- `金融投资/macro-monitor/`：content.md(7页×7字段) + web.html(14 <img>) + images/(7 PNG) + prompts/(7) + 锦绣/(横屏封面+竖屏封面+8 slides+readme 融合稿)
- `内容创作/橙皮书方法论/`：同结构

**3F 校验结果**
- 两个 case 均 `check-3f.py` → `EXIT=0`「✅ 全部通过 · PR 可接受」
- 修复项：base `images/` 误多一张 `pX_summary.png`（8≠7 页），删除后页数一致通过。规则固化：base `images/` 的 PNG 数必须严格等于 content.md 页数，仅 `锦绣/slides/` 允许 8-12。

**图片生成**
- 本地 Pillow 离线出图（字体 `/System/Library/Fonts/STHeiti Light.ttc`，非 PingFang.ttc），不依赖在线 AI 出图，稳定可复现。

**git**
- commit `fbd2a23` 已落地本地仓；未 push（push 到公开上游需用户确认）。
