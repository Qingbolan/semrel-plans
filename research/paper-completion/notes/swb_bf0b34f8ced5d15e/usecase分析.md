# 具体用例

ARC 案例：每道题给出若干输入–输出网格示例，要求学会变换规则并预测测试网格的输出。

元智能体在第 3 轮发现“用多条 CoT 生成候选答案、精炼后集成最好的答案”，之后的设计普遍沿用这一模式。最终最佳智能体“Structured Feedback and Ensemble Agent”的流程是：5 条 CoT 各生成答案；由效率、可读性、简洁性等专家和模拟人类的评审给出结构化反馈；精炼 3 次；评估后取前 3 个答案集成为最终答案（Figure 3b）。

迁移结果（Table 3）：这一智能体在 GPT-3.5 上为 13.7%，但换成 Claude-Haiku 为 5.0%、Claude-Sonnet 为 38.7%，分别低于 Self-Refine 的 6.3% 和 39.3%。Claude-Sonnet 下最高的是另一个搜得的“Dynamic Memory and Refinement Agent”（48.3%）。作者据此认为更强的模型更适合反馈简单、精炼更多的智能体。这也说明正文“搜得智能体在各模型上一致领先”并非对每个搜得智能体都成立（阅读者分析）。

依据：§4.1、Figure 3，PDF pp.5–6；§4.3、Table 3，PDF pp.8–9；§6，PDF p.11；Appendix D，PDF pp.25–27。
