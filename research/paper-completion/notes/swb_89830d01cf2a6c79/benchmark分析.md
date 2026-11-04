# 评测与边界

**设置**：监督方法 PURE、PL-Marker（pipeline）与 HGERE（joint），编码器为 SciBERT，5 个随机种子取平均。LLM 为 GPT-3.5-Turbo、Llama3-70b、Qwen2-72b，少样本用 SimCSE 检索 30 个相似示例，提示中加入标注指南。指标：NER 为跨度+类型严格匹配 F1；Rel 要求实体边界与关系正确，Rel+ 还要求实体类型正确；RE 为给定金标准实体的关系分类 F1。

**实验 1（主结果，Table 3）**：

| 方法 | ID NER | ID Rel+ | OOD NER | OOD Rel+ |
|---|---|---|---|---|
| HGERE（监督 joint） | 86.85 | 61.10 | 81.32 | 58.32 |
| PL-Marker（监督 pipeline） | 83.31 | 59.24 | 73.93 | 56.68 |
| Llama3-70b 零样本 pipeline | 61.69 | 21.71 | 53.09 | 25.57 |
| Qwen2-72b 少样本 pipeline | 71.44 | 41.22 | 61.72 | 37.13 |
| Qwen2-72b 少样本 joint | 63.73 | 34.87 | 49.21 | 33.17 |

监督方法从 ID 到 OOD 的 NER 下降最多近 10 点；LLM 的 pipeline 普遍优于 joint。LLM 在 RE 上偏弱，作者归因于 NULL 占比超 60% 且 LLM 倾向把 NULL 判为某种关系。

**实验 2（提示消融，Fig.3）**：去掉标注指南中的标签定义和注意事项后，Llama3-70b 少样本各任务都下降；NER 的 HTML 标签进一步有帮助。

**实验 3（训练规模，Fig.4）**：PL-Marker 的 NER 随训练文档增加而收益递减，关系抽取对数据量更敏感。

**边界**：GPT-3.5 因成本只在每个测试集抽 200 句、跑 3 次（附录 B.2），与其他模型在全部样本上跑 5 次不同口径。Limitations 承认仅三类实体、无嵌套实体、PDF 解析错误导致部分句子有噪声、LLM 提示未充分优化。

依据：[EMNLP 2024，pp.13083–13100](https://aclanthology.org/2024.emnlp-main.726.pdf)，§4.4–5.3，Table 3、Fig.3–4，PDF pp.6–8；附录 B–C，pp.13–15；Limitations，p.9。
