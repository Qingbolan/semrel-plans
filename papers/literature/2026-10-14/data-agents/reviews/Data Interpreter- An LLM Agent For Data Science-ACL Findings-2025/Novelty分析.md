# Novelty分析

[论文原文](https://arxiv.org/html/2402.18679v4)

贡献是两个粒度的执行反馈：动作代码修复和任务图修订；工具以代码组合进入上下文。Table 4显示在4个ML任务上的综合得分从纯代码执行0.37、加入图修订0.85、再加入节点生成0.94。分析：任务DAG是规划结构，若要映射semantic operators需另核实每节点输入输出与语义，不能把所有Python操作叫semantic operator。
