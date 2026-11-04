# 评测与边界

比较 BM25、QL、通用或法律领域模型，以及 Dense-STARD、Dense-CAIL、Dense-GPT4 和分类式 LSI。主指标为 Recall@k、MRR@k；Table 3 中 Dense-STARD 的 R@100 为 0.9065。监督信息不同的组别应分开看。

下游 RAG 收益依赖检索器和生成模型，Table 4 并非所有配置都提升。语料限定中国法律体系，不能靠翻译推断跨法域有效性。

依据：[Findings of EMNLP 2024, pp.10658–10671](https://aclanthology.org/2024.findings-emnlp.625.pdf)，§6–7、§10、Tables 3–4，PDF pp.6–9。
