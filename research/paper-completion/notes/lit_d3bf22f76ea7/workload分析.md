# 工作负载

| 集合 | 规模 | 说明 | 位置 |
|---|---|---|---|
| WikiTQ_hybrid | 510（原 4,344） | 短答案 | §3，p.5 |
| TabFact_hybrid | 303（原 2,000） | 事实核查 | §3，p.5 |
| FinQA_hybrid | 1,006（原 8,281） | 数值推理 | §3，p.5 |
| FinQA_MM、OTT-QA_MM | 各 3,000 题 | 表格 + 表外段落 | §3，p.4 |
| MMTabQA_MM | 1,600 题，206 张表 | 表格中含图片，需要 VLM | §3，p.4 |
| 大表子集 | 98 张表，超过 30 行，平均 17,731 token | 取自 WikiTQ_hybrid | §3.2，p.7 |
| 优化实验 | 随机抽取 200 题 | Table 5 | §3.2，p.8 |
| BIRD 抽样 | dev 集中人工挑选 30 题 | 仅 SQL 即可完成 | App. E.1，p.25 |

**筛选方法**：WikiTQ 和 TabFact 保留 Binder 生成的 SQL 中含 LLM UDF 的问题（作者不验证 Binder 输出是否正确）；FinQA 依据 `qa` 对象排除简单查表题；所有候选再经人工确认确实需要 SQL 与 LLM 两类步骤（§3，p.5；App. D，p.24）。

**模型与提示**：GPT-4o、GPT-4o-mini、Gemini-2.0-Flash、DeepSeek-R1-Distill-Llama-70B，温度 0.01。计划阶段使用三个人工编写、不取自任何数据集的 few-shot 示例（§3，p.5；App. C，p.22）。

依据：§3、Appendix B–E，PDF pp.4–8、22–25。
