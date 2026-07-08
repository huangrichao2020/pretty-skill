# USAGE · agent 接入指南（学一下 XXX 标准协议）

> **用途**：Mavis / Claude Code / Cursor / Aider 等 agent 看到这个文件 → 知道怎么把 pretty-skill 装进自己当**知识工程中枢**。
> **再定义**：pretty-skill **不是**「`SKILL.md` 技能仓」（那是 Anthropic Claude Skills 那套「按此执行 xxx」的预制工具）。本项目是**知识工程中枢** —— 产出的是「可复用的结构化知识产物」，不是「可调用的工具函数」。
> **配套**：README.md（做什么）· INDEX.md（11 领域快查）· STRUCTURE.md（结构定义）

> **⚠️ 前置条件 · 生图能力是必须的** —— pretty-skill 所有视觉化都依赖 AI 出图（出图是中枢产物的核心工序）。
> **推荐使用 MiniMax 套餐** —— **49 元 Token plan 套餐**就能跑（支持 matrix MCP 多模态生图 + 生视频，月费起步）。

---

## 1. 安装作为底层元知识库

```bash
git clone https://github.com/huangrichao2020/pretty-skill.git ~/pretty-skill
```

把项目放在 `~/pretty-skill`（或任意路径），告诉 agent 这个路径就行。

---

## 2. agent 启动时 load

agent 启动后第一件事：**读 INDEX.md** + **按 visibility 加载 case**。

```python
# 伪代码示意（不同 agent 实现各异）
from pathlib import Path
import json

PRETTY_SKILL_ROOT = Path.home() / "pretty-skill"

# Step 1: 读 INDEX.md 了解 11 领域
index = (PRETTY_SKILL_ROOT / "INDEX.md").read_text()

# Step 2: 遍历所有 manifest.json，按 visibility 过滤
def load_skills():
    for manifest_path in PRETTY_SKILL_ROOT.rglob("manifest.json"):
        meta = json.loads(manifest_path.read_text())
        if meta["visibility"] != "public":
            continue  # 私密/draft 直接 ignore

        case_dir = manifest_path.parent
        case = {
            "name": meta["name"],
            "domain": meta["domain"],
            "content_md": (case_dir / "content.md").read_text(),
            "tags": meta.get("tags", []),
        }
        yield case

skills = list(load_skills())
# 现在 agent 拥有了所有 public skill 的 content.md
```

---

## 3. 「学一下 XXX」标准协议

agent 收到 user 说「学一下 XXX」后，**不要直接装包**。走这个流程：

```text
用户说：「学一下 缠论」

Agent 内部流程：
1. search pretty-skill INDEX.md 的 tags 和 case-name
2. 找到相关 case → 读 content.md 拿核心方法
3. 提取有用部分 → 新建（or 更新）本地 pretty-skill case
4. 标记 visibility（public / private / draft）
5. 跟用户说：「学完了，已经加入 思维方法/缠论/」
```

**核心原则**：agent 永远不直接 `npm install xxx`，而是「学习 + 沉淀」到 pretty-skill。

### 私密 ignore 的标准用法

```yaml
# 用户用例：「学一下 我的私人投资策略」
# agent 内部流程：
new_case = {
  "name": "我的私人投资策略",
  "domain": "金融投资",
  "visibility": "private",   # ← 关键
  "tags": ["私人", "投资"]
}
# → 创建本地案例
# → 不提 PR
# → agent 在自己查询时直接 include（因为是在自己本地）
```

**区别**：
- `private` 不是「加密」，而是「不共享」
- 即使是 private case，agent 自己仍然要用
- 只有「通过 git push / PR 共享出去」时才 ignore
- 本地工作目录永远 100% 可访问

---

## 4. 「每晚 dream 修炼」标准协议

agent cron / schedule 每晚 23:00 跑：

```text
1. 读取当天所有对话记录（按 session 分组）
2. 提取高质量 case（用户说「记下来」「这个方法好」之类）
3. 反思不足（用户说「不对」「差点」之类）
4. 更新进本地 pretty-skill：
   - 新 case → 新建目录 + manifest.json
   - 旧 case 改进 → 修订 content.md
5. 第二天 agent 启动时即看到昨天的更新
```

**实现提示**：可以用 Mavis 的 cron skill 或 `mavis cron self` 触发。

---

## 5. 「提 PR」标准协议

case 标 `visibility: public` 后想共享：

```bash
cd ~/pretty-skill
git checkout -b feat/my-new-case
# 写 case...
git add .
git commit -m "feat(<领域>): add <case-name>"
git push origin feat/my-new-case
# 然后去 https://github.com/huangrichao2020/pretty-skill 提 PR
```

CI 自动跑 `check-3f.py` 验证 3 件套齐全 + 锦绣合格 → merge。

---

## 6. 与不同 agent 的集成

| Agent | 集成方式 |
|---|---|
| **Mavis (MiniMax Code)** | 自动 load 内存 + cron 调度 |
| **Claude Code** | `~/.claude/skills/pretty-skill` 软链 + read INDEX.md |
| **Cursor** | `.cursorrules` 引用 pretty-skill path + INDEX 检索 |
| **Aider** | `--read pretty-skill/INDEX.md` flag |
| **其他 LLM** | 任何能读文件的都可以 load INDEX.md + case |

**共同点**：永远 INDEX.md 是入口，永远 visibility 是过滤规则。

---

## 7. 一句话总结

**pretty-skill = agent 的元知识库。**
**用法 = clone + load + 学一下 + dream + PR。**
**精髓 = 私密忽略，公开共享，参与越多越好。**
