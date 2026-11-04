# 工作负载

**训练数据（附录 A.2、Table 3，PDF pp.17–18）**：共 145,619 条（正文约记为 150k）。

| 来源 | 条数 |
|---|---|
| GPT-4 Alpaca / Stanford Alpaca / FLAN-V2 / ShareGPT / OpenAssistant | 26,168 / 25,153 / 17,817 / 13,406 / 9,464 |
| Wizard of Wikipedia / NQ / FEVER | 17,367 / 15,535 / 9,966 |
| OpenBookQA / ARC-Easy / ASQA | 4,699 / 2,147 / 3,897 |

critic 的 GPT-4 标注数：Retrieve 12,594（原文写作 “1,2594”）、IsSup 11,181、相关性 19,317、有用性 3,831（PDF p.17）。

**评测（§4.1，PDF pp.6–7）**：全部为零样本。
- 闭集：PubHealth 事实核验、ARC-Challenge，指标为准确率；
- 短文本：PopQA 长尾子集 1,399 条（月浏览量 < 100 的实体）、TriviaQA-unfiltered 11,313 条测试问题，判定金答案是否出现在输出中；
- 长文本：传记生成（FactScore）、ALCE-ASQA（str-em、rouge、MAUVE、引用精确率和召回率）。

PubHealth、ARC 和传记任务的样本数在正文中未给出。阅读者分析：训练集含 ASQA 3,897 条，评测也用 ASQA；原文未讨论二者在问题层面是否有重叠。
