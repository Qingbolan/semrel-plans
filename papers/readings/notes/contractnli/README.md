# ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts

ContractNLI 把 NDA 审查建模为文档级自然语言推理：给定合同与固定假设，判断蕴含/矛盾/未提及，并定位支持证据；同时提出 Span NLI BERT。关键结果：BERT-large 的 NLI 准确率 0.875，但矛盾类 F1 仅 0.357（Table 4）。

[原文](https://aclanthology.org/2021.findings-emnlp.164.pdf)

阅读版本：Findings of EMNLP 2021, pp.1907–1919。本轮已阅读问题、方法、实验及边界相关正文，具体范围见下表；未将未读附录计为已核验。状态为 READ（单人阅读与自查，未做独立证据复核）。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §3，PDF pp.4–5 |
| 评测 | §4–5，PDF pp.5–7，Tables 3–8 |
| 局限 | §2.1 固定 NDA 假设；§5.2 例外否定与不连续证据 |

本页区分作者的任务与结果、本项目使用方式，以及明确标注的分析推断。原文已保存并记录 SHA256；不是本项目的运行复现。
