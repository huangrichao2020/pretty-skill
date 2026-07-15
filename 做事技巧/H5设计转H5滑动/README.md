# H5 设计转 H5 滑动适配 · 方法论

> **来源**：aliyun `ai10088.com/skill-arsenal/`（pretty-skills 实战 22 幕 talk）
> **场景**：1920×1080 设计的桌面端作品 → H5 端（手机）支持左滑右滑翻页
> **沉淀时间**：2026-07-16
> **类型**：轻量级方法论沉淀（非完整 case 流程，无 9 张讲解图 + PDF）

---

## 一句话定位

1920×1080 设计的桌面端 PPT/作品，**H5 适配 = viewport 修复 + 等比缩放 + 触屏滑动翻页**。保留桌面端设计不变 + H5 端按 vh 适配 + 横向 stage 居中裁剪。

## 5 步工作流

| 步 | 动作 | 关键 |
|---|---|---|
| 1 | 修 viewport meta | `width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1.0, user-scalable=no` |
| 2 | 触屏滑动 JS | `touchstart`/`touchend` + 40px 阈值 + 800ms 内触发 |
| 3 | stage 自适应 | `transform: scale(vh/STAGE_H) translateX((vw-visualW)/2)` + 横向居中裁剪 |
| 4 | 进度条 | 顶部绿条 + 左上 "1/22" 计数 + 主题色变量 |
| 5 | 桌面端兼容 | 不改 stylesheet · JS inline 改 width/height · desktop 1920×1080 不动 |

## 关键代码

### 1. viewport（最关键 · 一行修复桌面端适配）

```html
<meta name="viewport"
  content="width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1.0, user-scalable=no" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
<meta name="format-detection" content="telephone=no" />
```

### 2. 触屏滑动 JS（40px 阈值 + 800ms 防误触）

```javascript
let touchStartX = 0, touchStartY = 0, touchStartTime = 0;
const SWIPE_DX = 40, SWIPE_DT = 800;

document.addEventListener('touchstart', e => {
  if (e.touches.length !== 1) return;
  touchStartX = e.touches[0].screenX;
  touchStartY = e.touches[0].screenY;
  touchStartTime = Date.now();
}, { passive: true });

document.addEventListener('touchend', e => {
  if (overviewMode) return;  // O 概览模式不响应触屏
  const dx = e.changedTouches[0].screenX - touchStartX;
  const dy = e.changedTouches[0].screenY - touchStartY;
  const dt = Date.now() - touchStartTime;
  if (Math.abs(dx) < SWIPE_DX) return;
  if (Math.abs(dx) < Math.abs(dy)) return;  // 横向滑动才触发（避免上下滚误触）
  if (dt > SWIPE_DT) return;
  if (dx < 0) next(); else prev();
}, { passive: true });
```

### 3. stage 自适应（vh 优先 + 横向居中 + 左右裁剪）

```javascript
const STAGE_W = 1920, STAGE_H = 1080;
const stage = document.getElementById('stage');

function fitStage() {
  const vw = window.innerWidth;
  const vh = window.innerHeight;
  // vh 优先：每段占满屏幕高度；stage 横向居中，左右裁剪
  const scale = vh / STAGE_H;
  const visualW = STAGE_W * scale;
  const offsetX = (vw - visualW) / 2;
  stage.style.transformOrigin = 'top left';
  stage.style.transform = `translateX(${offsetX}px) scale(${scale})`;
  stage.style.width = STAGE_W + 'px';
  stage.style.height = STAGE_H + 'px';
  document.body.style.width = vw + 'px';
  document.body.style.height = vh + 'px';
  document.body.style.overflow = 'hidden';
}
window.addEventListener('resize', fitStage);
window.addEventListener('orientationchange', () => setTimeout(fitStage, 100));
fitStage();
```

### 4. 进度条 CSS

```css
#progress-bar {
  position: fixed; top: 0; left: 0; right: 0;
  height: 3px; background: rgba(0,0,0,0.08);
  z-index: 9999; pointer-events: none;
}
#progress-bar-fill {
  height: 100%; background: var(--c-accent, #497568);
  width: 0%; transition: width 0.3s ease;
}
#progress-text {
  position: fixed; top: 8px; left: 12px;
  font-size: 11px; opacity: 0.65;
  z-index: 9999; pointer-events: none;
  font-family: system-ui, -apple-system, "PingFang SC", sans-serif;
  color: var(--c-ink, #1a1f1c);
  background: rgba(255,255,255,0.78);
  padding: 2px 8px; border-radius: 10px;
}
```

## 取舍：3 种 H5 适配策略

