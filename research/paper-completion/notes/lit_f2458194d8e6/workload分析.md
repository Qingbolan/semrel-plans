# 工作负载

评测只用 BIRD development set，且不使用 BIRD 的 evidence（作者认为 evidence 本身提供表与字段的理解信息）（§3，PDF p.4）。原文未写 dev 集的问题数、数据库数或任何抽样，也未给出生成描述覆盖的表/列数量。

SQL 生成器为三个开源模型：Qwen2.5-Coder-14B、Codestral-22B、Llama3.1-8B；schema 以 M-Schema 格式提供；指标为执行准确率 EX。对比三种条件：无描述、本文生成描述、人工描述（BIRD 自带）（§3，PDF p.4）。

每个模型只有一次运行，未报告方差；0.42–1.55 个百分点的差异在 BIRD dev 规模下是否显著，原文未检验（阅读者分析）。“人工描述”指 BIRD 提供的列描述文件，属于基准自带标注，不是本文另行编写。

依据：§3、Table 1，PDF pp.3–4。
