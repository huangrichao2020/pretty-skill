# pretty-skills-creator（创）

> **创** — 让创建新 skill 像"填一个表"一样简单。

## 当前状态

⚠️ **Day 4-5 迁移中**。本目录是占位，完整功能从 `~/.mavis/skills/create-skill-html/` 迁移过来。

临时使用方式见 Mavis 本地：

```bash
ls ~/.mavis/skills/create-skill-html/
cat ~/.mavis/skills/create-skill-html/SKILL.md
```

## 计划包含

- `create_skill.py` — 主脚本（被 `ps create` 调用）
- `templates/image.html` — 生图式风格模板
- `templates/code-swiss.html` — 瑞士风模板
- `templates/code-tech.html` — 技术深色模板
- `templates/code-paper.html` — 学术 paper 模板
- `manifest_form.py` — 交互式填 manifest.yaml 的表单
- `push_to_pretty_skill.sh` — 提 PR helper

## 进度

- [ ] 复制 4 HTML 模板从 `~/.mavis/skills/create-skill-html/templates/`
- [ ] 集成 4 风格 picker 到 `ps create` 主命令
- [ ] 写 manifest 表单
- [ ] 测试 4 风格 + 提 PR 全链路
- [ ] 撤回旧 PR #2（如果冲突）
