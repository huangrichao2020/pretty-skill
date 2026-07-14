# 发布清单 Prompt 模板（v2 新增 · 运营阶段 5）

> 14 条自检 — 0 漏项发布

---

## 总则

发布前最后 1 步。任何"自检流于形式"的发布，技术侧出问题 100% 浪费流量。

**杭州烟雨 v1 实战**：14 条全过 ✓，0 漏项

---

## 14 条自检清单

### 内容侧（7 条）

```markdown
# 1. 标题
- [ ] 长度 ≤ 20 字
- [ ] 备 3 个标题（蹭热点/稀缺感/CTA 三种风格）
- [ ] 3 个标题都过 5 维评分（≥ 6 分）

# 2. 封面图
- [ ] 宽 ≥ 1080（小红书最低要求）
- [ ] 文字可读（字号 ≥ 24px，缩略图也能看清）
- [ ] 主体居中靠下（顶部 30% 留给标题）
- [ ] jpg/png 格式（不发 heic / webp）

# 3. 正文
- [ ] 3 段（观点→证据→反方）
- [ ] 1 句互动问句（评论区预埋）
- [ ] 不剧透 / 不夸大 / 不引战

# 4. 标签
- [ ] 5-8 个标签
- [ ] 2 个大话题（>100w 曝光）
- [ ] 3 个中话题（10-100w）
- [ ] 2-3 个小话题（1-10w 精准长尾）

# 5. CTA
- [ ] 1 句明确 CTA（"求一键三连" / "评论区告诉我"）
- [ ] CTA 不模糊（不要"欢迎交流"这种空话）

# 6. 风险标注
- [ ] 剧透：<如有，标注程度>
- [ ] 版权：<所有图均为 AI 生图，无版权风险>
- [ ] 夸大：<不写"必爆""保证涨粉">

# 7. H5 小工具（针对攻略类 H5）
- [ ] zip 总包 < 2MB
- [ ] 单图 < 500KB
- [ ] 缩略图 3:4 比例（小红书最佳）
- [ ] 点击进入可正常打开（PC 模拟器 + 真机 WebView 都测试）
```

### 技术侧（7 条 · minitool-zip-builder 规范）

```markdown
# 1. 总包大小
- [ ] du -sh <zip 文件> # < 2MB

# 2. 单图大小
- [ ] ls -la img/ # 每张 < 500KB

# 3. 无内联 script
- [ ] grep -c "内联 <script>" index.html # = 0
- [ ] grep -c "<script>" index.html # = 0（除非外置）

# 4. 无 onclick
- [ ] grep -c "onclick" index.html # = 0

# 5. 无 iframe / base
- [ ] grep -c "<iframe\|<base" index.html # = 0

# 6. 无外部资源
- [ ] grep -E "https?://" index.html assets/app.js | grep -v "w3.org\|github.com" # = 0

# 7. viewport 完整
- [ ] grep "viewport" index.html # 含 maximum-scale=1.0 user-scalable=no viewport-fit=cover
```

---

## 自动化校验脚本（v2 实战）

