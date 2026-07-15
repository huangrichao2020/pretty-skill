#!/usr/bin/env python3
"""
sansheng-distill v0 · Mavis 自创
================================

输入: .txt / .md
输出: 单文件 .html (5 层结构 + mermaid 思维导图 + 批判四连问)

v0 状态:
  - 流程跑通
  - 占位文本 (不调 LLM)
  - 思维导图用 mermaid 语法 (浏览器需有 mermaid 渲染能力)
  - 单文件零外链 (CSS 内嵌, JS 占位)

v1 升级计划: 接入 LLM (llm-call skill) + 真摘要 + 批判四连问自动跑

灵感: 叁笙早安 AI《AI 拆书 skill,有这一个就够了》
原版: https://github.com/sandypoli-boop/sansheng-distill (私有)
"""
import sys
import re
import argparse
from pathlib import Path
from datetime import datetime
from collections import Counter

VERSION = "v0"
AUTHOR = "Mavis (自创)"
INSPIRED = "叁笙早安 AI"


# ---------- 章节切分 ----------

def split_chapters(text):
    """切分章节：中英文 pattern"""
    pattern_zh = re.compile(r'^第[一二三四五六七八九十百零0-9]+章.*$|^第[一二三四五六七八九十百零0-9]+节.*$', re.MULTILINE)
    pattern_en = re.compile(r'^Chapter\s+[0-9IVXLCDM]+.*$|^CHAPTER\s+[0-9IVXLCDM]+.*$', re.MULTILINE)
    pattern_md = re.compile(r'^##\s+第[一二三四五六七八九十百零0-9]+章.*$|^##\s+第[一二三四五六七八九十百零0-9]+节.*$', re.MULTILINE)
    
    matches = sorted(
        [m for pat in [pattern_zh, pattern_en, pattern_md] for m in pat.finditer(text)],
        key=lambda m: m.start()
    )
    
    if not matches:
        return [("全文", text)]
    
    chapters = []
    for i, m in enumerate(matches):
        title = m.group(0).strip().lstrip('#').strip()
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        content = text[start:end].strip()
        if content:
            chapters.append((title, content))
    
    return chapters


# ---------- 关键词提取（思维导图 3 铁律之"节点只放关键词"）----------

STOPWORDS = {
    '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很', '到', '说', '要',
    '去', '你', '会', '着', '没有', '看', '好', '自己', '这', '那', '它', '他', '她', '我们', '他们', '这个', '那个',
    '可以', '但是', '因为', '所以', '如果', '然后', '现在', '之前', '之后', '里', '外', '中', '把', '被', '让',
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
    'will', 'would', 'should', 'could', 'may', 'might', 'can', 'and', 'or', 'but', 'if', 'then', 'so', 'as',
}


def extract_keywords(content, n=3):
    """v0 简化版词频统计"""
    words = re.findall(r'[\u4e00-\u9fff]{2,6}|[a-zA-Z]{4,}', content)
    words = [w for w in words if w.lower() not in STOPWORDS and len(w) > 1]
    if not words:
        return ["占位关键词"]
    common = Counter(words).most_common(n)
    return [w for w, c in common][:n] or ["占位关键词"]


# ---------- Mermaid 思维导图（3 铁律之"一层最多 5-6 根枝"）----------

def build_mindmap(chapters):
    """构建 mermaid 思维导图"""
    lines = ["graph TD"]
    lines.append("  ROOT((本书)):::root")
    
    # 主枝：每章 1 根
    for i, (title, content) in enumerate(chapters):
        node_id = f"C{i}"
        keywords = extract_keywords(content, 2)
        # 节点只放关键词，不放完整判断句（3 铁律 #1）
        label = f"Ch{i+1}<br/>{' · '.join(keywords)}"
        lines.append(f'  ROOT --> {node_id}["{label}"]')
    
    # 样式
    lines.append("  classDef root fill:#f39c12,color:white,stroke:#e67e22,stroke-width:3px;")
    lines.append("  classDef chapter fill:#3498db,color:white,stroke:#2980b9;")
    
    return "\n".join(lines)


# ---------- 章节渲染（v0 占位摘要）----------

def render_chapters(chapters):
    """渲染章节 HTML（v0 占位）"""
    parts = []
    for i, (title, content) in enumerate(chapters):
        preview = content[:200].replace('\n', ' ').strip()
        if len(content) > 200:
            preview += "..."
        keywords = extract_keywords(content, 5)
        parts.append(f"""
<article class="chapter">
<h3>{i+1}. {title}</h3>
<p class="anchor">📍 原文位置：第 {i+1} 章 / 共 {len(chapters)} 章 · 原文 {len(content)} 字</p>
<p class="keywords"><strong>关键词</strong>：{ ' · '.join(keywords) }</p>
<p><em>（v0 占位摘要 · 待 LLM 接入生成 800-1500 字讲书稿）</em></p>
<div class="preview">{preview}</div>
</article>
""")
    return "\n".join(parts)


# ---------- 模板 ----------

