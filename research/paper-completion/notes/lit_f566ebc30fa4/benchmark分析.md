# 评测与边界

**基线**：微调类 SENSE、CodeS、Distillery、XiYanSQL-QwenCoder、BASE-SQL、OmniSQL、CSC-SQL、CHASE-SQL、XiYan-SQL；提示类 DIN-SQL、DAIL-SQL、SuperSQL、RSL-SQL、CHESS、OpenSearch-SQL v2、Alpha-SQL；Spider 2.0 上另有 Spider-Agent、ReFoRCE、LinkAlign（§4.1，p.14）。

**指标**：EX（BIRD/Spider 严格结果相等；Spider 2.0 用官方宽松比较）、Upper-bound EX（候选中存在正确 SQL 的比例）、表/列召回、token 与延迟（p.14）。

**主要结果**：

| 设置 | 结果 |
|---|---|
| BIRD-Dev，Qwen3-Coder-30B-A3B | 73.5%（XiYan-SQL 73.3%、CHASE-SQL 73.0%、Alpha-SQL 69.7%） |
| Gemma3-27B / Qwen2.5-Coder-32B | 71.1% / 70.9% |
| BIRD-Test（官方） | 75.07%；换 Gemini-3-Pro、N=1 为 76.58%（榜单第 5） |
| Spider-Test | 89.8%（与 OmniSQL 持平） |
| Spider 2.0 Snow / Lite（DeepSeek-R1） | 50.5% / 38.2%（ReFoRCE 38.0/29.6，LinkAlign Lite 33.1） |
| 同骨干对比（Gemma3-27B） | 较 CoT 基线 +16.9 点，CHESS +11.9、Alpha-SQL +14.4 |
| 模式链接 | 表/列召回 98.1/95.4%，上下文 5,486.2→627.4 token |
| N-version | 合并 EX 71.7%，UB-EX 81.1%（最佳单生成器 78.5%） |
| 消融 | 去 ICL 生成 −2.5，去值检索 −2.1，去检查器 −2.1，去置信选择 −0.8 |
| 效率 | 17.8 s/题；CHESS 284.4 s、Alpha-SQL 377.1 s |

来源：Tables 3–11，pp.15–21。置信度与 EX 的 Pearson 相关 0.954（Fig.6）；θ_conf∈[0.4,1.0] 时 EX 均高于 73.0%（Fig.7）。

**局限**（RQ10，pp.22–23）：人工检查 BIRD-Dev 上 407 个失败；模式类错误最多（126），主要是列选择与 join 路径；约 30%（122 个）属于题目歧义或金标 SQL 错误。

阅读者分析：基线数字多取自原论文的不同骨干（GPT-4o、Gemini），只有 Table 5 是同骨干比较；Table 11 中 CHESS（67.9）、Alpha-SQL（71.2）的 EX 与 Table 3 不同，应是配置/骨干不同，论文未逐项说明。所有结果均为单次报告，无方差。

依据：[arXiv v3，PACMMOD Article 158，28 页](https://arxiv.org/abs/2510.17586)，§4，pp.14–23。
