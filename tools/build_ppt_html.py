#!/usr/bin/env python3
"""从 PPT HTML 模板生成具体 case 的 web.html（v3.18 增强）

用法（3 种）：

1. 自动模式（推荐）— 从 manifest.json 读 title + 从 images/ 读图序：
   python3 tools/build_ppt_html.py <case_dir>

2. 半自动 — 手动传 case_title（覆盖 manifest）：
   python3 tools/build_ppt_html.py <case_dir> "自定义标题"

3. 全手动 — 完全控制（兼容旧用法）：
   python3 tools/build_ppt_html.py <case_dir> "标题" p0_cover p1_problem ...

输出：<case_dir>/web.html（实例化好的 PPT 演示版 · 可本地浏览器打开）

跨平台：
- macOS: open web.html
- Linux: xdg-open web.html
- Windows: start web.html

v3.18 增强：
- 从 manifest.json 自动读 title / page_count
- 从 images/ 读 p*.png 顺序（按文件名排序）
- 不需要传图片列表参数
- --open 参数创建完自动打开浏览器
"""
import json
import sys
import subprocess
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "_模板/案例/web.html"


def load_manifest(case_dir: Path) -> dict | None:
    """读 manifest.json（如果存在）"""
    p = case_dir / "manifest.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"⚠️  manifest.json 解析失败: {e}")
        return None


def discover_images(case_dir: Path) -> list[str]:
    """从 images/ 自动读 p*.png（按文件名排序）"""
    images_dir = case_dir / "images"
    if not images_dir.exists():
        return []
    return sorted([f.name for f in images_dir.glob("p*.png")])


def generate(case_dir: Path, case_title: str, page_images: list[str], page_notes: list[str] = None) -> str:
    """实例化模板"""
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
    html = html.replace("{DEFAULT_NOTE}", f"{case_title} · pretty-skills PPT 演示版")

    return html


def open_in_browser(file_path: Path) -> None:
    """跨平台打开 web.html 在默认浏览器"""
    try:
        import platform
        system = platform.system()
        if system == "Darwin":  # macOS
            subprocess.Popen(["open", str(file_path.absolute())])
        elif system == "Linux":
            subprocess.Popen(["xdg-open", str(file_path.absolute())])
        elif system == "Windows":
            # Windows 需要 start 命令（cmd 内置）
            subprocess.Popen(["cmd", "/c", "start", "", str(file_path.absolute())], shell=False)
        else:
            print(f"⚠️  未知平台 {system}，跳过自动打开")
            return
        print(f"🌐 已自动打开浏览器: {file_path}")
    except FileNotFoundError:
        print(f"⚠️  找不到 open/xdg-open/start 命令，请手动打开: {file_path}")
    except Exception as e:
        print(f"⚠️  自动打开失败: {e}")


def main():
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print(__doc__)
        sys.exit(0 if "--help" in sys.argv else 1)

    # 解析参数
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    flags = {a for a in sys.argv[1:] if a.startswith("-")}
    open_after = "--open" in flags

    case_dir = Path(args[0])

    if not case_dir.exists():
        print(f"❌ Case 目录不存在: {case_dir}")
        sys.exit(1)

    # 自动从 manifest 读 title
    manifest = load_manifest(case_dir)
    auto_title = manifest.get("title") if manifest else None

    # 自动从 images/ 读图
    auto_images = discover_images(case_dir)

    # 解析剩余参数
    case_title = auto_title
    page_images = auto_images

    if len(args) >= 2:
        case_title = args[1]  # 手动标题覆盖 manifest
    if len(args) >= 3:
        page_images = args[2:]  # 手动图列表覆盖自动发现

    # 校验
    if not case_title:
        print("❌ 拿不到 case title（manifest.json 没 title 字段，也没传参数）")
        sys.exit(1)
    if not page_images:
        print(f"❌ 拿不到图片列表（{case_dir}/images/ 里没有 p*.png，也没传参数）")
        sys.exit(1)

    print(f"📝 Case: {case_dir}")
    print(f"📝 标题: {case_title}")
    print(f"📝 页数: {len(page_images)}")

    html = generate(case_dir, case_title, page_images)
    output = case_dir / "web.html"
    output.write_text(html, encoding="utf-8")

    size_kb = output.stat().st_size / 1024
    print(f"✅ 生成 {output} ({size_kb:.1f} KB)")

    if open_after:
        open_in_browser(output)


if __name__ == "__main__":
    main()