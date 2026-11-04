# 工作负载

**数据集**：只用 VisEval（Chen et al., 2024，基于 nvBench 构造）。原文给出的规模是 1,150 个不同可视化、2,524 个（NL, VIS）对、146 个数据库，带人工校对的标准答案和“可行可视化选项”元信息（§4.1，p.4）。

**划分**：分单表与多表两个场景；可视化按难度分为 easy / medium / hard / extra hard 四级（§4.1，p.4；案例见附录 D）。原文没有给出单表、多表各自的样本数，也没有训练/测试切分——方法是无训练的提示流程，few-shot 示例为作者“精心设计”（§4.5，p.7）。

**图表类型**：错误分析覆盖 Bar、Line、Pie、Scatter、Stacked Bar、Grouping Line、Grouping Scatter（Figure 5，p.7）。

**人工评测子集**：可读性评分器校准用 500 个样本的人工标注子集；Elo 对比用单表、多表各 1,000 个样例对，由 5 位作者标注（§4.1、§4.6，附录 A，pp.5、7、13–14）。

**资源**：所有方法以 temperature=0 调用 Azure OpenAI 的 GPT-4o、GPT-4o-mini、GPT-3.5-turbo（附录 A，p.14）。单表时 nvAgent 平均每样本约 5,900 tokens，CoML4Vis 约 2,895；多表时分别约 6,628 和 3,377（Table 7，p.14）。

| 方法 | 单表总 tokens | 多表总 tokens |
|---|---|---|
| LIDA | 1624.13 | N/A |
| Chat2Vis | 865.65 | N/A |
| CoML4Vis | 2894.62 | 3377.29 |
| nvAgent | 5900.62 | 6628.06 |

依据：§4.1、§4.5–4.6，PDF pp.4–7；附录 A、Tables 7–8，PDF pp.13–14。
