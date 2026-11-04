# 评测与边界

模型：SVM/逻辑回归（n-gram 与词性特征）、CRF（token、lemma、词性、mat2vec）、BiLSTM（叠加 word2vec、mat2vec、bpe、BERT/SciBERT 嵌入，句分类加注意力层，序列标注加 CRF）、微调 BERT-base/SciBERT（序列标注加 CRF）；分词用 ChemDataExtractor（§6–7，pp.5–6）。

**实验 1（实验句识别，Table 5，p.7）**：测试 F1 最高为 BERT-large 68.6，SciBERT 67.0，RBF SVM 59.4；人类 78.3。

**实验 2（实体识别，Table 6，p.7）**：测试宏 F1 最高为 BiLSTM+…+SciBERT 81.5 与 SciBERT 81.5，CRF 60.3；人类 95.8。VALUE 较易，MATERIAL 与 DEVICE 较难。

**实验 3（槽位填充，Tables 7–8，p.8）**：

| 模型 | 开发宏 F1 | 测试宏 F1 |
|---|---|---|
| CRF | 45.3±5.6 | 41.3 |
| BiLSTM SciBERT | 67.8±12.9 | 62.6 |
| BiLSTM+…+SciBERT | 67.1±13.3 | 59.7 |
| SciBERT（微调） | 65.6±13.2 | 56.4 |
| 人类 | — | 83.4 |

此任务上 BiLSTM 叠加 (Sci)BERT 嵌入优于直接微调。分槽位看，PowerDensity 97.6、Resistance 93.9，而 InterlayerMaterial 10.7、AnodeMaterial 19.0；作者认为材料角色常需前文语境与领域知识（Table 8，§7，p.8）。

**实验 4（迁移，Table 9，p.8）**：在 Mysore et al. 合成流程数据（200/15/15 篇）上，BiLSTM+all（SciBERT）微平均 F1 92.2，Mysore et al. 2017 为 77.5–77.6，但作者注明数据略有不同，不可直接比较。

边界：一句一实验假设、实验间链接与跨句关系未建模（§4、§8，pp.4、9）；人类分数来自子集，不可直接比较（§7，p.6）。阅读者分析：补充表与正文表有不一致，如 Table 5 与 Table 12 中"+SciBERT"和"BiLSTM SciBERT"两行数值互换；Table 6 的 SciBERT 测试行与 Table 13 的 SciBERT 开发列相同，而 Table 13 测试列为 80.4（阅读者分析）。

依据：[ACL 2020，2020.acl-main.116，14 页](https://aclanthology.org/2020.acl-main.116.pdf)，§6–8、Tables 5–9，PDF pp.5–9；补充 Tables 12–13，p.13。
