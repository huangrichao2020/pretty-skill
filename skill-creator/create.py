#!/usr/bin/env python3
"""skill-creator · pretty-skills v3 自动化工具 · v0.2 真实实现

输入 .md 知识 → 1 键生成完整 pretty-skills case 目录：
  - content.md (按页 4-7 字段)
  - manifest.json (含 --visibility 字段)
  - 锦绣/ 4 形态骨架 (cover-横屏 + cover-竖屏 + slides/ + readme.md)
  - web.html (PPT 演示版 HTML)
  - prompts/ (每页 matrix prompt 模板)
  - 接下来要做的步骤清单

用法：
  python create.py --input my-knowledge.md --domain "trading-review"
  python create.py --url https://example.com/article --domain "pkm-decision"
  python create.py --input my.md --domain "ai-agent" --visibility private

v0.2 新增：
  ✅ 真分页（按 ## 一、二、三 / ## P1: title）
  ✅ 真写 content.md + manifest.json + 锦绣骨架 + web.html + prompts
  ✅ 自动 kebab-case 化 case name
  ✅ 输出「下一步做什么」清单

依赖：
  pip install python-pptx (可选 · v0.2 不强求)

⚠️ 前置条件 · 生图能力是必须的
   这个工具生成的是「骨架」，要真视觉化必须调 AI 出图：
   **推荐使用 MiniMax 套餐** —— **49 元 Token plan 套餐**就能跑
   （支持 matrix MCP 多模态生图 + 生视频，月费起步）。
   没生图能力 = 只能跑骨架，骨架不是 pretty-skills 的精髓。
"""
import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

PRESET_DOMAINS = [
    "AI能力", "ai-agent",
    "编程开发", "coding",
    "数据科学", "data-science",
    "产品设计", "product-design",
    "商业运营", "business-model",
    "金融投资", "trading-review",
    "内容创作", "content-ops",
    "教育学习", "learning",
    "游戏玩家", "gaming",
    "生活方式", "lifestyle",
    "思维方法", "pkm-decision",
]

PRESET_STYLES = [
    "马卡龙", "古铜金", "蓝白灰", "深色科技风", "城市插画", "真实生活感",
]

# pretty-skills 锁定偏好（MEMORY § 11 · 2026-07-08 立）
DEFAULT_STYLE = "手绘马卡龙"
STYLE_DESCRIPTIONS = {
    "手绘马卡龙": "手绘叙事风 + 5 色马卡龙（粉/薄荷/淡黄/淡蓝/薰衣草）+ cream paper 底 + 深棕文字 → 经典 pretty-skills 风格",
    "马卡龙": "5 色马卡龙（粉/薄荷/淡黄/淡蓝/薰衣草）+ cream paper 底 → 简洁版马卡龙（less 手绘感）",
    "古铜金": "古铜色 + 金色 + 深棕背景 → 高端商业 / B 端产品发布",
    "蓝白灰": "蓝白灰极简 → 严谨商务 / 数据分析",
    "深色科技风": "deep slate (#0A0E14) + cyan (#00D4AA) 强调 → 程序员 / 极客 / Stripe / Linear 风格",
    "城市插画": "手绘城市建筑风 → 旅行 / lifestyle / 文化",
    "真实生活感": "写实摄影风 → 美食 / 健康 / 家居",
}


