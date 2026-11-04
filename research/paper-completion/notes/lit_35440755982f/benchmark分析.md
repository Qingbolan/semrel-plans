# benchmark

- **基线**：DataWise（Infi-DA-Bench 上的 SOTA）、Agent-Poirot（InsightBench 上的 SOTA），均按官方仓库超参数，与 CIPHER 共用推理配置和 3 个种子；框架内部基线为 Base 生成 + Random 选择。
- **主效应（Table 1，两模型、两预算、三种子合并）**：Ensemble vs Base +3.36pp（95% CI [2.86, 3.85]，p<0.001），其中 Infi +6.44、InsightBench +0.29；Conditional +0.19pp（p=0.207）；选择策略：Clustering +0.15、Goal-Align +0.12、MaxEnt +0.44（p=0.040）；leader vs self 聚合 +0.46pp（CI [0.04, 0.89]，p=0.018）。
- **排名（Table 2/9）**：第一为 Ensemble+Random、M=5、leader：Infi 82.49%、InsightBench 51.87%、总体 67.18%，P(best)=57.7%；另有五个 M=5 的 Ensemble 配置与之无显著差异；同预算的 Base+Random 排第 11（总体 63.89%）。只看 M=3 时 Ensemble+MaxEnt 居首（附录 D.3）。
- **对专用基线（Table 3）**：Infi——Haiku：DataWise 84.18±0.59 vs CIPHER 83.40±0.45；DeepSeek：82.75±1.12 vs 81.58±0.59。InsightBench——Haiku：Agent-Poirot 54.05±0.97 vs CIPHER 55.14±2.00；DeepSeek：49.84±1.89 vs 48.60±0.47。即 CIPHER 在 Infi 上略低于 DataWise，在 InsightBench 上与 Agent-Poirot 互有高低。
- **局限（附录 F）**：选择策略不利用 token 级概率；N 个候选一次性生成，未做按失败自适应扩充；只在数据科学任务上验证。
- **阅读者分析**：(1) InsightBench 使用了任务元数据中的探索性假设作引导，并以 LLM 评审判分，结果不能与无引导设置直接比较；(2) 正文称参考配置把"single-plan agent"从 76.5 提升到 82.5，但全文未报告 CIPHER(1,1) 的准确率；76.5 与 Table 2 中同预算 M=5 的 Base+Random（Infi 76.52）吻合，"single-plan"可能指单一提示而非单条执行路线，阅读者无法确认；(3) 聚合增益仅 +0.46pp，且 leader 用了更贵的模型，成本-收益文中只给 token，没有美元成本。

依据：[arXiv:2607.14386v2，17 页](https://arxiv.org/abs/2607.14386)，§4、Tables 1–3、附录 B、D.3、F，PDF pp.4–5、9、13–14、17。
