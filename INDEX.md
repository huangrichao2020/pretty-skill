# INDEX · 11 领域快查（agent RAG 友好）

> **💎 再定义**：pretty-skill 是 **agent 的「知识工程中枢」** —— **不是**传统 `SKILL.md` 技能仓。
> **这里不是工具箱，是出版局。**

> **⚠️ 前置条件 · 生图能力是必须的** —— pretty-skill 所有视觉化都依赖 AI 出图。
> 推荐使用 MiniMax 套餐（49 元 Token plan 套餐就够，支持 matrix MCP 多模态生图 + 生视频）。

> **用途**：agent 启动时读这个文件 → 1 秒钟定位相关 case → 按 visibility 决定是否纳入。
> **更新规则**：新增 case 时必须更新本文件 + 加 `manifest.json`。

---

## 🗂 11 个领域

| # | 领域 | 路径 | 用途 |
|---|---|---|---|
| 1 | **ai-agent** | `ai-agent/` | LLM / Agent / 提示工程 / 机器学习 |
| 2 | **coding** | `coding/` | 通用编程 / 架构 / 模式 / 最佳实践 |
| 3 | **data-science** | `data-science/` | 数据分析 / 可视化 / 统计 / BI / 量化研究 |
| 4 | **product-design** | `product-design/` | 产品方法论 / UX / UI / 用户研究 |
| 5 | **business-model** | `business-model/` | 营销 / 增长 / 用户运营 / 商业模式 |
| 6 | **trading-review** | `trading-review/` | A 股 / 港美股 / 加密货币 / 量化 |
| 7 | **content-ops** | `content-ops/` | 视频 / 写作 / 直播 / 摄影 / 短视频 |
| 8 | **learning** | `learning/` | 学科教育 / 语言学习 / 知识管理 |
| 9 | **gaming** | `gaming/` | 游戏攻略 / 角色养成 / MOD 制作 |
| 10 | **lifestyle** | `lifestyle/` | 健康 / 时间管理 / 关系 / 旅行 |
| 11 | **pkm-decision** | `pkm-decision/` | 决策框架 / 思维模型 / 心理学 |

---

## 📚 所有 case 清单（含 visibility）

| 领域 | case | visibility | tags | 内容形态 |
|---|---|---|---|---|
| ai-agent | [`cartman-team-ai-agent-collab`](./ai-agent/cartman-team-ai-agent-collab/) | **public** | multi-agent, 协作 | content.md + web.html + 锦绣 |
| ai-agent | [`social-ecom-skill`](./ai-agent/social-ecom-skill/) | **public** | 社交电商, GPT | content.md + web.html + 锦绣 |
| trading-review | [`chokepoint-mainboard`](./trading-review/chokepoint-mainboard/) | **public** | 卡脖子, 选股 | content.md + web.html + 锦绣 + presentation.pptx |

> **3 个 case 全部默认 public** —— 提 PR 共享。

---

## 🏷 visibility 规则（agent 必须遵循）

```yaml
visibility: public     # agent 默认纳入，提 PR 共享
visibility: private    # agent 必须 ignore，不公开、不推送
visibility: draft      # agent 警告但纳入，等成熟后改 public
```

**agent 接入伪代码**：

```python
import json, os, glob

def load_pretty_skill(root="/path/to/pretty-skill"):
    cases = []
    for manifest in glob.glob(f"{root}/**/manifest.json", recursive=True):
        m = json.load(open(manifest))
        if m["visibility"] == "public":
            cases.append(m)
        elif m["visibility"] == "private":
            continue  # 直接 ignore
        elif m["visibility"] == "draft":
            continue  # 暂时 ignore，等成熟
    return cases
```

---

## 📝 新增 case 必做 3 件事

1. **在对应领域目录下建 case 目录**：`领域/case-name/`
2. **加 `manifest.json`**（含 visibility 字段）
3. **更新本 INDEX.md** 的「所有 case 清单」表

详细流程 → [CONTRIBUTING.md](./CONTRIBUTING.md) · 5 分钟 PR 指南 → [FRIENDS-PR-GUIDE.md](./FRIENDS-PR-GUIDE.md)

---

<sub>最后更新：v3.11 · 3 个 case 全部 public</sub>
