// 7 节课数据：标题 / 简介 / 时长 / 详情正文 / 金句 / 行动
window.COURSE_DATA = {
  meta: {
    title: `零基础入门 AI 知识`,
    subtitle: `从大脑到手脚 · 从工具到车间`,
    motto: `不会写代码也能用 AI，把每个痛点变成流水线`,
    coverImage: "./00-cover.jpg",
    author: 'Mavis'
  },
  courses: [
    {
      id: 1,
      title: `4 层栈总览`,
      subtitle: `为什么这个框架能撬动 AI 时代所有问题`,
      duration: `5 分钟`,
      image: `./02-stack.jpg`,
      built: true,
      hook: `为什么很多人用 AI 用得累？因为他们只看到第 1 层——LLM。但真正能用 AI 撬动杠杆的人，都在用 4 层。`,
      sections: [
        {
          heading: "01 · AI / LLM：能想不能",
          body: `最底层是 AI/LLM。ChatGPT、Claude、Gemini、DeepSeek 都是 LLM。它们能想、能写、能推理，但有一个致命问题：<strong>它们不能动</strong>。你说"帮我订机票"，它给你步骤，不能真去订。这一层是"大脑"——能想，但手脚是空的。`
        },
        {
          heading: '02 · Agent：能跑工具的 A',
          body: `第二层是 Agent。Agent = LLM + 工具 + 记忆。它能调用浏览器、文件、API、MCP 工具——你说"帮我订机票"，它真能打开浏览器、查航班、填表单、付款。这一层是"手脚"——大脑 + 四肢才是一个完整的人。`
        },
        {
          heading: "03 · Skill：1 次能力变 100 ",
          body: `第三层是 Skill。Skill 是 Agent 的"轮子"——把一次验证有效的能力（prompt + 流程 + 工具调用）封装成可复用资产。daily-market-review、wechat-delivery、ai-image-to-pptx 都是 skill。一次写好，100 次调用，从"重复劳动"到"流水线"。`
        },
        {
          heading: '04 · 工具项目：方法论的车',
          body: `最上层是工具项目。一堆 skill 串起来 + 方法论 + 工作流 = 工具项目。knowhub、pretty-skills、feishuclaw 都是工具项目——它们不是单点工具，是"作坊"。这一层是"车间"——单个 skill 是螺丝刀，工具项目是整套工具箱。`
        }
      ],
      quote: "AI 不会让你失业，但会用 AI 的人",
      action: `找 1 个你最近用的 AI 工具（ChatGPT / 飞书 AI / Notion AI 都可以），标出它在哪一层。做完你会发现：90% 的工具你只用了 1/4 能力。`
    },
    {
      id: 2,
      title: `AI = 大脑`,
      subtitle: `LLM 能想不能动的真相`,
      duration: `5 分钟`,
      image: `./00-cover.jpg`,
      built: true,
      hook: `你以为你用的是 AI，其实你用的是 LLM——一个只有大脑、没有手脚的"思考者"。理解这一点，是你开始用 AI 的第一步。`,
      sections: [
        {
          heading: 'LLM 是什',
          body: `LLM = Large Language Model（大语言模型）。ChatGPT、Claude、Gemini、DeepSeek、文心一言、通义千问都是 LLM。它的本质是：<strong>输入一段文字 → 输出另一段文字</strong>。它做的事就是"接话"，但接得非常好——好到你以为它在"思考"。实际上它只是在做"最可能的下一句话是什么"的统计游戏。`
        },
        {
          heading: "LLM 的能力边",
          body: `<strong>LLM 能做的</strong>：回答问题、写文章、写代码、翻译、总结、推理、生成结构化数据。<br><strong>LLM 不能做的</strong>：① 联网获取实时信息（除非外挂 RAG）② 打开文件、操作软件 ③ 记忆超过上下文的对话 ④ 执行真实动作（下单、发邮件、改文件）。你让它"帮我订机票"，它只能给你步骤，不能真去订。`
        },
        {
          heading: '为什么 LLM 不等于 A',
          body: `很多人把"AI"和"ChatGPT"画等号。这是 2023 年的认知——那时候我们能接触到的只有 LLM。但 2026 年的 AI 是 4 层栈：LLM + Agent + Skill + 工具项目。只用 LLM 等于"只用了大脑"——会想不会做，永远停留在"写周报、改文案"的层面。`
        },
        {
          heading: "怎么用 LLM 才算不浪",
          body: `① <strong>做内容</strong>：写文章、写邮件、写代码、写文案 ② <strong>做研究</strong>：读 PDF、总结长文、提取要点 ③ <strong>做决策辅助</strong>：列选项、算 trade-off、给建议 ④ <strong>做翻译 / 解释</strong>：把复杂概念讲简单。这些是 LLM 的"甜区"，其他场景交给 Agent。`
        }
      ],
      quote: 'LLM 是大脑，不是手脚——别让它做它做不到的',
      action: `打开你常用的 AI（ChatGPT / Claude / 飞书 AI），写一个你上周重复做过 3 次以上的任务。把任务描述发给 AI 5 遍，看它的回复模式。如果每次回复结构都类似，说明这就是 LLM 的"甜区"——下次直接套 prompt 模板。`
    },
    {
      id: 3,
      title: `Agent = 手脚`,
      subtitle: `有行动力的 AI`,
      duration: `5 分钟`,
      image: `./01-hook.jpg`,
      built: true,
      hook: `大多数人以为 Agent = AI 的升级版，其实 Agent = LLM + 工具 + 记忆。理解这个公式，你才能用对 Agent。`,
      sections: [
        {
          heading: `Agent 的 3 个组件`,
          body: `Agent 不是新东西，它就是把 3 件事拼起来：<br><strong>① LLM（大脑）</strong>：负责想、规划、决定下一步做什么<br><strong>② 工具（手脚）</strong>：能调用浏览器、文件、API、终端、MCP 服务<br><strong>③ 记忆（短期 + 长期）</strong>：短期是当前对话的上下文，长期是 localStorage / 数据库里的历史<br>这 3 个组件的组合方式，决定了 Agent 能干多复杂的活。`
        },
        {
          heading: `Agent 能跑什么工具`,
          body: `<strong>浏览器</strong>：自动打开网页、点按钮、填表单（你能干的他都能干）<br><strong>文件</strong>：读 PDF、写代码、改 Excel、生成 PPT<br><strong>API</strong>：调第三方服务（订机票、发邮件、查天气、下单）<br><strong>终端</strong>：跑命令行（git、docker、部署脚本）<br><strong>MCP 服务</strong>：标准化接入（GitHub MCP、Notion MCP、Figma MCP）<br>工具越多，Agent 的能力越强——但也越容易失控。`
        },
        {
          heading: `Agent vs LLM vs Bot：3 个易混概念`,
          body: `<strong>LLM</strong>：只会说不会做——给它一个 prompt，它给你一段文字<br><strong>Bot</strong>：按规则执行——你说"打开空调"，它就执行开空调命令，没有思考<br><strong>Agent</strong>：思考 + 决策 + 行动——你说"把屋里调到 25 度"，它先想"现在 28 度，要降 3 度"，再选"开空调还是开窗"，最后执行<br>大多数人用 Bot 干 Agent 的活，所以觉得 AI 没用——其实是没用对工具。`
        },
        {
          heading: `怎么用 Agent 才不出错`,
          body: `<strong>① 先 LLM 再 Agent</strong>：能纯文本完成的事别上 Agent（Agent 慢、贵、易错）<br><strong>② 给清晰边界</strong>：明确告诉 Agent 能用什么工具、不能碰什么数据<br><strong>③ 关键步骤要确认</strong>：付款、删除、发送 这类不可逆操作前让 Agent 停下来问你<br><strong>④ 看它的思考过程</strong>：Cursor / Claude Code / Manus 都会显示 Agent 的"内心戏"，看它走错路就打断重来<br>Agent 是新手司机，你得坐副驾看着。`
        }
      ],
      quote: `Agent 是手脚不是大脑——别让它替你思考`,
      action: `找 1 个你昨天手动操作超过 5 次的任务（比如查快递、填周报、汇总数据）。打开 Cursor / Claude Code，写 1 句需求，让 Agent 跑一遍。看完它的思考过程后告诉我：哪些环节你想自己来，哪些环节你愿意让它干。`
    },
    {
      id: 4,
      title: `Skill = 工具包`,
      subtitle: `把 1 次能力变 100 次`,
      duration: `5 分钟`,
      image: ``,
      built: true,
      hook: `你 1 次设计好的 prompt，第二次还想用同样的——恭喜你，你需要 1 个 Skill。`,
      sections: [
        {
          heading: `Skill 是什么`,
          body: `Skill = <strong>1 套验证有效的 prompt + 流程 + 工具调用</strong>，封装成可复用的资产。形态一般是 1 个文件夹，里面有：<br><strong>SKILL.md</strong>：写清楚场景、流程、约束（给 AI 看的说明书）<br><strong>scripts/</strong>：可执行脚本（数据处理、API 调用）<br><strong>data/</strong>：配置 / 模板 / 静态数据<br><strong>examples/</strong>：1-2 个真实使用案例<br>Skill 不是 prompt 模板，prompt 模板是死的，Skill 是"活的说明书 + 工具箱"。`
        },
        {
          heading: `怎么写 1 个 Skill：4 步`,
          body: `<strong>① 找场景</strong>：你最近 1 个月重复做 3 次以上的事<br><strong>② 写流程</strong>：把这件事拆成 3-7 步（钩子 → 调研 → 写作 → 出图 → 校对）<br><strong>③ 列工具</strong>：每步需要调什么数据 / API / 工具（curl 拉数据 / matrix 生图 / python 处理）<br><strong>④ 写 SKILL.md</strong>：把流程 + 工具 + 约束写清楚（让 AI 能照着干）<br>写完跑 3 次，3 次都对就沉淀到 pretty-skills。下次同样场景直接调，不用再设计。`
        },
        {
          heading: `Skill vs Prompt vs Workflow：3 个易混概念`,
          body: `<strong>Prompt</strong>：1 句话指令——"帮我写 1 份周报"<br><strong>Workflow</strong>：多步流程——"先拉数据 → 再分析 → 再写报告 → 再发邮件"<br><strong>Skill</strong>：1 套可复用资产——"周报生成 skill"（包含 prompt 模板 + 拉数据脚本 + 排版规则）<br>区别在于：<strong>可复用性</strong>。Prompt 用 1 次就丢，Workflow 写完还得手动执行，Skill 写完存好下次直接调。`
        },
        {
          heading: `怎么用 Skill 提效：1 个公式`,
          body: `<strong>高频 + 重复 + 流程化 = 必须 Skill 化</strong><br>低频的事（1 年做 1 次）不用 Skill——写了也忘<br>重复的事（每天 / 每周做）必须 Skill——省的时间 N 倍回本<br>流程化的事（步骤清晰可拆解）能 Skill——AI 能照着干<br>模糊的事（每次都不一样）暂时不能 Skill——等规律出来再写<br>先找 1 个你每周必做 1 次的事，写成 skill 跑 4 周。4 周后你会发现：再也不想手动做了。`
        }
      ],
      quote: `Skill 是轮子不是方向盘——别让 skill 替你做决策`,
      action: `把你今天重复过的 1 件事（写周报 / 整理数据 / 翻译 / 校对），按 4 步法写成 1 个 Skill 草稿（SKILL.md + 1 个 example）。存到 pretty-skills，下周同样场景调 1 次看效果。`
    },
    {
      id: 5,
      title: `工具项目 = 车间`,
      subtitle: `方法论的归宿`,
      duration: `5 分钟`,
      image: ``,
      built: true,
      hook: `单个 Skill 是螺丝刀，工具项目是整套工具箱。差别不是数量，是<strong>方法论的沉淀</strong>。`,
      sections: [
        {
          heading: `工具项目是什么`,
          body: `工具项目 = <strong>Skill × N + 方法论 + 工作流 + 文档</strong>，服务 1 个领域。<br>单个 Skill 是"做 1 件事"的工具，工具项目是"做 1 类事"的作坊。<br>一个工具项目通常包含：<br>① 定位文档（README）：这个项目解决什么问题、适用谁、不适用谁<br>② 多个 Skill：每个 Skill 解决 1 个子问题<br>③ 方法论：背后沉淀的范式（怎么思考、怎么拆解、怎么决策）<br>④ 案例库：3-5 个真实使用案例<br>工具项目不是 1 个 GitHub 仓库——是 1 套"能交付的方法论"。`
        },
        {
          heading: `怎么搭 1 个工具项目：4 步`,
          body: `<strong>① 定领域</strong>：1 个具体的方向（"小红书运营" / "A 股复盘" / "AI 教学"），不要太大<br><strong>② 沉淀 3-5 个 Skill</strong>：从高频任务开始写，慢慢覆盖整个领域<br><strong>③ 写方法论文档</strong>：把"为什么这么做"的思考过程沉淀下来（不只是"做什么"）<br><strong>④ 找 3 个案例背书</strong>：自己用 1 次 + 朋友用 1 次 + 公开教程带 1 次<br>案例是工具项目最值钱的部分——证明"我说的不是空话"。`
        },
        {
          heading: `4 大仓库 = 4 个工具项目范式`,
          body: `我手上有 4 个工具项目范式可以参考：<br><strong>feishuclaw</strong>：飞书 / Lark 生态——服务 1 个工具平台<br><strong>knowhub</strong>：认知框架——服务"方法论沉淀"<br><strong>how-to-agent</strong>：Agent 进化方法——服务"AI 工作流"<br><strong>destiny-skill</strong>：四乡修行法门——服务"个人成长"<br>共同特征：<strong>1 个领域 + 多个 Skill + 1 套方法论 + 公开案例</strong>。你可以从这 4 个里挑 1 个对标，照着搭。`
        },
        {
          heading: `什么时候该做工具项目`,
          body: `<strong>满足 3 个条件再做</strong>：<br>① 重复 3 次以上——做 1 次是经验，做 3 次是规律<br>② 多人能用上——自己用是 skill，多人用是工具项目<br>③ 长期有价值——3 个月后还有用，不是 1 次性<br><strong>不满足就别做</strong>：<br>① 想法阶段——先跑 3 次再说，别上来就开项目<br>② 只想 1 次——用 Skill 够了，别升级到工具项目<br>③ 还没人用——自己用明白后再开放<br>工具项目最常见的死法：<strong>搭完没人用</strong>。先解决"自己每天用"，再考虑开放。`
        }
      ],
      quote: `工具项目不是建仓库，是建方法论的归宿`,
      action: `选 1 个你最近 3 个月反复研究的领域（运营 / 交易 / 写作 / 教学 / 设计）。建 1 个空工具项目：1 个 README.md 写清 3 件事（解决什么问题 / 适用谁 / 不适用谁）。别急着写 Skill，先有定位。`
    },
    {
      id: 6,
      title: `0→6 周上手`,
      subtitle: `搭出你的 4 层栈`,
      duration: `5 分钟`,
      image: `./03-flow.jpg`,
      built: true,
      hook: `6 周 42 天，从"会用 AI"到"搭出 4 层栈"。每天 1 小时，6 周后你的工作流会换 1 次血。`,
      sections: [
        {
          heading: `W1 · 学用 AI：先把"对话"玩熟`,
          body: `<strong>目标</strong>：能用 ChatGPT / Claude 完成日常 80% 文本工作<br><strong>动作</strong>：<br>① 每天 30 分钟跟 AI 对话（写周报 / 翻译 / 总结 / 改文案）<br>② 学 5 个 prompt 模式（角色 / 示例 / 步骤 / 约束 / 输出格式）<br>③ 把每天用 AI 完成的事记下来（1 个 list）<br><strong>验收</strong>：1 周后你的"写"类工作（邮件 / 文档 / 报告）有 50% 是 AI 起草的。`
        },
        {
          heading: `W2 · 学调 AI：从"用"到"调"`,
          body: `<strong>目标</strong>：会用 API 调 LLM，知道 Function Calling / MCP 是什么<br><strong>动作</strong>：<br>① 跑 1 个最简单的 LLM API 调用（Python 5 行代码）<br>② 试 1 次 Function Calling（让 LLM 调 1 个工具）<br>③ 看 1 遍 MCP 协议文档（知道它怎么工作的）<br><strong>验收</strong>：你能用 1 个脚本调 LLM + 1 个外部 API（天气 / 翻译 / 翻译都行）。`
        },
        {
          heading: `W3-4 · 学搭 Agent：让 AI 跑工具`,
          body: `<strong>目标</strong>：用 Cursor / Claude Code 跑 1 个 5 步内能完成的真实项目<br><strong>动作</strong>：<br>① W3 装 Cursor / Claude Code，跑 1 个 demo 项目<br>② W4 选 1 个你工作里的真实小需求，让 Agent 跑通（拉数据 / 写报告 / 提交 PR）<br>③ 看 Agent 的思考过程（看懂它为什么这么做）<br><strong>验收</strong>：你有 1 个"Agent 跑过"的项目记录（截图 + 思考过程）。`
        },
        {
          heading: `W5 · 学写 Skill：把 1 次变 100 次`,
          body: `<strong>目标</strong>：写出第 1 个能跑通的 Skill<br><strong>动作</strong>：<br>① 选 1 个你最近每周都做的任务（写周报 / 整理数据 / 翻译）<br>② 按"场景 → 流程 → 工具 → SKILL.md"4 步写完<br>③ 跑 3 次验证，3 次都对就沉淀到 pretty-skills<br><strong>验收</strong>：你 pretty-skills 仓库里多了 1 个 case。`
        },
        {
          heading: `W6 · 学组工具项目：从"用"到"建"`,
          body: `<strong>目标</strong>：搭出第 1 个工具项目的框架（README + 3 个 Skill）<br><strong>动作</strong>：<br>① 选 1 个领域（运营 / 交易 / 写作 / 教学）<br>② 写 README：定位 + 适用 + 不适用<br>③ 把 W5 写的 Skill 放进去，再补 2 个相关 Skill<br>④ 找 1 个朋友让他用一遍，给你反馈<br><strong>验收</strong>：你有 1 个能交付的"工具项目 v0.1"。`
        }
      ],
      quote: `6 周不长，但够你从"用 AI"变成"AI 化的自己"`,
      action: `今天就选 W1 任务：写 1 个你最常用的 prompt（比如"帮我把会议纪要整理成待办事项"），跑 5 遍看回复模式。如果 5 次结构都类似——这就是你 W1 第一个 prompt 模板。`
    },
    {
      id: 7,
      title: `3 件事今天开始`,
      subtitle: `把 4 层栈从概念变行动`,
      duration: `5 分钟`,
      image: ``,
      built: true,
      hook: `7 节讲完，你已经知道 4 层栈是什么。问题是：今天做什么？`,
      sections: [
        {
          heading: `第 1 件事 · 装 1 个 Skill`,
          body: `去 pretty-skills 或 knowhub 找 1 个<strong>跟你工作直接相关</strong>的 Skill（比如做公众号找 wechat-delivery，做 A 股找 daily-market-review，做教学找 wechat-delivery 类）。<br>装上，跑 1 次真实任务。<br>看清楚"自己手动做"和"用 Skill 做"差多少时间。<br>差 10 倍以上 = 你已经赚到 1 个工具。差 3 倍 = 你用得不够深，调 2 次参数再试。`
        },
        {
          heading: `第 2 件事 · 写 1 个 prompt 模板`,
          body: `把你上周重复过 3 次以上的 1 件事（写周报 / 翻译 / 整理数据 / 校对），写成 1 个 prompt 模板。<br>模板包含 3 部分：<strong>角色设定</strong>（你是谁）+ <strong>任务描述</strong>（做什么）+ <strong>输出格式</strong>（怎么输出）。<br>写完存到本地（备忘录 / Obsidian / Notion 都行）。<br>下次同样场景直接套——5 秒开干，不用想。`
        },
        {
          heading: `第 3 件事 · 搭 1 个 Agent 跑通`,
          body: `用 Cursor / Claude Code / Manus 跑 1 个 <strong>5 步内能完成</strong>的小项目。<br>建议从这些里挑：<br>① 自动整理 1 周的微信聊天记录 → 总结成日报<br>② 自动抓某个 GitHub 仓库的 issue → 总结成周报<br>③ 自动把 1 个 PDF 转成 1 张思维导图<br>跑通 1 次，你就知道 Agent 能干什么、不能干什么。`
        },
        {
          heading: `为什么是这 3 件事`,
          body: `不是 1 件不是 10 件——3 件对应 3 个层次：<br><strong>第 1 件（装 Skill）</strong>= 用现成工具——跨越第 3 层<br><strong>第 2 件（写 prompt）</strong>= 沉淀自己方法——跨越第 1 层<br><strong>第 3 件（搭 Agent）</strong>= 整合多步任务——跨越第 2 层<br>3 件事做完，你 4 层栈已经跑通 3 层。剩下第 4 层（工具项目）需要更长周期——等做了 30 天 skill 再说。`
        }
      ],
      quote: `AI 不会让你失业，但会用 AI 的人会`,
      action: `今天就做 1 件事——只做 1 件，做完告诉我你做了哪件、效果如何。如果 3 件都想做，<strong>选阻力最小的那件</strong>——完成 > 完美。`
    }
  ]
};
