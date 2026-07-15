# templates/ · 教程类 H5 骨架

> 4 个核心文件 · 复制后改 data.js 即可出活 · 30-60 分钟出 1 个新 H5

## 文件清单

| 文件 | 大小 | 作用 | 改不改 |
|---|---|---|---|
| `index.html` | < 1KB | 壳（顶栏 + 视图容器 + 2 个 script src） | ❌ 一般不改 |
| `main.js` | < 8KB | SPA 路由 + 3 视图（home / course-X / placeholder） | ❌ 一般不改 |
| `data.js` | < 3KB | **4 节占位 + 1 节完整示例** | ✅ 主要改这个 |
| `style.css` | < 10KB | 杂志海报风蓝白灰（统一视觉） | ❌ 一般不改 |

## 30 分钟起步

```bash
# 1. 复制整个 templates/ 到新项目目录
cp -r templates/ my-new-course/
cd my-new-course/

# 2. 改 data.js（占位的部分）
#    - meta.title / subtitle / motto / coverImage
#    - courses[].title / subtitle / built
#    - 把 4 节都改成 built: true + 完整 sections

# 3. 准备图（4 张 16:9 + 1 张 1:1 logo）
#    - 共享 [4 STYLE] 段（参考 SKILL.md 决策 1）
#    - matrix MCP 批量生图
#    - 拍平到项目根（不是 assets/ 子目录）

# 4. 跑自检 + 打 zip + 上传
```

## 字符串陷阱（**必读**）

**data.js 里的所有 string value 必须用反引号 \` 包**——不能用双引号或单引号。

```js
// ❌ 错的（双引号嵌套）
hook: "你以为你用的是 AI，其实是 LLM"思考者""
// ↑ "思考者"" 终止外层字符串

// ✅ 对的（反引号）
hook: `你以为你用的是 AI，其实是 LLM"思考者"`
// ↑ " 不影响反引号字符串
```

**自动检测**：

```bash
grep -nE '"[^"]*"[^,]*"[^"]*"' data.js
# 输出空 = 没有嵌套问题
```

## 拍平 vs 子目录（**必读**）

小红书"小工具"容器对 `assets/` 子目录图片有 bug，**必须拍平**到项目根：

```
my-new-course/
├── index.html
├── main.js
├── data.js
├── style.css
├── 00-cover.jpg       ← 拍平（不是 assets/00-cover.jpg）
├── 01-section-1.jpg
├── 02-section-2.jpg
├── 03-section-3.jpg
└── 00-logo.jpg         ← 1:1 logo（给小红书"图标"框用）
```

data.js 里：

```js
image: "./00-cover.jpg"  // 不是 "./assets/00-cover.jpg"
```

## 6 项自检（打包前必走）

```bash
# 1. 包结构
unzip -l my-new-course.zip | head -3
# 期望第一行是 index.html（不是 my-new-course/index.html）

# 2. DOCTYPE / lang / charset / viewport
grep -c "<!DOCTYPE html>" index.html     # = 1
grep -c 'lang="zh-CN"' index.html         # = 1
grep -c 'charset="UTF-8"' index.html      # = 1
grep -c "viewport-fit=cover" index.html   # = 1

# 3. 禁用项
grep -cE "<script>[^<]" index.html        # = 0
grep -c "onclick=" index.html             # = 0
grep -cE "eval\(|new Function\(" main.js # = 0
grep -c "<iframe" index.html             # = 0

# 4. 外链
grep -E 'src="|href="' index.html | grep -E 'https?://'  # 空输出

# 5. 路径
grep -E 'src="/|href="/' index.html  # 空输出

# 6. 体积
du -sh my-new-course.zip  # < 3MB
```

## 打包 + 上传

```bash
# 打包（注意：压缩目录内容，不是目录本身）
zip -r ../my-new-course.zip . -x '*.DS_Store'

# 上传
# 创作者中心 → 小工具 → 上传 zip
# 第一次失败 = vibe RPC timeout，等 5 分钟重试
```

## 跟 examples/ 的关系

- **templates/** = 骨架（4 节占位）· 适合"想从 0 开始"
- **examples/ai-knowledge-stack/** = 完整案例（7 节 6,722 字）· 适合"想看真实效果"

## 复用边角

同一份模板可以出多种 H5：

- **零基础入门 AI 知识**（4 层栈 · examples 已做）
- **零基础入门交易知识**（4 层栈 · 改 7 节课内容）
- **零基础入门小红书运营**（5 步流程 · 改课程结构）
- **零基础入门 Python**（3 模块 · 改课程数）

**核心不变**：templates/ 4 文件 + SPA 架构 + 杂志海报风。**只改 data.js**。
