# 评测与边界

基线包括 TF-IDF/SVM、基于 token 起止位置的 SQuAD BERT 和 Span NLI BERT。证据定位报告 mAP、80% recall 下的 precision；NLI 报告准确率与分标签 F1。Table 4 中 BERT-large 的 NLI 准确率为 0.875，但矛盾类 F1 仅 0.357，不能只用总体准确率描述能力。

论文检验了例外否定、oracle 证据和不连续片段；没有测量本项目查询的端到端延迟、LLM 费用或 SQL 等价性（阅读者分析）。

依据：[Findings of EMNLP 2021, pp.1907–1919](https://aclanthology.org/2021.findings-emnlp.164.pdf)，§4–5、Tables 4、6–8，PDF pp.5–7。
