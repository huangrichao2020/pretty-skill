# baoyu-design · 本地化 Claude Design 的 Agent skill

> **一句话定位**：把 Claude Design 的设计引擎打包成本地 Agent skill · Cursor / Claude Code / Codex 都能跑 · 自包含 HTML 输出。

---

## 这个 case 是什么

**页数**：4 页 · **领域**：视觉创作
**作者**：宝玉 xp（@jimliu）
**仓库**：`github.com/JimLiu/baoyu-design`
**状态**：case 草稿（未实跑 · 待 GitHub 网络恢复后 clone 验证）

## 核心论点

Claude Design 在线版很强,但**没法在本地 Agent 里跑**。宝玉把它的设计引擎打包成本地 skill——**不依赖云端 · 团队成员各自独立 · 设计风格一致**。

## 核心能力

- **本地化运行**：Cursor / Claude Code / Codex 70+ AI 代理支持
- **设计系统绑定**：从 Figma .fig 文件导入,自动重建设计系统
- **自包含输出**：纯 HTML + CSS + JS,断网可开,Git 友好
- **多格式导出**：独立 HTML / PDF / 可编辑 PPTX / Figma / Canva

## 4 步工作流

1. **需求澄清**（Agent 提问明确设计需求）
2. **设计上下文收集**（导入 Figma / GitHub / HTML/CSS 现有资源）
3. **设计系统绑定**（选择团队共享的设计系统）
4. **原型制作 → 评审 → 迭代**（预览链接 + 直接编辑修改）

## 5 个核心特性

| 特性 | 学到的 |
|---|---|
| **版本控制友好** | 纯 HTML/CSS/JS,可 Git 管理 |
| **设计系统绑定** | 避免"AI 味"（推荐 Adobe Spectrum 2）|
| **实时预览** | `python3 -m http.server 4311 --directory designs` |
| **二次编辑** | 直接在预览中改元素 |
| **团队协作** | 共享设计系统 + 锁版本 |

## 中文排版硬规矩 + AI 审美俗套黑名单（学得到）

宝玉的 baoyu-design 里默认带：
- **中文排版硬规矩**：行距 / 字间距 / 标点挤压 / 字体回退
- **AI 审美俗套黑名单**：禁止蓝紫渐变 / 禁止过度圆润 / 禁止统一圆角等

> 已被 sansheng-distill 第 12 条吸收

## 团队协作目录结构

```
team-project/
├── designs/              # 所有设计项目
│   ├── marketing-site/
│   └── mobile-app/
├── design-systems/       # 团队设计系统
│   ├── brand-system/
│   └── component-library/
└── shared-assets/
```

## 安装（待 clone 验证）

```bash
# 网络恢复后执行
npx skills add JimLiu/baoyu-design
# 或全局安装
npx skills add JimLiu/baoyu-design -g
```

**推荐配置**：Claude Opus 4.8（最佳设计效果）

## 触发词

"UI mockup" / "UI 设计" / "本地设计" / "Claude Design" / "Figma 导入" / "设计系统" / "baoyu" / "宝玉" / "自包含 HTML"

---

## 关联沉淀

- 内容创作相关 → `pretty-skills/内容创作/baoyu-skills/`
- AI 审美黑名单 / 中文排版 → `Mavis memory/distillation-review.md` 第 3 条
