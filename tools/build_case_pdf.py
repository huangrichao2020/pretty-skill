#!/usr/bin/env python3
"""从 case 的 images/ 合并 PNG 成 xxx讲解.pdf（v3.20 · 极简版）

为什么改：v3.19 用 HTML 渲染加边框/页码 → 丑 + 图片被裁剪
v3.20 极简：图片按顺序合并成 PDF，每页 1 张图，无任何装饰

用法：
    python3 tools/build_case_pdf.py <case_dir>
    python3 tools/build_case_pdf.py <case_dir> --output "custom.pdf"
    python3 tools/build_case_pdf.py <case_dir> --open

依赖：Pillow（pip install Pillow）
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image


def load_manifest(case_dir: Path) -> dict | None:
    p = case_dir / "manifest.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def discover_images(case_dir: Path) -> list[Path]:
    images_dir = case_dir / "images"
    if not images_dir.exists():
        return []
    return sorted(images_dir.glob("p*.png"))


def merge_to_pdf(image_paths: list[Path], output_pdf: Path) -> None:
    """PIL 直接合并 PNG 为多页 PDF（无装饰）"""
    if not image_paths:
        raise ValueError("没有 PNG 可合并")

    # PIL PDF 限制：所有 page 必须是 RGB（不能 RGBA）
    first = Image.open(image_paths[0]).convert("RGB")
    rest_rgb = [Image.open(p).convert("RGB") for p in image_paths[1:]]

    first.save(
        output_pdf,
        "PDF",
        save_all=True,
        append_images=rest_rgb,
        resolution=100.0,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="合并 PNG 成 PDF（极简版 · 每页 1 张图 · 无装饰）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("case_dir", help="case 目录路径（含 images/p*.png）")
    parser.add_argument("--output", "-o", default=None,
                        help="PDF 输出文件名（默认 <case_name>讲解.pdf）")
    parser.add_argument("--open", action="store_true",
                        help="生成后自动用默认 PDF 阅读器打开")

    args = parser.parse_args()

    case_dir = Path(args.case_dir).resolve()
    if not case_dir.exists():
        print(f"❌ 目录不存在: {case_dir}", file=sys.stderr)
        return 1

    # 1. 解析图片
    image_paths = discover_images(case_dir)
    if not image_paths:
        print(f"❌ images/ 下没找到 p*.png", file=sys.stderr)
        return 1
    print(f"🖼  {len(image_paths)} 张图")

    # 2. 输出 PDF 名
    manifest = load_manifest(case_dir)
    if args.output:
        pdf_name = args.output
    else:
        case_name = manifest.get("name", case_dir.name) if manifest else case_dir.name
        pdf_name = f"{case_name}讲解.pdf"
    output_pdf = case_dir / pdf_name

    # 3. 合并
    print(f"📄 合并中...")
    merge_to_pdf(image_paths, output_pdf)
    size_kb = output_pdf.stat().st_size / 1024
    print(f"✅ 生成: {output_pdf.name} ({size_kb:.0f} KB · {len(image_paths)} 页)")

    # 4. 可选：打开
    if args.open:
        import subprocess, platform
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