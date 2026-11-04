# Deep Research is the New Analytics System: Towards Building the Runtime for AI-Driven Analytics

语义算子能被优化，但按迭代器逐条处理，不适合需要跨文件推理的交互式分析；Deep Research 智能体规划灵活，却常走捷径、过早停止。本文在 Palimpzest 中加入 Context 抽象（迭代、索引、自定义工具与自然语言描述）和由 CodeAgent 实现的 compute/search 算子，让智能体能写出并执行经过优化的语义算子程序。

两条查询、各跑 3 次：KramaBench 身份盗窃比值查询上误差 0.02%（手写语义程序 17.00%、CodeAgent 27.56%），但更慢；Enron 邮件筛选上 F1 98.67%，比纯 CodeAgent 高 1.95 倍，并比把语义算子当工具的 CodeAgent+ 省 76.8% 费用、72.7% 时间。

[原文](https://www.vldb.org/cidrdb/papers/2026/p30-russo.pdf)

版本：CIDR 2026（Russo, Kraska，MIT），愿景论文加初步原型；本地全文为 arXiv 2509.02751v1（已带 CIDR'26 版式），共 §1–6、Figures 1–2、Tables 1–2。数字已对照该全文核对，未运行作者代码；文中的逻辑重写等优化多为未来工作，不能当作已实现能力。
