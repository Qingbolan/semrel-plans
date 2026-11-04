# Li et al. — Prompt4Vis: Prompting Large Language Models with Example Mining (and Schema Filtering) for Tabular Data Visualization

Prompt4Vis 用上下文学习让 LLM 把自然语言问题翻译成数据可视化查询（DVQ）：示例挖掘模块综合相似度、影响力（对比学习训练的影响力模型）与多样性挑选示例，模式过滤模块用 GPT-3.5-Turbo few-shot 选出相关表。在 NVBench 5 折交叉验证中，整体准确率测试集 52.69%、开发集 60.39%，相对 RGVisNet 提升约 71.3% 与 35.9%。已阅读预印本全文（共 10 页，无独立局限一节）。

[原文](https://link.springer.com/article/10.1007/s00778-025-00912-0)

版本：目录指向 VLDB Journal 2025 正式版，但出版社 PDF 未能获取（Springer 返回 HTML 页面而非 PDF）；本次阅读的是作者 arXiv 预印本 arXiv:2402.07909v1（2024-01-29，标题含“and Schema Filtering”），10 页。正式版可能有扩展实验或修改，下文数字均来自预印本。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2、Figure 1，PDF pp.1–3 |
| method | §3（Algorithm 1、Figures 2–3、Table 1），PDF pp.3–5 |
| evaluation | §4、Tables 2–4、Figures 4–5，PDF pp.5–8 |
| limitations | 无独立局限一节；§4.2.1 末段与 §6，PDF pp.5、9 |
