# 具体用例

PaperTab 中的一个查询：“根据论文 One Size Does Not Fit All: Generating and Evaluating Variable Number of Keyphrases，用于关键短语生成的 StackEx 数据集按问题数大约多大？”标准答案为约 330k。答案所在文档混在约 10 份其他论文中。

视觉 RAG 找到 Table 1，却读了 %Pre 列，回答“约 57.5%”；文本 RAG 读到训练 298k，忽略了验证 16k 与测试 16k，回答“298k”。融合步骤比较两条推理链，判断前者用错列、后者漏算，得出 298k+16k+16k≈330k（Figure 5、Figure 11 的 Qwen2-VL 例子）。

附录也给出失败例：SPIQA 上融合偏向了更长但错误的视觉 RAG 回答（Figure 14）。

阅读者分析：此类“在文档集合中找到某表并做简单计算”的查询，可用于测试语义检索与抽取算子能否先定位正确文档再读表；但基准不含跨多份文档汇总的问题。

依据：[NAACL 2025，pp.6088–6109，22 页](https://aclanthology.org/2025.naacl-long.310.pdf)，§7.2、Figure 5、Figures 11、14、附录 A.3.2，pp.8、15–19。
