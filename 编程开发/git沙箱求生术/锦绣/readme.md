# Git 沙箱求生术 · 锦绣融合稿

> 一份稿，三端用：公众号 / 小红书 / AI 阅读。

---

## 公众号版（深度 · 1200-1800 字）

标题：**你的 git fetch 卡死 120 秒？不是网不好，是路径错了**

你有没有过这种经历：在 WorkBuddy 沙箱里跑 `git fetch`，屏幕静悄悄卡了 120 秒，最后甩一个 `RC=124` 超时给你。第一反应一定是"网络不通"或"SSH key 配错了"，然后开始重配密钥、翻文档。

别急着重配。先跑三条命令自证清白：
- `ssh -T git@github.com` —— 正常，说明认证没问题；
- `git ls-remote` —— 正常，说明能连上远端；
- `git push` —— 正常，说明上行没问题。

唯独 `git fetch` 卡死。这就排除了认证，把锅甩给了 SSH 协议在 fetch 阶段（upload-pack 协商）的路径 stall——是沙箱网络环境对这个协议路径的特殊限制，不是 GitHub 拒绝你。

**解法只有一句话：换条路。**

公开仓免认证用 HTTPS 智能 HTTP 拉取：
`git fetch https://github.com/<user>/<repo>.git main:refs/remotes/origin/main`
实测 8MB/s 秒回，用来确认"不落后"再 rebase，比死等 SSH 强太多。

私有仓把 PAT 塞进 URL：`git fetch https://<PAT>@github.com/...git`。一个 PAT 通吃 huangrichao2020 名下所有仓（含 knowhub），不用每个仓配一遍。

两条纪律记牢：**rebase 时 `--ours` 是目标分支（新真相）、`--theirs` 是正在重放的旧提交**，方向别搞反；还有，看校验的**真实退出码**，别被 `| grep` 的退出码掩盖了失败。

## 小红书版（精简 · 300 字 + 3 竖屏图）

"git fetch 卡了 120 秒？先别重配 SSH！
我踩过的坑：ssh -T 正常、push 正常，唯独 fetch 卡死。
不是认证问题，是 SSH 的 fetch 路径在沙箱里 stall 了。
解法：公开仓直接 `git fetch https://github.com/用户/仓.git main:refs/remotes/origin/main`，秒回。
私有仓加 PAT 进 URL 就行，一个 PAT 管你所有仓。
记住：能秒回的，不要死等。"

## AI 阅读版（结构化要点 · 供摘要 / 检索）

- 现象：沙箱内 `git fetch` 走 SSH 静默卡死，120s 超时（RC=124）。
- 诊断：ssh -T / ls-remote / push 均正常 → 排除认证。
- 根因：SSH upload-pack 路径 stall，与权限 / 2FA 无关。
- 解法-公开仓：`git fetch https://github.com/u/r.git <branch>:<refs/remotes/origin/<branch>>`，免认证、秒回。
- 解法-私有仓：`git fetch https://<PAT>@github.com/u/r.git ...`。
- 跨仓：单 PAT 覆盖 huangrichao2020 全仓（含 knowhub）。
- 纪律：rebase `--ours`=目标分支、`--theirs`=旧提交；校验看真实退出码。

---

## 配图

- 封面：`cover-横屏.png` / `cover-竖屏.png`
- 正文 7 图见 `../images/p0-p6.png`
- 讲解图集：`slides/s0-s7.png`（8 张）
