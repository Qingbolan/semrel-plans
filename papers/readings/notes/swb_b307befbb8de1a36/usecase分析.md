# 具体用例

Table 2 中 BioRED 关系类别错误的例子（PMID 15485686）：原文为 “… intravenous lidocaine infusion or a high dose of mexiletine … controlled the ventricular tachycardia.”

GPT-4 把（mexiletine, ventricular tachycardia）标为 “positive correlation”。语义上 mexiletine 对该病有治疗作用，但 BioRED 指南规定：药物治疗疾病或减轻其严重程度时应标为 “negative correlation”。因此预测“看起来合理但违反指南”。

按 §3.2 的指令检索流程，系统先判断这一化学物–疾病实体对是否存在关系，再检索 “Disease-chemical” 子节中的关系类型要求进行分类，最后用规则校验处理特殊情况。§4.1 报告：表中 6 个失败案例里，5 个由“两步推理 + 指南指令检索”解决，PMID 9400934 由“动态 3-shot + 指南指令检索”解决。

阅读者分析：这说明对语义过滤或抽取类算子，标签语义来自数据集指南而非常识；项目若用 LLM 做同类判断，应把指南条款作为输入的一部分。这一建议是阅读者推断，不是本文实验结论。

依据：[arXiv:2503.03261v2，21 页](https://arxiv.org/pdf/2503.03261v2)，Table 2，PDF p.5；§3.2，PDF pp.8–9；§4.1，PDF p.10。
