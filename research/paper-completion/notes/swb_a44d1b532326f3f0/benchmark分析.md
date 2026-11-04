# 评测与边界

论文没有基线、指标或实验结果，也没有用户研究；所有"效果"只通过 Figs.1–3 的输出示例展示（pp.3–5）。因此不能从本文得出关于性能、可用性提升或覆盖率的定量结论。

原文自述的局限（§5，p.6）：

1. 尚不支持 FrameNet 网站"Lexical Entry"报告中的配价模式（valence patterns），即 FE 在已标注 token 中的句法实现汇总。
2. 计划加入更复杂的标注查询/浏览功能，以及更好的 FE 句法信息展示，可参考 FrameSQL 与 Valencer。
3. 尚未适配其他语言的 FrameNet，以及 Multilingual FrameNet 项目中 14 个 FrameNet 的跨语言映射。

另一个实用边界：`propagate_semtypes()` 默认不执行，因为运行需数秒，查看 FE 语义类型前需手动调用（§4.4，p.5）。

阅读者分析：本文适合作为 FrameNet 数据访问方式的引用来源，而不是评测基准；版本绑定 FrameNet 1.7 与 2017 年的 NLTK，后续 API 变化需查当前文档。

依据：[EMNLP 2017 Demo，D17-2001，6 页](https://aclanthology.org/D17-2001.pdf)，§4.4、§5，PDF pp.5–6。
