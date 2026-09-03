# 第 4 讲 · 大模型智能体与水文工作流（备课）

> ⚠️ 教师向文档：本讲教学规划与素材索引，面向教师备课，学生可跳过。学生入口见[第 4 讲 README](../../04-水文智能体/README.md)。

## 建议主题名

《大模型智能体与水文工作流》，副标题「从工具调用、Skills 到专业任务执行」。对应 OneDrive PPT《4-水文智能体》。

## 与第 2 讲的边界

第 2 讲已介绍大模型、Agent 与水文 Agent 的概念；第 4 讲只用 1–2 页承接，不重复展开 AI 发展史与 Agent 定义。过渡语示例：

> 上一节我们知道了 Agent 能够调用工具；这一节打开机器盖子，看看它为什么能够操作文件、运行代码和完成一项真实工作。

## 本讲核心问题

> Agent 怎样把模型、上下文、工具、Skills、权限和反馈组织起来，可靠地完成一项水文任务？

## 学生实操设计（四阶段故事）

按贯穿故事组织：写代码 → 做分析 → 沉淀 Skill → 组合工作流。教程入口见[第 4 讲 tutorials](../../04-水文智能体/tutorials/README.md)。

| 阶段 | 学生动手 | 位置 | 状态 |
|---|---|---|---|
| 0. 环境 | 装好一个终端 AI 编程 Agent，并配好模型 | tutorials/ 前置 | — |
| 1. 让 AI 写代码 | 指挥它读一份降雨/流量数据，画出过程线 | tutorials/lab01-draw-hydrograph/ | ✅ 骨架 |
| 2. 让 Agent 完成分析 | 找数据→查格式→跑模型→算 NSE→画曲线→解释异常 | lab02 | 规划 |
| 3. 把经验变成 Skill | 把数据检查/模型运行规则沉淀为 Skill | lab03 | 规划 |
| 4. 组合成水文工作流 | 多 Skills 协作，人工确认后出报告 | lab04 | 规划 |

## 语雀素材索引（备课 / 进阶，非课堂必读）

- [AI 编程 Agent 工具使用简介](https://dlut-water.yuque.com/kgo8gd/tnld77/wmcwtsbgux0a3v6q) —— 工具安装与生态，讲次卡片与 lab00 的数据来源
- [给 Agent 配置 MCP 服务](https://dlut-water.yuque.com/kgo8gd/tnld77/yscxlcp6l3mzs1y5) —— 三场景递进，lab04 组合工作流的延伸
- [知汛 Agent](https://dlut-water.yuque.com/kgo8gd/tnld77/czb64tasb896nh3o) / [知汛 Agent MCP tools 构建](https://dlut-water.yuque.com/kgo8gd/tnld77/mdrgb93k4hkhucko) —— 真实水文 Agent 案例（团队内部数据/API，演示用）
- [Hermes — 你的 AI 秘书](https://dlut-water.yuque.com/kgo8gd/tnld77/spd4ky6b5i7dicbs) / [OpenClaw — 你的 AI 工具人](https://dlut-water.yuque.com/kgo8gd/tnld77/tkxlsdqhg2ciyc6k) —— 「个人工具 → Agent 工作环境」视角，供教师提炼

## 待定事项（开放问题）

- [ ] 课堂默认演示哪个 CLI Agent？（Claude Code / Codex / opencode / DeepSeek Harness 之一）
- [ ] lab01 数据：本目录给了合成样例可跑通；正式课堂数据用公开数据集还是教师小样本？
- [ ] 学生是否需要自带模型 API（学校提供见语雀「大模型厂商 API 配置」）
- [ ] lab02–lab04 是否依赖[第 2 讲](../../02-人工智能与流域水文模型/)/[第 3 讲](../../03-深度学习水文模型/)的模型与数据教程（跨讲引用）

## 学生反馈与迭代记录

| 日期 | 来源 | 反馈 | 处理 |
|---|---|---|---|
