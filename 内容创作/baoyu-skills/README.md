# baoyu-skills · 宝玉的内容创作 skill 矩阵

> **一句话定位**：5 个 sub-skill 一把抓 · 文章插图 / 封面 / 小红书 / PPT / 故事漫画 · 风格×布局二维选择 · 配置化 Prompt 工程的范本。

---

## 这个 case 是什么

**页数**：5 页 · **领域**：内容创作
**作者**：宝玉 xp（@jimliu）
**仓库**：`github.com/JimLiu/baoyu-skills`
**状态**：case 草稿（未实跑 · 待 GitHub 网络恢复后 clone 验证）

## 核心论点

Prompt 工程的终局是 **"消失"**——不让你写"你是一个资深设计师,请用…风格…",而是用 `--style notion` / `--layout pyramid` 这种参数代替。**审美的事交给 skill,用户只管选参数**。

## 5 个 sub-skill 速查表

| Skill | 适用场景 | 核心卖点 | 常用命令 |
|---|---|---|---|
| **baoyu-xhs-images** | 小红书运营 / 知识卡片 | 风格×布局二维选择,一键多图 | `/baoyu-xhs-images post.md --style notion` |
| **baoyu-infographic** | 技术原理 / 流程图 | **20 种布局 + 17 种风格** | `/baoyu-infographic arch.md --layout pyramid` |
| **baoyu-cover-image** | 博客/公众号封面 | 5 维度定制(类型/配色/渲染/文字/氛围) | `/baoyu-cover-image blog.md --quick` |
| **baoyu-slide-deck** | 技术分享 / 汇报 | 自动生成大纲,出 PPTX/PDF | `/baoyu-slide-deck talk.md --style blueprint` |
| **baoyu-comic** | 讲故事 / 寓教于乐 | 知识漫画,能控制分镜 | `/baoyu-comic story.md --art manga` |

## 内容即数据

直接读你的 **Markdown 文章**,自动提取关键信息生成 PPT/图表,不用重新喂一遍内容。

## 风格字典（学得到）

**风格（style）选项**（部分）：
- `notion`（干净、黑白线条）
- `blueprint`（蓝图风）
- `manga`（漫画风）
- 还有 ~17 种...

**布局（layout）选项**（部分）：
- `pyramid`（金字塔）
- `timeline`（时间线）
- `dense`（密集干货）
- 还有 ~20 种...

## 安装（待 clone 验证）

```bash
# 网络恢复后执行
npx skills add jimliu/baoyu-skills
# 或
npx skills add jimliu/baoyu-skills -g
```

需要 Claude Code / Trae / Cursor 这类"能动手"的 AI 工具。

## 触发词

"封面" / "小红书配图" / "信息图" / "PPT" / "故事漫画" / "宝玉" / "baoyu" / "技术配图" / "排版"

---

## 关联沉淀

- 视觉设计相关 → `pretty-skills/视觉创作/baoyu-design/`（本地化 Claude Design）
- 中文排版 + AI 审美黑名单 → `Mavis memory/distillation-review.md` 第 3 条
