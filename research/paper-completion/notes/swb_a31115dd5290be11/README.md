# Bikaun et al. — MaintIE: A Fine-Grained Annotation Schema and Benchmark for Information Extraction from Maintenance Short Texts

MaintIE 是面向维修工单短文本（MST）的实体识别与关系抽取标注方案及语料：5 个顶层类、共 224 个叶子实体类、6 种关系；包含专家双人标注且完全一致的细粒度语料（摘要写 1,076 条）和 7,000 条单人校正的粗粒度语料。论文用 SpERT 与 REBEL 在 2/5/32/224 类层级上给出基线，并比较“先粗粒度预微调再细粒度微调”。SpERT 实体识别 micro F1 在 5 类时为 87.4，到 224 类降至 64.4；REBEL 在 224 类上 strict 关系抽取 F1 为 0（Table 4，p.8）。已读正文、统计表、Table 4 与附录 C。

[原文](https://aclanthology.org/2024.lrec-main.954)

版本：LREC-COLING 2024，pp.10939–10951，ACL Anthology 2024.lrec-main.954 PDF，13 页（含参考文献与附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1–2，PDF pp.1–3 |
| 方法 | §3–5、Table 1、Figure 2，PDF pp.3–6 |
| 评测 | §6–8、Tables 2–4、附录 C Tables 5–7，PDF pp.5–10 |
| 局限 | §8.1–8.2、§9，PDF pp.6–9 |
