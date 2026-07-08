#!/usr/bin/env python3
"""从 PPT HTML 模板生成具体 case 的 web.html

用法：
  python3 tools/build_ppt_html.py <case_dir> <case_title> [图片列表...]

例：
  python3 tools/build_ppt_html.py \\
    AI能力/cartman-team-ai-agent-collab \\
    "团队如何与 AI Agent 高效协作" \\
    p0_cover p1_problem p2_vision p3_context_layers p4_observation p5_memory_evolve p6_human_role p7_takeaways
"""
import sys
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "_模板/案例/web.html"


def generate(case_dir: Path, case_title: str, page_images: list[str], page_notes: list[str] = None) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    if page_notes is None:
        page_notes = [f"第 {i+1} 页 · {Path(img).stem}" for i, img in enumerate(page_images)]

    # 生成缩略图
    thumbs = "\n".join(
        f'    <div class="thumb" data-idx="{i}">'
        f'<img src="images/{img}" alt="P{i}">'
        f'<span class="thumb-num">{i+1}</span>'
        f'</div>'
        for i, img in enumerate(page_images)
    )

    # 生成 slide
    slides = "\n    ".join(
        f'<div class="slide" data-idx="{i}"><img src="images/{img}" alt="P{i}"></div>'
        for i, img in enumerate(page_images)
    )

    # 替换占位符
    html = template
    html = html.replace("{CASE_TITLE}", case_title)
    html = html.replace("{THUMBNAILS}", thumbs)
    html = html.replace("{SLIDES}", slides)
    html = html.replace("{PAGE_COUNT}", str(len(page_images)))
    html = html.replace("{PAGE_IMAGES_JS}", str(page_images))
    html = html.replace("{PAGE_NOTES_JS}", str(page_notes))
    html = html.replace("{DEFAULT_NOTE}", f"{case_title} · pretty-skill PPT 演示版")

    return html


def main():
    if len(sys.argv) < 3:
        print("用法: python3 build_ppt_html.py <case_dir> <case_title> [图片列表...]")
        print("例:  python3 build_ppt_html.py AI能力/cartman ... p0_cover p1_problem ...")
        sys.exit(1)

    case_dir = Path(sys.argv[1])
    case_title = sys.argv[2]
    page_images = sys.argv[3:]

    if not page_images:
        # 自动从 images/ 读取 p*.png
        images_dir = case_dir / "images"
        if images_dir.exists():
            page_images = sorted([f.name for f in images_dir.glob("p*.png")])
            print(f"  自动读取 {len(page_images)} 张图: {page_images[:3]}...")
        else:
            print("❌ 没提供图片列表 + images/ 目录也不存在")
            sys.exit(1)

    print(f"📝 Case: {case_dir}")
    print(f"📝 标题: {case_title}")
    print(f"📝 页数: {len(page_images)}")

    html = generate(case_dir, case_title, page_images)
    output = case_dir / "web.html"
    output.write_text(html, encoding="utf-8")

    size_kb = output.stat().st_size / 1024
    print(f"✅ 生成 {output} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()