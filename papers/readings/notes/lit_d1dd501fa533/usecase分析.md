# 具体用例

**Figure 1（p.1）的对比**：
- 标准提示需要两次调用。每次都带任务描述 "This is a deduplication task." 和两条示例（iphone-13 对 iphone-14、mac14-pro 对 mac14-air，都不匹配），再问一个问题。
- 批量提示只调用一次：同样的描述和示例，后面跟 Q1（RTX3050 对 RTX2080）和 Q2（gpt3.5-06 对 gpt-3.5，id 相同），模型分别回答 A1 "No" 和 A2 "Yes, same identifier"。这样省去了一份任务描述和两条示例的 token（Example 3，p.3）。

**Figure 4（p.5）的特征示例**：q1 是两条音乐记录（title 都是 Rashi，album 为 "Here Comes the Fuzz" 与 "Here Comes The Fuzz [Explicit]"，genre 不同）。结构感知特征按 Levenshtein ratio 得到向量 [1, 0.73, 0.42]，q2 为 [0.33, 0, 0.46]（Example 5，p.5）。多样分批会把这类向量差别大的问题放进同一批。

阅读者分析：对语义连接或语义过滤算子来说，这篇论文给出了一个可直接复用的代价维度：一次调用中放多少个元组对（批大小），以及示例如何在批间共享。作者发现相似分批会让模型对整批给出相同答案（§VI-C，p.9），说明批内组成会影响正确率，不能只当作成本参数。

依据：§I–§IV、§VI-C，pp.1–5、9。
