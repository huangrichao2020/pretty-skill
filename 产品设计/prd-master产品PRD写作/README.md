# prd-master · 产品 PRD 写作 case

> **沉淀时间**：2026-07-15
> **来源**：RedSkill 商店 prd-master@1.0.1（小红书开源）
> **方法论作者**：prd-master 团队
> **沉淀者**：Mavis（按 pretty-skills 流程）

## 这是什么

小红书开源的 prd-master skill，被 Mavis 装到本地（`~/.minimax/agents/mavis/workspace/skills/prd-master`）后，按 pretty-skills 流程沉淀成可公开访问的 case。

**核心价值**：让 PRD 从"需求堆砌"变成"证据驱动的决策文档"。

## 文件结构

```
prd-master产品PRD写作/
├── README.md                  # 本文件
├── SKILL.md                   # 触发词 + 一句话定位
├── content.md                 # 8 步 + 8 段 + 7 路由 + 边界 + 对抗审查 完整心法
├── prd-master产品PRD写作讲解.pdf  # PDF 讲解版（9 张图纯图片拼接）
├── images/                    # 9 张讲解图
│   ├── p1.png ~ p9.png
├── prompts/                   # 9 段出图 prompt
│   ├── README.md
│   ├── p0_cover.md ~ p8.md
├── 锦绣/                      # 多平台素材
│   ├── cover-横屏.png
│   ├── cover-竖屏.png
│   ├── slides/                # 9 张讲解图副本
│   └── readme.md              # 融合 md（公众号 + 自媒体稿 + AI 阅读）
```

## 核心心法

- **8 步工作流**：诊断→提问→选型→写→4句话→证据→对抗→自评→导出
- **8 段框架**：决策摘要 / 用户场景 / 竞品研究 / 目标范围 / 核心方案 / 推进验证 / 风险依赖 / 埋点指标
- **7 种路由**：A 探索 Brief / B 0→1 策略 / C 功能 PRD / D 实验方案 / E 平台 API / F 改版迁移 / G 上线运营 + H AI 模块
- **强制边界条件块**：5 行必填（适用性 / 输入 / 失败恢复 / 兼容性 / 信任隐私）
- **对抗式审查**：context-isolated，自己审自己 = 没审

## 适用场景

- 写功能 PRD / 0→1 策略 / 改版迁移 / 平台 API / 实验方案
- 任何"先 evidence 后结构"的产品文档

## 用户拿到后

- 写一篇功能 PRD：从 5h 草草列功能 → **30 min 出可评审决策文档**（8 步 + 8 段框架 + 强制边界 + 对抗 review）
- 写 0→1 策略备忘录：1 周拍脑袋 → **2h 出有证据的策略文档**
- 改版迁移：1 周讨论 → **1h 出有边界条件的方案**
- **整体：不再写"需求堆砌"，写"证据驱动的决策文档"**

## 与同类方法论对比

prd-master 与 dashiai-ppt（HTML PPT）、CyberPPT（PPT）、wechat-delivery 8 维 rubric（公众号）共享**"先 evidence 后结构"**的同源思路，但 prd-master 是这个思路在产品文档上的最严格实现。

## 安装路径

RedSkill 商店：

```bash
curl -fsSL https://fe-video-qc.xhscdn.com/fe-platform-file/...sh | bash
export PATH="$HOME/.local/bin:$PATH"
redskill install prd-master
```

## 相关引用

- prd-master 主页：[github.com/crazyykhllc-bit/CyberPPT](https://github.com/)（实际路径待确认）
- pretty-skills 主项目：[huangrichao2020/pretty-skills](https://github.com/huangrichao2020/pretty-skills)

## 沉淀版本

v1.0 · 2026-07-15
