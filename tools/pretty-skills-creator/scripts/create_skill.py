#!/usr/bin/env python3
"""
create_skill.py — pretty-skills-creator 主脚本 · v3.20 PDF 时代

被 `ps create <name>` 调用。生成一个新 skill 的 4 件套：
  - xxx讲解.pdf.placeholder.md（PDF 必填占位说明，跑 build_case_pdf.py 生成真 PDF）
  - manifest.yaml (符合 pretty-skills manifest schema)
  - SKILL.md (agent 加载入口)
  - CHANGELOG.md (空模板)

校验：title ≥ 5 字 / description ≥ 100 字 / ≥ 3 个 trigger

v3.20 改造：
  - ❌ 删 web.html（GitHub 不能预览 + PPT 时代已被 PDF 替代）
  - ❌ 删 4 风格 HTML 模板（image / code-swiss / code-tech / code-paper）
  - ❌ 删 --style 参数（PPT 风格 picker 不再需要）
  - ✅ 改用 build_case_pdf.py（PIL 直接合并 PNG → PDF · 零装饰）
  - ✅ 4 件套：xxx讲解.pdf.placeholder.md + manifest.yaml + SKILL.md + CHANGELOG.md
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path


def validate_inputs(args) -> list[str]:
    errors = []
    if len(args.name) < 2 or len(args.name) > 64:
        errors.append(f"name '{args.name}' 长度不合法（2-64 字符）")
    if not all(c.islower() or c.isdigit() or c == '-' for c in args.name):
        errors.append(f"name '{args.name}' 必须全小写字母 + 数字 + -")
    if args.name.startswith('-') or args.name.endswith('-'):
        errors.append(f"name '{args.name}' 不能以 - 开头或结尾")
    if len(args.title) < 5:
        errors.append(f"title 太短 ({len(args.title)} 字)，至少 5 字")
    if len(args.description) < 100:
        errors.append(f"description 太短 ({len(args.description)} 字)，至少 100 字")
    if len(args.triggers) < 3:
        errors.append(f"触发词太少 ({len(args.triggers)} 个)，至少 3 个")
    return errors


def render_pdf_placeholder_md(args) -> str:
    """生成 xxx讲解.pdf 的占位说明 · 告诉用户怎么用 build_case_pdf.py 跑出来"""
    pdf_name = f"{args.title}讲解.pdf"
    return f"""# {pdf_name} · 生成占位

> **v3.20 PDF 时代**：每个 case 必须有 `{pdf_name}`（替代 v3.18 的 web.html）。
> GitHub 原生 PDF 预览 + 邮件分享 + 离线阅读，全面胜出。

## 用法

```bash
# 1. 把 AI 出图放到 images/ 目录
ls images/*.png
# slide-01.png / slide-02.png / ...  （每页 1 张图）

# 2. 跑 build_case_pdf.py 自动合并 → {pdf_name}
python3 ../../tools/build_case_pdf.py "{args.name}"
# 工具路径：pretty-skill/tools/build_case_pdf.py

# 3. 校验
python3 ../../content-triple-format/check-3f.py "{args.name}"
# F3 · xxx讲解.pdf 存在且 ≥ 0.1 MB → 通过
```

## 格式

- PIL 直接合并 PNG（v3.20 极简版 · 5 行核心）
- 零装饰：0 边框 / 0 页码 / 0 logo（用户明确要求）
- 16:9 横屏（1920×1080 默认）
- 文件大小：通常 1-5 MB（含 N 张图）

## 为什么不直接生成 web.html

| 维度 | web.html（旧）| {pdf_name}（v3.20）|
|---|---|---|
| GitHub 预览 | ❌ 不能（JS 渲染）| ✅ 原生 PDF preview |
| 邮件分享 | ❌ 多依赖 | ✅ 通用 |
| 离线阅读 | ⚠️ 需浏览器 | ✅ 任意 PDF 阅读器 |
| 文件大小 | 200-500 KB | 1-5 MB |
| 视觉表现力 | ⭐⭐⭐⭐⭐ 中央大图 + 翻页 | ⭐⭐⭐⭐ PDF 平铺 |

详见 `content-triple-format/case-pdf-spec.md`。
"""


def render_manifest_yaml(args) -> str:
    """生成符合 pretty-skills manifest schema 的 YAML。"""
    tags_str = "\n".join(f"  - {t}" for t in (args.tags or [])) or "  []"
    triggers_str = "\n".join(f"  - {t}" for t in args.triggers)

    return f"""name: {args.name}
