# PR 模板 · pretty-skill

> **所有 PR 请按此模板填写**。
> **必跑检查**：`python content-triple-format/check-3f.py "<中文领域>/<你的 case 目录>"` 退出码 0 才提。
> **必含**：3F Content（`.md` + `.pptx` + `.html`）+ **锦绣**（`锦绣/` 4 形态）

---

## 这个 PR 改了什么

<!-- 简要描述（1-3 句） -->

## 所属领域（必选 · 11 选 1 或新增）

> v3 预设 11 个中文领域 · 全球开发者都可以 PR 新领域（需附 README + ≥ 1 个 case）

### 11 预设领域

- [ ] **AI能力**（LLM / Agent / 提示工程 / 机器学习）
- [ ] **编程开发**（通用编程 / 架构 / 模式 / 最佳实践 / 前后端）
- [ ] **数据科学**（数据分析 / 可视化 / 统计 / BI）
- [ ] **产品设计**（产品方法论 / UX / UI / 用户研究）
- [ ] **商业运营**（营销 / 增长 / 用户运营 / 商业模式）
- [ ] **金融投资**（A 股 / 港美股 / 加密货币 / 量化）
- [ ] **内容创作**（视频 / 写作 / 直播 / 摄影）
- [ ] **教育学习**（学科教育 / 语言学习 / 知识管理）
- [ ] **游戏玩家**（游戏攻略 / 角色养成 / 副本流程 / MOD）
- [ ] **生活方式**（健康 / 时间管理 / 关系 / 旅行）
- [ ] **思维方法**（决策框架 / 思维模型 / 心理学 / 认知科学）
- [ ] **🆕 新增领域**（必须附 `新领域/README.md` + `新领域/案例1/`）

### 路径声明

- 领域目录：（11 选 1）
- Case 路径：`<领域>/<case 名>/`
- Case 名格式：（英文 kebab-case / 中文 kebab-case）

## 3F Content 检查（必填 · 给 AI 读）

- [ ] `content.md` 已写完（每页 4-7 字段）
- [ ] `output/<case_name>.pptx` 已生成（≥ 1 MB）
- [ ] `web.html` 已生成（含 `<img>` 标签）
- [ ] `images/` 目录有 N 张 PNG（与 content.md P{n} 数量一致）
- [ ] `prompts/` 目录有 N 个 prompt 文件（不是只有 README）

## 锦绣检查（必填 · 给人看 · v3.1 简化）

- [ ] `锦绣/cover-横屏.png` 已生成（1 张 16:9 大图）
- [ ] `锦绣/cover-竖屏.png` 已生成（1 张 3:4 或 9:16 大图）
- [ ] `锦绣/slides/` 已生成（8-12 张讲解图）
- [ ] `锦绣/readme.md` 已生成（融合 md · 公众号 + 自媒体稿 + AI 阅读）
- [ ] 视觉风格选自 6 套预设（马卡龙 / 古铜金 / 蓝白灰 / 深色科技风 / 城市插画 / 真实生活感）

> **不限定发哪个平台** —— creator 拿到素材后自己决定发朋友圈/小红书/抖音/推特/...

## 本地校验（必跑 · 退出码 0 才能提）

```bash
python content-triple-format/check-3f.py "<领域>/<case 名>/"
```

输出（截屏 or 贴文字）：
```
[ 这里贴 check-3f.py 输出 · 确认全部 ✓ OK + 锦绣层校验通过 ]
```

## 数据源（如适用）

- 行情数据：（通达信 MCP / 腾讯财经 / 东财 / 其他）
- 研报/资料：（来源 + 链接）
- AI 出图：（matrix / DALL-E / Midjourney / 其他）

## 风格（必填）

- 风格类型：（马卡龙 / 古铜金 / 蓝白灰 / 深色科技风 / 城市插画 / 真实生活感）
- 配色 hex：（必填 · 锦绣视觉一致性靠这个）

## 检验（必填）

- [ ] 中文无错字
- [ ] 数字 / 时间 / 百分比 ≥ 1 个
- [ ] 金句 ≥ 1 句
- [ ] content.md 页数 == images/ PNG 数 == build_pptx.py PAGES 数

## 来源

- 案例来源：（公司 / 个人 / 公开演讲 / 内部培训 / 自创 / 等）
- 原始材料：（如有 PDF / 链接）
- 是否用 skill-creator 生成初稿：（是 / 否）

---

## ⚠️ 提交前必看

- [ ] 我已经本地跑过 `check-3f.py` 看到 exit 0
- [ ] 我没有「直接拿 .md 转 .pptx」（文字 PPT 会被自动拦截）
- [ ] 我没有「直接用 .md 转 .html」（纯文字网页会被自动拦截）
- [ ] 我没有「跳过 AI 出图步骤」
- [ ] 我没有「跳过锦绣 4 形态」
- [ ] 我的领域选择正确（11 预设之一 或 PR 新增）

**5 个反模式 = 5 个自动拦截 = PR 100% 退回**。参考 [before-after-example.md](./content-triple-format/before-after-example.md) 看正确路径。

---

参考：
- [CONTRIBUTING.md](./CONTRIBUTING.md) · 完整贡献指南
- [STRUCTURE.md](./STRUCTURE.md) · 目录结构决策
- [content-triple-format/README.md](./content-triple-format/README.md) · 3F Content 范式
- [content-triple-format/锦绣.md](./content-triple-format/锦绣.md) · 锦绣范式
- [onboarding-guide.md](./content-triple-format/onboarding-guide.md) · 5 步流程
- [check-3f.py](./content-triple-format/check-3f.py) · PR 自动校验脚本