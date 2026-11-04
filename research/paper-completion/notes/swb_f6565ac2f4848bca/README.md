# Remaki et al. — SynCABEL: Synthetic Contextualized Augmentation for Biomedical Entity Linking

本文提出 SynCABEL：用 LLM（Llama-3-70B）为知识库中的候选概念批量生成带上下文的合成训练句，与人工标注数据交错混合，微调生成式实体链接模型并配合基于前缀树的受限解码。Llama-3-8B+SynCABEL 在 MedMentions-ST21pv、QUAERO（MEDLINE/EMEA）、SPACCC 四个测试上 Recall@1 均为表中最高（平均 75.3），并在 60%（MM、SPACCC）或 40%（QUAERO）人工数据下达到全量人工监督的水平。已阅读全部正文（含 LLM 评审协议与效率分析）；论文未给出训练/测试划分细节，相关实现指向 GitHub。

[原文](https://arxiv.org/abs/2601.19667)

版本：arXiv:2601.19667v3（2026-05-18），9 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–2 |
| 方法 | §3.2–3.7，PDF pp.2–3 |
| 评测 | §4、Tables 1–6，PDF pp.3–6 |
| 局限 | §5–6，Tables 7–8、Figure 5，PDF pp.6–7 |
