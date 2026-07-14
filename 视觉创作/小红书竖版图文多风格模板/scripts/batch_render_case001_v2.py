#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2: 修复 bug - 每章重读 base.html，封面用占位符强替换"""
import re
import json
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/tingchi/.mavis/knowledge/pretty-skills/视觉创作/小红书竖版图文多风格模板/references/base.html")
THEMES_CSS = Path("/Users/tingchi/.mavis/knowledge/pretty-skills/视觉创作/小红书竖版图文多风格模板/references/themes.css")
JSON_PATH = Path("/Users/tingchi/Desktop/小红书_5风格实测/CASE001_19chapters.json")
OUT_DIR = Path("/Users/tingchi/Desktop/小红书_CASE001_手绘风回测")
THEME = "hand-drawn"


def fresh_base_with_inline_themes():
    """每次重读 base.html + 注入 themes.css"""
    h = BASE.read_text(encoding="utf-8")
    h = h.replace('</head>', f'<style>{THEMES_CSS.read_text(encoding="utf-8")}</style>\n</head>')
    h = re.sub(r'<link rel="stylesheet" href="themes\.css">', '', h)
    h = h.replace('data-theme="hand-drawn"', f'data-theme="{THEME}"')
    return h


def make_cover(ch):
    """封面：用 placeholder 强替换，不依赖 base.html 原文"""
    h = fresh_base_with_inline_themes()
    # 替换所有占位符
    h = h.replace('{{栏目名}}', '造物者说')
    h = h.replace('{{受访者}}', '叶孤城fight')
    h = h.replace('{{编号}}', ch["tag"])
    # 章节号 / 主标题 / 正文 / 金句 / 数据卡 全部替换为空
    h = re.sub(r'<div class="chapter-num">[^<]+</div>', '', h, count=1)
    h = re.sub(r'<h1 class="title">[^<]+</h1>', '', h, count=1)
    h = re.sub(r'<div class="body">.*?</div>', '', h, count=1, flags=re.DOTALL)
    h = re.sub(r'<div class="quote">[^<]+</div>', '', h, count=1)
    h = re.sub(r'<div class="cards">.*?</div>', '', h, count=1, flags=re.DOTALL)
    # case-num 替换
    h = re.sub(r'<div class="case-num">[^<]+</div>', f'<div class="case-num">{ch["tag"]}</div>', h)
    # 注入封面 title
    cover_title = f'<h1 class="title" style="top: 480px; text-align: center; font-size: 110px; line-height: 1.3; color: var(--accent);">{ch["title"]}</h1>'
    h = h.replace('<h1 class="title"></h1>', cover_title)
    # 注入封面副标
    subtitle_html = f'<div class="body" style="top: 1200px; text-align: center; font-size: 38px; padding: 0 100px;"><p>{ch["subtitle"]}</p></div>'
    h = h.replace('<div class="body"></div>', subtitle_html)
    return h


def make_chapter(ch):
    """章节页"""
    h = fresh_base_with_inline_themes()
    # 占位符
    h = h.replace('{{栏目名}}', '造物者说')
    h = h.replace('{{受访者}}', '叶孤城fight')
    h = h.replace('{{编号}}', 'CASE 001')
    h = h.replace('STYLE TEST', 'CASE 001')
    h = h.replace('01 / 5 风格对比测试', f'{ch["chapter"]} / {ch["topic"]}')
    h = h.replace('5 大 AI 生图风格对比', ch["title"])
    # 正文
    body = ch["body"].replace("\n", "</p>\n    <p>")
    h = re.sub(r'<div class="body">.*?</div>',
               f'<div class="body"><p>{body}</p></div>', h, count=1, flags=re.DOTALL)
    h = h.replace('骨架统一，色彩换调性。', ch["quote"])
    # 数据卡
    cards = ch["cards"]
    cards_html = "\n".join(
        f'    <div class="card">\n      <div class="num">{c[0]}</div>\n      <div class="label">{c[1]}</div>\n    </div>'
        for c in cards
    )
    h = re.sub(r'<div class="cards">.*?</div>', f'<div class="cards">\n{cards_html}\n  </div>', h, count=1, flags=re.DOTALL)
    return h


async def render():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    chapters = data["chapters"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 1920}, device_scale_factor=1)
        for ch in chapters:
            page = await ctx.new_page()
            html = make_cover(ch) if ch.get("type") == "cover" else make_chapter(ch)
            await page.set_content(html, wait_until="domcontentloaded")
            await page.wait_for_timeout(300)
            tag = "cover" if ch.get("type") == "cover" else ch["chapter"]
            out = OUT_DIR / f"p{tag}.png"
            await page.screenshot(path=str(out), full_page=True, omit_background=False)
            await page.close()
            print(f"[PNG] {out.name} {out.stat().st_size//1024}KB")
        await browser.close()


asyncio.run(render())

# 拼总览
images = sorted(OUT_DIR.glob("p*.png"), key=lambda p: (
    0 if "cover" in p.name else 1,
    p.name
))
print(f"\n[GRID] 共 {len(images)} 张")
if len(images) >= 20:
    cell_w, cell_h, label_h = 300, 400, 40
    cols = 5
    rows = (len(images) + cols - 1) // cols
    grid = Image.new("RGB", (cell_w * cols, (cell_h + label_h) * rows), (245, 245, 245))
    draw = ImageDraw.Draw(grid)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 18)
    except Exception:
        font = ImageFont.load_default()
    for i, p in enumerate(images):
        col, row = i % cols, i // cols
        im = Image.open(p).convert("RGB")
        im.thumbnail((cell_w, cell_h), Image.LANCZOS)
        x = col * cell_w + (cell_w - im.width) // 2
        y = row * (cell_h + label_h) + (cell_h - im.height) // 2
        grid.paste(im, (x, y))
        label = p.stem
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        draw.text((col * cell_w + (cell_w - tw) // 2, row * (cell_h + label_h) + cell_h + 8), label, fill=(20, 20, 20), font=font)
    grid_path = OUT_DIR / "CASE001_20章缩略总览.png"
    grid.save(grid_path, optimize=True)
    print(f"[GRID] {grid_path.name} {grid_path.stat().st_size//1024}KB")
