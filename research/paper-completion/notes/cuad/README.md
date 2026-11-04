# CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review

CUAD 是 EDGAR 合同的专家标注条款抽取数据集（510 份合同、41 类条款），把合同审查建模为从长合同中高亮相关条款。关键结果：最强的 DeBERTa-xlarge 在 80% 召回下精度仅 44.0%、90% 召回下 17.8%（Table 2）。

[原文](https://arxiv.org/pdf/2103.06268v2)

阅读版本：arXiv:2103.06268v2, 2021-11-08。本轮已阅读问题、方法、实验及边界相关正文，具体范围见下表；未将未读附录计为已核验。状态为 READ（单人阅读与自查，未做独立证据复核）。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–4 |
| 方法 | §3–4.1，PDF pp.3–6 |
| 评测 | §4，PDF pp.5–8，Table 2 |
| 局限 | §3 对 contract analysis/counseling 的区分；§4.2 分类别结果 |

本页区分作者的任务与结果、本项目使用方式，以及明确标注的分析推断。原文已保存并记录 SHA256；不是本项目的运行复现。