def pick_style_interactive() -> str:
    """v3.17+ · 弹出 7 选项让用户选风格 · 显式交互

    非交互 stdin（agent PIPE / 重定向 / EOF）→ 直接用默认「手绘马卡龙」+ 印提示
    """
    print("""
╔════════════════════════════════════════════════════════════╗
║  pretty-skills · 请选 PPT 视觉风格 + 主题颜色                  ║
╚════════════════════════════════════════════════════════════╝

选 1 个数字（默认 = 1 = pretty-skills 锁定的手绘马卡龙）：
""")

    options = list(STYLE_DESCRIPTIONS.items())
    for i, (name, desc) in enumerate(options, 1):
        marker = " ← pretty-skills 锁定的默认" if name == DEFAULT_STYLE else ""
        print(f"  {i}. {name}{marker}")
        print(f"     {desc}")

    print()

    # 非交互 stdin（agent 用 PIPE 调 create.py）→ 兜底默认
    if not sys.stdin.isatty():
        print(f"  ⚠️  检测到非交互 stdin（agent / 管道调用）→ 使用默认 = {DEFAULT_STYLE}")
        print(f"  💡 如需选其它风格：传 --style <name> 或在交互 shell 中跑")
        return DEFAULT_STYLE

    while True:
        raw = input(f"  请输入数字 (1-{len(options)}) 或直接回车（默认 = 1 = {DEFAULT_STYLE}）：").strip()
        if raw == "":
            print(f"  → 默认 = {DEFAULT_STYLE}")
            return DEFAULT_STYLE
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            chosen = options[int(raw) - 1][0]
            print(f"  → 选了：{chosen}")
            return chosen
        print(f"  ⚠️  请重新输入 1-{len(options)} 范围内的数字")


