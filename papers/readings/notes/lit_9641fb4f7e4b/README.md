# Zhang et al. — AFlow: Automating Agentic Workflow Generation

AFlow 把 agentic workflow 的构建看作一个搜索问题：工作流用代码表示，由调用 LLM 的节点和代码边组成；搜索使用 MCTS 变体，配合预定义算子（Ensemble、Review & Revise 等）、树状经验和执行反馈逐轮修改工作流。在六个推理基准上，以 GPT-4o-mini 为执行模型，平均得分 80.3，高于最好的手工方法（CoT SC 76.0）和 ADAS（67.2）。已阅读正文、算法、主要表格，以及成本、开放任务和理论讨论附录。

[原文](https://arxiv.org/abs/2410.10762)

版本：ICLR 2025，arXiv:2410.10762v4（2025-04-15），38 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–5 |
| method | §3.2、§4、Algorithm 1、App. A，PDF pp.5–7、15–19 |
| evaluation | §5、Tables 1–2、Figs. 4–6、App. D，PDF pp.7–10、30 |
| limitations | §3.2、App. F、App. G，PDF pp.6、31–38 |
