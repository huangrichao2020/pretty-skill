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

### 2026-07-08 23:00 复核（每日 dream 修炼自动化）

- **git 状态**：自 20:13 提交以来工作树干净，无新增未提交改动。
- **全量 3F 复核**：对当日全部 5 个 case 跑 `check-3f.py`，**均 `EXIT=0`**：
  - `内容创作/橙皮书方法论`（7 页）
  - `金融投资/macro-monitor`（7 页）
  - `金融投资/chokepoint-mainboard`（9 页）
  - `AI能力/cartman-team-ai-agent-collab`（8 页）
  - `AI能力/social-ecom-skill`（8 页）
- **补全记录**：20:13 那条仅记了 `fbd2a23` 的 2 个 case；本日实际共沉淀 **5 个** 3F case（另 3 个来自 `cf31d1b`：chokepoint-mainboard / cartman-team-ai-agent-collab / social-ecom-skill）。
- **新增沉淀**：无。自 20:13 以来无新对话 / 新工作成果，未新建或硬造 case（遵循「无高价值内容不硬造」原则）。

---

## 2026-07-09

**沉淀了什么 / 做了什么**
- 先 `git pull --rebase` 拉取远端：远端有大重构 `128c81f`（仓库名 `pretty-skill`→`pretty-skills`，11 领域目录从中文名统一改为**英文名**，并把 check-3f.py 升级到 **v3.11**，新增强制 `manifest.json`（含 visibility 字段））。同时拉到新 tag `v0.1.0`。
- 我本地 rebase 上来的 2 个 case 仍留在旧中文目录、且缺 v3.11 要求的 manifest.json → 对齐修复。

**新建/更新了哪些 case**
- 迁移目录对齐英文规范：`内容创作/橙皮书方法论` → `content-ops/橙皮书方法论`；`金融投资/macro-monitor` → `trading-review/macro-monitor`（`git mv`，删空的中文目录）。
- 为 2 个 case 各补 `manifest.json`（visibility=public + tags + page_count 等）。
- `INDEX.md`：case 清单从 3 条补到 5 条，计数文案 3→5；`roadmap.md` 计数同步。

**3F 校验结果**
- 迁移后首校 `EXIT=1`（v3.11 缺 manifest.json）→ 补 manifest 后 `content-ops/橙皮书方法论` 与 `trading-review/macro-monitor` 均 `check-3f.py` → **`EXIT=0`**。

**git**
- 已 rebase 到远端最新，本地领先的提交将 **push 到 origin/main**（用户本轮明确授权 push）。

---

## 2026-07-09（18:46 · case slug 英文化收尾）

**背景**：上一轮把 2 个 case 迁到英文领域目录后，`content-ops/橙皮书方法论` 的**文件夹名仍是中文**，而其 `manifest.json` 里 `name` 已声明为英文 `orange-book-method` —— 名实不符，是全仓唯一的中文 slug 残留。

**改动**
- `git mv content-ops/橙皮书方法论 → content-ops/orange-book-method`（与 manifest.name 对齐；28 文件 rename 保留历史）。
- `INDEX.md`：链接与 slug 更新为 `orange-book-method`。
- 全仓已无指向旧路径的有效引用（仅历史 dream-log 记录保留，不改写）。

**3F 校验**：`content-ops/orange-book-method` → `check-3f.py` **`EXIT=0`**。

**git**：commit 后 push 到 `origin/main`（用户已授权）。至此全部 5 个 case 的领域目录与 slug 均符合 v3.11 英文规范。

---

## 2026-07-09（18:51 · 领域与 case 全面中文化）

**背景**：用户要求领域名改回中文、case（技能）名也用中文且"别太生硬、易传播、有噱头"。

**关键发现（验证中翻出的脏数据）**
- `check-3f.py` 与 `skill-creator/create.py` 各自硬编码英文 `PRESET_DOMAINS`，是中文领域的硬门槛——不改这俩，改成中文目录后校验/脚手架全失效。
- 之前误以为 5 个 case 都过校验：其实只有 2 个（橙皮书/宏观雷达）真过；另 3 个（cartman、social-ecom 的 `domain=AI能力`、chokepoint 的 `domain=金融投资`）的 manifest.domain **根本不在英文预设里**，一直是 `EXIT=1`，只是被管道 `grep` 的退出码掩盖了。

