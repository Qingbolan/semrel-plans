# 贡献与评价

原文声称的贡献（§1，pp.2–3）：
1. 据作者所知首个面向电子表格领域的端到端 RL 后训练方法。
2. Spreadsheet Data Agent：从 ExcelForum 自动收集带附件和讨论的帖子，用 Claude Code、Codex 等编码智能体在真实 Excel 中执行讨论中的方案生成 oracle 表，再用规则过滤（去掉触发 Excel 错误的样本、验证值可由公式计算）（§3.2.1，p.5）。
3. Spreadsheet Gym：真实 Excel（支持 FILTER、UNIQUE、MAP 等动态数组函数）+ 代码沙箱，每条 rollout 使用隔离的文件系统工作区（§3.2.2，A.9）；异步 submit-and-poll 的 Excel 验证服务（A.11）。
4. 表格原生工具 harness：find_cells、inspect_range、fill_formula、clear_range、delete_rows/columns、recalculate_and_read、code_interpreter；只读调用可并发（≤20），写操作串行；inspect→modify→verify 工作流（§3.2.3）。
5. Domain-Spreadsheet 评测集（§4）。

阅读者分析：方法本身是标准 GRPO + 结果奖励，新意主要在数据构造、环境工程与工具设计。Table 1 的分解显示 harness 与工具贡献 12.0→19.3，RL 贡献 19.3→23.4，即工具设计带来的提升大于 RL 本身；摘要把 12.0→23.4 整体称为"Spreadsheet-RL 的提升"。训练与 Domain-Spreadsheet 的 oracle 均由编码智能体生成、无人工验证，原文未报告 oracle 错误率。
