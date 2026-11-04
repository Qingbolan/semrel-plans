# workload

- **基准**：Infi-DA-Bench 257 个封闭题（如"用 1.5×IQR 找出 gdpPercap_1982 为离群值的国家，按 @outlier_countries[list] 格式返回"）；InsightBench 100 个开放任务，共 428 条真值洞察（如分析计算机资产的保修期、成本分布及其相关性并给出 5 条洞察）。合计 357 个任务。1pp 约合 Infi 2.57 题、InsightBench 4.3 条洞察。
- **模型套件**：Claude 4.5 Haiku（leader 聚合器 Claude 4.5 Sonnet）；DeepSeek-V3.2（leader 聚合器 DeepSeek-R1）。所有方法（含基线）共用温度 0.5、top-p 0.99、top-k 500。
- **扫描空间**：3 种生成 × 4 种选择 = 12 种配置；N=10，执行预算 M ∈ {3,5}；2 种聚合 → 48 个配置点；每点在 2 模型 × 2 基准上、3 个随机种子运行，共 96 个 sweep 单元（Tables 5–8 含每题输入/输出 token）。
- **统计**：配对对比、在题目簇上分层 bootstrap 得 95% CI 和单侧 p；排名的 P(best) 用 10000 次配对 bootstrap，机会水平 2.1%。
- 无训练集；所有结果均为对既有公开基准的推理评测。

依据：[arXiv:2607.14386v2，17 页](https://arxiv.org/abs/2607.14386)，§4、Tables 1–2、附录 B、C.1–C.2、D，PDF pp.4–5、8–12、17。
