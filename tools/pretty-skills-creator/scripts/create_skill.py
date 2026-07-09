#!/usr/bin/env python3
"""
create_skill.py — pretty-skills-creator 主脚本

被 `ps create <name>` 调用。生成一个新 skill 的 4 件套：
  - web.html (4 风格之一)
  - manifest.yaml (符合 pretty-skills manifest schema)
  - SKILL.md (agent 加载入口)
  - CHANGELOG.md (空模板)

校验：title ≥ 5 字 / description ≥ 100 字 / ≥ 3 个 trigger
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
VALID_STYLES = ["image", "code-swiss", "code-tech", "code-paper"]


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
    if args.style not in VALID_STYLES:
        errors.append(f"style '{args.style}' 不支持。可选：{VALID_STYLES}")
    return errors


def load_template(style: str) -> str:
    template_path = TEMPLATES_DIR / f"{style}.html"
    if not template_path.exists():
        raise FileNotFoundError(f"模板不存在：{template_path}")
    return template_path.read_text(encoding="utf-8")


def render_cover_html(args) -> str:
    if args.cover_image:
        return f'<img src="{args.cover_image}" alt="{args.title} 封面">'
    return '<div class="cover-placeholder">🆕 占位版暂无封面 · 完整版稍后补</div>'


def render_triggers_html(style: str, triggers: list[str]) -> str:
    if style == "image":
        return "".join(f"<span>{t}</span>" for t in triggers)
    elif style == "code-swiss":
        return "".join(f"<span>{t.upper()}</span>" for t in triggers)
    elif style == "code-tech":
        return "".join(f"<span>{t}</span>" for t in triggers)
    elif style == "code-paper":
        return "".join(f"<span>{t}</span>" for t in triggers)
    return ""


def render_html(args) -> str:
    from jinja2 import Template
    template_src = load_template(args.style)
    trigger_html = render_triggers_html(args.style, args.triggers)
    cover_html = render_cover_html(args) if args.style == "image" else ""

    status_badge = "🆕 占位 · 还在完善" if args.status == "placeholder" else "✅ 完整版"
    status_hint = (
        f"本 skill 当前为占位版 · 由 {args.contributor} 发起 · "
        f"完整 content.md / 锦绣 4 形态 / 真实 .pptx 稍后补充"
        if args.status == "placeholder"
        else f"本 skill 已完整发布 · 由 {args.contributor} 维护"
    )

    # 用 Jinja2 渲染（新模板）
    return Template(template_src).render(
        title=args.title,
        name=args.name,
        description=args.description,
        contributor=args.contributor,
        trigger_html=trigger_html,
        related=args.related or "（暂无）",
        created=args.created,
        cover_html=cover_html,
        status_class="" if args.status == "placeholder" else "complete",
        status_badge=status_badge,
        status_hint=status_hint,
    )


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
        description="生成新 skill 的 4 件套（web.html / manifest.yaml / SKILL.md / CHANGELOG.md）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("name", help="Skill 名（kebab-case，2-64 字符）")
    p.add_argument("--title", required=True, help="Skill 标题（≥ 5 字）")
    p.add_argument("--description", required=True, help="简介（≥ 100 字）")
    p.add_argument("--contributor", default="@anonymous", help="作者标识")
    p.add_argument("--triggers", nargs="+", required=True, help="触发词（≥ 3 个）")
    p.add_argument("--related", default="", help="关联资源描述")
    p.add_argument("--cover-image", default="", help="封面图 URL（仅 image 风格使用）")
    p.add_argument("--tags", nargs="*", default=[], help="标签")
    p.add_argument("--status", default="placeholder", choices=["placeholder", "complete"])
    p.add_argument("--created", default="2026-07-09", help="创建日期 YYYY-MM-DD")
    p.add_argument("--style", default="image", choices=VALID_STYLES,
                   help="HTML 风格: image(生图式, 默认) / code-swiss(瑞士风) / code-tech(技术深色) / code-paper(学术 paper)")
    p.add_argument("--out-dir", required=True, help="输出目录")
    p.add_argument("--dry-run", action="store_true", help="只看输出，不写文件")
    args = p.parse_args()

    errors = validate_inputs(args)
    if errors:
        print("❌ 校验失败：", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    html = render_html(args)
    manifest_yaml = render_manifest_yaml(args)
    skill_md = render_skill_md(args)
    changelog_md = render_changelog_md()

    out_dir = Path(args.out_dir) / args.name
    if args.dry_run:
        print(f"[dry-run] style: {args.style}")
        print(f"[dry-run] would write to: {out_dir}/")
        print(f"  - web.html ({len(html)} bytes)")
        print(f"  - manifest.yaml ({len(manifest_yaml)} bytes)")
        print(f"  - SKILL.md ({len(skill_md)} bytes)")
        print(f"  - CHANGELOG.md ({len(changelog_md)} bytes)")
        print(f"\n[preview] web.html head:\n{html[:500]}\n")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "web.html").write_text(html, encoding="utf-8")
    (out_dir / "manifest.yaml").write_text(manifest_yaml, encoding="utf-8")
    (out_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (out_dir / "CHANGELOG.md").write_text(changelog_md, encoding="utf-8")

    print(f"✅ [{args.style}] {out_dir}/")
    print(f"  - web.html ({len(html)} bytes)")
    print(f"  - manifest.yaml ({len(manifest_yaml)} bytes)")
    print(f"  - SKILL.md ({len(skill_md)} bytes)")
    print(f"  - CHANGELOG.md ({len(changelog_md)} bytes)")
    print()
    print(f"下一步：")
    print(f"  1. cd {out_dir} && 编辑 SKILL.md / manifest.yaml 补细节")
    print(f"  2. ps add {args.name}  装到本地（先验）")
    print(f"  3. ps contribute {args.name}  推回主项目（提 PR）")


if __name__ == "__main__":
    main()
