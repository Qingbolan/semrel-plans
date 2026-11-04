# Ahmadnia et al. — Opinion Mining Using Pre-Trained Large Language Models: Identifying the Type, Polarity, Intensity, Expression, and Source of Private States

本文清理并转换了完整的 MPQA 2.0 意见语料（修正偏移、去除无法对齐的标注、转成 JSON），在其上建立两组任务的基线：给定短语与句子，分类私有状态的类型、极性、强度（BERT、T5、FLAN-T5）；以及用 T5 生成式地抽取意见表达及其嵌套来源。FLAN-T5 在类型/极性/强度上分别取得 F1 83.8 / 87.1 / 73.0；来源抽取在带前缀输入下精确匹配 F1 为 83.5（只看最后一个来源）。已阅读正文 §1–6、Limitations、Ethics 及附录 11–13；未复现实验。

[原文](https://aclanthology.org/2024.lrec-main.1093)

版本：LREC-COLING 2024，pp.12481–12495，ACL Anthology 2024.lrec-main.1093，15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–3，PDF pp.1–4 |
| 方法 | §2.2 语料修订、§4 方法、附录 12–13，PDF pp.3–6、13–15 |
| 评测 | §5、Tables 6–13，PDF pp.6–9 |
| 局限 | §5.5、§6、§8 Limitations、§9 Ethics，PDF pp.9–10 |
