# 评测与边界

**模型**：SpERT（bert-base-cased，最大跨度 32）与 REBEL（bart-large，最大源/目标长度 64）。REBEL 不能抽取无关系的实体，因此只评关系（§7.2，p.5）。指标为实体及关系（strict、loose）的 micro/macro F1。strict 要求关系类型、头尾实体跨度和类型都正确；loose 只要求关系类型和头尾跨度正确（§5、§7.1）。

**实验 1（Table 4，F1，p.8）**：FG 表示只在细粒度语料上微调，CG→FG 表示先在粗粒度语料上预微调。

| 模型/策略 | 类数 | ER micro/macro | RE strict micro/macro | RE loose micro/macro |
|---|---|---|---|---|
| SpERT FG | 5 | 87.4/88.8 | 67.1/62.3 | 68.3/62.6 |
| SpERT FG | 224 | 64.4/38.7 | 27.3/35.1 | 55.7/61.1 |
| SpERT CG→FG | 224 | 55.4/27.0 | 15.5/26.5 | 71.4/72.7 |
| REBEL FG | 32 | — | 0.8/0.6 | 69.0/70.2 |
| REBEL FG | 224 | — | 0.0/0.0 | 66.7/53.5 |
| REBEL CG→FG | 32 | — | 37.4/51.1 | 71.1/72.5 |
| REBEL CG→FG | 224 | — | 0.0/0.0 | 76.1/77.3 |

**结论**：类数越多，实体识别越差；REBEL 在 32 和 224 类上的 strict 关系抽取失败。粗到细预微调对 REBEL 有帮助（32 类 macro strict 0.6→51.1），对 SpERT 的 strict 指标反而下降，作者推测因粗粒度阶段固化了五类权重（§8.2，pp.8–9）。

**标注一致性**：1,400 条双标文本的 F1 为实体 91.8%、strict 关系 64.1%、loose 关系 75.5%（§8.1，p.7）。

**表格不一致**：附录 Table 7（SpERT FG strict，224 类）给 micro 35、macro 27，Table 4 为 27.3/35.1；Table 6 也与 Table 4 的 micro/macro 对调。疑似附录中 micro/macro 标签互换（阅读者分析）。

**边界**：224 类中只用到 156 类，数据偏向采矿资产；文本过短导致细类难以消歧；单次划分，未报告方差；粗粒度语料无一致性评估（§6.2、§8.1）。

依据：§5–8、Table 4、Tables 5–7，PDF pp.4–10。
