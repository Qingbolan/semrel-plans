# Suri, Mathur, Lipka, Dernoncourt, Rossi, Manocha — ChartLens: Fine-grained Visual Attribution in Charts

本文提出“图表的事后细粒度视觉归因”任务：给定图表图像和一条与图表相关的文本回答，找出支持该回答的具体图表元素（柱、线段、扇区）。方法 ChartLens 先用启发式加 SAM 分割柱和扇区，用 LineFormer 分割折线，给元素打上编号标记，再用 Set-of-Marks 提示 GPT-4o 进行验证和归因。

作者构建 1,244 条查询的 ChartVA-Eval 基准。柱状图 F1 为 69.28/34.65/64.14，零样本 GPT-4o 框预测为 22.77/3.30/7.75（Table 2）。全文与附录已读，Tables 1–4 已渲染核对。

[原文](https://aclanthology.org/2025.acl-long.1094/)

版本：ACL 2025 Long Papers 正式版，16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，PDF pp.1–3 |
| method | §5、Fig.2、附录 Alg.1–2，PDF pp.5–6、13、16 |
| evaluation | §4、§6–7、Tables 1–4、附录，PDF pp.4、6–8、11–13；pp.4、7 已渲染核对 |
| limitations | §9–10，PDF p.9 |
