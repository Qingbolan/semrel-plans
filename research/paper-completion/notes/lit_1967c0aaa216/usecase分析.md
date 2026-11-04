# 具体用例

**用例：Titanic（Task 1）的端到端运行**（§3、§4，pp.4–10）。

输入是 overview.txt 和 train/test 文件。流程如下：
1. Reader 理解背景；
2. Planner 为每个阶段制定计划；Developer 写代码，必要时调用 FillMissingValues、OneHotEncode 等工具；
3. 每个阶段运行单元测试（如清洗后的训练集无缺失、提交行数与样例一致），未通过则进入调试；
4. Reviewer 评审，Summarizer 输出阶段报告；
5. 最终生成 submission.csv，人工上传到 Kaggle 评分。

**结果**：Titanic 在 5 次试验中全部产生有效提交（VS=1），综合得分 0.888（Table 1，p.7）。在“不允许调试”的消融中，8 个任务里只有 Titanic 有一次成功（§4.3，p.10）。

**调试示例**（§4.4，pp.11–12）：遇到 FileNotFoundError 时，Developer 先定位错误，再加入 os.makedirs 和文件名清洗，最后把修正后的代码段合并回原代码。

如果把这类系统视为“数据分析算子”，需要注意它的工作单元是整场竞赛（多小时、多次 LLM 调用），而不是单条查询。原文没有报告 token 用量或费用（阅读者分析）

依据：[arXiv:2410.20424v3，44 页](https://arxiv.org/pdf/2410.20424v3)，§3–§4，PDF pp.4–12；附录 B，p.16。