version: 0.1.0
description: |
  {args.description}
author: {args.contributor}
license: MIT
tags:
{tags_str}
triggers:
{triggers_str}
agents:
  claude-code: true
  codex: true
  mavis: true
  cursor: true
  windsurf: true
entry: SKILL.md
homepage: https://github.com/huangrichao2020/pretty-skills/tree/main/tools/{args.name}
format:
  content_md: content.md
  case_pdf: {args.title}讲解.pdf
  jinxiu: false
"""


def render_skill_md(args) -> str:
    return f"""---
name: {args.name}
description: |
  {args.description}
triggers:
{chr(10).join(f"  - {t}" for t in args.triggers)}
---

# {args.title}

> {args.description.split(chr(10))[0]}

## 触发词

{chr(10).join(f"- {t}" for t in args.triggers)}

## 一句话定位

{args.description}

## 相关资源

{args.related or "（暂无）"}

## 维护者

@{args.contributor}

## 创建日期

{args.created}
"""


def render_changelog_md() -> str:
    return """# Changelog

## [0.1.0] - 创建

- 初始版本（占位）
"""


def main():
    p = argparse.ArgumentParser(
        description="生成新 skill 的 4 件套（xxx讲解.pdf + manifest.yaml + SKILL.md + CHANGELOG.md）· v3.20 PDF 时代",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("name", help="Skill 名（kebab-case，2-64 字符）")
    p.add_argument("--title", required=True, help="Skill 标题（≥ 5 字）")
    p.add_argument("--description", required=True, help="简介（≥ 100 字）")
    p.add_argument("--contributor", default="@anonymous", help="作者标识")
    p.add_argument("--triggers", nargs="+", required=True, help="触发词（≥ 3 个）")
    p.add_argument("--related", default="", help="关联资源描述")
    p.add_argument("--tags", nargs="*", default=[], help="标签")
    p.add_argument("--created", default="2026-07-10", help="创建日期 YYYY-MM-DD")
    p.add_argument("--out-dir", required=True, help="输出目录")
    p.add_argument("--dry-run", action="store_true", help="只看输出，不写文件")
    args = p.parse_args()

    errors = validate_inputs(args)
    if errors:
        print("❌ 校验失败：", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    pdf_placeholder = render_pdf_placeholder_md(args)
    manifest_yaml = render_manifest_yaml(args)
    skill_md = render_skill_md(args)
    changelog_md = render_changelog_md()

    out_dir = Path(args.out_dir) / args.name
    pdf_name = f"{args.title}讲解.pdf.placeholder.md"
    if args.dry_run:
        print(f"[dry-run] would write to: {out_dir}/")
        print(f"  - {pdf_name} ({len(pdf_placeholder)} bytes)")
        print(f"  - manifest.yaml ({len(manifest_yaml)} bytes)")
        print(f"  - SKILL.md ({len(skill_md)} bytes)")
        print(f"  - CHANGELOG.md ({len(changelog_md)} bytes)")
        print(f"\n[preview] xxx讲解.pdf 占位说明 head:\n{pdf_placeholder[:500]}\n")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / pdf_name).write_text(pdf_placeholder, encoding="utf-8")
    (out_dir / "manifest.yaml").write_text(manifest_yaml, encoding="utf-8")
    (out_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (out_dir / "CHANGELOG.md").write_text(changelog_md, encoding="utf-8")

    print(f"✅ v3.20 PDF 时代 · {out_dir}/")
    print(f"  - {pdf_name}")
    print(f"  - manifest.yaml")
    print(f"  - SKILL.md")
    print(f"  - CHANGELOG.md")
    print()
    print(f"下一步：")
    print(f"  1. cd {out_dir}")
    print(f"  2. 编辑 SKILL.md / manifest.yaml 补细节")
    print(f"  3. 准备 images/*.png（每页 1 张图）")
    print(f"  4. 跑 build_case_pdf.py 生成 {args.title}讲解.pdf：")
    print(f"     python3 ../../tools/build_case_pdf.py \"{args.name}\"")
    print(f"  5. ps add {args.name}  装到本地（先验）")
    print(f"  6. ps contribute {args.name}  推回主项目（提 PR）")


if __name__ == "__main__":
    main()
