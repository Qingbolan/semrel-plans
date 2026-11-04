# 具体用例

Figure 1 以 Cochrane 综述 “Systemic antibiotics for treating diabetic foot infections” 为例。综述协议包含摘要（比较全身抗生素与其他疗法在糖尿病足感染中的效果与安全性）和纳入标准（随机对照试验；1 型或 2 型糖尿病且足部伤口被诊断为感染等）。

**阶段 1（标题/摘要）**：候选文献 “The Safety and Efficacy of Daptomycin” 的标题与摘要被填入提示模板 `Does the {{ publication.title }} and {{ publication.abstract }} meet the eligibility criteria {{ review.criteria }} for the review …?`，回答 Yes 后进入下一阶段。

**阶段 2（全文）**：同一文献的正文被填入全文模板，输出 Yes，或 `No, because {{ explanation }}`。

阅读者分析：该例把筛查看作“一条问题同时检查全部标准”的问答；论文也给出按标准拆成多问再 AND 聚合的形式，但未报告按标准拆分的实验。项目若把它当作语义过滤算子，应保留两阶段输入差异和纳入标准文本。

依据：[NeurIPS 2023 D&B，17 页](https://proceedings.neurips.cc/paper_files/paper/2023/file/4962a23916103301b27bde29a27642e8-Paper-Datasets_and_Benchmarks.pdf)，Figure 1 与 §2，PDF pp.2–3。
