# novelty

原文自述的贡献：（1）一个开源的 RAG 抽取框架，按 ESRS 的 501 个定量指标从企业报告中抽数；（2）覆盖 STOXX Europe 600（2023 年成分股）2014–2023 年、16 国、11 个 SICS 行业的 ESG 指标数据集（OSF q2jpv 公开）；（3）基于该数据的透明度与绩效描述性分析（不作因果结论）。原文称其比商业数据集（如 Refinitiv）更全面，且可扩展、可定期更新。

方法本身是标准 RAG 组件的组合：PyMuPDF 解析 → 400 字符块/100 重叠的递归切分 → all-MiniLM-L12-v2 嵌入 + FAISS → 向量与 BM25 等权混合检索 top-30 → Llama-Rank-V1 重排取 top-10 并拼接前后块 → Llama-3.1-70B-Instruct（温度 0）输出 JSON → 正则 + Pint 单位标准化。

阅读者评估：新颖性主要在规模、指标覆盖面与开放数据，以及把监管指标表当作抽取 schema；算法上没有新组件，也没有对检索/模型选择做消融。验证依赖外部数据集回归斜率与小规模人工标注，抽取质量的逐指标细节在补充材料中（本次未读）。

依据：[Nature Communications 17:5940，17 页](https://www.nature.com/articles/s41467-026-75160-z)，Discussion，PDF pp.8–12；Methods，PDF pp.12–14。
