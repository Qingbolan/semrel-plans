# Abdallah et al. — MoCA-Agent: A Market-of-Claims Code Agent for Financial and Numerical Reasoning

MoCA-Agent 把金融/表格问答拆成至多 10 条带类型的原子声明（事实、公式、单位、符号、方向等），让四个"交易员"角色对每条声明下买/卖单，按加权成交量清算为接受/拒绝/不确定，再只用未被拒绝的声明合成 Python 程序，并由代码感知验证器、一次修复和备选方案委员会兜底。论文用单一 Qwen3.6-27B 骨干在 10 个公开基准（12 个评测轨道）上报告结果，例如 FinQA 78.29%、MultiHiertt 71.17%；在固定骨干的重实现对比中比最强竞争智能体高 3.79/7.47 点。已阅读正文、局限性、附录 A–C 和部分 D；未逐项核对附录 B 的全部排行榜行。

[原文](https://arxiv.org/abs/2606.11537)

版本：arXiv:2606.11537v2（2026-06-17），30 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–4 |
| method | §3.2–3.6，PDF pp.4–5；附录 C、D，PDF pp.21–30 |
| evaluation | §4–5、Tables 1–7，PDF pp.5–8；附录 A（Table A.1）、B.9，PDF pp.13–15、21 |
| limitations | Limitations、Ethical Considerations，PDF p.9 |
