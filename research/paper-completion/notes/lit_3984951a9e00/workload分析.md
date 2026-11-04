# 工作负载

**数据集**（§4.1，p.6）：

| 数据集 | 规模 | 用途 |
|---|---|---|
| Spider 训练集 | 8,659 个实例 | 少样本示例候选；监督微调训练数据 |
| Spider-dev | 1,034 个实例，Spider 共覆盖 200 个数据库 | 主要评测（测试集未公开） |
| Spider-Realistic | 508 个实例 | 从 Spider-dev 选出，人工改写问题、SQL 不变，更难 |

另在附录 F.2 报告 BIRD 排行榜结果：DAIL-SQL 比 DIN-SQL 在 BIRD dev 高 4.04 个百分点、在 test 高 1.51 个百分点，但正文没有 BIRD 的受控实验（p.22）。

**模型**：OpenAI 的 GPT-4、GPT-3.5-TURBO、TEXT-DAVINCI-003；开源的 LLaMA-7B/13B/33B、Falcon-40B、Alpaca-7B、GPT4ALL-7B、Vicuna-7B/13B/33B、LLaMA-2-CHAT-7B/13B/70B、CodeLLaMA-34B（§4.2、§4.4.1，pp.7、9–10）。

**设置**（§4.1，p.7）：最大上下文 OpenAI 4,096、开源 2,048 token，预留 200 token 给回复；温度 0；取回复中第一条 SQL。评测脚本为 test-suite-sql-eval。

**指标**：EM 比较 SQL 关键字集合；EX 比较在数据库实例上的执行结果。token 效率按每题平均提示 token 数衡量（§4.5，p.11）。

作者在局限中承认 Spider 与 Spider-Realistic 的数据库可能不够大，表很多时会出现新的效果和效率挑战（§5，p.13）。

依据：§4.1–4.5、§5、附录 F.2，PDF pp.6–7、9–11、13、22。
