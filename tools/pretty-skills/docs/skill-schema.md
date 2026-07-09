# Skill Manifest Schema

每个 pretty-skills 必须在根目录带 `manifest.yaml`，被 `ps` 工具扫描、验证、装到 5 agent。

## 必填字段

```yaml
name: serenity-stock-choke       # 必填 · 全局唯一 · 2-64 字符 [a-z0-9-]
version: 1.0.0                   # 必填 · semver · 0.0.0 形式
description: |                   # 必填 · 20-500 字符 · 一句话定位
  A股通用"卡脖子"选股技能，找"一旦断货整个产业就停工"的瓶颈环节。
author: huangrichao2020          # 必填
license: MIT                     # 必填 · SPDX
```

## 推荐字段

```yaml
tags:                            # 分类标签（最多 8）
  - stock
  - china
  - analysis

triggers:                        # 触发词（agent 用来判断要不要加载这个 skill）
  - 卡脖子
  - serenity分析
  - A股瓶颈

dependencies:                    # 依赖的其他 skill
  - name: pretty-skills
    version: ">=0.1.0"
    optional: false
  - name: qcc-stock
    optional: true               # 可选依赖（缺失时警告但不阻塞）

agents:                          # 兼容的 agent
  claude-code: true
  codex: true
  mavis: true
  cursor: true
  windsurf: true

entry: SKILL.md                  # 入口文件（默认 SKILL.md）
homepage: https://github.com/huangrichao2020/pretty-skills
```

## 完整示例

```yaml
name: serenity-stock-choke
version: 1.0.0
description: |
  A股通用"卡脖子"选股技能。应用 Serenity 的供应链瓶颈理论，
  对任意 A 股板块/产业链进行结构化分析，寻找"一旦断货整个产业就停工"的瓶颈环节。
author: huangrichao2020
license: MIT
tags: [stock, china, analysis]
triggers:
  - 卡脖子
  - serenity分析
  - A股瓶颈
dependencies:
  - name: pretty-skills
    version: ">=0.1.0"
  - name: qcc-stock
    optional: true
agents:
  claude-code: true
  codex: true
  mavis: true
  cursor: true
  windsurf: true
entry: SKILL.md
homepage: https://github.com/huangrichao2020/pretty-skills/tree/main/tools/serenity-stock-choke
```

## JSON Schema 验证

正式 schema 见 [`manifest-schema.json`](../manifest-schema.json)。

手动验证：

```bash
pip install jsonschema pyyaml
python3 -c "
import yaml, json, jsonschema
manifest = yaml.safe_load(open('manifest.yaml'))
schema = json.load(open('manifest-schema.json'))
jsonschema.validate(manifest, schema)
print('✅ manifest 合法')
"
```

## 为什么需要 manifest？

- **跨 agent 一致性** — Claude Code / Codex / Mavis / Cursor / Windsurf 都靠这个发现 skill
- **依赖图透明** — `ps graph` 靠 dependencies 字段生成 Mermaid 图
- **质量门** — `ps add` 拒绝没有合法 manifest 的 skill（防垃圾）
- **未来支持** — `ps search` / `ps publish` / `ps audit` 都基于 manifest 工作