**改动**
1. `PRESET_DOMAINS` 中文化：`check-3f.py`（字典 → 中文 key + 英文别名兼容）、`create.py`（列表 → 中英并列）。
2. 11 个领域目录 `git mv` 改中文：ai-agent→AI能力、coding→编程开发、data-science→数据科学、product-design→产品设计、business-model→商业运营、trading-review→金融投资、content-ops→内容创作、learning→教育学习、gaming→游戏玩家、lifestyle→生活方式、pkm-decision→思维方法。
3. 5 个 case 目录改中文噱头名：cartman-team-ai-agent-collab→**AI狼群战法**、social-ecom-skill→**社交电商掘金术**、orange-book-method→**橙皮书方法论**（保留品牌）、chokepoint-mainboard→**卡脖子猎手**、macro-monitor→**宏观雷达**。
4. 重写 5 个 `manifest.json`：`name`=中文 slug、`domain`=中文领域名，顺手根治上面 3 个 domain 错配。
5. Python 正则（ASCII 词边界，修正中文被当单词字符导致 `\b` 失效）批量替换 36 个文档里的英文领域/case 名为中文；排除 `.git`/`.workbuddy`/历史 `dream-log.md`/已手改的两脚本/5 个 manifest。

**3F 校验**：5 个 case 全部 `check-3f.py` **`EXIT=0`**（真实退出码，非管道欺骗）。

**git**：commit 后 push 到 `origin/main`（用户已授权）。

---

## 2026-07-09（续 · knowhub 领域对齐复核）

**背景**：用户要求「把 knowhub/domains 的 11 个领域在 pretty-skills 建对应中文领域」。pull 后发现远端 `origin/main`(be04aba) 已被用户在另一台机器**基本做完这件事**——12 领域 PRESET 已对齐 knowhub 且用了中文噱头名（`Agent知识`/`情感领域`/`玄学修炼`/`做事技巧`…），7 个 case 全部 `check-3f EXIT=0`。

**发现 & 处理**：
- knowhub 11 领域里，远端已含 7 个（含改名对齐）；**仅缺 4 个**：`橙皮书`(orange-book)、`社交主导`(social-dominance)、`视觉创作`(visual-creation)、`故事写作`(writing-storycraft)。
- 我之前提交的 6 个目录里，`情感关系`/`哲学现实` 与远端已有的 `情感领域`/`玄学修炼` **重名同义**——按「有重复尽量改为 knowhub 意思」原则**丢弃我的重名版、保留远端版**；`社交主导`/`视觉创作`/`故事写作`/`橙皮书` 为真正缺失项。
- 行动：`git reset --hard origin/main` 丢弃冗余提交，在 be04aba 上**只补 4 个缺失领域**。

**改动**：
- 新建 `橙皮书/`、`社交主导/`、`视觉创作/`、`故事写作/` 4 目录，各带 `README.md`（占位风格 + knowhub 含义一行）。
- `check-3f.py` + `create.py` 的 `PRESET_DOMAINS` 增加这 4 个中文名。
- `INDEX.md` / `STRUCTURE.md` 领域表各加 4 行，计数 **12 → 16**（含目录树、H2、命名逻辑表、PR 模板下拉等）；保留 5 处历史发布记录行(12)不改写。

**3F 校验**：现有 7 个 case 全部 `check-3f.py` **`EXIT=0`**（真实退出码）；2 脚本语法正常；PRESET 两处均含 4 新领域。

**git**：commit 后 SSH push 到 `origin/main`（用户已授权）。至此 knowhub 11 领域全部对齐 pretty-skills（16 领域总量）。

**技术坑记录**：
- `git fetch` 走 SSH 在此沙箱**卡死**（120s 零输出，RC=124），但 `ssh -T`/`ls-remote`/之前的 push/HTTPS 下载均正常 → 是 SSH 协议 upload-pack 路径 stall，非认证问题。**公开仓可免认证用 HTTPS 智能 HTTP fetch**（`git fetch https://github.com/huangrichao2020/pretty-skills.git`）瞬时成功。
- rebase 冲突中 `--ours`=目标分支(origin/main 新真相)、`--theirs`=正在重放的旧提交——方向别搞反。
