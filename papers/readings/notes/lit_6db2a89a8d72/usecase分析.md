# 具体用例

**论文案例：跨任务技能合成与复用（§6.5、Figure 2，pp.8–9）。**

- **Case 1（技能合成）：** DA-Code 任务要求基于 Health Insurance Cross Sell Prediction 数据集预测 test.csv 中用户的 Response，并按 sample_submission.csv 格式写出 submission.csv。agent 识别出这是需要处理类别不平衡的二分类问题，而现有分类工具未显式包含不平衡处理，于是调用 machine_learning_tool_creation("imbalanced_binary_classification") 合成新技能，最终生成提交文件。
- **Case 2（复用）：** 另一任务要求预测 Stroke Prediction 数据集中个体是否中风（stroke 病例仅 4.65%），结果写入 stroke.csv。agent 检查可用工具后直接调用此前合成的 imbalanced_binary_classification，避免重复探索。
- **Case 3（失败）：** 用历史股价求 95% 置信水平下最小化 CVaR 的组合权重；agent 自行写 Python 计算 CVaR，因领域知识不足导致执行逻辑错误。

**规模化证据：** 测试期间共合成 279 个技能，被调用 925 次，跨任务复用率 69%（§6.4，p.8）。

**阅读者分析：** 这一用例说明“可执行技能库”是一种把一次性 LLM 推理固化为可复用代码的机制，与语义算子“编译为代码”的思路相近；但 EvoDS 的技能由 agent 在任务中自行命名和触发，没有算子语义契约或正确性校验之外的质量保证（验证仅检查可执行性和输出有效性，§4.2）。
