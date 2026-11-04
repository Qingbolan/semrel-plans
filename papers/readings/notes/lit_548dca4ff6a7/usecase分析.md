# 具体用例

**案例 2（colleges）**：用户输入 "Show debt and earnings for Public and Private colleges."，三个模型给出三种合理但不同的解读（§4.2，p.9；Figure 6）：
- GPT-3 画了 Median Debt 与 Median Earnings 的散点图，按院校类型着色，与 NL4DV 的输出相似。
- Codex 画了柱状图，展示每类院校的债务和收入均值。
- ChatGPT 画了箱线图，比较公立和私立院校的分布。

三个模型都根据提示中列出的类别值，识别出 "Control" 列就是公立/私立标记，并推断出"debt""earnings"分别对应 "Median Debt""Median Earnings" 两列。

**案例 3（能源）** 显示了错误情形："since 2004" 这个过滤条件，GPT-3 和 ChatGPT 正确处理了，Codex 却画了从 2000 年开始的数据；NL4DV 选错了图（§4.3，p.9）。

这个用例说明，提示中的类别值枚举是列语义消歧的关键信号，同时也会把真实数据值暴露给 API。"自由选图"对同一查询会产生多个都说得通的答案，所以这类任务的评测需要明确定义"什么算正确"，不能只看是否出了图（阅读者分析）

依据：§3.2、§4.2–4.3，pp.5–9。
