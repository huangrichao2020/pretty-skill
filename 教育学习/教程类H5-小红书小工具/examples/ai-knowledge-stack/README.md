# examples/ai-knowledge-stack/

> **真实案例 · 零基础入门 AI 知识** · 7 节课 · 6,722 字 · 3.0MB zip · 已上传小红书

## 这个 case 是什么

**主题**：零基础入门 AI 知识 · 4 层栈（AI / Agent / Skill / 工具项目）
**课程数**：7 节
**总字数**：6,722 字
**配图**：4 张 16:9 + 1 张 1:1 logo
**zip 大小**：3.0MB
**风格**：杂志海报风蓝白灰（Wired × MIT Tech Review）
**上传结果**：✅ 成功（用户反馈"效果不错"）
**生成日期**：2026-07-14

## 文件清单

```
ai-knowledge-stack/
├── index.html              # 壳（顶栏 + 视图容器）
├── main.js                 # SPA 路由 + 3 视图（home / course-X）
├── data.js                 # 7 节课完整数据（钩子 + 4 段 + 金句 + 行动）
├── style.css               # 杂志海报风蓝白灰
├── 00-cover.jpg            # 课程封面（4 层金字塔）
├── 01-hook.jpg             # 钩子图（你 vs 隔壁对比）
├── 02-stack.jpg            # 4 层栈剖面图
├── 03-flow.jpg             # 5 步流程图
└── 00-logo.jpg             # 1:1 logo（AI / FROM ZERO）
```

## 7 节课清单

| # | 标题 | 段数 | 字数 |
|---|---|---|---|
| 1 | 4 层栈总览 | 4 | 540 |
| 2 | AI = 大脑 | 4 | 684 |
| 3 | Agent = 手脚 | 4 | 1,044 |
| 4 | Skill = 工具包 | 4 | 1,120 |
| 5 | 工具项目 = 车间 | 4 | 1,149 |
| 6 | 0→6 周上手 | 5（W1-W6） | 1,272 |
| 7 | 3 件事今天开始 | 4（3 件 + 总） | 913 |

## 怎么用这个案例

### A. 本地预览（不依赖小红书）

```bash
# Mac 直接双击 index.html
open index.html

# 或起个 http server
python3 -m http.server 8000
# 访问 http://localhost:8000
```

### B. 上传小红书

```bash
# 1. 打包（注意压缩目录内容）
zip -r ../ai-knowledge-stack.zip . -x '*.DS_Store'

# 2. 创作者中心 → 小工具 → 上传 zip
#    第一次失败 = vibe RPC timeout，等 5 分钟重试

# 3. 把 00-logo.jpg 上传到"图标"框（1:1，< 5MB）
```

### C. 套用到新主题

```bash
# 1. 复制整个 examples/ai-knowledge-stack/ 到新目录
cp -r examples/ai-knowledge-stack/ my-new-course/

# 2. 改 my-new-course/data.js
#    - meta.title / subtitle / motto / coverImage
#    - courses 7 节内容（保持"钩子 + 4 段 + 金句 + 行动"结构）
#    - 字符串用反引号 ` 包（避免引号陷阱）

# 3. 替换 4 张配图 + 1 张 logo（matrix MCP 生图，共享 [4 STYLE] 段）

# 4. 跑 6 项自检 + 打 zip + 上传
```

## 5 步可视化（推荐对照 SKILL.md 一起看）

| SKILL.md 步骤 | 这个案例做了什么 |
|---|---|
| Step 1 主题规划 | 7 节 × 600-1200 字，4 段结构 |
| Step 2 内容准备 | data.js 6,722 字，钩子+段+金句+行动 |
| Step 3 视觉准备 | 4 张 16:9（杂志风蓝白灰）+ 1 张 1:1 logo |
| Step 4 代码编写 | index.html / main.js / style.css（4 文件模板）+ data.js（7 节） |
| Step 5 打包上传 | 3.0MB zip · 创作者中心 → 小工具 → 成功 |

## 关键决策回看

1. **图必须拍平**（不能放 assets/）✅ 4 张图 + 1 logo 全在根
2. **JS 字符串用反引号**（避免引号嵌套）✅ data.js 全部反引号
3. **AI 图里 0 中文**（HTML 文字层覆盖）✅ 4 张图只有英文标签
4. **logo 强调主题**（不强调内部框架）✅ logo 是 "AI / FROM ZERO"，不是 "4 / STACK"

## 真实反馈（用户原始 quote）

- ✅ "效果不错"
- ✅ "4 看不懂，4 从来不是重点，小白也能看懂的 AI 知识才对" → 触发 logo 改版
- ✅ "大标题改为 零基础入门AI知识，奇怪的日期也全都去掉" → 触发 date/volume 清理
- ✅ "里面具体每节的内容 记得补好" → 触发 3-7 节完整内容补完
- ⚠️ 早期反馈"评分小工具很鸡肋" → 触发架构从"互动测评"升级为"长篇课程"

## 跨引用

- [主 SKILL.md](../../SKILL.md) — 5 步工作流 + 4 决策 + 5 反模式
- [templates/](../../templates/) — 4 文件模板
- [manifest.json](../../manifest.json) — 元数据
