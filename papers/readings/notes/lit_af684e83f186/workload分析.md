# 工作负载

**基准统计**（Table 1，PDF p.5；附录 C，PDF p.12）：

| 任务 | 数据集 | 平均 token | 最大 token | 样本数 |
|---|---|---|---|---|
| 多跳 | HotpotQA | 9.4k | 15.9k | 300 |
| 多跳 | 2WikiMultihopQA | 8.8k | 15.9k | 300 |
| 多跳 | MuSiQue | 15.5k | 16.0k | 200 |
| 多跳 | HotpotWikiQA-mixup（LV-Eval） | 142.4k | 370.8k | 250 |
| 单跳 | NarrativeQA | 29.7k | 63.7k | 200 |

前四个 LongBench 数据集（HotpotQA、2Wiki、MuSiQue、NarrativeQA）来自 LongBench。HotpotWikiQA-mixup 把支持文档与干扰文档混合成 16k、32k、64k、128k、256k 五档长度；为控制成本，每档只取前 50 条（共 250 条）。token 数用 TikToken 的 GPT-4 分词器计算。

附录 E 另在 QuALITY（长文多选，按普通问答处理）和 Natural Questions 上补充实验，正文未给这两者的样本数（PDF pp.12–13）。

**图统计**（附录 H、Table 9，PDF pp.14–15）：长文本的节点和原子事实更多；归一化后每个节点平均约 10 个邻居、约 2 条原子事实；NarrativeQA 因剧本中主角反复出现，单节点原子事实最多。

**评价单位**：每个问题的答案，以 LLM 评分 LR-1（严格）、LR-2（宽松）、EM、F1 计分；LV-Eval 使用其 F1*（先检查答案关键词召回，低于阈值则记 0）（§4.1、附录 B，PDF pp.5、12）。

依据：§4.1、Table 1、附录 B、C、E、H，PDF pp.4–5、12–15。
