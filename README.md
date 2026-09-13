# Health Planner

[中文](#中文) · [English](#english)

## 中文

用很低的认知成本，换取持续的自我觉察。

Health Planner 是一个个人健康管理 Skill。你随手说说睡眠、饮食、活动、指标或身体感受，它负责把一天整理清楚，结合当前目标给出反馈，并在每周、每两周和每个月主动与你复盘。

### 为什么做它

我在管理体重时发现，持续记录让我更容易注意到每天的选择：吃了什么、活动多少、身体有什么变化，以及接下来最值得做什么。我从这个过程里受益，因此把它整理成可以分享的工作方法。这是个人经验，不是对减重效果的保证。

### 日常就像聊天

你说：

> 午饭吃了米饭、青菜和豆腐，刚走了十五分钟。

它将新信息放回今天的时间线，已出现的时间段都看得见。以前的内容简短概括，本次新增内容加粗，末尾用一段 💬 自然说清值得留意的变化和一个主要行动。

不需要填表，不要求按顺序汇报，也不会每次生成 HTML 或让你打开新页面。

| 你在做什么 | 它怎样回复 |
|---|---|
| 随手新增／更正 | 全天时间线摘要，展开本次更新 |
| 查看全天／当天收尾 | 展开当天完整记录和关键测量背景 |
| 提出具体问题 | 先回答问题，再按需要附进度 |
| 到达复盘周期 | 主动在当前对话展示分析、讨论调整并跟进结果 |

看看虚构示例：[随手记录](evals/examples/fragment.md)、[完整日结](evals/examples/daily.md)、[纯查看全天](evals/examples/view-only.md)。普通反馈不再使用四个机械栏目，也不用对勾区分新增。新增／更正的健康内容和末尾主要行动可加粗；其余健康内容正常展示。

### 计划要适合真实生活

支持睡眠、体重、血糖、血压／心率、用药、饮食、饮水、活动、压力和症状记录。只跟踪与你目标有关的项目；偶然提到一件事，不会从此变成每天的必填项。

制定减重或健康改善计划时，先利用已有档案，只补问影响方案的信息，考虑生活条件、已知疾病、现有用药和相关限制。每阶段优先一两项改变，说明依据、观察什么、什么时候再看。建议与已接受计划分开，下一轮要检查执行难点和效果。

反复症状作为连续问题跟进。已经约好“明早接着分析”，下次互动就接上；问题恢复后结束额外追问。事实、可能解释和医生确认的结论分别保留。

### 复盘由它主动发起

- 每日收尾：整理当天事实并归档；
- 每 7 天：检查近期变化、重复模式和执行困难；
- 每 14 天：完整比较前后两周，复核上一轮安排并讨论调整；
- 每个自然月：评估长期目标、可持续性和下个月的重点。

周期从已确认记录起点计算，不因迁移或更新 Skill 重新开始。第 14 天收尾后可以立即复盘；未收尾则在窗口结束后的首次互动发起。缺失记录会明确说明，不因此无限拖延。重合周期合并呈现，仍分析各自窗口。

复盘必须在对话中交付。文件生成、对话交付和讨论进度分开记录，不能只留下文件。之后与你讨论最重要的一两个问题，接受的调整进入计划，下次复盘检查结果。

这里的“主动”指在互动及归档节点自行检查周期，无需你提醒。无人发消息时定时启动，需要另外授权配置宿主的定时任务；本 Skill 不自带后台服务，也不会安装后自动创建提醒。

### 专业支持与边界

可以解释指标与报告，提供循证的生活方式支持，跟进症状并帮助判断就医紧迫性，核对药物信息，准备就医摘要。首批深入场景是成年人健康改善及体重／代谢管理。

涉及医学判断、阈值、药物或具体建议时，核查适用的现行官方指南、说明书等来源，标明依据和不确定性。不同条件的测量分开分析，不把短期波动等同于疗效，不把“喝水还行”写成“医学达标”。

它不能确诊、替代临床医疗或自行调整处方药。专业流程和测试不等于临床认证；面向更广泛人群使用前，应由相关临床专业人员审阅医学场景。潜在急症优先处理，不等待复盘。

### 安装和使用

在 Codex 中发送：

```text
使用 $skill-installer 安装这个 Skill：
https://github.com/rigenmu/health-planner
```

或在尚未安装时手动克隆：

```bash
git clone https://github.com/rigenmu/health-planner.git ~/.agents/skills/health-planner
```

开始使用：

```text
使用 $health-planner 帮我建立轻量健康计划。
我的主要目标是控制体重，想先记录睡眠、晨重、饮食和活动。
```

已有档案继续使用：

```text
重新读取最新版 $health-planner，保留现有档案、周期起点和已接受计划。
按新版对话样式继续记录，并检查是否有到期或只生成文件、尚未在对话交付的复盘。
```

无需每条消息重复调用。若宿主没有加载更新，重新选择 Skill 或重启后再试；以实际加载情况为准。

### 数据与后续方向

默认在可访问对话中记录。长期文件只写入你已同意的位置，沿用每日集中归档或你另外选择的保存频率。公共仓库不保存个人健康数据，更新 Skill 不会自动迁移私人档案。

未来计划包装为 Plugin，在支持的网页、桌面和移动端使用同一套工作方法。[OpenAI 官方说明](https://learn.chatgpt.com/docs/build-skills)

跨设备长期档案需要单独的存储与同步能力，安装 Plugin 不等于手机能直接访问电脑文件。后续考虑可选的私人数据库和独立应用，用户之间隔离，支持导出和删除；不默认把个人数据用于共享统计。本仓库当前尚未提供这些功能。

### 维护与验证

运行环境：Skill 说明本身不要求 Python；可选周期检查工具使用 Python 3.9+。以下依赖仅用于开发验证：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/check_response.py evals/examples/*.md
```

GitHub Actions 执行相同检查。测试覆盖中文加粗渲染、引用块与反馈分隔、周期边界、月份和时区、报告已生成但未交付、重合周期及防重复交付。另按 [行为验收场景](evals/behavioral-cases.md) 检查真实交互与医学边界。

加粗检查针对可复现的转义和中文标点定界问题；它不能修改客户端渲染器，也不能保证所有未来生成回复零错误。

---

## English

Health Planner turns casual health updates into a chronological view of the day, evidence-informed plans, and proactive weekly, fortnightly, and monthly reviews. The aim is continuous self-awareness with very little mental effort.

### Everyday conversation

Log naturally, without a form or a required order. A brief update keeps every relevant part of the day visible, expands the new facts, and uses bold for new or corrected content. One conversational paragraph combines feedback with a useful next action. Ask for the full day to expand the details. Routine replies use native Markdown, not generated HTML cards.

Track only what matters to your goals: sleep, weight, glucose, blood pressure, medication, food, fluids, activity, stress, or symptoms. Missing information stays unknown. A suggested plan is not treated as accepted or completed without evidence.

### Plans and follow-up

The skill uses existing history and asks only for information that changes a decision. Plans consider real-life constraints and relevant medical context, prioritize one or two changes, and specify what to observe and when to reassess. Recurring symptoms are tracked over time, with facts, possible explanations, and clinician-confirmed conclusions kept separate.

### Proactive reviews

Seven-day and fourteen-day windows run from the confirmed tracking start date. Monthly reviews follow calendar months, with partial first months labeled. Review at final-day closure or the first interaction after the window ends. Missing observations do not postpone reviews indefinitely.

Reports must be presented in the conversation, not merely saved. File generation, actual delivery, and discussion are separate states. Overlapping reviews share one delivery while retaining their respective analysis windows. Accepted changes are followed up in the next review.

Proactive means checking during interactions and daily closure. Running while the user is absent requires a separately authorized host automation; this skill does not create background jobs or notifications by itself.

### Install

Ask Codex to use `$skill-installer` with this repository URL, or clone it into an available skill directory:

```bash
git clone https://github.com/rigenmu/health-planner.git ~/.agents/skills/health-planner
```

Start with:

```text
Use $health-planner to build a lightweight health plan.
My main goal is weight management. Start with sleep, morning weight, meals, and activity.
```

When updating, reload the skill and retain existing records, review anchors, and accepted plans. Private-record migration requires its own authorization.

### Evidence, privacy, and scope

Supports measurement and report explanations, lifestyle planning, symptom follow-up, urgency assessment, medication-information checks, and clinician summaries. Initial in-depth coverage focuses on adults and weight/metabolic management. Substantive advice requires current applicable authoritative sources and explicit uncertainty. It does not diagnose, prescribe, independently change medication, or claim clinical certification. Clinical review remains necessary for broader medical deployment.

Records stay in accessible conversation context unless you authorize a storage location. No personal health records belong in this repository. Future Plugin packaging and optional private storage are planned, not implemented. Cross-device access requires actual storage and sync capabilities; packaging alone does not provide them.

Version 2.0.0 includes response-parsing tests, a read-only review-window helper, and behavioral evaluation cases. Development checks are shown above. They test workflow and formatting, not clinical efficacy or every host renderer.

## License

MIT
