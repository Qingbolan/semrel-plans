# Kong et al. — TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning

TimeSage-MT 是面向时间序列智能体的多轮对话基准：240 个任务、2,680 个对话轮次，分 L1 开放探索到 L4 完整决策四级（每级 60 个），L3–L4 覆盖 8 个领域。对话由 Claude Opus 4.6 生成，数值答案由参考代码在原始序列上确定性抽取，经规则审计、LLM 复查和人工审阅。六个前沿模型在代码执行设置下总分集中在 35–40；代码执行显著优于直接回答，技能库与结构化流水线 TimeSage 的收益依模型而定。已读正文、附录 B 的构造与审计部分和附录 H，未逐项阅读附录 C–E 的全部子检查与提示词。

[原文](https://arxiv.org/abs/2606.01498)

版本：arXiv:2606.01498v1（2026-05-31），39 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1、Fig.1，PDF pp.1–3 |
| method | §3、Figs.2–4，pp.4–6；附录 B，pp.14–20（抽读） |
| evaluation | §4、Figs.5–8、Table 2，pp.6–9 |
| limitations | §5，pp.9–10；附录 H，p.38 |
