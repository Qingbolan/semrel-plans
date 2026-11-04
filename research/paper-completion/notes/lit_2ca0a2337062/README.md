# Zhang et al. — TableLlama: Towards Open Large Generalist Models for Tables

本文构建表格指令微调数据集 TableInstruct（14 个数据集、11 类任务），并在 LongLoRA 7B（Llama 2）上全参数微调得到开源通用表格模型 TableLlama。在 8 个域内任务中，7 个与各任务 SOTA 相当或更好；在 6 个未训练的域外数据集上，比未微调的基座模型高 5–44 个绝对点。已阅读正文 §1–7 与 Tables 1–4，附录只核对了 Table 5–6；未逐项审计附录中的提示样例。

[原文](https://aclanthology.org/2024.naacl-long.335/)

版本：NAACL 2024 Long Papers，pp.6024–6044（ACL Anthology 2024.naacl-long.335），21 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1，PDF pp.1–3 |
| 方法 | §2.1–2.2、§3、Figure 2、Table 1，PDF pp.3–5 |
| 评测 | §4.1–4.2、Tables 2–4，PDF pp.6–8 |
| 局限 | §7 Limitations、§4.1 行填充误差分析，PDF pp.6、9 |
