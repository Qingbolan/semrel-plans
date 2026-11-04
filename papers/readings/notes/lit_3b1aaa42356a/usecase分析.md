# 具体用例

**场景 1：自动多模态分析（§3，p.4；Fig.2）**
1. 数据准备：把销售记录上传到数据源面板（Fig.2-B），把领域知识文档上传到知识库（Fig.2-A）。
2. 意图理解与上下文绑定：用户在聊天面板（Fig.2-C）用 “@” 选择 @Sales Database 和 @Financial Metrics，再输入“Help me analyze the 2025 global sales performance.”；作者称这一机制在规划前就消除了数据选择上的歧义。
3. 编排与优化：规划器结合绑定的上下文生成逻辑计划（Fig.2-D），引擎编译成 DAG 并显示在工作流画布（Fig.2-E）。运行时优化器把 Knowledge Search Node（查指标定义）和 Datasource Read Node（读数据库）放进同一执行层并行执行。
4. 多模态合成：执行成功后生成数据视频、仪表盘和分析报告（Fig.2-G）。

**场景 2：人在回路的修订（§3，p.4）**
- 透明检查：点击 SQL Generator Node，检查面板（Fig.2-F）显示节点 I/O 模式与参数；SQL 生成使用作者的 DeepEye-SQL。
- 交互调试：手动修改 SQL 后，若该节点连到不兼容的下游节点，校验器立即报 “Schema Mismatch”。
- 执行反馈：重新运行后，进程监视器实时显示日志与规划器的 “Thought-Action” 轨迹。

阅读者分析：该用例展示的是“表格 + 文档”联合分析的交互流程，与 atlas 中跨结构化/非结构化数据的语义查询相关；但论文未说明文档中的指标定义如何具体约束 SQL 或计算结果，也未给出输出正确性的检验方法。
