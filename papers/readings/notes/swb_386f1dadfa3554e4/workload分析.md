# 工作负载

三个 PubMed 摘要 NER 基准，只用实体标注，不用关系（§4.2，PDF p.6）：

| 数据集 | 修订集 | 评测集 | 评测实体数与类型 |
|---|---|---|---|
| NCBI Disease | 训练集随机 10 篇 | 开发集全部 100 篇 | 791；SpecificDisease 409、Modifier 218、DiseaseClass 127、CompositeMention 37 |
| BC5CDR | 训练集随机 10 篇 | 开发集 500 篇中随机 100 篇 | 2,146；Chemical 1,195、Disease 951 |
| BioRED | 训练集随机 10 篇 | 开发集全部 100 篇 | 3,531；6 类（Gene 1,085、Disease/Phenotype 982、Chemical 822 等） |

实体数来自 Table 1 与附录 Table 5（PDF pp.7、14）。原测试集被刻意保留不用（§4.2，PDF p.6）。

**模型**：gpt-5-2025-08-07（reasoning_effort low/high）、gemini-2.5-pro（thinking_budget min/max）、deepseek-chat 与 deepseek-reasoner，均用默认超参（§4.3，PDF pp.6–7）。

**提示**：系统指令 + `{{entitySchema}}` + `{{guidelines}}` + JSON 输出规则 + `{{inputText}}`（Figure 5a，PDF p.12）。

阅读者分析：评测集来自官方开发集，与文献中官方测试集上约 89–94 的 F1 不可直接比较，作者也这样说明（§4.2，PDF p.6）。
