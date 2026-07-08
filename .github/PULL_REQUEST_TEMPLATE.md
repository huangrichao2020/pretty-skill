# PR 模板 · pretty-skill

> **所有 PR 请按此模板填写**。
> **必跑检查**：`python content-triple-format/check-3f.py "<中文领域>/<你的 case 目录>"` 退出码 0 才提。

---

## 这个 PR 改了什么

<!-- 简要描述（1-3 句） -->

## 路径（必填 · 中文领域一级目录）

- 中文领域（一级目录名）：（AI培训 / 金融分析 / 教育 / 自定义中文）
- Case 路径：`<中文领域>/<case 名>/`
- Case 名格式：（英文 kebab-case / 中文 kebab-case / 自选）

**示例**：
- 正确：`金融分析/chokepoint-mainboard/`
- 正确：`教育/小红书爆款拆解/`
- 错误：`cases/chokepoint-mainboard/`（已 deprecated）
- 错误：`domains/financial-analysis/chokepoint-mainboard/`（已 deprecated）

## 3 件套检查（必填）

- [ ] `content.md` 已写完（每页 4-7 字段）
- [ ] `output/<case_name>.pptx` 已生成（≥ 1 MB）
- [ ] `web.html` 已生成（含 `<img>` 标签）
- [ ] `images/` 目录有 N 张 PNG（与 content.md P{n} 数量一致）
- [ ] `prompts/` 目录有 N 个 prompt 文件（不是只有 README）

## 本地校验（必跑 · 退出码 0 才能提）

```bash
python content-triple-format/check-3f.py "<中文领域>/<case 名>/"
```

输出（截屏 or 贴文字）：
```
[ 这里贴 check-3f.py 输出 · 确认全部 ✓ OK + 一致性检查通过 ]
```

## 数据源（如适用）

- 行情数据：（通达信 MCP / 腾讯财经 / 东财 / 其他）
- 研报/资料：（来源 + 链接）
- AI 出图：（matrix / DALL-E / Midjourney / 其他）

## 风格（必填）

- 风格类型：（商务科技 / 手绘科教 / 城市插画 / 真实生活感 / 反套路金句 / 博物图鉴 / **深色科技风**）
- 配色：（马卡龙 / 古铜金 / 蓝白灰 / 红涨绿跌 A 股 / 自选 hex）
- 引用风格预设：[deep-themes.md 预设 1/2/自选]

## 检验（必填）

- [ ] 中文无错字
- [ ] 数字 / 时间 / 百分比 ≥ 1 个
- [ ] 金句 ≥ 1 句
- [ ] content.md 页数 == images/ PNG 数 == build_pptx.py PAGES 数

## 来源

- 案例来源：（公司 / 个人 / 公开演讲 / 内部培训 / 自创 / 等）
- 原始材料：（如有 PDF / 链接）

---

## ⚠️ 提交前必看

- [ ] 我已经本地跑过 `check-3f.py` 看到 exit 0
- [ ] 我没有「直接拿 .md 转 .pptx」（文字 PPT 会被自动拦截）
- [ ] 我没有「直接用 .md 转 .html」（纯文字网页会被自动拦截）
- [ ] 我没有「跳过 AI 出图步骤」

**4 个反模式 = 4 个自动拦截 = PR 100% 退回**。参考 [before-after-example.md](./content-triple-format/before-after-example.md) 看正确路径。

---

参考：
- [CONTRIBUTING.md](./CONTRIBUTING.md) · 完整贡献指南
- [STRUCTURE.md](./STRUCTURE.md) · 目录结构决策
- [onboarding-guide.md](./content-triple-format/onboarding-guide.md) · 5 步流程
- [check-3f.py](./content-triple-format/check-3f.py) · PR 自动校验脚本