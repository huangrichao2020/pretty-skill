# web-access · 联网操作统一入口

> **一句话定位**：所有联网操作的统一入口 · 搜索 + 抓取 + 登录 + 反爬 + 动态渲染

---

## 这个 case 是什么

**作者**：MiniMax 官方 + Mavis 沉淀
**生成日期**：2026-07-10
**页数**：4 页
**所属领域**：做事技巧

## 核心论点

联网操作不该用 10 个不同工具 · web-access = 所有联网操作统一入口 · 搜索 / 抓取 / 登录 / 动态渲染 / 反爬 / 抓社交媒体。

## 核心方法论

### 1 · 触发场景（6 类）
- 搜索信息 / 查看网页 / 访问登录网站 / 操作网页界面
- 抓社交媒体（小红书 / 微博 / 推特）
- 读取动态渲染页面（JS SPA）

### 2 · 6 项核心能力
- 网页搜索（关键词 → URL 列表）
- 网页抓取（HTML → Markdown / 文本）
- 登录后操作（OAuth / Cookie 持久化）
- 动态渲染（JS SPA 渲染后内容）
- 反爬对抗（stealth / 验证码识别）
- 社交媒体抓取（小红书 / 微博 / 推特）

### 3 · 4 步工作流
识别任务类型 → 选择策略（搜索 / 抓取 / 操作）→ 执行（带反爬）→ 返回结果

### 4 · 与 web-automation / agent-browser 差异
- web-access：联网操作统一入口（含反爬）
- web-automation：智能整合（Playwright + OCR + MinerU）
- agent-browser：Rust 高性能浏览器

## 跨引用

- [3F Content 范式](../../content-triple-format/)
- [pretty-skills/做事技巧/agent-browser/](../agent-browser/)

## 贡献者

- @huangrichao2020（需求方）
- @Mavis（方法论沉淀）