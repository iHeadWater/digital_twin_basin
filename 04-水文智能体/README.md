# 第 4 讲 · 大模型智能体与水文工作流(Hydro AI Agents)

> 建议主题名:《大模型智能体与水文工作流》,副标题「从工具调用、Skills 到专业任务执行」。
> 本目录是第 4 讲 PPT 的**公开实操配套层**——PPT 讲概念与原理,本目录放学生能跟着动手的教程。作业不在此仓库(作业在独立仓库实施,这里最多给「参考起点/骨架」)。

## 本讲回答的核心问题

> Agent 怎样把模型、上下文、工具、Skills、权限和反馈组织起来,可靠地完成一项水文任务?

承接第 2 讲:上一节我们知道了「Agent 能调用工具」;这一讲打开机器盖子,看它为什么能操作文件、运行代码、完成一项真实水文工作。

## 概念速查(承接第 2、3 讲)

| 概念 | 一句话 |
|---|---|
| **Prompt** | 告诉 Agent 这一次应该怎样做 |
| **Skill** | 规定以后遇到这一类任务应该怎样做(可复用方法) |
| **MCP / API** | 让 Agent 连接外部数据、软件与服务 |
| **Agent** | 理解任务、选择能力、执行步骤、根据结果继续行动 |
| **Workflow** | 把多个步骤组织成完整、可检查、可复现的过程 |

> 一句话主线:**Agent 负责执行,Skill 负责沉淀能力,MCP 负责连接数据与工具,工作流负责组织全过程。**
> Skill 不是让模型重新训练,而是给 Agent 增加一套可复用、可检查的专业工作方法。

## 本讲实操教程入口

按「四阶段故事」组织(源自课程设计工作稿的贯穿故事:写代码 → 做分析 → 沉淀 Skill → 组合工作流):

| 阶段 | 学生动手 | 教程位置 |
|---|---|---|
| 0. 环境 | 装好一个终端 AI 编程 Agent,并配好模型 | [tutorials/](tutorials/) 前置说明 |
| 1. 让 AI 写代码 | 指挥它读一份降雨/流量数据,画出过程线 | [tutorials/lab01-draw-hydrograph/](tutorials/lab01-draw-hydrograph/) ✅ |
| 2. 让 Agent 完成分析 | 找数据→查格式→跑模型→算 NSE→画曲线→解释异常 | lab02(规划) |
| 3. 把经验变成 Skill | 把数据检查/模型运行规则沉淀为 Skill | lab03(规划) |
| 4. 组合成水文工作流 | 多 Skills 协作,人工确认后出报告 | lab04(规划) |

学生入口统一走 [tutorials/README.md](tutorials/README.md)。

## 语雀素材索引(备课 / 进阶,非课堂必读)

- [AI 编程 Agent 工具使用简介](https://dlut-water.yuque.com/kgo8gd/tnld77/wmcwtsbgux0a3v6q) —— 工具安装与生态,讲次卡片与 lab00 的数据来源
- [给 Agent 配置 MCP 服务](https://dlut-water.yuque.com/kgo8gd/tnld77/yscxlcp6l3mzs1y5) —— 三场景递进,lab04 组合工作流的延伸
- [知汛 Agent](https://dlut-water.yuque.com/kgo8gd/tnld77/czb64tasb896nh3o) / [知汛 Agent MCP tools 构建](https://dlut-water.yuque.com/kgo8gd/tnld77/mdrgb93k4hkhucko) —— 真实水文 Agent 案例(团队内部数据/API,演示用)
- [Hermes — 你的 AI 秘书](https://dlut-water.yuque.com/kgo8gd/tnld77/spd4ky6b5i7dicbs) / [OpenClaw — 你的 AI 工具人](https://dlut-water.yuque.com/kgo8gd/tnld77/tkxlsdqhg2ciyc6k) —— 「个人工具 → Agent 工作环境」视角,供教师提炼

## 待定事项(开放问题)

- [ ] 课堂默认演示哪个 CLI Agent?(Claude Code / Codex / opencode / DeepSeek Harness 之一)
- [ ] lab01 数据:本目录给了合成样例可跑通;正式课堂数据用公开数据集还是教师小样本?
- [ ] 学生是否需要自带模型 API(学校提供见语雀「大模型厂商 API 配置」)
- [ ] lab02–lab04 是否依赖[第 2 讲](../02-人工智能与流域水文模型/)/[第 3 讲](../03-深度学习水文模型/)的模型与数据教程(跨讲引用)

## 学生反馈与迭代记录

| 日期 | 来源 | 反馈 | 处理 |
|---|---|---|---|
