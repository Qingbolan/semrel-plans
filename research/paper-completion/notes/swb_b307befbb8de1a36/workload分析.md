# 工作负载

**数据集（Table 1）**：

| 任务 | 数据集 | 训练/验证/测试 | 基线 | 标注指南 |
|---|---|---|---|---|
| NER | BC5CDR-Chemical/Disease | 4560/4581/4797 | BioLinkBERT-Large | 有，8 页 |
| NER | NCBI-Disease | 5424/923/940 | BioBERT-Large v1.2 | 有，5 页 |
| RE | BioRED | 4873/1162/1163 | BiomedBERT | 有，16 页 |
| RE | BC5CDR-RE | 1323/1343/1375 | BioLinkBERT-Large、BioGPT | 有，8 页 |
| 多标签分类 | LitCovid | 24960/6239/2500 | BioBERT-Large v1.2 | 无 |
| 多标签分类 | HoC | 1108/157/315 | BioLinkBERT-Large | 无 |

NER 用实体级指标，RE 与分类用宏平均指标。论文未说明表中数字的计数单位（句子、文档或实例）。

**评测子集**：因 API 成本，LitCovid 只随机抽 500 个测试样本评测 LLM。阅读者分析：论文没有说明 BERT 基线是否在同样 500 个样本上评测，LLM 与基线可能不是同一测试集。

**BC5CDR-RE 基线训练**：直接微调 BioBERT 几乎全预测负例，作者把训练集负正比降采样到 2:1 后才得到表中结果。

**蒸馏数据**：HoC 用原检索词获取 2024 年 4 月后 PubMed 文献，GPT-4o 标注后去掉无正标签文献，得 3,000 篇；BC5CDR-RE 得 2,361 篇、5,930 条 CDI，负样本按 2:1 随机配对。

**自动提示优化**：仅 LitCovid 与 BC5CDR-Chemical；批大小 100，每轮 3 个伪梯度，beam 保留 3 个，共 10 轮。

依据：[arXiv:2503.03261v2，21 页](https://arxiv.org/pdf/2503.03261v2)，Table 1 及脚注，PDF p.3；§3.3，PDF pp.9–10；附录 7.3，PDF pp.20–21。
