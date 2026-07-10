#!/usr/bin/env python3
"""从 case 内容 + 图片生成 xxx讲解.pdf（v3.19 · 替代 web.html）

为什么改：HTML 在 GitHub 不能预览，PDF 原生支持。

用法（3 种）：

1. 自动模式（推荐）— 从 manifest.json 读 title + 从 images/ 读图序：
   python3 tools/build_case_pdf.py <case_dir>

2. 半自动 — 手动传 title：
   python3 tools/build_case_pdf.py <case_dir> "自定义标题"

3. 显式参数 — 自定义输出名（默认 `<case_name>讲解.pdf`）：
   python3 tools/build_case_pdf.py <case_dir> --output "公众号内容交付方法论讲解.pdf"

输出：<case_dir>/<case_name>讲解.pdf

依赖：playwright + chromium（ms-playwright 已装）

v3.19 增强：
- PDF 替代 web.html（GitHub 原生预览支持）
- 每页 1 张图（大图）+ 标题
- 多页合并为单文件
- A4 横版 + 16:9 图自适应
- 自动从 manifest.json 读 title / 从 images/ 读 p*.png
"""
import argparse
import json
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌ playwright 未装。请先：pip install playwright && playwright install chromium",
          file=sys.stderr)
    sys.exit(1)

TEMPLATE_PATH = Path(__file__).parent.parent / "_模板/案例/case_pdf.html"


def load_manifest(case_dir: Path) -> dict | None:
    p = case_dir / "manifest.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"⚠️  manifest.json 解析失败: {e}")
        return None


def discover_images(case_dir: Path) -> list[Path]:
    images_dir = case_dir / "images"
    if not images_dir.exists():
        return []
    return sorted(images_dir.glob("p*.png"))


def build_html(case_title: str, image_paths: list[Path], case_dir: Path) -> str:
    """渲染 HTML 用于 PDF"""
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    # 把 image 路径转 file:// URL（chromium 可加载）
    page_html = ""
    for i, img in enumerate(image_paths, 1):
        img_url = img.absolute().as_uri()
        page_html += f'''
        <section class="page">
          <div class="page-header">
            <span class="page-num">{i:02d} / {len(image_paths):02d}</span>
            <span class="page-title">{case_title}</span>
          </div>
          <div class="page-image">
            <img src="{img_url}" alt="P{i}">
          </div>
          <div class="page-footer">
            <span>by Mavis</span>
            <span>pretty-skills · v3.19</span>
          </div>
        </section>'''

    return template.replace("{CASE_TITLE}", case_title).replace("{PAGES}", page_html)


def render_pdf(html: str, output_pdf: Path) -> None:
    """playwright + chromium 渲染 PDF"""
    import os
    chrome_path = (
        os.environ.get("CHROME_PATH")
        or "/Users/tingchi/Library/Caches/ms-playwright/"
           "chromium-1223/chrome-mac-arm64/"
           "Google Chrome for Testing.app/Contents/MacOS/"
           "Google Chrome for Testing"
    )
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            executable_path=chrome_path if Path(chrome_path).exists() else None,
        )
        context = browser.new_context()
        page = context.new_page()
        page.set_content(html, wait_until="networkidle")
        page.pdf(
            path=str(output_pdf),
            format="A4",
            landscape=True,
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从 case 目录生成 xxx讲解.pdf（替代 web.html）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("case_dir", help="case 目录路径（含 manifest.json + images/）")
    parser.add_argument("title", nargs="?", default=None,
                        help="自定义标题（默认从 manifest.json 读）")
    parser.add_argument("--output", "-o", default=None,
                        help="PDF 输出文件名（默认 <case_name>讲解.pdf）")
    parser.add_argument("--open", action="store_true",
                        help="生成后自动用默认 PDF 阅读器打开")

    args = parser.parse_args()

    case_dir = Path(args.case_dir).resolve()
    if not case_dir.exists():
        print(f"❌ 目录不存在: {case_dir}", file=sys.stderr)
        return 1

    # 1. 解析 title
    manifest = load_manifest(case_dir)
    if args.title:
        case_title = args.title
    elif manifest and "title" in manifest:
        case_title = manifest["title"]
    elif manifest and "name" in manifest:
        case_title = manifest["name"]
    else:
        case_title = case_dir.name
    print(f"📝 Case: {case_title}")

    # 2. 解析 images
    image_paths = discover_images(case_dir)
    if not image_paths:
        print(f"❌ images/ 下没找到 p*.png", file=sys.stderr)
        return 1
    print(f"🖼  {len(image_paths)} 张图")

    # 3. 输出 PDF 名
    if args.output:
        pdf_name = args.output
    else:
        case_name = manifest.get("name", case_dir.name) if manifest else case_dir.name
        pdf_name = f"{case_name}讲解.pdf"
    output_pdf = case_dir / pdf_name

    # 4. 渲染
    html = build_html(case_title, image_paths, case_dir)
    print(f"📄 渲染中...")
    render_pdf(html, output_pdf)
    size_kb = output_pdf.stat().st_size / 1024
    print(f"✅ 生成: {output_pdf} ({size_kb:.0f} KB)")

    # 5. 可选：打开
    if args.open:
        import subprocess
        import platform
        system = platform.system()
        if system == "Darwin":
            subprocess.Popen(["open", str(output_pdf)])
        elif system == "Linux":
            subprocess.Popen(["xdg-open", str(output_pdf)])
        elif system == "Windows":
            subprocess.Popen(["start", str(output_pdf)], shell=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())