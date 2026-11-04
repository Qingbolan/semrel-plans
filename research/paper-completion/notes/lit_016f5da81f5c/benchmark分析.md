# 评测与边界

**方法**（§4.1，PDF pp.5–6）：提示类 LLM 方法 4 个（DINSQL、DAILSQL、DAILSQL(SC)、C3SQL）；微调类 LLM 方法 9 个（SFT CodeS 1B/3B/7B/15B，以及 Llama2-7B、Llama3-8B、StarCoder-7B、CodeLlama-7B、Deepseek-Coder-7B）；PLM 方法 7 个（Graphix-3B+PICARD、RESDSQL Base/Large/3B 及其 +NatSQL 版本）。

**实验 1（复杂度，Tables 3–4，PDF p.6）**：

| 方法 | Spider-Dev EX | Spider-Dev EM | BIRD-Dev EX |
|---|---|---|---|
| C3SQL（GPT-3.5） | 82.0 | 46.9 | 50.2 |
| DAILSQL（GPT-4） | 83.1 | 70.0 | 54.3 |
| DAILSQL(SC) | 83.6 | 68.7 | 55.9 |
| SFT CodeS-7B | 85.4 | 79.4 | 57.0 |
| SFT CodeS-15B | 84.9 | 78.3 | 58.5 |
| RESDSQL-3B+NatSQL | 84.1 | 80.5 | – |
| SuperSQL | 87.0 | 72.1 | 58.5 |

DINSQL 因 GPT 资源限制未在 BIRD 上运行；RESDSQL 在 BIRD 上重训，但因代码不可用未加 NatSQL（Exp-1）。

**实验 2–4**：子查询、逻辑连接词、JOIN 场景中 LLM 方法整体更好；ORDER BY 结论随数据集变化；QVT 与领域适配均无明确赢家（Findings 2–7，PDF pp.7–8）。

**实验 6（成本，Table 5，PDF p.9）**：每查询平均成本，C3SQL 为 $0.0103（Spider），DINSQL $0.2988，DAILSQL $0.0288，SuperSQL $0.0354；按 EX/成本，GPT-3.5 方案性价比最高。正文称 SuperSQL 比其他 GPT-4 方法 token 和成本都更少，但在 Spider 上它的 942 token、$0.0354 均略高于 DAILSQL 的 930 token、$0.0288（阅读者分析）。

**实验 7–9**：模型越大延迟与显存越高；VES 无明确赢家，SuperSQL 在 Spider/BIRD 开发集的 VES 为 99.18/61.99；训练样本约 4,000 条时即可达到可接受性能，之后边际收益递减（Findings 10–12，Tables 6–7、Figure 12，PDF pp.9–10）。

**边界**：§6 指出歧义问句、脏数据与 schema 歧义、schema linking 不足会导致错误 SQL，并提出可信性、低成本和自适应训练数据三个方向（PDF p.12）。各结论只基于 Spider/BIRD 开发集，属于公开基准，作者自己也承认真实场景更复杂（§1）（阅读者分析）。
