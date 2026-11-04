# 评测与边界

NER 使用 micro F1；实体链接报告 accuracy/R@1、R@10；报告级技术和策略识别报告 F1。Tables 7–8 的链接实验使用 gold 实体 span/type；Table 9 才包含句子检测后的流程和 oracle 对照。两者必须分开。

知识库描述增强可改善技术识别，但各任务收益不同。专用层主要由单个专家标注，知识库又会更新，论文明确讨论了标注一致性、迁移与未见类别的限制。

依据：[LREC-COLING 2024, pp.1147–1160](https://aclanthology.org/2024.lrec-main.103.pdf)，§3.4、§5、Limitations，PDF pp.5–9。
