# Zhao et al. — LightVA: Lightweight Visual Analytics With LLM Agent-Based Task Planning and Execution

LightVA 是一个可视分析（VA）框架与系统：用户上传数据并给出高层目标，LLM 代理以"推荐器/分解器（planner）—执行器（executor）—控制器（controller）"递归流程把目标拆成任务、生成 Python 分析代码与 Altair/Vega-Lite 交互图、产出结构化 insight，并按需继续分解。评估方式是一个 VAST 2021 MC3 使用场景和 3 名专家的定性研究，没有定量对比基线；作者称场景中工作量从约 108 小时降到约 25 小时。

阅读的是 arXiv v2 预印本（TVCG 接收版的作者稿），正文与附录 A–B 均已阅读，附录 A 中的完整 prompt/输出示例只做浏览。

[原文](https://doi.org/10.1109/tvcg.2024.3496112)

版本：arXiv:2411.05651v2（2025-06-21，作者预印本；对应 IEEE TVCG 2025，DOI 10.1109/TVCG.2024.3496112），27 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §I、§III-A/B（挑战 C1–C2、需求 R1–R5），PDF pp.1–3 |
| method | §III-C、§IV-A–C、Prompt Template 1–3、Fig. 1–4，PDF pp.3–8；附录 A 算法，p.14 起 |
| evaluation | §V 使用场景、§VI 专家研究、Fig. 5–7，PDF pp.8–11；附录 B 性能测试、Table I、Fig. 8–13，PDF pp.23–27 |
| limitations | §VII Discussion，PDF pp.11–12；§V 末段，p.9 |
