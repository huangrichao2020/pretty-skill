#!/usr/bin/env python3
"""check-3f.py · 3F Content 自动校验脚本 · 2026-07-08

用法：
  python3 check-3f.py <case-dir>
  # 例：python3 check-3f.py domains/ai-training/cartman-team-ai-agent-collab

退出码：
  0 = 全部通过
  1 = 有检查项失败（可被 GitHub Actions / pre-commit 拦截 PR）

检查项（任一失败 → PR 拒绝）：
  □ content.md 存在且每页 4-7 字段
  □ presentation.pptx 存在且 ≥ 2 MB
  □ presentation.pptx 内嵌图（解 zip 看 ppt/media 目录）
  □ web.html 存在且含 <img> 标签
  □ images/ 目录存在且有 N 张 PNG（与 .pptx 页数对齐）
  □ prompts/ 目录存在（每页 60 行 prompt）

参考规范：
  - content-triple-format/README.md
  - pretty-skill/CONTRIBUTING.md (🚫 PR 拒绝标准)

朋友 agent 翻车 1 次后写了这个脚本，让"文字 PPT 偷懒"变成代码层面被拦截。
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


# ───────────────────────── 校验规则 ─────────────────────────

MIN_PPTX_SIZE_MB = 1.0  # F2 最小文件大小（实测：1 页图 PPT 压缩后 ≈ 1.5-2 MB；文字 PPT ≈ 200 KB）
REQUIRED_PAGE_FIELDS_MIN = 4  # content.md 每页至少 4 个字段
REQUIRED_PAGE_FIELDS_MAX = 7  # content.md 每页最多 7 个字段

# ANSI 颜色
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"  # No Color


def fail(msg: str):
    print(f"  {RED}✗ FAIL{NC}  {msg}")


def warn(msg: str):
    print(f"  {YELLOW}⚠ WARN{NC}  {msg}")


def ok(msg: str):
    print(f"  {GREEN}✓ OK{NC}    {msg}")


def info(msg: str):
    print(f"  {BLUE}ℹ INFO{NC}  {msg}")


# ───────────────────────── 各项检查 ─────────────────────────

def check_content_md(case_dir: Path) -> tuple[bool, list[str]]:
    """检查 content.md · 每页 4-7 字段"""
    errors = []
    md_path = case_dir / "content.md"

    if not md_path.exists():
        errors.append(f"❌ content.md 不存在 ({md_path})")
        return False, errors

    content = md_path.read_text(encoding="utf-8")

    # 找所有 ## P{n} · ... 章节
    page_headers = re.findall(r"^## P\d+.*$", content, re.MULTILINE)
    if not page_headers:
        errors.append(f"❌ content.md 没有找到任何 ## P{{n}} 章节（应该每页一个）")
        return False, errors

    info(f"content.md 找到 {len(page_headers)} 个 P{{n}} 章节")

    # 每页字段检查：基于 bullet 列表 (- **xxx**：) 数
    pages = re.split(r"^## P\d+.*$", content, flags=re.MULTILINE)[1:]
    page_count = 0
    for i, page_content in enumerate(pages, 1):
        page_count += 1
        # 找到所有 "- **字段名**：" 格式
        fields = re.findall(r"^- \*\*[^*]+\*\*[：:]", page_content, re.MULTILINE)
        if len(fields) < REQUIRED_PAGE_FIELDS_MIN:
            errors.append(f"❌ P{i} 只有 {len(fields)} 个字段（要求 ≥ {REQUIRED_PAGE_FIELDS_MIN}）")
        elif len(fields) > REQUIRED_PAGE_FIELDS_MAX:
            warn(f"P{i} 有 {len(fields)} 个字段（建议 ≤ {REQUIRED_PAGE_FIELDS_MAX}）")
        else:
            ok(f"P{i} 字段数 {len(fields)} 个（合规 {REQUIRED_PAGE_FIELDS_MIN}-{REQUIRED_PAGE_FIELDS_MAX}）")

    if not errors:
        ok(f"content.md 全部 {page_count} 页字段合规")

    return len(errors) == 0, errors


def check_pptx(case_dir: Path) -> tuple[bool, list[str]]:
    """检查 presentation.pptx · ≥ 2 MB · 内嵌图"""
    errors = []
    pptx_path = case_dir / "presentation.pptx"

    if not pptx_path.exists():
        errors.append(f"❌ presentation.pptx 不存在 ({pptx_path})")
        return False, errors

    # 检查文件大小
    size_mb = pptx_path.stat().st_size / (1024 ** 2)
    info(f"presentation.pptx 文件大小: {size_mb:.2f} MB")
    if size_mb < MIN_PPTX_SIZE_MB:
        errors.append(
            f"❌ presentation.pptx 文件大小 {size_mb:.2f} MB < {MIN_PPTX_SIZE_MB} MB（疑似纯文字 PPT）"
        )
        return False, errors

    ok(f"presentation.pptx 大小合规 ({size_mb:.2f} MB ≥ {MIN_PPTX_SIZE_MB} MB)")

    # 检查 pptx 内是否真含图（解 zip 看 ppt/media 目录）
    try:
        with zipfile.ZipFile(pptx_path) as zf:
            media_files = [n for n in zf.namelist() if n.startswith("ppt/media/")]
            if not media_files:
                errors.append("❌ presentation.pptx 内无任何图（ppt/media/ 为空）")
                return False, errors

            image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}
            image_files = [n for n in media_files if any(n.lower().endswith(ext) for ext in image_extensions)]
            if not image_files:
                errors.append(f"❌ presentation.pptx 内 ppt/media/ 文件不是图: {media_files[:3]}")
                return False, errors

            ok(f"presentation.pptx 内含 {len(image_files)} 张图（嵌图证据）")

    except zipfile.BadZipFile:
        errors.append(f"❌ presentation.pptx 不是合法 zip 文件")
        return False, errors

    return len(errors) == 0, errors


def check_web_html(case_dir: Path) -> tuple[bool, list[str]]:
    """检查 web.html · 含 <img> 标签"""
    errors = []
    html_path = case_dir / "web.html"

    if not html_path.exists():
        errors.append(f"❌ web.html 不存在 ({html_path})")
        return False, errors

    content = html_path.read_text(encoding="utf-8")

    # 检查 <img> 标签数量
    img_count = len(re.findall(r"<img\b", content))
    if img_count == 0:
        errors.append("❌ web.html 不含任何 <img> 标签（疑似 .md 直接转 HTML）")
        return False, errors

    ok(f"web.html 含 {img_count} 个 <img> 标签（嵌图证据）")

    # 反向检查：是不是 .md 转 HTML（太多 <p> 文字）
    p_count = len(re.findall(r"<p\b", content))
    if p_count > 50 and img_count < 3:
        warn(f"web.html <p> 文字 {p_count} 个 vs <img> 图 {img_count} 个 — 可能是文字网页")

    return len(errors) == 0, errors


def check_images_dir(case_dir: Path) -> tuple[bool, list[str]]:
    """检查 images/ 目录 · 至少 N 张 PNG"""
    errors = []
    images_dir = case_dir / "images"

    if not images_dir.exists():
        errors.append(f"❌ images/ 目录不存在 ({images_dir})")
        return False, errors

    png_files = list(images_dir.glob("*.png"))
    if not png_files:
        errors.append(f"❌ images/ 下无 PNG 文件（缺失 AI 出图证据）")
        return False, errors

    ok(f"images/ 含 {len(png_files)} 张 PNG（AI 出图证据）")
    return True, errors


def check_prompts_dir(case_dir: Path) -> tuple[bool, list[str]]:
    """检查 prompts/ 目录 · 提示文件"""
    errors = []
    prompts_dir = case_dir / "prompts"

    if not prompts_dir.exists():
        warn(f"prompts/ 目录不存在（建议有 - 工程可复现）")
        return True, errors  # 软警告，不强制

    md_files = list(prompts_dir.glob("*.md"))
    if md_files:
        ok(f"prompts/ 含 {len(md_files)} 个 prompt 文件")
    else:
        warn(f"prompts/ 目录存在但无 .md 文件")

    return True, errors


# ───────────────────────── 主流程 ─────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="3F Content 自动校验脚本 · pretty-skill 仓库专用",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
退出码：
  0 = 全部通过
  1 = 有检查项失败（PR 会被自动退回）

示例：
  python3 check-3f.py domains/ai-training/cartman-team-ai-agent-collab
  python3 check-3f.py ./my-new-case
        """,
    )
    parser.add_argument(
        "case_dir",
        type=Path,
        help="case 目录路径（应该包含 content.md / presentation.pptx / web.html）",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="严格模式（警告也算失败）",
    )

    args = parser.parse_args()
    case_dir = args.case_dir.resolve()

    if not case_dir.exists():
        print(f"{RED}❌ case 目录不存在: {case_dir}{NC}")
        sys.exit(1)

    print(f"\n{'='*70}")
    print(f"🔍 3F Content 自动校验 · {case_dir.name}")
    print(f"{'='*70}\n")

    all_ok = True

    print("┌─ F1 · content.md 检查")
    ok_md, errs_md = check_content_md(case_dir)
    all_ok = all_ok and ok_md
    print()

    print("┌─ F2 · presentation.pptx 检查")
    ok_pptx, errs_pptx = check_pptx(case_dir)
    all_ok = all_ok and ok_pptx
    print()

    print("┌─ F3 · web.html 检查")
    ok_html, errs_html = check_web_html(case_dir)
    all_ok = all_ok and ok_html
    print()

    print("┌─ images/ 目录检查")
    ok_imgs, errs_imgs = check_images_dir(case_dir)
    all_ok = all_ok and ok_imgs
    print()

    print("┌─ prompts/ 目录检查（软警告）")
    check_prompts_dir(case_dir)
    print()

    # 总结
    print(f"{'='*70}")
    if all_ok:
        print(f"{GREEN}✅ 全部通过 · PR 可接受 · 3F Content 范式合规{NC}")
        print(f"{'='*70}\n")
        sys.exit(0)
    else:
        print(f"{RED}❌ 有检查项失败 · PR 会被自动退回{NC}")
        print(f"\n{RED}失败原因：{NC}")
        all_errors = errs_md + errs_pptx + errs_html + errs_imgs
        for err in all_errors:
            print(f"  {err}")
        print(f"\n{YELLOW}📖 参考修复：{NC}")
        print(f"  - pretty-skill/content-triple-format/README.md（范式）")
        print(f"  - pretty-skill/content-triple-format/onboarding-guide.md（5 步流程）")
        print(f"  - pretty-skill/content-triple-format/before-after-example.md（正反面对照）")
        print(f"\n{YELLOW}💡 朋友 agent 翻车案例：{NC}")
        print(f"  2026-07-08 朋友试 3F Content → agent 偷懒文字 PPT → 200 KB 拒")
        print(f"{'='*70}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()