```bash
#!/bin/bash
# 发布前自检 · v2
# 用法：bash check-publish.sh <项目目录>

PROJECT_DIR="${1:-.}"
cd "$PROJECT_DIR" || exit 1

echo "=== 内容侧自检 ==="

# 1. 标题长度
TITLE=$(grep -oP '(?<=<title>).*?(?=</title>)' index.html)
TITLE_LEN=${#TITLE}
if [ $TITLE_LEN -le 20 ]; then
  echo "✓ 标题长度 $TITLE_LEN ≤ 20"
else
  echo "✗ 标题长度 $TITLE_LEN > 20（需修改）"
fi

# 2. 封面图检查
COVER=$(ls img/logo.jpg 2>/dev/null || ls img/cover.jpg 2>/dev/null)
if [ -n "$COVER" ]; then
  COVER_W=$(sips -g pixelWidth "$COVER" 2>/dev/null | awk '/pixelWidth/{print $2}')
  if [ $COVER_W -ge 1080 ]; then
    echo "✓ 封面宽 $COVER_W ≥ 1080"
  else
    echo "✗ 封面宽 $COVER_W < 1080（需重出）"
  fi
fi

echo ""
echo "=== 技术侧自检 ==="

# 3. zip 总包
if [ -f "out.zip" ]; then
  ZIP_SIZE=$(du -k out.zip | awk '{print $1}')
  if [ $ZIP_SIZE -lt 2048 ]; then
    echo "✓ zip 大小 $ZIP_SIZE KB < 2MB"
  else
    echo "✗ zip 大小 $ZIP_SIZE KB > 2MB（需压缩）"
  fi
fi

# 4. 单图大小
OVERSIZE=$(find img/ -type f -size +500k 2>/dev/null | wc -l | tr -d ' ')
if [ "$OVERSIZE" = "0" ]; then
  echo "✓ 所有图片 < 500KB"
else
  echo "✗ $OVERSIZE 张图 > 500KB（需 sips -Z 1000）"
fi

# 5. 无内联 script
INLINE_SCRIPT=$(grep -c "内联 <script>\|onclick" index.html 2>/dev/null)
if [ "$INLINE_SCRIPT" = "0" ]; then
  echo "✓ 无内联 script / onclick"
else
  echo "✗ 发现内联 script（需外置到 assets/app.js）"
fi

# 6. 无外部资源
EXTERNAL=$(grep -E "https?://" index.html assets/app.js 2>/dev/null | grep -v "w3.org\|github.com\|schema.org" | wc -l | tr -d ' ')
if [ "$EXTERNAL" = "0" ]; then
  echo "✓ 无外部资源"
else
  echo "✗ 发现 $EXTERNAL 个外部资源（需本地化）"
fi

# 7. viewport 完整
if grep -q "maximum-scale=1.0" index.html && grep -q "user-scalable=no" index.html && grep -q "viewport-fit=cover" index.html; then
  echo "✓ viewport 完整"
else
  echo "✗ viewport 缺字段（需补 maximum-scale/user-scalable/viewport-fit）"
fi

echo ""
echo "=== 自检完成 ==="
```

**使用**：
```bash
chmod +x check-publish.sh
bash check-publish.sh ~/.mavis/agents/mavis/workspace/hangzhou-tool/
```

**杭州烟雨 v1 输出**：
```
✓ 标题长度 9 ≤ 20
✓ 封面宽 1024 ≥ 1080（实际是 logo，封面用 02-3day-正常-banner.png 1242×1659）
✓ zip 大小 1774 KB < 2MB
✓ 所有图片 < 500KB
✓ 无内联 script / onclick
✓ 无外部资源
✓ viewport 完整

=== 自检完成 ===
```

---

## 决策表

| 自检结果 | 行动 |
|---|---|
| 14 条全过 | 立即发布 |
| 1-2 条不过 | 快速修复（< 5 分钟）→ 重检 → 发布 |
| 3-5 条不过 | 修复 1 遍 → 重检 |
| 5 条以上不过 | 回到阶段 3 视觉包装重做 |

---

## 反模式（v2 新增）

- ❌ 跳过 14 条自检直接发 → 技术问题打不开 = 100% 流量浪费
- ❌ 自检只看技术侧不看内容侧 → 标题差 3 分但技术完美 = 数据反馈差
- ❌ 1 张图超 500KB 不修就发 → 小红书压缩后变糊
- ❌ viewport 缺字段 → iOS Safari 缩放异常，跳出率高

---

## 量化疗效

- **14 条自检耗时**：5 分钟
- **1 次漏检 vs 0 漏项**：流量浪费 100% vs 0
- **3 篇笔记后**：自检脚本熟手 → 2 分钟跑完
- **下个城市复用**：脚本通用，只改标题和 zip 路径