| 策略 | 实现 | 优点 | 缺点 |
|---|---|---|---|
| **A. vw 等比**（推荐） | `scale = vw/1920` | 每段占满屏幕宽度 | 段高 219px，下面 625px 空白（iPhone） |
| **B. vh 等比 + 横向裁剪** | `scale = vh/1080` + `translateX` 居中 | 每段占满屏幕高度 | 左右裁剪（设计 1500px 宽只看到中间 390px） |
| **C. min 等比** | `scale = min(vw/1920, vh/1080)` | 完整可见 | 段高 219px，下面 625px 空白（iPhone） |

**推荐 B**：用户能"滑动翻页"是核心需求，每段必须占满屏幕高度。横向裁剪是设计 1920 宽固有限制（A/C 留白多，22 幕看 1 幕就跳，体验差）。

## 实战对比

| 状态 | 桌面 1920×1080 | H5 iPhone 390×844 |
|---|---|---|
| 改造前 | ✓ 正常 | ❌ 横屏溢出 / 缩太小 / 无翻页手势 |
| 改造后 | ✓ 正常（不变） | ✓ 每段占满屏幕 + 左右滑翻页 + 进度条 |

## 反模式（必避坑）

| 反模式 | 后果 | 正确做法 |
|---|---|---|
| viewport 不改 | H5 端用 1920 渲染，自动缩太小 | `device-width, initial-scale=1` |
| 用 vw 适配 + 没 minHeight | 22 幕只看到顶部 26% | 用 vh 适配 + 横向居中 |
| 触屏阈值太低（10px） | 误触频繁 | 40px 阈值 + 800ms 内 |
| 没防 vertical swipe | 上下滚触发翻页 | `if (Math.abs(dx) < Math.abs(dy)) return;` |
| 进度条用 absolute 不 fixed | 翻页滚时进度条跑了 | `position: fixed` + z-index 9999 |
| 进度文字和主题按钮重叠 | UI 拥挤 | 进度文字放左上，主题按钮放右上 |
| 改 stylesheet 而非 JS | 桌面端 1920×1080 坏了 | JS inline 改 width/height/desktop 兼容 |
| O 概览模式响应触屏 | 概览里滑动会跳幕 | `if (overviewMode) return;` |
| 监听 touchmove | 卡顿 | 只监听 touchstart/touchend（passive: true） |
| 没 hideHint | 提示文字一直显示 | 4.5s 自动隐藏 + 首次交互后立即隐藏 |

## 适用 / 不适用

**适用**：
- 1920×1080 设计的桌面端 PPT/作品（slidev / reveal.js / keynote 导出 HTML / 自制）
- 22 幕以内的演示文稿（再长需要分章节）
- 单页 SPA 形式（不是多页跳转）

**不适用**：
- 移动端原生应用（用 framework 自带方案）
- 多页跳转的网站（要重构成 SPA）
- 8000+ 幕的图库（需要分章节 + 概览）
- 视频 / 动画内容（用 H5 视频方案）

## 工具对比

| 方案 | 优点 | 缺点 |
|---|---|---|
| **手写 JS（本方案）** | 0 依赖 · 完全可控 · 20 行代码 | 没现成动画 |
| swiper.js | 动画丰富 · 兼容好 | 50KB+ 依赖 · 改 stylesheet 困难 |
| fullpage.js | 全屏滚动流畅 | 同上 · 移动端复杂 |
| slidesv | 写 markdown 出 slide | 需要重做内容 · 不适合现有 HTML |

**推荐手写 JS**：1920×1080 设计 + 22 幕以内的演示文稿，手写 20 行 JS 完全够用。

## 配套改动清单

- ✓ viewport meta（5 个标签）
- ✓ 触屏滑动 JS（22 行）
- ✓ fitStage JS（17 行）
- ✓ 进度条 CSS（30 行）
- ✓ 进度条 DOM（4 行）
- ✓ 触屏设备检测 + 提示（10 行）
- ✓ 进度更新 hook（7 行）
- ⏸ 反模式：没改 stylesheet · 桌面端 1920×1080 不动

**总改动量**：约 110 行（CSS 30 + JS 70 + HTML 5 + meta 5）。

## 用户拿到后

- 拿到任何 1920×1080 设计的桌面端 PPT/作品 → **30 min 适配 H5 滑动翻页**
- 桌面端 1920×1080 不动
- H5 端每段占满屏幕 + 左滑右滑翻页 + 进度条
- 不引入任何依赖

## 相关引用

- aliyun-server-ops skill（部署运维）：`~/.mavis/agents/mavis/skills/aliyun-server-ops/`
- 实战项目：`https://www.ai10088.com/skill-arsenal/`（22 幕 pretty-skills 实战 talk）
- 备份：`/www/wwwroot/skill-arsenal/index.html.bak-20260716-0158`

## 沉淀版本

v1.0 · 2026-07-16
