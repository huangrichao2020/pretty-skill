# INDEX · 11 领域快查（agent RAG 友好）

> **用途**：agent 启动时读这个文件 → 1 秒钟定位相关 case → 按 visibility 决定是否纳入。
> **更新规则**：新增 case 时必须更新本文件 + 加 `manifest.json`。

---

## 🗂 11 个领域

| # | 领域 | 路径 | 用途 |
|---|---|---|---|
| 1 | **AI能力** | `AI能力/` | LLM / Agent / 提示工程 / 机器学习 |
| 2 | **编程开发** | `编程开发/` | 通用编程 / 架构 / 模式 / 最佳实践 |
| 3 | **数据科学** | `数据科学/` | 数据分析 / 可视化 / 统计 / BI / 量化研究 |
| 4 | **产品设计** | `产品设计/` | 产品方法论 / UX / UI / 用户研究 |
| 5 | **商业运营** | `商业运营/` | 营销 / 增长 / 用户运营 / 商业模式 |
| 6 | **金融投资** | `金融投资/` | A 股 / 港美股 / 加密货币 / 量化 |
| 7 | **内容创作** | `内容创作/` | 视频 / 写作 / 直播 / 摄影 / 短视频 |
| 8 | **教育学习** | `教育学习/` | 学科教育 / 语言学习 / 知识管理 |
| 9 | **游戏玩家** | `游戏玩家/` | 游戏攻略 / 角色养成 / MOD 制作 |
| 10 | **生活方式** | `生活方式/` | 健康 / 时间管理 / 关系 / 旅行 |
| 11 | **思维方法** | `思维方法/` | 决策框架 / 思维模型 / 心理学 |

---

## 📚 所有 case 清单（含 visibility）

| 领域 | case | visibility | tags | 内容形态 |
|---|---|---|---|---|
| AI能力 | [`cartman-team-ai-agent-collab`](./AI能力/cartman-team-ai-agent-collab/) | **public** | multi-agent, 协作 | content.md + web.html + 锦绣 |
| AI能力 | [`social-ecom-skill`](./AI能力/social-ecom-skill/) | **public** | 社交电商, GPT | content.md + web.html + 锦绣 |
| 金融投资 | [`chokepoint-mainboard`](./金融投资/chokepoint-mainboard/) | **public** | 卡脖子, 选股 | content.md + web.html + 锦绣 + presentation.pptx |

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
