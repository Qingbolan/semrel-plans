# Wu et al. — ExCyTIn-Bench: Evaluating LLM agents on Cyber Threat Investigation

本文构建一个让 LLM 智能体通过 SQL 查询安全日志来做威胁调查的基准：来自 Azure 演示租户 "Alpine Ski House" 的 57 张 Microsoft Sentinel 等日志表、8 条模拟攻击链，以及从告警—实体二部图自动生成的 7,542 道问答（测试集 589 道）。最好的模型 Claude-Opus-4.5 平均奖励 0.606（Table 2）。已阅读正文 §1–5 及附录 C、D、E.1–E.4；未逐项审计附录中的全部轨迹、事件报告与提示词。

[原文](https://arxiv.org/abs/2507.14201)

版本：arXiv:2507.14201v3（2026-05-01，ICML 2026 / PMLR 306），44 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §3.1–3.3、Algorithms 1–3，附录 C、D，PDF pp.3–5、13–17 |
| 评测 | §4.1–4.3、Tables 2–4，附录 E.2–E.4、Tables 5–8，PDF pp.6–8、14–19 |
| 局限 | §4.3、Broader Impacts、C.5、E.3，PDF pp.8–9、15、19 |
