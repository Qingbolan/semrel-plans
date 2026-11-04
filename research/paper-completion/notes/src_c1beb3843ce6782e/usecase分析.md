# usecase

Figure 1 给出的 Task A 示例：查询是 “Machine Learning Engineer” 职位描述，相关简历包括 P2（AI Engineer – MSc CS，技能 ML、Python）和 P13（DL Consultant – PhD AI，技能 DL、TensorFlow），系统要把它们排在前面。Figure 2 的 Task B 示例：同一职位名称应召回 Python（Core）、Data Processing（Core）、NLP Techniques（Contextual）。第二名 QTPride 的做法可以说明一种具体流程：先用 LLM 把职位描述和简历解析成结构化 JSON，再分别按全文、工作经历和 ESCO 知识图谱三种视图检索，最后用倒数秩融合合并。

阅读者分析：若在本项目中把匹配写成“语义抽取 + 语义连接/过滤”计划，须保留原任务的排序语义（MAP/NDCG）和语言设置，不能把二值过滤的结果与本文的排行榜直接对比。

依据：[arXiv:2606.31692v1（2026-06-30），22 页（正文 17 页）](https://arxiv.org/abs/2606.31692v1)，§2.1–2.2、§4.1，Figures 1–2，PDF pp.4、6、13。
