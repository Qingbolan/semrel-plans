# 具体用例

**原文示例**（Example 1.1，§1 p.2）：

```sql
SELECT * FROM docs WHERE
  AI_FILTER('{0} is a research paper', docs.text)
  AND AI_FILTER('{0} discusses optimization techniques in database systems', docs.text);
```

朴素做法按书写顺序求值。对 AND 来说，应先求值更可能返回 False 的那个过滤器，从而短路掉另一个调用。困难在于两者的选择率与相关性取决于数据，事先未知。

**Larch-Sel 在该查询上的执行流程**（据 §3.3–3.4 组合描述）：
1. 对一行文档，取其预计算嵌入和两个谓词的嵌入，经 MLP 预测每个谓词的通过概率 ŝ_i(r)；
2. 结合两次调用的 token 代价 c_i，用 DP 计算期望代价最小的首个谓词（两叶 AND 时相当于比较 c_1 + ŝ_1·c_2 与 c_2 + ŝ_2·c_1）；
3. 把该谓词发给 LLM；等待期间后台线程用上一次观测到的标签对 MLP 做一次 BCE 更新；
4. 若返回 False，整棵树为 False，这一行结束；否则继续求值剩余谓词；
5. 下一行重新预测、重新求解，因此不同文档可能采用不同顺序。

**规模化的效果**（§4.2，Table 1）：在 BigPatent 的 Conjunction 工作负载（平均选择率 4%）上，PZ/Quest 约 580M token、超额 32.0%，几乎不比不重排的 Simple（33.2%）好；Larch-Sel 446.7M token，最优下界 439.4M，超额 1.7%（作者称相对 PZ/Quest 降低 19 倍）。

阅读者分析：第 2 步中的两叶公式是阅读者对 DP 递推式的特化，原文只给出一般递推。

依据：[arXiv 2606.07923v1](https://arxiv.org/abs/2606.07923)，§1 Example 1.1、§3.3–3.4、§4.2、Table 1，PDF pp.2、6–9。
