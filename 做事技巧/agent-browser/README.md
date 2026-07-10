# Agent Browser · Rust 浏览器自动化

> **一句话定位**：快速 Rust 无头浏览器 · 网页抓取 + 自动化测试 + 截图 · AI 代理专用

---

## 这个 case 是什么

**作者**：MiniMax 官方 + Mavis 沉淀
**生成日期**：2026-07-10
**页数**：4 页
**所属领域**：做事技巧

## 核心论点

AI 代理需要浏览器但 WebDriver 太重 · agent-browser = Rust 无头浏览器 · 快速 + AI 友好 · 支持网页抓取 + 自动化测试 + 页面导航 + 表单填写 + 截图。

## 核心方法论

### 1 · 触发场景
- 浏览器自动化 / 网页抓取 / 自动化测试 / 页面导航 / 表单填写 / 截图 / 无头浏览器

### 2 · 4 项核心能力
- 网页抓取（content extraction）
- 自动化测试（UI 交互）
- 页面导航（URL 跳转 + 表单提交）
- 截图（视觉证据）

### 3 · 5 步工作流
启动浏览器实例 → 导航到 URL → 等待加载 → 提取内容 / 截图 → 关闭浏览器

### 4 · 与 web-access / web-automation 差异
- agent-browser：Rust 实现 · 高性能 · 适合大批量任务
- web-access：联网操作统一入口 · 包含反爬支持
- web-automation：智能整合（Playwright + OCR + MinerU）

## 跨引用

- [3F Content 范式](../../content-triple-format/)
- [pretty-skills/做事技巧/web-access/](../web-access/)

## 贡献者

- @huangrichao2020（需求方）
- @Mavis（方法论沉淀）