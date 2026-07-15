# H5 设计转 H5 滑动适配 · 方法论

> **来源**：aliyun `ai10088.com/skill-arsenal/`（pretty-skills 实战 22 幕 talk）
> **场景**：1920×1080 设计的桌面端作品 → H5 端（手机）支持左滑右滑翻页
> **沉淀时间**：2026-07-16
> **类型**：轻量级方法论沉淀（非完整 case 流程，无 9 张讲解图 + PDF）

---

## 一句话定位

1920×1080 设计的桌面端 PPT/作品，**H5 适配 = 强制横屏 + min scale 完整显示**。保留桌面端设计不变 + H5 竖屏提示用户旋转 + 横屏下 min 等比缩放完整显示 22 幕。

## ⚠️ v1 失败方案（2026-07-16 实战踩坑）

第一次实现用 vh 优先 + 横向 stage 居中裁剪：让每段占满屏幕高度，stage 视觉 1500×844 横向居中裁剪到 390 视口。

**真机问题**：
- iPhone Safari 上 `transform: translateX + scale` 组合在某些 iOS 版本有渲染异常
- 用户反馈"全部溢出屏幕"
- 横向裁剪让设计核心内容（印章、左侧大标题）被裁

**结论**：放弃 vh 优先裁剪方案，改用强制横屏。

## v2 方案（当前 · 强制横屏）

| 步 | 动作 | 关键 |
|---|---|---|
| 1 | 修 viewport meta | `width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1.0, user-scalable=no` |
| 2 | 触屏滑动 JS | `touchstart`/`touchend` + 40px 阈值 + 800ms 内触发 |
| 3 | 竖屏检测（CSS） | `@media (orientation: portrait) and (max-width: 900px)` → 隐藏 stage + 显示 portrait-hint |
| 4 | 横屏 stage（JS） | `transform: translate(offsetX, offsetY) scale(min(vw/1920, vh/1080))` + 居中显示 |
| 5 | 进度条 | 顶部绿条 + 左上 "1/22" 计数 + 主题色变量 |
| 6 | 桌面端兼容 | `if (max-width: 900px) isMobile` → 否则原 1920×1080 不动 |

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

### 3. stage 自适应（v2 · 强制横屏 + min scale 居中）

```javascript
const STAGE_W = 1920, STAGE_H = 1080;
const stage = document.getElementById('stage');

function fitStage() {
  const vw = window.innerWidth;
  const vh = window.innerHeight;
  // H5 强制横屏：竖屏被 CSS 拦截（显示 portrait-hint）
  // 横屏下：min scale 完整显示，stage 居中
  const isMobile = matchMedia('(max-width: 900px)').matches;
  if (isMobile) {
    const scale = Math.min(vw / STAGE_W, vh / STAGE_H);
    const visualW = STAGE_W * scale;
    const visualH = STAGE_H * scale;
    const offsetX = (vw - visualW) / 2;
    const offsetY = (vh - visualH) / 2;
    stage.style.transformOrigin = 'top left';
    stage.style.transform = `translate(${offsetX}px, ${offsetY}px) scale(${scale})`;
    stage.style.width = STAGE_W + 'px';
    stage.style.height = STAGE_H + 'px';
    document.body.style.width = vw + 'px';
    document.body.style.height = vh + 'px';
    document.body.style.overflow = 'hidden';
  } else {
    // 桌面端 1920×1080 不动
    stage.style.transform = '';
    stage.style.transformOrigin = '';
    stage.style.width = '';
    stage.style.height = '';
    document.body.style.width = '';
    document.body.style.height = '';
    document.body.style.overflow = '';
  }
}
window.addEventListener('resize', fitStage);
window.addEventListener('orientationchange', () => setTimeout(fitStage, 100));
fitStage();
```

### 3.5. 竖屏提示 CSS（关键 · 强制横屏核心）

```css
#portrait-hint {
  position: fixed; inset: 0;
  background: var(--c-paper, #fafaf7);
  z-index: 10000;
  display: none;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  font-family: "Songti SC", "STSong", serif;
  text-align: center;
  padding: 40px;
}
#portrait-hint .hint-icon {
  font-size: 72px; margin-bottom: 28px;
  animation: rotate-hint 2.4s ease-in-out infinite;
  display: inline-block;
}
#portrait-hint .hint-text {
  font-size: 26px; font-weight: 700; margin-bottom: 12px;
  letter-spacing: 2px;
}
#portrait-hint .hint-sub {
  font-size: 15px; opacity: 0.55; line-height: 1.6;
  max-width: 320px;
}
@keyframes rotate-hint {
  0%, 100% { transform: rotate(0deg); }
  50% { transform: rotate(90deg); }
}
/* 竖屏窄屏：显示提示 + 隐藏 stage */
@media (orientation: portrait) and (max-width: 900px) {
  .stage { display: none !important; }
  #portrait-hint { display: flex !important; }
  #progress-bar, #progress-text, #h5-swipe-hint { display: none !important; }
}
```

### 3.6. 竖屏提示 DOM

```html
<div id="portrait-hint">
  <span class="hint-icon">📱</span>
  <div class="hint-text">请横屏查看</div>
  <div class="hint-sub">将手机旋转 90°<br>横屏获得最佳演示体验</div>
</div>
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

| 策略 | 实现 | 优点 | 缺点 | 推荐度 |
|---|---|---|---|---|
| **A. vw 等比** | `scale = vw/1920` | 每段占满屏幕宽度 | 段高 219px，下面 625px 空白（iPhone） | ⭐⭐ |
| **B. vh 等比 + 横向裁剪** | `scale = vh/1080` + `translateX` 居中 | 每段占满屏幕高度 | 左右裁剪 + iOS Safari 渲染异常 | ⭐（失败）|
| **C. min 等比** | `scale = min(vw/1920, vh/1080)` | 完整可见 | 段高 219px，下面 625px 空白（iPhone）| ⭐⭐ |
| **D. 强制横屏 + min 等比（v2 推荐）** | 竖屏提示 + 横屏下走 C | 横屏 22 幕完整可见 | 需用户旋转手机 | ⭐⭐⭐⭐⭐ |

**推荐 D（v2 方案）**：
- 横屏 844×390 → min scale = 0.361 → 22 幕占满 692×390 视口（左右 76 居中）
- 用户能横屏看完整 22 幕
- 桌面 1920×1080 完全不动

**为什么不用 A/C**：iPhone portrait 视口 390×844，22 幕在 219×390 内，下方 625px 留白 → 用户看不到完整 22 幕，体验差。

**为什么 B 失败**：iOS Safari 上 `transform: translateX + scale` 组合在某些版本有渲染异常，stage 视觉内容真机溢出屏幕。

## 实战对比（v2）

| 状态 | 桌面 1920×1080 | iPhone 竖屏 390×844 | iPhone 横屏 844×390 |
|---|---|---|---|
| 改造前 | ✓ 正常 | ❌ 横屏溢出 / 缩太小 / 无翻页手势 | ❌ 体验差 |
| v1 改造后 | ✓ 正常（不变） | ⚠️ 真机渲染异常 / 用户拒绝 | ❌ 留白多 |
| **v2 改造后** | ✓ 正常（不变） | ✓ "请横屏查看" 提示 + 旋转动画 | ✓ 22 幕完整可见 + 触屏滑动 |

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
