---
name: pretty-skills-creator
description: |
  创建新 skill 的入口，自动带 4 风格 HTML 占位 + 可选 PPT。
  Use when 用户说"创建 skill / 做个新 skill / 做 skill / create skill / 沉淀到 pretty-skills / 提个新 skill"。
  流程: ps create <name> → 选 4 风格之一 → 填 manifest → 提 PR。
triggers:
  - 创建 skill
  - 做个新 skill
  - 做 skill
  - 沉淀到 pretty-skills
  - 提个新 skill
---

# pretty-skills-creator

> **创** — 让创建新 skill 像"填一个表"一样简单。

> ⚠️ **状态**：**Day 4-5 迁移中**。本目录是占位，完整功能从 `~/.mavis/skills/create-skill-html/` 迁移过来。
> 临时使用方式见 `~/.mavis/skills/create-skill-html/SKILL.md`。

## 一句话

**pretty-skills-creator = 创建 skill 的 5 步流水线。**

```
ps create <name>
  → 选 4 风格之一（image / code-swiss / code-tech / code-paper）
  → 填 manifest.yaml 表单
  → 自动生成 web.html 占位 + 镜像
  → 提 PR 到主项目
```

## 4 风格

| 风格 | 适合什么 | 例子 |
|---|---|---|
| **image**（生图式默认） | 视觉类 case / 故事 | 案例展示 / 训练营介绍 |
| **code-swiss**（瑞士风） | 工具说明 / 文档型 | API 文档 / 配置说明 |
| **code-tech**（技术深色） | 技术类 case | 调试案例 / 性能分析 |
| **code-paper**（学术 paper） | 论文 / 研究 | 研究报告 / 白皮书 |

## 流程细节

详见 [`docs/` 目录](docs/)（待写）。
