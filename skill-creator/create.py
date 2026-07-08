#!/usr/bin/env python3
"""skill-creator · pretty-skill v3 自动化工具 · 主脚本

任何知识 → 1 键生成完整 pretty-skill 目录（3F Content + 锦绣）

用法：
  python create.py --input my-knowledge.md --domain "金融投资" --style "深色科技风"
  python create.py --url https://example.com/article --domain "思维方法"

依赖：pip install python-pptx
"""
import argparse
import sys
from pathlib import Path

PRESET_DOMAINS = [
    "AI能力", "编程开发", "数据科学", "产品设计", "商业运营",
    "金融投资", "内容创作", "教育学习", "游戏玩家", "生活方式", "思维方法",
]

PRESET_STYLES = [
    "马卡龙", "古铜金", "蓝白灰", "深色科技风", "城市插画", "真实生活感",
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="skill-creator · pretty-skill 自动化工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python create.py --input my-knowledge.md --domain "金融投资" --style "深色科技风"
  python create.py --url https://example.com/article --domain "思维方法"
        """,
    )
    parser.add_argument("--input", help="输入 .md 文件路径")
    parser.add_argument("--url", help="输入 URL（与 --input 二选一）")
    parser.add_argument(
        "--domain", required=True, choices=PRESET_DOMAINS + ["新增"],
        help="11 预设领域之一（AI能力 / 编程开发 / 数据科学 / 产品设计 / 商业运营 / 金融投资 / 内容创作 / 教育学习 / 游戏玩家 / 生活方式 / 思维方法 / 新增）",
    )
    parser.add_argument(
        "--style", default="蓝白灰", choices=PRESET_STYLES,
        help="视觉风格（马卡龙 / 古铜金 / 蓝白灰 / 深色科技风 / 城市插画 / 真实生活感）· 默认蓝白灰",
    )
    parser.add_argument("--pages", type=int, default=9, help="PPT 页数（默认 9）")
    parser.add_argument("--output", default="./output/", help="输出目录（默认 ./output/）")
    parser.add_argument("--no-jinxiu", action="store_true", help="跳过锦绣 4 形态生成")
    parser.add_argument("--api-key", help="AI 出图 API key（默认读 MATRIX_API_KEY 环境变量）")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.input and not args.url:
        print("❌ 必须提供 --input 或 --url 其中之一")
        sys.exit(1)

    print(f"""
╔════════════════════════════════════════════════════════════╗
║  skill-creator · pretty-skill v3 自动化工具                  ║
╚════════════════════════════════════════════════════════════╝

📝 输入：     {args.input or args.url}
🎯 领域：     {args.domain}
🎨 风格：     {args.style}
📄 页数：     {args.pages}
📂 输出：     {args.output}
🌟 锦绣：     {'跳过' if args.no_jinxiu else '生成 4 形态'}
""")

    # TODO v0.1: 实现完整 3F Content + 锦绣生成
    print("⚠️  v0.1 还是 stub - 完整实现见 skill-creator/README.md 路线图")
    print()
    print("📋 v0.1 已实现：")
    print("  ✅ 命令行参数解析")
    print("  ✅ 11 领域 + 6 风格预设校验")
    print()
    print("🚧 v0.2 计划：")
    print("  - 解析 .md 输入 → content.md 4-7 字段/页")
    print("  - 调 matrix MCP 出图（9 张）")
    print("  - python-pptx 嵌图 → presentation.pptx")
    print("  - html-ppt-viewer → web.html")
    print("  - 锦绣 4 形态生成（cover + 9图 + PPT + 视频脚本）")
    print()
    print("🌟 完整 3F Content + 锦绣：参考 content-triple-format/ 范式")
    print("   📘 [content-triple-format/README.md](../content-triple-format/README.md)")
    print("   📘 [content-triple-format/锦绣.md](../content-triple-format/锦绣.md)")

    return 0


if __name__ == "__main__":
    sys.exit(main())