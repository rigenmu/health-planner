# Health Planner

[中文](#中文) · [English](#english)

## 中文

一个轻量、可持续的个人健康记录 Skill，适用于 ChatGPT 桌面端和 Codex。

它可以帮你随手记录睡眠、体重、血压、血糖、用药、饮食、活动、压力和身体反馈，并在每次记录、每日结束、7 日和 14 日四个节点提供不同深度的反馈。

### 为什么做这个 Skill

我在控制体重时发现一件很有意思的事：只要记得每天记录，体重往往就更容易朝希望的方向变化。

记录本身当然没有魔法。真正起作用的，可能是它让目标每天重新出现在眼前：吃了什么、睡得怎样、有没有活动、身体有什么反应，都不再只是模糊的感觉。持续记录带来觉察，及时反馈帮助下一次选择变得更容易。

Health Planner 想做的，就是把这种记录变得足够简单，让人愿意长期坚持。

### 它能做什么

- 接受自然语言、关键词、语音转写和碎片化记录，不要求填写复杂表格。
- 自动合并同一天的多条消息，并保留日期、单位和测量背景。
- 区分空腹与餐后血糖、服药前与服药后血压等不同条件。
- 每次记录后给出简短反馈，每日结束时总结，7 日分析趋势，14 日回顾调整效果。
- 导入既往健康对话，并优先以用户自己的原始记录为准。
- 涉及药物、异常读数或专业健康建议时，要求使用当前可靠来源并说明不确定性。
- 不把任何人的健康档案保存在 Skill 目录中。

### 安装

在 Codex 中发送：

```text
使用 $skill-installer 安装这个 Skill：
https://github.com/rigenmu/health-planner
```

也可以手动克隆到个人 Skills 目录：

```bash
git clone https://github.com/rigenmu/health-planner.git ~/.agents/skills/health-planner
```

如果安装后没有立即显示，请重启 Codex。

### 使用

第一次使用：

```text
使用 $health-planner 帮我建立健康记录。我的主要目标是控制体重，
我想记录睡眠、晨重、饮食和运动。请保持记录简单。
```

日常可以直接说：

```text
昨晚 00:20 睡，07:30 起，睡眠一般；今早体重 72.4 kg。
```

```text
今天结束了，帮我做每日总结。
```

```text
回顾最近 7 天，只分析有足够数据支持的趋势。
```

### 重要说明

Health Planner 用于个人记录、观察和就医沟通准备，不提供疾病诊断，也不能替代医生或自行调整处方药。若出现可能的紧急情况，应立即联系当地急救服务。

---

## English

A lightweight, sustainable personal health-tracking skill for ChatGPT desktop and Codex.

It helps you log sleep, weight, blood pressure, glucose, medication, meals, activity, stress, and body feedback in everyday language. It provides feedback at four useful moments: after each entry, at the end of the day, after 7 days, and after 14 days.

### Why this skill exists

While managing my weight, I noticed something surprisingly powerful: when I remember to log every day, my weight tends to move in the direction I want.

Logging is not magic. What may matter is that it brings the goal back into view every day. Food, sleep, movement, and body signals stop being vague impressions. Consistent tracking creates awareness, and timely feedback can make the next choice easier.

Health Planner is designed to make that process simple enough to continue.

### What it does

- Accepts natural language, short notes, voice transcripts, and fragmented updates without requiring a complicated form.
- Merges updates from the same day while preserving dates, units, and measurement context.
- Keeps fasting and post-meal glucose, or pre- and post-medication blood pressure, in separate series.
- Gives brief feedback after each entry, a daily summary, a 7-day trend review, and a 14-day intervention review.
- Imports previous health conversations while treating the user's original messages as the primary record.
- Requires current, reliable sources when discussing medication, abnormal readings, or substantive health recommendations.
- Never stores anyone's personal health history inside the skill directory.

### Install

Ask Codex:

```text
Use $skill-installer to install this skill:
https://github.com/rigenmu/health-planner
```

Or clone it into your personal skills directory:

```bash
git clone https://github.com/rigenmu/health-planner.git ~/.agents/skills/health-planner
```

Restart Codex if the skill does not appear immediately.

### Use

To get started:

```text
Use $health-planner to start a simple health record. My main goal is weight
management, and I want to track sleep, morning weight, meals, and exercise.
```

Everyday updates can be as simple as:

```text
Slept from 12:20 a.m. to 7:30 a.m., recovery felt average, morning weight 72.4 kg.
```

```text
The day is over. Please give me my daily review.
```

```text
Review the last 7 days and only describe trends supported by enough data.
```

### Important

Health Planner supports personal tracking, observation, and preparation for conversations with healthcare professionals. It does not diagnose disease, replace medical care, or independently change prescription medication. Seek local emergency care for potentially urgent symptoms.

## License

MIT
