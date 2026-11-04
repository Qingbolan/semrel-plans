# Wang, Feng, Shen, Rahman, Kandogan（Megagon Labs）— Towards Operationalizing Heterogeneous Data Discovery

这是一篇愿景论文：企业数据湖里同时有表、文档和知识图谱，用户往往不知道该查哪种来源。作者设想一个声明式多模态数据湖系统，用一组扩展关系代数的多模态算子写程序；来源未指定时隐式触发数据发现，再做跨模态查询规划、执行和结果汇总（Verifier），并列出待解决的研究挑战。

实证只有两个已发表基准的初步结果：CMDBench 的来源发现（作者称即使用最好的发现模型，各模态准确率也下降 46%）和 CypherBench 的零样本图查询生成（最好的 claude3.5-sonnet 执行准确率 61.58%）。系统本身没有实现评测。

[原文](https://arxiv.org/abs/2504.02059v1)

版本：arXiv 2504.02059v1（2025-04-02，cs.DB），8 页；PDF 的 PVLDB 卷页、DOI 和 artifact 字段为模板占位，不能作为已发表或系统已实现的证据。已通读正文 §1–6；2026-11 按全文重新核对，未复现实验。
