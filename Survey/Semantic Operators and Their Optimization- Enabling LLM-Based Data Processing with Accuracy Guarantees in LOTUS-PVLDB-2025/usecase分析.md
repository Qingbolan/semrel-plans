# 具体用例

**原文程序示例**（Figure 1，§2.1 p.4172，据原文转录）：

```python
def paper_digest(research_interest: str, baseline: str):
    return papers_df \
        .sem_search("abstracts", research_interest, K=100) \
        .sem_filter(f"the paper {{abstracts}} claim to outperform {baseline}") \
        .sem_agg(f"Write a digest summarizing {{abstracts}} and their relevance to {research_interest}")
```

先按研究兴趣做 top-100 语义检索，再筛出声称超过指定基线的论文，最后聚合成摘要。这是示例程序，不是论文中某个编号的评测问题。

**评测中最具体的用例：BioDEX 语义 join**（§5.2，Tables 3、5，pp.4179–4180）：任务是把 250 篇医学文章与约 24,000 个药物反应标签关联，判断每篇文章报告了哪些反应。参考算法是嵌套循环 join，需要约 609 万次 LLM 调用，估计耗时 2,144,560 s，实际无法运行。

| 计划 | RP@5 | RP@10 | 时间 (s) | LLM 调用 |
|---|---|---|---|---|
| Plan 1：sim-filter | 0.154 | 0.170 | 12,563 | 27,687 |
| Plan 2：project-sim-filter（被选中） | 0.212 | 0.213 | 2,116 | 5,290 |
| 参考算法（估计） | — | — | 2,144,560 | 6,092,500 |

Plan 2 先让 LLM 读每篇文章并直接写出可能的反应名，再用嵌入把它与标签表比较。优化器按 oracle 成本选中 Plan 2，它也更准：RP@5 高 37%，RP@10 高 25%（p.4180）。

**其他用例一览**：

| 用例 | 查询输入 | 辅助数据 | 输出 |
|---|---|---|---|
| FEVER 事实核验 | claim 文本 | Wikipedia 语料与 ColBERT 索引 | 是否被支持 |
| SciFact 检索 | 科学 claim | 论文语料与检索索引 | top-k 相关论文 |
| HellaSwag-bench | 含报告准确率的摘要 | 无 | 按准确率排序 |
| arXiv 主题分析 | 647 篇论文 | 无 | 5 个主题及归属 |

HellaSwag-bench 的 200 篇摘要由 Llama-70B 生成，准确率数值从 0–100% 随机抽取（脚注 7），是作者构建的合成任务，不是真实论文摘要。

依据：[PVLDB 18(11)](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)，§2.1、§5.2–5.4、Figure 1、Tables 3、5，pp.4172、4179–4181。
