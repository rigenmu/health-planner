# Health Planner

[中文](#中文) · [English](#english)

## 中文

Health Planner 是一个个人健康反馈 Skill。你只管随手记录，它会把零散信息整理成当天从早到晚的完整进度，告诉你哪里值得注意，以及下一步最该做什么。

它想解决的问题很简单：用很低的认知成本，换取持续的自我觉察。

### 为什么做它

我在管理体重时发现，只要还记得每天记录，体重往往就更容易朝希望的方向变化。

记录本身没有魔法。真正有用的是，每次记完之后，我都能马上看到今天做了什么、漏了什么、哪里可能做多了，以及现在最值得做的一件事。健康目标不再只在计划里出现，而是回到一天中的每一次选择里。

我已经从这种方式中受益，所以把它整理成了一个任何人都可以使用的 Skill。

### 它怎样工作

你可以像聊天一样记录，不需要填表，也不需要按顺序汇报：

```text
昨晚 00:40 睡，今天 08:30 起。早晨体重 72.4 kg，吃了一个鸡蛋和一片面包。
```

每次记录后，Health Planner 都会按固定结构回复：

1. 今日记录：按从早到晚的顺序更新全天进度；
2. 今天还差什么：只提醒已经到时间、属于你当前计划的项目；
3. 当下点评：说明最值得注意的变化或问题；
4. 下一步：给出一件现在最值得做的事。

用户输入可以很随意，Health Planner 的整理必须有序。

### 可以记录什么

- 睡眠与恢复感受；
- 体重、血糖、血压和心率；
- 用药、补充剂和注射；
- 饮食、饮品和饮水；
- 活动与运动；
- 压力、情绪和身体反馈。

只记录与你当前目标有关的内容。没有启用的项目不会被机械追问。

### 四个反馈节点

Health Planner 会在四个节点提供不同深度的反馈：

- 每次记录：更新全天状态，及时发现遗漏并给出一个下一步；
- 每日结束：完成当天总结；
- 每 7 天：分析条件相近的数据和重复出现的模式；
- 每 14 天：检查前一阶段的调整是否产生了变化。

涉及异常读数、症状、药物或实质性健康建议时，它会要求重新核查当前可靠来源，并明确说明不确定性。

### 安装

在 Codex 中发送：

```text
使用 $skill-installer 安装这个 Skill：
https://github.com/rigenmu/health-planner
```

也可以手动安装：

```bash
git clone https://github.com/rigenmu/health-planner.git ~/.agents/skills/health-planner
```

如果安装后没有显示，请重启 Codex。

### 开始使用

```text
使用 $health-planner 帮我建立一个轻量健康计划。
我的主要目标是控制体重，我想记录睡眠、晨重、饮食和运动。
```

之后直接记录生活即可：

```text
刚吃完午饭：半碗米饭、青菜和牛肉，饭后走了 20 分钟。
```

```text
今天结束了，帮我完成日结。
```

```text
回顾最近 7 天，只分析有足够数据支持的变化。
```

### 数据和隐私

- Skill 仓库不保存任何人的个人健康数据。
- 默认在当前对话中维护记录。
- 只有得到你的同意后，才会在你指定的位置建立长期档案。
- 不会主动把健康数据上传到外部服务。

Health Planner 用于自我记录、观察变化和准备就医沟通。它不能诊断疾病、替代医生或自行调整处方药。出现可能的紧急情况时，请立即联系当地急救服务。

### 接下来

当前版本先把健康反馈工作流做好。

- 下一步：把 Skill 包装成 Plugin，让它更容易安装，并能在支持的 ChatGPT 网页端、桌面端和移动端使用。参见 [OpenAI 的 Skill 构建说明](https://learn.chatgpt.com/docs/build-skills)；
- 以后：如果确实有更多人从中受益，再考虑提供可选择的线上私有数据库，或者开发独立 App。

未来的同步功能必须让用户清楚知道数据存在哪里、谁能访问，并保留导出和删除的权利。

---

## English

Health Planner is a personal health feedback skill. You log life as it happens; it organizes those fragments into a morning-to-night view of your day, points out what deserves attention, and gives you one useful next action.

The idea is simple: trade very little mental effort for continuous self-awareness.

### Why I made it

While managing my weight, I noticed that when I kept logging each day, my weight was more likely to move in the direction I wanted.

The log itself is not magic. What helped was seeing, after every update, what I had done, what I might have forgotten, what may have been too much, and what mattered next. My health goal became part of everyday decisions instead of something I only thought about when making a plan.

That experience helped me, so I turned the workflow into a skill anyone can use.

### How it works

Write naturally. There is no form to fill in and no required order:

```text
Slept from 12:40 a.m. to 8:30 a.m. Morning weight was 72.4 kg.
Had an egg and a slice of bread for breakfast.
```

After every health entry, Health Planner responds in the same order:

1. Today's record: the full day so far, arranged from morning to night;
2. What's still due: only items that are relevant and should already have happened;
3. Current feedback: the change or issue most worth noticing;
4. Next step: the one most useful thing to do now.

Your input can be casual. Health Planner's output stays organized.

### What you can track

- Sleep and recovery;
- Weight, glucose, blood pressure, and heart rate;
- Medication, supplements, and injections;
- Meals, drinks, and hydration;
- Activity and exercise;
- Stress, mood, symptoms, and other body feedback.

It follows the items that matter to your current goal instead of asking everyone to complete the same checklist.

### Feedback over time

- After every entry: update the day, surface anything already due, and give one next action;
- End of day: close the daily record;
- Every 7 days: review comparable measurements and recurring patterns;
- Every 14 days: check whether recent changes appear to be helping.

For abnormal readings, symptoms, medication questions, or substantive health recommendations, the skill requires current, reliable sources and clear uncertainty.

### Install

Ask Codex:

```text
Use $skill-installer to install this skill:
https://github.com/rigenmu/health-planner
```

Or install it manually:

```bash
git clone https://github.com/rigenmu/health-planner.git ~/.agents/skills/health-planner
```

Restart Codex if it does not appear immediately.

### Start using it

```text
Use $health-planner to start a lightweight health plan.
My main goal is weight management. I want to track sleep, morning weight, meals, and exercise.
```

Then log your day normally:

```text
Lunch was half a bowl of rice, vegetables, and beef. I walked for 20 minutes afterward.
```

```text
The day is over. Please close today's record.
```

```text
Review the last 7 days and only describe changes supported by enough data.
```

### Data and privacy

- This repository never stores personal health records.
- Records stay in the current conversation by default.
- Long-term files are created only with your approval and in a location you choose.
- Health data is not uploaded to an external service unless you explicitly request it.

Health Planner supports self-tracking, observation, and preparation for conversations with healthcare professionals. It does not diagnose disease, replace medical care, or independently change prescription medication. Seek local emergency care for potentially urgent symptoms.

### Roadmap

The current release focuses on getting the feedback workflow right.

- Next: package the skill as a Plugin so it is easier to install and can be used on supported ChatGPT web, desktop, and mobile surfaces. See [OpenAI's skill-building guide](https://learn.chatgpt.com/docs/build-skills);
- Later: if more people find it useful, consider an optional private online database or a standalone app.

Any future sync feature should make data location and access clear, with straightforward export and deletion.

## License

MIT
