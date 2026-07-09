# pretty-skills（管）

> **管** — 跨 agent 统一管理你的所有 skill 和知识。

## 一句话

**pretty-skills = 一个 `ps` 命令管 5 agent 的所有 skill。**

## 快速开始

```bash
# 一行装（首次）
curl -fsSL https://raw.githubusercontent.com/huangrichao2020/pretty-skills/main/tools/pretty-skills/install.sh | bash

# 之后随时用
ps list                        # 看本地装的所有 skill
ps info <name>                 # 看某个 skill 的详情
ps add <name>                  # 从主项目装一个
ps rm <name>                   # 卸载
ps update [name]               # 拉主项目最新
ps graph                       # 输出 Mermaid 依赖图
ps contribute <name>           # 把本地修改推回主项目（提 PR）
ps create <name>               # 调 pretty-skills-creator 创建新 skill
ps sync                        # 批量 update
```

## 文档

| 文档 | 干什么 |
|---|---|
| [`SKILL.md`](SKILL.md) | agent 加载入口（agent 读这个） |
| [`docs/install.md`](docs/install.md) | 安装指南 |
| [`docs/skill-schema.md`](docs/skill-schema.md) | manifest.yaml 怎么写 |
| [`docs/contributing.md`](docs/contributing.md) | 怎么提 PR |
| [`CHANGELOG.md`](CHANGELOG.md) | 版本变更 |
| [`manifest-schema.json`](manifest-schema.json) | JSON Schema 验证 |

## 目录结构

```
tools/pretty-skills/
├── SKILL.md                    # agent 加载入口
├── README.md                   # 你正在看
├── install.sh                  # 一键装 5 agent
├── manifest-schema.json        # JSON Schema
├── CHANGELOG.md                # 版本变更
├── lib/
│   └── common.sh               # 公共库（5 agent 安装都 source 这个）
├── cli/
│   ├── ps                      # 主命令（dispatcher）
│   ├── ps-list                 # 列出本地所有 skill
│   ├── ps-info                 # 显示 skill 详情
│   ├── ps-add                  # 从主项目装一个
│   ├── ps-rm                   # 卸载
│   ├── ps-update               # 拉主项目最新
│   ├── ps-graph                # 输出 Mermaid 依赖图
│   ├── ps-contribute           # 把本地修改推回主项目（提 PR）
│   ├── ps-create               # 调 pretty-skills-creator
│   └── ps-sync                 # 批量 update
└── docs/
    ├── install.md
    ├── skill-schema.md
    └── contributing.md
```

## 跟主仓库的关系

- **本仓库根目录的 `README.md`** — 讲整个 pretty-skills 是什么（双产品定位）
- **`tools/pretty-skills/`** — 管（这个目录）
- **`tools/pretty-skills-creator/`** — 创（完整迁移）
