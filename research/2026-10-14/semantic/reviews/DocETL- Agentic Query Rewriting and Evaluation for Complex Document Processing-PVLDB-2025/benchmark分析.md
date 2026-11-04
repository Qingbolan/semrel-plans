# 基准评测

CUAD用类别一致且span Jaccard>0.15判命中；表2优化F1=0.477，未优化0.379，LOTUS0.393。表3对应执行$1.46/180.30s，对未优化$0.08/23.43s，另付优化$1.58；质量提高伴随费用增加。优化选21个独立map，每个处理1–3相关条款，再reduce。

Steam表4：幻觉率0.465→0.312、Kendall tau0.470→0.631，但sentiment accuracy0.664→0.650。基线截断到context，优化处理完整输入，不能把费用差异视为相同处理量。

BlackVault表5优化抽取435地点、precision1.000；“Location Recall”列实际报告数量而非[0,1]比例。正文未优化事件类别233与表格164亦不一致，保留证据口径。BioDEX表6 DocETL RP@5/10=0.281/0.313；不同论文的LOTUS版本和模型不同，跨论文数字不可直接比较。未复现实验。

来源：[DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing](https://www.vldb.org/pvldb/vol18/p3035-shankar.pdf)。