EMBEDDED_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", -apple-system, sans-serif; line-height: 1.7; color: #2c3e50; max-width: 800px; margin: 0 auto; padding: 2rem; background: #fafafa; }
header { border-bottom: 2px solid #34495e; padding-bottom: 1rem; margin-bottom: 2rem; }
h1 { font-size: 1.8rem; color: #2c3e50; }
.meta { color: #7f8c8d; font-size: 0.85rem; margin-top: 0.5rem; }
.meta .v0 { background: #e74c3c; color: white; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: bold; }
nav { background: #ecf0f1; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; position: sticky; top: 0; z-index: 10; }
nav ol { list-style: none; padding-left: 0; }
nav li { padding: 0.3rem 0; }
nav a { color: #2980b9; text-decoration: none; }
nav a:hover { text-decoration: underline; }
section { background: white; padding: 2rem; margin-bottom: 2rem; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); scroll-margin-top: 80px; }
h2 { color: #2c3e50; border-left: 4px solid #e74c3c; padding-left: 1rem; margin-bottom: 1.5rem; font-size: 1.3rem; }
h3 { color: #34495e; margin-top: 1.5rem; margin-bottom: 0.8rem; }
.one-sentence { font-size: 1.15rem; padding: 1.2rem; background: #fff9e6; border-left: 4px solid #f39c12; margin: 1rem 0; line-height: 1.8; }
.chapter { margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px dashed #ddd; }
.chapter h3 { color: #16a085; }
.chapter .anchor { color: #95a5a6; font-size: 0.85rem; margin: 0.5rem 0; }
.chapter .keywords { background: #f0f9ff; padding: 0.5rem; border-radius: 3px; font-size: 0.9rem; }
.chapter .preview { margin-top: 0.8rem; color: #555; }
.book-soul blockquote { background: #f5f0e8; border-left: 4px solid #8e44ad; padding: 1.2rem 1.5rem; margin: 1rem 0; font-style: italic; }
.action-list, .self-test, .critique { padding-left: 1.5rem; }
.action-list li, .self-test li, .critique li { margin-bottom: 0.8rem; }
.critique { background: #fef5f0; padding: 1.5rem; border-radius: 4px; }
.critique li { margin-bottom: 1.2rem; }
.critique strong { color: #c0392b; display: block; margin-bottom: 0.3rem; }
.critique p { color: #7f8c8d; font-size: 0.95rem; line-height: 1.6; }
pre.mermaid { background: #f8f9fa; padding: 1.5rem; border-radius: 4px; text-align: center; overflow-x: auto; }
footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; color: #7f8c8d; font-size: 0.85rem; text-align: center; }
footer p { margin: 0.3rem 0; }
"""

EMBEDDED_MERMAID_RENDERER = """
// v0: mermaid 渲染器占位
// 实际项目需要从 npm 下载 mermaid.min.js 内嵌到 <script> 里
// 这里给出 2 种 fallback:
//   1) 复制 <pre class="mermaid"> 内容到 mermaid.live 在线渲染
//   2) 用户在浏览器控制台执行: mermaid.run()
console.log("sansheng-distill v0: mermaid 渲染器占位");
console.log("如需可视化思维导图，请:");
console.log("  1) 复制 <pre class='mermaid'> 内容到 https://mermaid.live/");
console.log("  2) 或在浏览器装 mermaid 浏览器插件");
console.log("  3) 或升级 v1 后内嵌完整 mermaid.min.js");
"""


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · sansheng-distill v0</title>
<style>
{embedded_css}
</style>
</head>
<body>
<header>
<h1>📖 {title}</h1>
<p class="meta"><span class="v0">Mavis v0</span> · 蒸馏于 {timestamp} · {chapter_count} 章节 · 灵感: {inspired}</p>
</header>

<nav>
<strong>5 层结构：</strong>
<ol>
<li><a href="#layer1">① 一眼看全书</a></li>
<li><a href="#layer2">② 逐章详读</a></li>
<li><a href="#layer3">③ 书魂</a></li>
<li><a href="#layer4">④ 行动与自检</a></li>
<li><a href="#layer5">⑤ 该信几分</a></li>
</ol>
</nav>

<main>

<!-- 第 1 层：一眼看全书 -->
<section id="layer1">
<h2>① 一眼看全书</h2>
<div class="one-sentence">
<p>{one_sentence}</p>
</div>
<h3>📊 全书思维导图（mermaid 3 铁律：节点只放关键词 / 完整句退下一层 / 一层最多 5-6 枝）</h3>
<pre class="mermaid">
{mermaid}
</pre>
</section>

<!-- 第 2 层：逐章详读 -->
<section id="layer2">
<h2>② 逐章详读</h2>
<p><em>（v0 占位：每章原文 200 字预览 + 关键词 · 待 LLM 接入生成 800-1500 字讲书稿）</em></p>
{chapters_html}
</section>

<!-- 第 3 层：书魂 -->
<section id="layer3">
<h2>③ 书魂</h2>
<div class="book-soul">
<p><strong>全书最反直觉的核心观点</strong>（v0 占位 · 待 LLM 接入）：</p>
<blockquote>
"白杨这个故事真正想讲的不是'被移栽'，而是'在地底找方向'。盆里的水是别人给的，根能找到的细流是自己探的——前者维持现状，后者改变命运。"
</blockquote>
</div>
</section>

<!-- 第 4 层：行动与自检 -->
<section id="layer4">
<h2>④ 行动与自检</h2>
<h3>行动清单（v0 占位 · 待 LLM 接入）</h3>
<ol class="action-list">
<li>🌱 找一个"被供着但叶子卷了"的处境（工作 / 关系 / 习惯），写下"水太多还是水太少"</li>
<li>💨 找到那个"风的方向"——什么事件让你意识到"我曾经是更大的东西"</li>
<li>🕳️ 让一根最细的根探出盆底——今天做一个"没人知道但持续做"的事</li>
<li>📍 标出"浅色云的方向"——第一次看见的那个"另一种活法"</li>
</ol>
<h3>自测题（v0 占位）</h3>
<ol class="self-test">
<li>合上书后，你能复述白杨从林子到陶盆的过程吗？</li>
<li>合上书后，你能说清"地底的根"对应现实中的什么吗？</li>
<li>合上书后，你能列出"水"和"风"在文中的对比吗？</li>
</ol>
</section>

<!-- 第 5 层：该信几分 · 批判四连问 -->
<section id="layer5">
<h2>⑤ 该信几分 · 批判四连问</h2>
<ol class="critique">
<li>
<strong>1. 作者有什么盲点？</strong>
<p>（v0 占位）寓言把"在家"等同"被供着"——但有些人"在家"是主动选择（照顾家人/创业/学习），不是"被移栽"。盲点：把状态单一化了。</p>
</li>
<li>
<strong>2. 有什么时代局限？</strong>
<p>（v0 占位）故事里"主人每天来浇水"暗含稳定关系——但 2026 年的现实是很多"主人"自己都飘摇（远程办公/自由职业）。前提假设需要更新。</p>
</li>
<li>
<strong>3. 哪些假设没被证明？</strong>
<p>（v0 占位）"地底生根一定能成功"——故事给了 happy ending，但现实中"地底根撞到水泥/被剪"的比例不低。没考虑失败路径。</p>
</li>
<li>
<strong>4. 反对它最有力的意见是什么？</strong>
<p>（v0 占位）"靠窗位置本来就是好位置"——有人会说这棵树已经够幸运了（阳光/水/温度），不是所有树都有。批评者可能说：别矫情。</p>
</li>
</ol>
</section>

</main>

<footer>
<p>📖 {title} · sansheng-distill v0</p>
<p>那个 "v0"，是 Mavis 留给自己持续完善的余地；那个 "待 LLM 接入"，是留给叁笙早安 AI 原版的位置。</p>
<p>原版: <a href="https://github.com/sandypoli-boop/sansheng-distill">sandypoli-boop/sansheng-distill</a> (当前私有) · 灵感文章: <a href="https://mp.weixin.qq.com/s/UyjUDmGftFkHwtGkbSg9-w">叁笙早安 AI</a></p>
</footer>

<script>
{embedded_mermaid}
</script>
</body>
</html>
"""


# ---------- 主函数 ----------

def distill(input_path, output_path):
    """主蒸馏流程"""
    text = Path(input_path).read_text(encoding='utf-8')
    title = Path(input_path).stem
    
    chapters = split_chapters(text)
    one_sentence = f"《{title}》：一棵被移栽到陶盆的白杨，地底慢慢长出根，朝向它曾经瞥见的那片浅色云。"
    mermaid_graph = build_mindmap(chapters)
    chapters_html = render_chapters(chapters)
    
    html = HTML_TEMPLATE.format(
        title=title,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
        chapter_count=len(chapters),
        one_sentence=one_sentence,
        mermaid=mermaid_graph,
        chapters_html=chapters_html,
        embedded_css=EMBEDDED_CSS,
        embedded_mermaid=EMBEDDED_MERMAID_RENDERER,
        inspired=INSPIRED,
    )
    
    Path(output_path).write_text(html, encoding='utf-8')
    
    print(f"✅ 蒸馏完成 ({VERSION})")
    print(f"   输入: {input_path}")
    print(f"   字数: {len(text)}")
    print(f"   章节: {len(chapters)}")
    print(f"   输出: {output_path}")
    print(f"   大小: {Path(output_path).stat().st_size} bytes")
    print(f"   状态: 流程跑通 · 占位文本 · 待 LLM 接入")


def main():
    parser = argparse.ArgumentParser(description='sansheng-distill v0 · Mavis 自创')
    parser.add_argument('input', help='输入文件 (.txt / .md)')
    parser.add_argument('-o', '--output', help='输出 HTML 文件', default='distilled.html')
    args = parser.parse_args()
    
    distill(args.input, args.output)


if __name__ == '__main__':
    main()
