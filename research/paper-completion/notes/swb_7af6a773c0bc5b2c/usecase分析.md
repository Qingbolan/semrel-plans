# usecase

用例：生物数据库整理人员只想找当前研究中确定的新发现。检索条件可以写成"事件类型=Positive_regulation，且 New Knowledge=Yes"，也就是 Source=Current、KT 为 Observation 或 Analysis、CL=L3。

- 例 2f 来自已有研究（Source=Other），会被排除；
- 例 2d 带有 suggest/might，CL 为 L1/L2，会被归为 Hypothesis 而不是新知识；
- 例 2c 为否定（Polarity=Negative），可以用于检测与其他事件的矛盾。

（Background 例 2；Tables 1–2）

**标注难点**（Annotation discrepancies）：
- 线索词与触发词距离较远时，生物学标注者容易漏标，例如例 11 中 indicated 对后面 ACTIVATED 事件的影响；
- "no significant INFLUENCE" 应标为 Manner=Low，而不是 Polarity=Negative 加 Manner=High；
- "In the absence of …" 表达的否定，作用于一个没有触发词的 Correlation 事件。

阅读者分析：如果把这一任务转换为语义过滤或分类负载，输入单元应是"事件加上下文"，而不是孤立的句子；同一句中的不同事件可能有不同的元知识值。

依据：[BMC Bioinformatics 12:393，PMC3222636 全文 XML](https://doi.org/10.1186/1471-2105-12-393)，Background、Methods（Hyper-Dimensions）、Annotation discrepancies。
