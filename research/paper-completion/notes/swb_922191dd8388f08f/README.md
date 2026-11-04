# Guo et al. — SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills

SKILL-DISCO 把智能体的成功轨迹看作未知 FSM 转移图上的路径，把“程序性技能”定义为可在参数绑定下匹配多条轨迹的参数化控制流子图（PFSM）。方法分两阶段：先蒸馏（轨迹转程序、子目标操作抽取、跨轨迹聚类），再编译（技能规格、Python 合成与留出集验证）。

在 ALFWorld 上，与 CodeAct 结合后成功率从 96.3% 升至 99.3%；在 WebArena 上，与 ReAct 结合后从 23.9% 升至 29.1%，轮数均下降。已阅读正文、Limitations、附录 A 结果表；附录 B 的提示词只浏览了结构。

[原文](https://arxiv.org/abs/2606.26669)

版本：arXiv:2606.26669v1（2026-06-25，cs.AI），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–4 |
| 方法 | §3、附录 B，PDF pp.4–6、10–16 |
| 评测 | §4、Tables 1–7，PDF pp.6–8、10–12 |
| 局限 | Limitations，PDF p.9 |
