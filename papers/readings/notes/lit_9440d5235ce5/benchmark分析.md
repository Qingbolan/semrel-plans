# 评测与边界

**基线**（§7.1，p.9）：LOTUS（sem_map + sem_extract）、Palimpzest（convert，使用同一 LLM）、Evaporate（代码生成+弱监督，LLM 成本忽略）、OpenIE6、DebertaV3、FrugalGPT（相同抽取方法、相同验证集）、LLM-Extract（同框架但只用 LLM 策略）。Doctopus 使用 OpenIE6、Evaporate、DebertaV3 与 GPT-4o。

**指标**：单元格准确率（文本 F1 匹配）、送入 GPT-4o 的输入 token 总数、每文档平均运行时间。

**主要结果**（§7.2，Fig.3，p.10）：
- Law：Doctopus、PZ、LOTUS 准确率都约 75%，但 PZ 和 LOTUS 分别消耗 380 万、580 万 token，是 Doctopus 的 3.2×、4.8×。LOTUS 需两个算子，每文档 LLM 调用加倍。
- Wikiart：FrugalGPT 77%，Doctopus 85%（0.75M token）。
- Financial：Doctopus 验证集仅耗 0.05M token，准确率 84%，FrugalGPT 78%，Evaporate 52%、DebertaV3 33%、OpenIE6 20%。
- 摘要级结论：同成本准确率提升 11%，同准确率成本降低 2.7×（p.1、p.3）。

**消融**：去掉任一非 LLM 方法（D-W-O/C/P）均下降（Fig.5）；查询增强优于仅验证集参考、仅 LLM 参考和无参考（Fig.4）；GPT-3.5、GPT-4o-mini 下仍优于 FrugalGPT 与 PZ（Fig.6）；DistilBERT-DA 包含概率准确率与 GPT-4o 相当（Fig.7）；人工参与验证集优于纯 LLM 验证集（Fig.10）。运行时间上 Evaporate 最快，Doctopus 快于 PZ、LOTUS、FrugalGPT（Fig.8）。

**局限**（p.12、p.10）：需要随 LLM 版本更新重新评估质量；未整合多个 LLM；假设每文档每属性单值；相关属性的联合质量估计留作未来工作。

阅读者分析：大部分结果只以曲线图给出，正文仅列少数数值，阅读时未逐点读取图中坐标；没有重复实验或方差。

依据：[PVLDB 18(11)，13 页](https://www.vldb.org/pvldb/vol18/p3695-chai.pdf)，§7、§9，pp.9–12。
