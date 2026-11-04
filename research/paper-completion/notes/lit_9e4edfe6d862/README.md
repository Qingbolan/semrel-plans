# Liao et al. — Bridging the Last Mile of Time Series Forecasting with LLM Agents

本文（Trip.com）把"基线预测之后的情境化修订"定义为 last-mile forecasting：TimesFM 先给出基线，LLM agent 在共享的预测工作表上调用工具取证，并只能通过受约束的修订动作改写 y_final，同时留下可审计的修订轨迹，另有 map-reduce 长时域分解与反思记忆。评估只是在一条匿名化的国内航线日票量序列上做三个案例研究：春节 23 天窗口内 MAE 507.28（Prophet）/857.28（TimesFM）降至 101.59；126 天长时域全程 MAPE 18.91%、MAE 与 Prophet 相当。已阅读正文全部与附录 A–C；无大规模基准、无重复运行，未说明所用 LLM。

[原文](https://arxiv.org/abs/2606.02497)

版本：arXiv:2606.02497v1（2026-06-01），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，PDF pp.1–3 |
| method | §4（Tables 1–2、Figs.1–2），附录 B（提示词与工具，Table 7），PDF pp.3–5、9–11 |
| evaluation | §5、Tables 3–5，附录 A（Table 6）与附录 C 修订记录，PDF pp.5–7、9–14 |
| limitations | §7，PDF p.7 |
