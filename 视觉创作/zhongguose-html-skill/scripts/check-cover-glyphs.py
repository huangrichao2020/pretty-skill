#!/usr/bin/env python3
"""Verify that a generated WOFF2 contains every requested Unicode character."""

from __future__ import annotations

import argparse
import base64
import io
import re
from pathlib import Path

from fontTools.ttLib import TTFont


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Path to the HTML with an embedded WOFF2, or to a generated WOFF2 file")
    parser.add_argument(
        "--text",
        action="append",
        required=True,
        help="Text whose characters must exist; repeat for multiple labels",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    source_path = args.source.resolve()
    if not source_path.is_file():
        raise SystemExit(f"Font or HTML not found: {source_path}")

    if source_path.suffix.lower() in {".html", ".htm"}:
        html = source_path.read_text(encoding="utf-8-sig")
        match = re.search(r"data:font/woff2;base64,([A-Za-z0-9+/=]+)", html)
        if not match:
            raise SystemExit(f"Embedded Zhongguose Cover WOFF2 not found: {source_path}")
        font = TTFont(io.BytesIO(base64.b64decode(match.group(1))))
    else:
        font = TTFont(source_path)
    codepoints = {
        codepoint
        for table in font["cmap"].tables
        for codepoint in table.cmap
    }

    failures: list[str] = []
    for text in args.text:
        missing = "".join(
            character
            for character in dict.fromkeys(text)
            if not character.isspace() and ord(character) not in codepoints
        )
        if missing:
            failures.append(f"{text}: {missing}")

    if failures:
        print("Cover-font glyph validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Cover-font glyph validation passed: {len(args.text)} text sample(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
