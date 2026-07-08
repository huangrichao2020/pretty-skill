# 仓库目录结构 · Structure Decision

> **TL;DR**：**所有新 case 用 `cases/<case-name>/` 扁平结构**。`domains/<area>/<case-name>/` 老结构**已 deprecated**——不要再用。
>
> **理由一句话**：扁平结构让 case 可发现性 + 跨领域可对比性都翻倍。

---

## ✅ 推荐结构 · `cases/<case-name>/`

```
cases/
├── chokepoint-mainboard/        ← 第一个 case
├── another-case/                ← 未来任意 case
└── ...
```

**为什么推荐扁平**：
1. **可发现性**：任何 case 都直接挂在 `cases/` 下，不需要先选「领域」再选「case」——少一步决策
2. **跨领域可对比**：你想对比「AI 培训 vs 金融 vs 教育」的同主题 case？直接看 `cases/` 即可，不需要翻 `domains/ai-training/` + `domains/financial-analysis/`
3. **命名自描述**：好的 case 名自带领域信息（`chokepoint-mainboard` = 主板卡脖子），不需要用「领域目录」分组
4. **避免分类争议**：很多 case 跨领域（`cartman-team-ai-agent-collab` 算 AI 培训还是协作方法论？），领域目录会引战

---

## ❌ Deprecated 结构 · `domains/<area>/<case-name>/`

```
domains/
├── ai-training/
│   ├── cartman-team-ai-agent-collab/  ← 第一个 case（v0 seed）
│   └── social-ecom-skill/
├── financial-analysis/
│   └── chokepoint-mainboard/          ← 朋友改路径时没删这个
└── ...
```

**为什么 deprecated**：
- ❌ 跨领域对比难（必须先选领域）
- ❌ 分类争议大（case 跨领域时塞哪个？）
- ❌ 路径长 3 层（`domains/financial-analysis/chokepoint-mainboard/content.md` 太深）
- ❌ 已有 1 个 PR 翻车：朋友改路径到 `cases/`，但**没删旧 `domains/financial-analysis/...`**—— 同一份内容在 2 个地方

**保留这个目录的原因**：
- 已有 v0 seed cases 在 `domains/ai-training/`（`cartman-team-ai-agent-collab` + `social-ecom-skill`）
- 不强行迁移，让 1.0 之后再说

---

## 🛠️ 现有 case 迁移路径（v0 → v1）

### 情况 A · 新 case（用 `cases/`）

直接复制 `_template/case/` 模板：

```bash
cp -r domains/_template/case cases/<你的-case-名>
cd cases/<你的-case-名>
# 改 content.md / build_pptx.py / web.html ...
```

### 情况 B · 改路径到 `cases/` 但忘了删旧（v2 PR 翻车）

如果你之前在 `domains/<area>/<name>/`，现在想改到 `cases/<name>/`：

```bash
# 1. 确认新路径已完整
ls cases/<name>/
# 应该有：content.md + build_pptx.py + web.html + images/ + output/ + prompts/

# 2. 删旧路径
git rm -r domains/<area>/<name>/
# ⚠️ 注意：不要删 domains/_template/case/（那是模板）

# 3. 改 README.md 跨引用（如果有指向旧路径的链接）
grep -r "domains/<area>/<name>" .  # 找引用
# 改 cases/<name> 替代

# 4. 跑 check-3f.py 验证
python content-triple-format/check-3f.py cases/<name>
# 退出码 0 = OK

# 5. 提交
git add -A
git commit -m "refactor: move <name> from domains/<area>/ to cases/"
git push
```

### 情况 C · 旧 `domains/ai-training/` 的 v0 seed cases

`cartman-team-ai-agent-collab` + `social-ecom-skill` 现在还在 `domains/ai-training/`。

**v1 不强迁**——保留作为历史。v2 之后（v1 路线图完成时）会统一迁到 `cases/` + 在 `domains/ai-training/README.md` 标 redirect。

---

## 📐 各路径约定

| 路径 | 用途 | 谁应该写 |
|---|---|---|
| `cases/` | **新 case 主目录** | 所有贡献者（新 PR） |
| `domains/<area>/` | **v0 老 case 保留** | 仓库主（v1 之后做迁移） |
| `domains/_template/case/` | **case 模板** | 仓库主（不要 PR 改这个） |
| `domains/README.md` | **领域类目说明**（如果将来加领域） | 仓库主 |
| `content-triple-format/` | **范式文档** | 仓库主（范式升级） |
| `.github/workflows/` | **CI/CD** | 仓库主 |
| `.github/PULL_REQUEST_TEMPLATE.md` | **PR 模板** | 仓库主 |
| `CONTRIBUTING.md` | **贡献指南** | 仓库主 |
| `FRIENDS-PR-GUIDE.md` | **5 分钟 PR 流程** | 仓库主 |

---

## 🚨 提 PR 时路径检查

**PR 提之前必查**：

```bash
# 1. 如果你提交了 cases/ 下的内容 → 确认没同时改 domains/ 下同名目录
diff -r cases/<你的-case> domains/<area>/<同名-case>
# 如果有差异 = 旧路径还在 = 必删

# 2. 跑 check-3f.py（自动校验）
python content-triple-format/check-3f.py cases/<你的-case>
# 退出码 0 = OK；1 = 失败 + 错误原因
```

**PR 模板**（`.github/PULL_REQUEST_TEMPLATE.md`）会强制你声明：
- [ ] 我用了 `cases/` 路径
- [ ] 如果我改路径到 `cases/`，已删旧 `domains/...` 路径
- [ ] 没有同一份内容在 2 个地方

---

## 🗓️ 未来计划

| 时间 | 改动 |
|---|---|
| **v1**（当前）| `cases/` 是新 case 标准；`domains/ai-training/` v0 seed 保留 |
| **v2**（v1 完成后）| 迁 `domains/ai-training/` → `cases/`；`domains/` 整目录标 deprecated |
| **v3**（长期）| `domains/` 目录删除（如果 v2 顺利） |

---

参考：
- [CONTRIBUTING.md](./CONTRIBUTING.md) · 完整贡献指南
- [FRIENDS-PR-GUIDE.md](./FRIENDS-PR-GUIDE.md) · 5 分钟 PR 流程
- [roadmap.md](./roadmap.md) · 仓库路线图