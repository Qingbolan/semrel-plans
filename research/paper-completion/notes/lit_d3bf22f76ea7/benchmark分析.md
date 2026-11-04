# 评测与边界

**基线**：End-to-End LLM QA、Binder 与 BlendSQL（UDF 查询引擎）、ReAcTable 与 H-STAR（剪枝）、ProTrix（计划后推理）（§3.1，p.5）。

**实验 1（混合子集 REM，Table 2，p.6）**：

| 模型 | 方法 | WikiTQ | TabFact | FinQA |
|---|---|---|---|---|
| GPT-4o-mini | E2E / H-STAR / ProTrix / Weaver | 60.4 / 59.0 / 61.4 / 65.0 | 84.4 / 83.0 / 81.5 / 89.4 | 44.7 / 40.1 / 46.4 / 49.3 |
| GPT-4o | E2E / H-STAR / ProTrix / Weaver | 66.4 / 61.0 / 61.7 / 70.7 | 80.8 / 87.0 / 80.5 / 83.4 | 58.3 / 46.0 / 54.3 / 60.8 |
| Gemini-2.0-Flash | E2E / H-STAR / ProTrix / Weaver | 67.5 / 63.5 / 62.2 / 69.6 | 81.8 / 86.1 / 80.8 / 85.4 | 29.4 / 38.7 / 42.9 / 44.5 |
| DeepSeek-R1-70B | E2E / H-STAR / ProTrix / Weaver | 76.4 / 68.7 / 41.4 / 73.0 | 82.5 / 55.6 / 81.1 / 91.2 | 52.4 / 50.3 / 60.4 / 65.0 |

正文称 Weaver“consistently outperforms”，但表中至少有三处例外：DeepSeek 下 WikiTQ 的 E2E 76.4 > 73.0；GPT-4o 下 TabFact 的 H-STAR 87.0 > 83.4；Gemini 下 TabFact 的 H-STAR 86.1 > 85.4。Table 3 中 GPT-4o 在 OTT-QA_MM 上也是 E2E 68.7 > Weaver 65.2（阅读者分析）。

Binder 和 BlendSQL 在 WikiTQ_hybrid 上只有 61% 和 66% 的问题能成功执行，其准确率只按成功执行的问题计算（§3.2，p.6）。

**实验 2（效率，Tables 4、8，pp.7、21）**：Weaver 每题约 5.31–5.87 次 API 调用，Binder 为 50–60 次，H-STAR 8 次，ProTrix 2 次。输入 token 与 H-STAR 相近（GPT-4o 下为 8,568 对 8,836）。

**实验 3（其他分析，pp.7–8）**：大表子集上 Weaver 65.6%，ProTrix 37.5%，H-STAR 35.9%。去掉计划验证使准确率下降 1%。

**内部不一致（阅读者分析）**：Table 5 的步数合计不成立（74+532≠616，59+513≠469），正文称 SQL 步减少 24.8% 也无法由表复算。Table 6 中 GPT-4o-mini 下 Weaver 的 SQL 错误率为 42.5%，高于 ProTrix 的 25.9%，与正文“三种模型下都降低 SQL 错误”的说法不符。

**原文承认的局限**：只支持英文表格，不处理层次表和多表查询，缺少成熟的混合问答 benchmark（Limitations，p.9）。

依据：§3、Tables 2–6、8，Limitations，PDF pp.5–9、21。
