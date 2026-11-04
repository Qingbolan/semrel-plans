# 贡献与评价

**论文自述贡献**（§I，p.1）：

1. 基于 LLM 代理任务规划与执行的轻量 VA 框架，支持人机协作完成任务分解、可视化和洞察发现。
2. 实现该框架的系统，含 Chat、Visualization、Task flow、Data table（table lens）四视图（Fig. 4，p.7）。
3. 用一个使用场景和一项专家研究展示有效性。

**方法要点**：

- planner（recommender + decomposer）、executor、controller 三模块递归运行，控制器算法在附录 A（§IV-A，p.5）。
- "先执行、按需分解"，以 LLM 自评 1–10 分触发分解（Prompt Template 3，p.7）。
- 给代码脚手架（`plot(data)` 内先预处理再出图）以减少分析代码与可视化代码不一致（§IV-A2，p.6）。
- 错误处理分三层：few-shot/CoT 提示、自反思调试与规则修复、交给用户编辑或回滚（§IV-C，pp.7–8）。

**评价（阅读者分析）**：

- 贡献偏向交互系统设计与人机协作流程，属于 VIS/HCI 类工作；与 Tableau Ask Data 的比较是功能清单式（§VII，p.11），没有用户任务完成时间或准确率的对照实验。
- 分解是否必要由 LLM 自评分数决定，论文未报告该评分的可靠性；E3 也指出"分解过程需要解释"（§VI-C，p.11）。
- 实现依赖 OpenAI GPT-4 与 Assistants Code Interpreter，Altair 部分在本地执行（§IV-A2 脚注，p.6；§V，p.8）。
