# PR 模板 · pretty-skill

> **所有 PR 请按此模板填写**。
> **必跑检查**：`python content-triple-format/check-3f.py "<中文领域>/<你的 case 目录>"` 退出码 0 才提。
> **必含 3F**：`.md` + `xxx讲解.pdf` + `images/` + `prompts/` + `manifest.json`
> **可选**：`.pptx`（仅二次编辑）· `锦绣/`（公众号 + 自媒体用）

---

## 这个 PR 改了什么

<!-- 简要描述（1-3 句） -->

## 所属领域（必选 · 12 选 1 或新增）

> v3 预设 12 个中文领域 · 全球开发者都可以 PR 新领域（需附 README + ≥ 1 个 case）

### 12 预设领域

- [ ] **Agent知识**（LLM / Agent / 提示工程 / 机器学习 / agent 框架 / agent 工具链）
- [ ] **编程开发**（通用编程 / 架构 / 模式 / 最佳实践 / 前后端）
- [ ] **数据科学**（数据分析 / 可视化 / 统计 / BI）
- [ ] **产品设计**（产品方法论 / UX / UI / 用户研究）
- [ ] **商业运营**（营销 / 增长 / 用户运营 / 商业模式）
- [ ] **金融投资**（A 股 / 港美股 / 加密货币 / 量化）
- [ ] **内容创作**（视频 / 写作 / 直播 / 摄影）
- [ ] **教育学习**（学科教育 / 语言学习 / 知识管理）
- [ ] **游戏玩家**（游戏攻略 / 角色养成 / 副本流程 / MOD）
- [ ] **情感领域**（男女关系 / 长期关系 / 社交关系 / 亲密 / 心理 / 自我接纳）
- [ ] **做事技巧**（决策框架 / 思维模型 / 心理学 / 认知科学 / 做事方法）
- [ ] **玄学修炼**（占星 / 塔罗 / 易经 / 风水 / 命理 / 灵修 / 冥想 / 禅修）

### PR 新增领域（如选这栏，请填）

- 建议目录名（中英）:
- 1 句话领域定位:
- 是否包含 ≥ 1 个 case：

## 3F Content 自检（v3.20 PDF 时代 · 必填）

- [ ] `content.md` 已写（每页 4-7 字段，参考 `_模板/案例/content.md.template`）
- [ ] `xxx讲解.pdf` 已生成（`python3 tools/build_case_pdf.py <case_dir>`）
- [ ] `images/` 含 N 张 PNG（N = content.md 页数 · 2K · 16:9）
- [ ] `prompts/` 含 N 个 .md 文件（出图 prompt · 工程可复现）
- [ ] `manifest.json` 存在（visibility 字段必填）
- [ ] 本地 `python3 content-triple-format/check-3f.py <case_dir>` 退出码 0

## CI 必跑检查

- [ ] `check-3f` workflow 通过
- [ ] 没有引入 web.html（v3.20 已废弃 · 只用 PDF）
- [ ] 没有引入 `domains/` 目录（已重命名为中文领域目录）

## 测试说明

<!-- 你怎么验证这个 case 的？比如：本机 `ps list` 跑过 / 手动查 PDF 渲染 -->

## 关联 Issue / 案例

<!-- 关联 #issue · 关联其他 case · 关联 knowhub 文档 -->

---

> 💡 **PR 拒绝标准**（自动检测）：
> - 讲解 PDF 缺失或 < 50KB（疑似纯文字 PDF）
> - manifest.json 缺 visibility 字段
> - images/ PNG 数 ≠ content.md 页数
> - 标题、PDF、文件名命名不规范
>
> 完整规范：[CONTRIBUTING.md](../../CONTRIBUTING.md)