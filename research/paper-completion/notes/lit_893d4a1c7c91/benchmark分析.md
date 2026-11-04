# 评测与边界

基线：Original、Header+Sample、MVP、ReasTAP、Pneuma（Table Summarizer）、LLM-GPT/Llama（5 行样本直接生成）；AutoDDG 用 GPT-4o-mini 与 Llama-3.1-8B-Instruct（§4.1，PDF pp.12–13）。

**实验 1（检索，BM25）**：Table 2，PDF p.14。

| 方法 | ECIR NDCG@10 | ECIR NDCG@20 | NTCIR NDCG@10 | NTCIR NDCG@20 |
|---|---|---|---|---|
| Original | 0.658 | 0.694 | 0.575 | 0.688 |
| LLM-GPT | 0.800 | 0.828 | 0.536 | 0.651 |
| AutoDDG-SFD-GPT | 0.856 | 0.887 | 0.585 | 0.705 |
| AutoDDG-SFD-Llama | 0.785 | 0.828 | 0.594 | 0.696 |

NTCIR 上提升幅度明显小于 ECIR，部分方法低于 Original（阅读者分析）。SPLADE 与 SFD 叠加最好（Fig.8，附录 Table 6）。

**实验 2（描述质量）**：无参考 LLM 评审用 GPT/Llama 交叉评价完整性、简洁性、可读性和成对胜率（Table 3）；SFD 完整性最高、UFD 简洁可读性最好。参考指标中 AutoDDG 的 BERTScore 略低于 LLM-only（Table 4）。

**实验 3（人工评估）**：Faithfulness：UFD-GPT 9.00、SFD-GPT 9.09、LLM-GPT 7.59、Original 5.47（Table 5，PDF p.16）；简洁性、可读性的评审一致性较低（r≈0.48–0.49）。

**实验 4（成本与消融）**：AutoDDG-MT 平均 8.63 s/数据集（Pneuma 2.40 s）；GP 将平均 token 从 16,370 降至 10,674；约 $0.003/数据集（GPT-4o-mini）（§4.4，PDF pp.18–19）。消融只在图中给出 noSP/noSFD 趋势（Fig.11），无数值表。

局限：作者承认人工评估发现的错误来自 profiler bug（如时间范围、单位）；幻觉仍需检测；仅支持表格（§4.3、§6，PDF pp.16、22–23）。阅读者分析：描述的检索提升由 BM25/SPLADE 衡量，未测试真实用户检索行为；ECIR 正例重建方式可能偏向 GDS 能检索到的数据集。

依据：§4、Tables 2–5、Figs.8–11、§6，PDF pp.12–23。
