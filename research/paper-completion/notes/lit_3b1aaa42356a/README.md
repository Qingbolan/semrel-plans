# Li, Peng, Xie, Lu, Zhu, Mu, Liu, Luo — DeepEye: A Steerable Self-driving Data Agent System

DeepEye 是一篇 4 页的系统演示论文（SIGMOD Companion ’26），提出以工作流为中心的数据智能体：用统一节点协议把数据库、文件与知识库接入同一 DAG，规划器把用户请求编译成由 AgentNode（LLM 子智能体）与 ToolNode（确定性算子）组成的工作流，再由借鉴 DBMS 的工作流引擎（编译、校验、优化、执行）运行，输出数据视频、仪表盘和分析报告。论文没有定量实验，只给出“全球销售业绩分析”两个演示场景。已通读全文。

[原文](https://arxiv.org/abs/2603.28889)

版本：arXiv 2603.28889v1（2026-03-30，cs.DB），即 SIGMOD Companion ’26 演示论文（DOI 10.1145/3788853.3801612），4 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1（Prior Art & Limitations、Challenges C1–C3），PDF pp.1–2 |
| method | §2.1–2.4、Fig.1，PDF pp.2–4 |
| evaluation | §3 演示场景 1–2、Fig.2，PDF pp.3–4（无定量评测） |
| limitations | 无独立章节；阅读者依据全文推断 |
