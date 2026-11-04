# 具体用例

**例 1：用表补充文本问答**（Example 1.1、3.1，Figures 1、3）。问题：“Which team drafted the tallest players on average for the point guard position over the years?”。Figure 3 的程序：

```python
lake = new DataLake(datalake_path);
table_results = Selection(input=lake, src="table", pred={'attribute': 'name', 'table': 'Team'})
text_results = LookUp(input=table_results, src="text", mode="prompt",
                      pred={'query': 'Which team drafted the tallest players on average for the point guard position over the years?'})
Output(text_results)
```

先从 Team 表取出所有球队名，再把结果交给 LookUp，以 LLM 提示模式在文本上作答；`src` 参数指定每个算子的模态。

**例 2：来源未指定时隐式发现**（Example 3.2，Figure 4）。程序要找 2023 年在同一地点举行的 NBA 比赛的参赛球队和比分；Join 的谓词写成自然语言（`'cond_type': 'natural language'`），并带 `filter: {'year': '2023'}`，Join 和 Projection 都没写 `src`。系统据所有算子的谓词隐式调用 Discovery，判定来源是表，再执行语义等价的 SQL。

**例 3：跨表与图的规划及优化机会**（Example 3.3、§4）。问题：“哪些马萨诸塞州的大学有球员被 1990 年代夺冠球队选中？”。原始计划：
1. 从表中找出 1990–1999 年的冠军球队；
2. 在图中用子图查询找这些球队选中的球员及其大学；
3. 过滤出属于马萨诸塞州的大学。

作者指出，若其他州的球员记录很多，图查询开销会很大；若把州的谓词下推到表模态的查询中，可先过滤无关结果（§4 Effective Query Optimization）。

阅读者分析：三个例子都是设计演示，没有运行结果、耗时或答案对比；例 3 的谓词下推是提出的机会，不是已实现的加速。例 3 中“大学属于哪个州”的信息原文未说明存于哪个模态，下推到表查询的前提是表中有此信息（阅读者分析）。

依据：[arXiv 2504.02059v1](https://arxiv.org/abs/2504.02059v1)，§1、§3.2、§4、Examples 1.1、3.1–3.3、Figures 1、3、4，PDF pp.1、3–5。
