// SPA 课程架构：hash 路由 + 视图切换
(function () {
  var data = window.COURSE_DATA;
  var app = document.getElementById('app');
  var navActions = document.getElementById('nav-actions');

  // === 工具函数 ===
  function escapeHTML(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
  function getCourse(id) {
    for (var i = 0; i < data.courses.length; i++) {
      if (data.courses[i].id === id) return data.courses[i];
    }
    return null;
  }
  function prevCourse(id) {
    return id > 1 ? getCourse(id - 1) : null;
  }
  function nextCourse(id) {
    return id < data.courses.length ? getCourse(id + 1) : null;
  }

  // === 首页 / 课程目录 ===
  function renderHome() {
    navActions.innerHTML = '<span class="nav-meta">' + data.meta.title + '</span>';
    var html = '';
    html += '<section class="section section-cover">';
    html += '  <div class="section-content">';
    html += '    <h1 class="hero-title">' + data.meta.title + '</h1>';
    html += '    <p class="hero-sub">' + data.meta.subtitle + '</p>';
    html += '    <img src="' + data.meta.coverImage + '" alt="封面" class="hero-img" />';
    html += '    <p class="hero-motto">' + data.meta.motto + '</p>';
    html += '  </div>';
    html += '</section>';

    html += '<section class="section section-courses">';
    html += '  <div class="section-content">';
    html += '    <h2 class="section-title">课程目录 · 共 ' + data.courses.length + ' 节</h2>';
    html += '    <p class="section-subtitle">每节 5 分钟 · 7 节 35 分钟看完</p>';
    html += '    <ul class="course-list">';
    data.courses.forEach(function (c) {
      var status = c.built ? '<span class="course-status status-ready">已开放</span>'
                          : '<span class="course-status status-soon">建设中</span>';
      html += '<li class="course-item">';
      html += '  <a href="#course-' + c.id + '" class="course-link">';
      html += '    <div class="course-num">' + String(c.id).padStart(2, '0') + '</div>';
      html += '    <div class="course-body">';
      html += '      <div class="course-header">';
      html += '        <h3 class="course-title">' + escapeHTML(c.title) + '</h3>';
      html += '        status';
      html += '      </div>';
      html += '      <p class="course-subtitle">' + escapeHTML(c.subtitle) + '</p>';
      html += '      <span class="course-duration">' + c.duration + '</span>';
      html += '    </div>';
      html += '    <div class="course-arrow">→</div>';
      html += '  </a>';
      html += '</li>';
    });
    html += '    </ul>';
    html += '  </div>';
    html += '</section>';

    html += '<footer class="footer"><p>' + data.meta.motto + '</p></footer>';
    app.innerHTML = html;
    window.scrollTo(0, 0);
  }

  // === 课程详情 ===
  function renderCourse(id) {
    var c = getCourse(id);
    if (!c) { renderHome(); return; }
    var prev = prevCourse(id);
    var next = nextCourse(id);

    // 顶栏操作
    var navHtml = '';
    navHtml += '<a href="#home" class="nav-btn nav-btn-back" aria-label="返回">←</a>';
    navHtml += '<span class="nav-counter">' + id + ' / ' + data.courses.length + '</span>';
    navHtml += '<span class="nav-spacer"></span>';
    if (prev) navHtml += '<a href="#course-' + prev.id + '" class="nav-btn nav-btn-prev" aria-label="上一节">‹</a>';
    if (next) navHtml += '<a href="#course-' + next.id + '" class="nav-btn nav-btn-next" aria-label="下一节">›</a>';
    navActions.innerHTML = navHtml;

    // 详情页内容
    var html = '';
    html += '<section class="section section-course">';
    html += '  <div class="section-content">';

    if (c.image) {
      html += '  <img src="' + c.image + '" alt="' + escapeHTML(c.title) + '" class="course-img" />';
    } else {
      html += '  <div class="course-img-placeholder"><span>COURSE ' + String(id).padStart(2, '0') + '</span></div>';
    }

    html += '    <span class="kicker">第 ' + id + ' 节 · ' + c.duration + '</span>';
    html += '    <h1 class="course-title-main">' + escapeHTML(c.title) + '</h1>';
    html += '    <p class="course-subtitle-main">' + escapeHTML(c.subtitle) + '</p>';

    if (!c.built) {
      html += '  <div class="placeholder-box">';
      html += '    <p class="placeholder-title">本节详细内容建设中</p>';
      html += '    <p class="placeholder-body">按 pretty-skills 节奏，先把架构搭好 + 1-2 节完整内容验证方向。这节内容等用户审完前 2 节后再补。</p>';
      html += '  </div>';
    } else {
      // 钩子
      html += '  <div class="course-hook"><p>' + escapeHTML(c.hook) + '</p></div>';

      // 正文段
      c.sections.forEach(function (s) {
        html += '  <div class="course-section">';
        html += '    <h3 class="course-section-heading">' + escapeHTML(s.heading) + '</h3>';
        html += '    <div class="course-section-body">' + s.body + '</div>';
        html += '  </div>';
      });

      // 金句
      if (c.quote) {
        html += '  <div class="quote-box">';
        html += '    <p class="quote-text">"' + escapeHTML(c.quote) + '"</p>';
        html += '  </div>';
      }

      // 行动
      if (c.action) {
        html += '  <div class="action-box">';
        html += '    <span class="action-label">本节作业</span>';
        html += '    <p class="action-text">' + escapeHTML(c.action) + '</p>';
        html += '  </div>';
      }
    }

    html += '  </div>';
    html += '</section>';

    // 底部导航
    html += '<nav class="bottom-nav">';
    if (prev) {
      html += '  <a href="#course-' + prev.id + '" class="bottom-nav-btn">';
      html += '    <span class="bottom-nav-dir">‹ 上一节</span>';
      html += '    <span class="bottom-nav-title">' + String(prev.id).padStart(2, '0') + ' · ' + escapeHTML(prev.title) + '</span>';
      html += '  </a>';
    } else {
      html += '  <a href="#home" class="bottom-nav-btn">';
      html += '    <span class="bottom-nav-dir">‹ 返回</span>';
      html += '    <span class="bottom-nav-title">课程目录</span>';
      html += '  </a>';
    }
    html += '  <a href="#home" class="bottom-nav-btn bottom-nav-center">';
    html += '    <span class="bottom-nav-dir">⌂</span>';
    html += '    <span class="bottom-nav-title">目录</span>';
    html += '  </a>';
    if (next && c.built) {
      html += '  <a href="#course-' + next.id + '" class="bottom-nav-btn bottom-nav-next">';
      html += '    <span class="bottom-nav-dir">下一节 ›</span>';
      html += '    <span class="bottom-nav-title">' + String(next.id).padStart(2, '0') + ' · ' + escapeHTML(next.title) + '</span>';
      html += '  </a>';
    } else {
      html += '  <span class="bottom-nav-btn bottom-nav-end">';
      html += '    <span class="bottom-nav-dir">已是末节</span>';
      html += '    <span class="bottom-nav-title">—</span>';
      html += '  </span>';
    }
    html += '</nav>';

    app.innerHTML = html;
    window.scrollTo(0, 0);
  }

  // === 路由 ===
  function handleRoute() {
    var hash = window.location.hash || '#home';
    if (hash === '#home' || hash === '') {
      renderHome();
    } else {
      var m = hash.match(/^#course-(\d+)$/);
      if (m) {
        var id = parseInt(m[1], 10);
        if (getCourse(id)) renderCourse(id);
        else renderHome();
      } else {
        renderHome();
      }
    }
  }

  window.addEventListener('hashchange', handleRoute);
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', handleRoute);
  } else {
    handleRoute();
  }
})();
