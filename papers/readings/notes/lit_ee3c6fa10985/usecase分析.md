# 具体用例

原文 Figure 1 的例子（PDF p.2）：问题 “How did US states get their names?”。

1. 模型先输出 Retrieve=Yes，检索到多个段落；
2. 对每个段落并行生成候选句，并评估 IsRel：如 “Texas 常见婴儿名 Emma” 的段落被判 Irrelevant；
3. 对候选句评估 IsSup：例如 “11 of 50 state names come from persons” 被判 Supported，而关于 California 来源的错误说法被判 Partially 或 Contradictory；
4. 选出得分最高的片段并继续生成下一段，必要时再次检索。

对照：对于 “Write an essay of your best summer vacation”，模型输出 No Retrieval，直接生成，只给出 IsUse 评分（Figure 2，PDF p.5）。

阅读者分析：在语义查询系统中，这对应“按需检索 + 逐段证据校验”的生成算子。IsSup 可以视为一种可调的引用一致性过滤器，但它是模型自评，本身也会出错（人评中并非完全一致）。
