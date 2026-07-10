# Agent Browser · Rust 浏览器自动化

> [3F Content 范式](../../content-triple-format/) · F1 源文字版

## P0 · 封面
- AI 代理专用 Rust 无头浏览器 · 快 + AI 友好

## P1 · 痛点 · WebDriver 的 3 大问题
- 启动慢（秒级）
- 配置复杂（driver + browser 版本匹配）
- 不适合 AI agent 调用

## P2 · 4 项核心能力
- 网页抓取（content extraction）
- 自动化测试（UI 交互）
- 页面导航（URL 跳转 + 表单提交）
- 截图（视觉证据）

## P3 · 5 步工作流
启动浏览器 → 导航到 URL → 等待加载 → 提取 / 截图 → 关闭

## P4 · 与同类工具差异
- agent-browser：Rust · 高性能 · AI 友好
- web-access：联网操作统一入口
- web-automation：智能整合（Playwright + OCR + MinerU）

完整规范：[README.md](../README.md)