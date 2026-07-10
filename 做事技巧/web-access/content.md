# web-access · 联网操作统一入口

> [3F Content 范式](../../content-triple-format/) · F1 源文字版

## P0 · 封面
- 所有联网操作的统一入口 · 反爬 + 动态渲染 + 社交媒体

## P1 · 痛点 · 联网操作的 5 大难题
- 反爬（验证码 / IP 限制 / 浏览器指纹）
- 动态渲染（JS SPA 内容获取）
- 登录态保持（OAuth / Cookie）
- 社交媒体抓取（小红书 / 微博 / 推特）
- 多端兼容（不同浏览器引擎）

## P2 · 6 项核心能力
- 网页搜索 / 网页抓取 / 登录后操作 / 动态渲染 / 反爬对抗 / 社交媒体抓取

## P3 · 4 步工作流
识别任务 → 选策略 → 执行（带反爬）→ 返回结果

## P4 · 与同类工具差异
- web-access：联网统一入口
- web-automation：智能整合（Playwright + OCR + MinerU）
- agent-browser：Rust 高性能

完整规范：[README.md](../README.md)