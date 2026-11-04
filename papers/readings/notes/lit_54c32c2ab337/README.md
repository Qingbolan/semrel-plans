# Nie et al. — DSGym: A Holistic Framework for Evaluating and Training Data Science Agents

DSGym 把多个数据科学智能体基准统一到同一个容器化执行框架中（任务对象、CodeAct 式智能体接口、manager–worker Docker 环境），并发布 DSGym-Tasks：经人工质检和“无数据也能答对”的捷径过滤后的 QRData/DAEval，加上 DABStep、MLEBench-Lite，以及新建的 DSBio（90 个生物信息任务）和 DSPredict（92 个 Kaggle 竞赛）。主要发现是现有基准有相当比例题目不读数据也能答对，前沿模型在 DSBio 上明显落后；附带用 2,000 条执行验证的合成轨迹微调出一个 4B 模型。已阅读正文与附录 A.1–A.2；未逐条阅读附录中的失败案例与竞赛清单。

[原文](https://arxiv.org/abs/2601.16344)

版本：arXiv:2601.16344v1（2026-01-22），37 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1、§3，PDF pp.1–2、5–6 |
| method | §2、§4.1–4.4、Figure 2/6、Table 1，PDF pp.3–9；附录 A.1–A.2，pp.20–21 |
| evaluation | §5、§6、Tables 2–5、Figures 3/8/9，PDF pp.5、9–13；Figure 5 (p.6) 已渲染核对 |
| limitations | §8 Discussion and Limitations，PDF p.14 |
