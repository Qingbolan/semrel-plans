# Dongre, Gui et al. — MIRAGE: A Benchmark for Multimodal Information-Seeking and Reasoning in Agricultural Expert-Guided Conversations

MIRAGE 是一个农业咨询领域的多模态基准，源自 AskExtension 平台 2012–2025 年间约 21.8 万次真实用户–专家交互。

它包含两项任务：单轮 MMST（根据问题、图片和元数据识别实体、给出因果解释和管理建议；Standard 8,184 条、Contextual 3,934 条，另有 17,532 条训练集）和多轮 MMMT（861 段对话，判断应追问还是直接回答，并生成相应话语）。评测由三个推理模型组成评审团完成：GPT-4.1 的识别准确率最高，也只有 43.9%；MMMT 最好的决策准确率约 63%（零样本）。

已阅读正文 §1–7、附录 C.1–C.2、G.1，以及微调相关附录段落；77 页中的其余附录（评审细则、提示词、大量表格）未逐项核对。

[原文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1fdee6bdc130776e489719d25d422073-Abstract-Datasets_and_Benchmarks_Track.html)

版本：NeurIPS 2025 Datasets and Benchmarks Track 论文集 PDF（Paper-Datasets_and_Benchmarks_Track.pdf），77 页（含附录与 checklist）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2、Table 1，PDF pp.1–4 |
| method（数据构建与任务定义） | §3–4（含 §3.1、§4.1），PDF pp.4–6；附录 C.1–C.2（Table 4），pp.27–28；附录 G.1（Table 25），p.56 |
| evaluation | §5、Tables 2–3、Figures 2–3，PDF pp.6–10；附录微调设置，p.40 |
| limitations | §6 末段、§7，PDF p.10 |
