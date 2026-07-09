# 领域增改避坑 · 锦绣融合稿

> 一份稿，三端用：公众号 / 小红书 / AI 阅读。

---

## 公众号版（深度 · 1200-1800 字）

标题：**你改了领域名，为什么 check-3f 还是报错？**

pretty-skill 把知识按 16 个中文领域分目录。看起来只是改个文件夹名，但踩过一次坑你就知道：改领域名最难的不是改名，是改一致性。

根因很隐蔽：`content-triple-format/check-3f.py` 和 `skill-creator/create.py` 里**各硬编码了一份 `PRESET_DOMAINS`**。一份是校验口径（决定你的 case 领域合不合法），一份是脚手架口径（决定新建 case 时能选哪些领域）。你只改一处，要么校验把你拦在门外，要么脚手架给你生成错领域。

更阴的是历史债：中文化那一轮，有 3 个老 case 的 `manifest.domain` 写的是旧英文领域（AI能力 / 金融投资），根本不在英文 PRESET 里——它们其实长期 `EXIT=1`，只是管道里 `| grep` 的退出码把真实失败掩盖了，肉眼看全是绿的。

**正确姿势只有一条：加 / 改领域，两处 PRESET 一起改，manifest.domain 写成 PRESET 里的 key（中文）。** 改完跑一次 `check-3f.py <case>`，盯着真实退出码。

还有个中文专属坑：批量替换文档里的领域名别用 `\b` 词边界——Python re 的 `\b` 按 ASCII 走，中文不是"单词字符"，匹配会错位漏改。换成显式分隔（前后是空白 / 标点）的写法才稳。

最终领域定稿 16 个中文名，和 knowhub 对齐。重名同义的（情感关系 = 情感领域）丢弃我的、留远端版。

## 小红书版（精简 · 300 字 + 3 竖屏图）

"改领域名后 check-3f 还报错？
坑在这：check-3f.py 和 create.py 各有一份 PRESET_DOMAINS，必须一起改。
我只改了一处，结果 3 个老 case 其实一直 EXIT=1，被 grep 骗成绿的。
教训：加领域 → 两脚本各加一条 → manifest.domain 写中文 key → 跑校验看真实退出码。
还有：中文别用 \\b 词边界替换，会漏！用空白/标点当分隔。"

## AI 阅读版（结构化要点 · 供摘要 / 检索）

- 根因：check-3f.py 与 create.py 各自硬编码 PRESET_DOMAINS（校验口径 vs 脚手架口径）。
- 失败模式：只改一处 → 校验拦 or 脚手架生成错领域。
- 历史坑：3 个老 case 的 manifest.domain 不在英文预设 → 长期 EXIT=1，被 `| grep` 退出码掩盖。
- 解法：加 / 改领域时两处 PRESET 同步改；manifest.domain = PRESET 里的中文 key；改完跑 check-3f 看真实退出码。
- 中文坑：批量替换别用 `\b`（ASCII 词边界对中文失效），用显式分隔写法。
- 决策：领域 11 → 16，全中文噱头名，与 knowhub 对齐（补橙皮书/社交主导/视觉创作/故事写作）。
- 加领域 4 步：改两脚本 → git mv 建目录+README → manifest.domain 写中文 → check-3f EXIT=0。

---

## 配图

- 封面：`cover-横屏.png` / `cover-竖屏.png`
- 正文 7 图见 `../images/p0-p6.png`
- 讲解图集：`slides/s0-s7.png`（8 张）