def parse_args():
    parser = argparse.ArgumentParser(
        description="skill-creator · pretty-skills 知识工程中枢自动化工具 v0.2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python create.py --input my-knowledge.md --domain "trading-review"
  python create.py --url https://example.com/article --domain "pkm-decision"
  python create.py --input my.md --domain "ai-agent" --visibility private

NOTE（v0.2 限制）:
  - 输入必须是 .md 文件（按 ## 一、二、三 风格分页）
  - 不真调 AI 出图（出图阶段需要用户手动调 matrix / DALL-E）
  - 不真嵌图到 PPTX（v0.2 之后才支持 · 用 --with-pptx 参数）
  - 输出的是「骨架」，用户填图后跑 check-3f.py 即可
        """,
    )
    parser.add_argument("--input", help="输入 .md 文件路径")
    parser.add_argument("--url", help="输入 URL（v0.2 仅做占位，v0.3+ 真支持）")
    parser.add_argument(
        "--domain", required=True, choices=PRESET_DOMAINS + ["新增"],
        help="11 预设领域之一（或「新增」= 走 PR 流程）",
    )
    parser.add_argument(
        "--style",
        choices=PRESET_STYLES + [DEFAULT_STYLE],
        help=f"视觉风格（7 选 1：{', '.join(PRESET_STYLES + [DEFAULT_STYLE])}）· 不传 = 弹出让用户选（默认 = {DEFAULT_STYLE}）",
    )
    parser.add_argument(
        "--pick-style", action="store_true",
        help="v3.17+ 显式弹出 interactive picker（默认未传也弹）",
    )
    parser.add_argument("--pages", type=int, default=9, help="PPT 页数（默认 9）")
    parser.add_argument("--output", default="./output/", help="输出父目录（默认 ./output/）")
    parser.add_argument("--case-name", help="case 目录名（默认 = .md 文件名 kebab-case）")
    parser.add_argument("--no-jinxiu", action="store_true", help="跳过锦绣 4 形态骨架生成")
    parser.add_argument(
        "--visibility", default="public",
        choices=["public", "private", "draft"],
        help="manifest.json 的 visibility 字段",
    )
    parser.add_argument(
        "--contributor", default="huangrichao2020",
        help="贡献者名字（默认 huangrichao2020）",
    )
    parser.add_argument(
        "--summary", default="",
        help="case 的一句话简介（留空则自动从首页提取）",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="v3.16+ 严格模式：检测到无生图能力时强制报错（不允许骨架图）",
    )
    return parser.parse_args()


# ───────────────────────── 输入解析 ─────────────────────────

def parse_input_md(content: str) -> tuple[str, list[dict]]:
    """解析 .md → (首页 / page 列表)

    分页规则（按优先级）：
      1. `## 一、xxx` / `## 二、xxx` （中文序号）
      2. `## P1: xxx` / `## P2: xxx` （P 数字）
      3. `## xxx` 普通 H2（依次 P1, P2...）
    """
    # 先提 H1 标题 + 首页 intro
    lines = content.split("\n")
    title_line = ""
    intro_lines = []
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("# ") and not title_line:
            title_line = line[2:].strip()
            body_start = i + 1
            continue
        if line.startswith("## "):
            break
        if line.strip().startswith(">") or line.strip() == "":
            intro_lines.append(line)
    intro = "\n".join(intro_lines).strip()

    # 按 H2 分页
    page_pattern = re.compile(r"^## (.+)$", re.MULTILINE)
    pages = []
    for match in page_pattern.finditer(content):
        title = match.group(1).strip()
        start = match.end()
        # 找下一个 H2 或文末
        next_match = page_pattern.search(content, pos=start)
        end = next_match.start() if next_match else len(content)
        page_body = content[start:end].strip()
        pages.append({"title": title, "body": page_body})

    return title_line or "Untitled", pages


def extract_fields(page_body: str) -> list[str]:
    """启发式提取 4-7 个字段

    优先级：
      1. `>` quote 块 → 1 字段
      2. bullet (`- xxx`) / numbered (`1. xxx`) 列表 → 每个 1 字段
      3. 段落（粗体强调） → 1 字段
      4. 没有就 fallback 到原 body 整段
    """
    fields = []

    # 1. quote blocks
    quote_blocks = re.findall(r"^>\s*(.+?)(?=\n[^>]|\Z)", page_body, re.MULTILINE | re.DOTALL)
    for q in quote_blocks:
        fields.append(q.strip().replace("\n", " "))
        if len(fields) >= 7: break

    # 2. bullet items
    if len(fields) < 4:
        bullets = re.findall(r"^[-*]\s+(.+)$", page_body, re.MULTILINE)
        for b in bullets:
            if len(fields) >= 7: break
            fields.append(b.strip())

    # 3. numbered items
    if len(fields) < 4:
        numbered = re.findall(r"^\d+\.\s+(.+)$", page_body, re.MULTILINE)
        for n in numbered:
            if len(fields) >= 7: break
            fields.append(n.strip())

    # 4. bold-emphasized line
    if len(fields) < 4:
        bolds = re.findall(r"\*\*([^*]+)\*\*", page_body)
        for b in bolds:
            if len(fields) >= 7: break
            fields.append(b.strip())

    # 5. fallback：整段
    if len(fields) < 4:
        plain = page_body.strip()
        if plain:
            fields.append(plain[:200])

    return fields[:7]


def to_kebab_case(s: str) -> str:
    """转 kebab-case：去特殊字符 + 全小写 + 空格转 -"""
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"[^\w\u4e00-\u9fff\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s.lower()


# ───────────────────────── 文件生成 ─────────────────────────

def write_manifest(case_dir: Path, args, page_count: int, summary: str):
    manifest = {
        "name": case_dir.name,
        "domain": args.domain,
        "title": case_dir.name,
        "visibility": args.visibility,
        "tags": ["待填"],
        "contributor": args.contributor,
        "contributor_github": args.contributor,
        "created": str(date.today()),
        "last_updated": str(date.today()),
        "format": {
            "content_md": "content.md",
            "web_html": "web.html",
            "锦绣": not args.no_jinxiu,
            "presentation_pptx": False,
        },
        "page_count": page_count,
        "summary": summary or "（v0.2 自动生成，待 creator 编辑）",
    }
    (case_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def write_content_md(case_dir: Path, title: str, intro: str, pages: list[dict]):
    """写 content.md（每页 4-7 字段 · YAML-like 格式）"""
    lines = [f"# {title}", ""]
    if intro:
        lines.extend([f"> {intro}", ""])
    lines.append("---")
    lines.append("")
    for i, page in enumerate(pages, 1):
        lines.append(f"## P{i}: {page['title']}")
        lines.append("")
        fields = extract_fields(page["body"])
        for f in fields:
            lines.append(f"- {f}")
        lines.append("")
    (case_dir / "content.md").write_text("\n".join(lines), encoding="utf-8")


def write_jinxiu_skeleton(case_dir: Path, args, page_count: int):
    """写 锦绣/ 4 形态骨架 + 提示"""
    if args.no_jinxiu:
        return
    jx = case_dir / "锦绣"
    jx.mkdir(exist_ok=True)
    # cover-横屏 占位
    cover_h = jx / "cover-横屏.png.placeholder"
    cover_h.write_text(
        f"# 占位 · cover-横屏.png\n"
        f"# 用法：调 matrix / DALL-E 出 1 张 16:9（1920×1080）横屏封面，\n"
        f"# 题目是「{case_dir.name}」，马卡龙 5 色手绘叙事风。\n"
        f"# 生成后保存到本文件名去掉 .placeholder。\n", encoding="utf-8"
    )
    # cover-竖屏
    cover_v = jx / "cover-竖屏.png.placeholder"
    cover_v.write_text(
        f"# 占位 · cover-竖屏.png\n"
        f"# 用法：1 张 3:4（1080×1440）或 9:16（1080×1920）竖屏封面，小红书/抖音/视频号专用。\n"
        f"# 题目同上，手绘马卡龙风。\n", encoding="utf-8"
    )
    # slides/
    slides = jx / "slides"
    slides.mkdir(exist_ok=True)
    for i in range(1, page_count + 1):
        (slides / f"slide-{i:02d}.png.placeholder").write_text(
            f"# 占位 · slide-{i:02d}.png\n"
            f"# 用法：1 张 16:9 讲解图，对应 content.md 中第 {i} 页。\n"
            f"# 马卡龙 5 色手绘叙事风，不堆字。\n", encoding="utf-8"
        )
    # readme.md（融合稿）
    readme = jx / "readme.md"
    readme.write_text(
        f"# {case_dir.name} · 融合稿\n\n"
        f"> 这是「锦绣」的融合 md，用于公众号 + 自媒体 + AI 阅读三用。\n\n"
        f"## 一句话简介\n\n"
        f"{args.summary or '（v0.2 自动生成，请在 manifest.json 和 web.html 中精修）'}\n\n"
        f"## 几个核心要点\n\n"
        f"（待 creator 填 · v0.2 占位）\n\n"
        f"## 一图胜千言\n\n"
        f"![cover](cover-横屏.png)\n", encoding="utf-8"
    )


def write_web_html(case_dir: Path, title: str, pages: list[dict]):
    """写 PPT 演示版 web.html（v3.2 规范）"""
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{title} · pretty-skills</title>
  <link rel="stylesheet" href="../../_模板/案例/web.css">
</head>
<body>
  <div class="ppt">
    <div class="slide cover">
      <h1>{title}</h1>
      <p class="subtitle">pretty-skills · 知识工程中枢</p>
      <p class="meta">visibility: {case_dir.parent.parent.name} · auto-generated by skill-creator v0.2</p>
    </div>
'''
    for i, page in enumerate(pages, 1):
        fields = extract_fields(page["body"])
        html += f'''    <div class="slide">
      <h2>P{i}: {page["title"]}</h2>
      <ul>
'''
        for f in fields:
            html += f'        <li>{f}</li>\n'
        html += '''      </ul>
    </div>
'''
    html += '''  </div>
</body>
</html>
'''
    (case_dir / "web.html").write_text(html, encoding="utf-8")


def write_prompts(case_dir: Path, title: str, pages: list[dict], args):
    """写 prompts/ · 每页 1 个 matrix prompt 模板"""
    prompts = case_dir / "prompts"
    prompts.mkdir(exist_ok=True)
    for i, page in enumerate(pages, 1):
        fields = extract_fields(page["body"])
        prompt_text = f'''# slide-{i:02d}.png prompt · pretty-skills · {title}

Style: 手绘叙事 + 马卡龙配色，cream paper 底色，深棕文字 #6B4423
Aspect: 16:9 (1920x1080)
Resolution: 2K

[主视觉]
{page["title"]}

[4-7 个要点（每点图标化）]
{chr(10).join(f"- {f}" for f in fields)}

[装饰]
手绘云 / 星星 / 咖啡杯 / 铅笔 / 便利贴（不同倾斜角）

[避免]
NO tech aesthetic, NO dark mode, NO neon, NO multi-color rainbow, NO English body, NO emoji as standalone
'''
        (prompts / f"slide-{i:02d}.md").write_text(prompt_text, encoding="utf-8")


def write_next_steps(case_dir: Path, args, page_count: int):
    """写 NEXT_STEPS.md · 接下来做什么"""
    next_md = f'''# Next Steps · 接下来做什么

> v0.2 骨架生成完成 · **你需要做的 5 步**：

## 1. 看骨架（5 分钟）

打开这两个文件：

- `content.md` —— 看每页要点是否齐全
- `web.html` —— 浏览器打开看 PPT 演示版是否 OK

## 2. 调 matrix 出图（10-30 分钟，**可选**走 prompts/）

```bash
# 用 prompts/slide-NN.md 作为 prompt 模板
# 调 matrix 或 DALL-E 出 16:9 2K PNG
# 保存到对应位置：
#   images/slide-NN.png   （喂 web.html）
#   锦绣/slides/slide-NN.png   （锦绣用）
#   锦绣/cover-横屏.png + cover-竖屏.png
```

> **不调出图也行** —— v0.2 留了 `.placeholder` 文件，check-3f.py 跑时会温和提醒。

## 3. 调 manifest（2 分钟）

打开 `manifest.json`：
- 填 `tags` 数组（多个）
- 填 `summary`（一句话讲清 case 是什么）
- `visibility` 字段已经按你传入的 `--visibility` 填好

## 4. 跑 check-3f 校验（30 秒）

```bash
python3 ../../content-triple-format/check-3f.py "{args.domain}/{case_dir.name}"
```

退出码 0 = 通过 / 1 = 失败 + 原因。

## 5. 提 PR 或本地使用

**如果 visibility=public**：
```bash
git add "{args.domain}/{case_dir.name}"
git commit -m "feat({args.domain}): add {case_dir.name}"
git push origin main  # 提 PR
```

**如果 visibility=private**：本地用，git push 时不共享。

---

> **v0.2 范围**：解析 .md → 4 件套骨架（content.md + manifest.json + web.html + 锦绣骨架）+ prompts 模板
>
> **v0.3 计划**：真调 matrix 出图 + 嵌图到 PPTX + 自动跑 check-3f
'''
    (case_dir / "NEXT_STEPS.md").write_text(next_md, encoding="utf-8")


def write_gitignore(case_dir: Path):
    """占位说明文件 .gitignore（让 placeholders 不入 git）"""
    (case_dir / "锦绣" / ".gitignore").write_text(
        "# 占位说明文件不入 git\n*.placeholder\n",
        encoding="utf-8"
    ) if (case_dir / "锦绣").exists() else None


# ───────────────────────── 主流程 ─────────────────────────

def main():
    args = parse_args()

    if not args.input:
        print("❌ 必须提供 --input（或 v0.3+ 的 --url）")
        sys.exit(1)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ 输入文件不存在: {input_path}")
        sys.exit(1)

    # v3.17+ · 视觉风格 picker · 没传 --style 就弹出让用户选（跑通关键流程）
    if not args.style or args.pick_style:
        args.style = pick_style_interactive()

    # v3.16+ · 严格模式检测 · 防止 agent 用代码生图凑合
    if args.strict and not args.no_jinxiu:
        has_api = bool(os.environ.get("MATRIX_API_KEY"))
        if not has_api:
            print("""
❌ 严格模式（--strict）+ 生图环节默认开启 → 需要 AI 出图 API

你没设环境变量 MATRIX_API_KEY，也没能调通的 AI 出图 API。

pretty-skills **不允许**用以下方式凑合当图：
  - Pillow / PIL 程序画图
  - HTML5 canvas 截图 → PNG
  - SVG → PNG 转码
  - matplotlib / seaborn 图表
  - ASCII art / emoji 拼接
  - 重复 1 张图 9 次
  - 空骨架 images/

v3.16+ 规则：
  没生图能力的 agent 应当**终止并报错**，不允许提交骨架或代码伪图。

请：
  A. 配 matrix MCP / MiniMax 套餐的环境变量 MATRIX_API_KEY
  B. 升级 MiniMax 套餐（49 元 Token plan）https://minimax.io/
  C. 切换到有生图能力的 agent（Mavis / Claude Code with MiniMax-M3 等）
""")
            sys.exit(2)

    # 1. 解析输入
    content = input_path.read_text(encoding="utf-8")
    title, pages = parse_input_md(content)

    if not pages:
        print(f"❌ .md 文件必须含至少 1 个 H2（## xxx）才能分页")
        print(f"   当前文件 {input_path} 没有 H2，v0.2 stub 退化为单页")
        pages = [{"title": "默认", "body": content}]

    # 2. case name 推导
    case_name = args.case_name or to_kebab_case(input_path.stem)
    if not case_name:
        case_name = "untitled-case"
    if not re.match(r"^[a-z0-9\-\u4e00-\u9fff]+$", case_name):
        print(f"⚠️  case-name '{case_name}' 含特殊字符，自动清理")
        case_name = re.sub(r"[^a-z0-9\-\u4e00-\u9fff]", "-", case_name)

    # 3. 准备目录
    output_dir = Path(args.output) / args.domain / case_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # 4. 写文件
    summary = args.summary
    if not summary and pages:
        # 自动从首页第 1 个 quote 提取
        first_page_fields = extract_fields(pages[0]["body"])
        summary = first_page_fields[0] if first_page_fields else ""

    print(f"""
╔════════════════════════════════════════════════════════════╗
║  skill-creator · pretty-skills v0.2 真实生成                ║
╚════════════════════════════════════════════════════════════╝

📥 输入：     {input_path.name} ({len(pages)} 页)
🎯 领域：     {args.domain}
🎨 风格：     {args.style}
📂 输出：     {output_dir}
🔒 可见性：   {args.visibility}
""")

    write_manifest(output_dir, args, len(pages), summary)
    print(f"  ✅ manifest.json ({args.visibility})")

    write_content_md(output_dir, title, "", pages)
    print(f"  ✅ content.md ({len(pages)} 页)")

    write_web_html(output_dir, title, pages)
    print(f"  ✅ web.html (PPT 演示版骨架)")

    write_jinxiu_skeleton(output_dir, args, len(pages))
    if not args.no_jinxiu:
        print(f"  ✅ 锦绣/ 4 形态骨架 (cover × 2 + {len(pages)} slides + readme.md)")

    write_prompts(output_dir, title, pages, args)
    print(f"  ✅ prompts/{len(pages)} 个 (matrix prompt 模板)")

    write_next_steps(output_dir, args, len(pages))
    print(f"  ✅ NEXT_STEPS.md (接下来做什么)")

    write_gitignore(output_dir)

    vis_msg = {
        "public": "shared globally via PR",
        "private": "private local · skip on git push",
        "draft": "draft · change to public later",
    }[args.visibility]

    print(f"""
🎉 v0.2 生成完成！

接下来：
  1. cd {output_dir}
  2. 打开 NEXT_STEPS.md · 看 5 步清单
  3. 调 matrix 出图（可选）→ 跑 check-3f.py 校验 → 提 PR

visibility={args.visibility} → {vis_msg}

详细文档：[content-triple-format/锦绣.md](../../content-triple-format/锦绣.md)
""")

    return 0


if __name__ == "__main__":
    sys.exit(main())
