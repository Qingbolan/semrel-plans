# El Yadouni & Li — TraceCompiler: Skill-Guided Mining and Compilation of LLM Agent Traces into Mostly Deterministic Workflows

TraceCompiler 把同一意图的多条嘈杂 agent 工具调用轨迹聚类、去噪，并编译为“基本确定”的类型化工作流；只有当消费者参数中的值唯一可归因于更早的生产者调用时，才承认工具间的硬依赖。论文的突出特点是大量自我限定：T1 上机械化规则 P/R=0.928/0.943（15,775 条边），AppWorld 回放 563 条 token 边 P=0.993（作者称之为自洽性检查）；Venmo 意图 34→11 次调用、留一执行 15/21；Spotify/Todoist 意图被拒绝编译。已阅读正文 §1–7 全部内容，附录 A 仅浏览。

[原文](https://arxiv.org/abs/2608.02680)

版本：arXiv:2608.02680v1 [cs.SE]（2026-08-03），17 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §3.1–3.5、§4，PDF pp.3–5 |
| 评测 | §5–6、Tables 1–5、Figures 2–4，PDF pp.4–11 |
| 局限 | §6.3 末尾、§6.5–6.6 的“不能测试什么”、§7，PDF pp.7–12 |
