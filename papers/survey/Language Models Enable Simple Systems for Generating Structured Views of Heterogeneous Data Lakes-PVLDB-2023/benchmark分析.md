# 评测与边界

**对比对象**：内部为 Evaporate-Direct、Evaporate-Code、Evaporate-Code+；外部在 SWDE 上与 ZeroShot Ceres、RoBERTa-Base、RoBERTa-Structural、DOM-LM 比较（这些基线在领域内训练）；无结构文本上作者认为没有强基线，OpenIE6 只能处理规整句子（§4.3）。主实验 LLM 为 text-davinci-003。

**实验 1（与 SoTA 比较，Table 2，p.10）**：SWDE 上 ClosedIE 用 Text F1，OpenIE 用 Pair F1。

| 系统 | Movie Closed | Movie Open | University Closed | University Open |
|---|---|---|---|---|
| ZeroShot Ceres | – | 50.0 | – | 50.0 |
| RoBERTa-Base | 49.3 | 35.6 | 36.6 | 38.0 |
| RoBERTa-Structural | 47.7 | 39.9 | 46.5 | 42.3 |
| DOM-LM | 71.9 | 54.1 | 68.0 | 55.2 |
| Evaporate-Direct | 84.4 | 45.2 | 72.6 | 53.8 |
| Evaporate-Code | 55.0 | 33.0 | 40.5 | 22.2 |
| Evaporate-Code+ | 79.5 | 56.8 | 73.7 | 59.0 |

**实验 2（Direct vs Code+ 的质量与成本，Table 3，p.11）**：Pair F1；成本按每万篇文档。Direct 因费用只在抽样上评测（FDA、Wiki 20%，SWDE 2%，Enron 0.0002%）。

| 数据 | Direct F1 | Direct token | Code+ F1 | Code+ token | F1 差 | 成本降幅 |
|---|---|---|---|---|---|---|
| FDA | 45.5 | 145.6M | 62.8 | 1.9M | +17.3 | 77× |
| Enron | 93.8 | 21.2M | 86.9 | 0.6M | −6.9 | 35× |
| Wiki NBA | 44.8 | 650.1M | 68.2 | 3.0M | +23.4 | 217× |
| SWDE Movie | 45.2 | 282.9M | 56.8 | 2.3M | +11.6 | 123× |
| SWDE University | 53.8 | 190.1M | 59.0 | 1.9M | +5.2 | 100× |
| 平均 | 56.6 | 258M | 66.7 | 1.9M | +10.1 | 110× |

按文档数算，函数生成的成本交叉点约为 40 篇；按属性数算，约为 2,500 个属性（§4.4.1，Figure 3）。单个函数处理一篇 FDA 文档平均 0.00025 s（2 CPU）。

**实验 3（聚合方式，Table 4，p.11）**：平均 Pair F1 为多数投票 56.2、弱监督 57.7、弱监督 + 过滤 64.8、再加弃权处理 66.7。没有 Algorithm 1，质量不会超过 Direct。

**实验 4（换模型，Table 5，p.12）**：在 10 篇样本上，GPT-4、Claude-V1、Jurassic Jumbo-2 都能运行该框架；Code+ 的平均精确率（70.9、67.6、50.9）高于 Direct（61.9、55.1、49.9），体现精确率与召回率的取舍。

**边界**：

- Direct 只在抽样上评测，而 Code+ 在全集上，Table 3 的质量对比样本不同（阅读者分析）。
- 证明批量复用程序是强替代基线，不证明所有语义字段都可程序化（阅读者分析）。
- 净收益应计入函数生成、验证与聚类成本，不能只比稳态的逐文档调用（阅读者分析）。
- §4.4.1 写"Evaporate-Direct 随文档数渐近更高效"，从上下文看应指 Evaporate-Code+，疑为笔误（阅读者分析）。

依据：[arXiv 2304.09433v3](https://arxiv.org/abs/2304.09433v3)，§4.3–4.4、Figure 3、Tables 2–5，pp.9–12。
