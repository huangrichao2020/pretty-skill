# 贡献指南

感谢你愿意贡献！pretty-skill 是一个 **对 AI 友好的中文 skill 沉淀仓库**，每个 skill 都按 **3 件套**（`.md` + `.pptx` + `.html`）发布。

## 5 分钟快速贡献

### 1. Fork 这个仓库

```bash
git clone https://github.com/<your-account>/pretty-skill
cd pretty-skill
```

### 2. 创建新 case

```bash
# 复制模板
cp -r domains/_template/case domains/ai-training/<your-case-name>

# 编辑文件
cd domains/ai-training/<your-case-name>
# 1. 改 content.md（用你的真实内容）
# 2. 改 README.md（用例说明）
# 3. 替换 presentation.pptx（用 ppt-orchestrator / 你的方式）
# 4. 替换 web.html（用 html-ppt-viewer / 你的方式）
```

### 3. 3 件套 checklist

```
✅ content.md           每页 4-7 字段（标题/副标/主张/要点/数字/金句）
✅ presentation.pptx    16:9 宽屏 · PowerPoint 可编辑 · 图嵌入（不是文字直转）
✅ web.html             浏览器直接看 · 键盘翻页 · 图嵌入（不是 .md 转 HTML）
✅ README.md            case 说明 + 跨引用 + 元信息
✅ images/              8 张 PNG（matrix 出图证据）
✅ prompts/             每页 60 行 prompt 文件（工程可复现）

**3 件套不全不收** —— 这是这个仓库的核心约定。
```

### 4. 流程必查（防 agent 偷懒文字直转 PPT）

**反模式**：直接拿 `.md` 文字转 `.pptx` → 文字 PPT（丑、缺图、信息密度低）

✅ **正确流程**：必须经过中间"AI 出图"步骤
```
content.md  →  prompt × N  →  matrix AI 出图  →  图嵌入 .pptx + .html
```

详细规范：[content-triple-format/README.md](./content-triple-format/README.md)

**PR 自动检测**：
- `.pptx` 内必须 embed 图（文件大小 ≥ 2 MB 通常含图）
- `web.html` 内必须含 `<img>` 标签（不是纯 `<p>` 文字）
- PR 时若检测到文字直转 → 自动退回

### 🚫 PR 拒绝标准（硬指标 · 自动检测）

**任一项打 ✗ = 拒绝 PR · 不接受修改余地**

```
□ F2 .pptx 文件大小 ≥ 2 MB（含图证据）
□ F2 .pptx 通过 add_picture() 嵌入 N 张 PNG（不是 text_frame 铺文字）
□ F3 .html 含 <img> 标签（不是纯 <p> 文字）
□ F3 .html 视觉是"设计稿"，不是"提纲列表"
□ images/ 目录下有 N 张原图（≥ 8 张）
□ prompts/ 目录下有 N 个 prompt 文件（每页 60 行）
```

**常见 PR 退回理由**：
| 你提交的 | 实际状态 | 退回原因 |
|---|---|---|
| 1 MB 的 .pptx | 文字 PPT | F2 必须 ≥ 2 MB |
| .html 全是 `<p>` | .md 转 HTML | F3 必须含 `<img>` |
| 只有 content.md 和 .pptx，没 images/ | 跳过了 AI 出图 | 必须有出图证据 |
| .pptx 是用 python-pptx `add_text` 写的 | text_frame 偷懒 | 必须 `add_picture` |

### 5. 提 PR

```bash
git add domains/ai-training/<your-case-name>
git commit -m "feat(ai-training): add <your-case-name> case (3F Content)"
git push origin main
# 然后在 GitHub 上开 PR
```

### 6. PR 模板（自动填充）

```
## 3 件套检查
- [ ] content.md 已写完
- [ ] presentation.pptx 已生成
- [ ] web.html 已生成
- [ ] README.md 已写

## 来源
- 案例来源：（公司 / 个人 / 公开演讲 / 内部培训 / 等）
- 原始材料：（如有 PDF / 链接）

## 风格
- 风格类型：（商务科技 / 手绘科教 / 城市插画 / 真实生活感 / 反套路金句 / 博物图鉴 / 自选）
- 配色：（马卡龙 / 古铜金 / 蓝白灰 / 自选）

## 检验
- 中文无错字
- 数字 / 时间 / 百分比 ≥ 1 个
- 金句 ≥ 1 句
```

## 4 条硬规则

1. **3 件套齐全** —— 不收不齐的 PR
2. **`.md` 为单一真相** —— `.pptx` / `.html` 内文以 `.md` 为准
3. **作者署名** —— `content.md` 顶部加作者 / 来源 / 日期
4. **不刷 star** —— 内容质量 > 互推数字

## 完整规范

[content-triple-format/README.md](./content-triple-format/README.md) —— 详细 3F Content 范式

## 提了 PR 之后

- ✅ README 同步收录到对应领域目录
- ✅ 自动加入 [CONTRIBUTORS.md](./CONTRIBUTORS.md)
- ✅ 你 GitHub 个人页 + 1 个「贡献者」标记

## 任何问题

- 提 Issue
- 或在 PR 评论里讨论

我们优先回复 —— 这是中文圈第一个按 3F Content 范式做的开源仓库，欢迎贡献者共建。