# 工作负载

作者只在测试集上评测，不在训练集上微调（理由是 LLM 调用成本）。

| 数据集 | 任务 | 评测切分与规模 | 指标 |
|---|---|---|---|
| TabFact | 表格事实核查，众包陈述基于 Wikipedia 表 | 官方 test-small：2,024 条陈述、298 张表 | 二分类准确率 |
| WikiTableQuestions | 复杂问答（比较、聚合、算术） | 验证集 2,381、测试集 4,344 | 指称（denotation）准确率 |
| FetaQA | 自由文本长答案问答，常需非连续单元格 | 测试集 2,003 | BLEU、ROUGE-1/2/L |

**提示示例**：最终推理步骤分别人工标注 4、2、6 个示例（TabFact、WTQ、FetaQA），采用 self-consistency 解码；模型为 code-davinci-002。

**难度划分**（消融用）：TabFact 依官方难度标签分 Simple/Complex；WTQ 按问题长度划分；FetaQA 不划分。

**表规模**：Figure 3 报告分解前后平均单元格数，WTQ 从 164 降到 56；作者概括为子证据约小 3 倍。TabFact、FetaQA 的具体前后值在提取文本中难以与柱子一一对应，此处不转述。

依据：§5.1–5.3，pp.7–8；§5.6，p.10；§5.8、Figure 3，pp.11–12。
