# Zhang, Henkel, Floratou, Cahoon, Deep, Patel（UW-Madison / Microsoft）— ReAcTable: Enhancing ReAct for Table Question Answering

本文研究单表表格问答（TQA）：表中语义常藏在复合字符串里，一次性生成 SQL 或纯语言推理容易出错。ReAcTable 把 ReAct 思路用于 TQA：LLM 每轮选择生成 SQL、生成 Python 或直接作答，执行结果作为中间表放回提示，逐步把数据变成易于回答的形式；另加执行异常处理和三种多数投票。

用 Codex（code-davinci-002）、无需训练，在 WikiTQ 上达到 68.0%（比此前最佳 Dater 高 2.1 个百分点）；TabFact 小测试集 86.1%，仍低于有监督的 PASTA 90.8%（Tables 1–2）。

[原文](https://arxiv.org/abs/2310.00815)

版本：arXiv 2310.00815（v1，14 页）；arXiv PDF 首页 PVLDB 卷期与 DOI 为模板占位。正式版为 PVLDB 17(8):1981–1994（2024），据 arXiv 2504.02059 参考文献 [52]，本笔记未核对正式版。已通读正文 §1–7；2026-11 按全文重新核对数字，未复现实验。
