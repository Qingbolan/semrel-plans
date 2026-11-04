# 具体用例

论文 Figure 1 与附录 E 的例子：问题 “Where did the performer of song I'll Say It graduate from?”（歌曲 I'll Say It 的演唱者毕业于哪里？）。

| 方法 | 看到的信息 | 回答 |
|---|---|---|
| 长上下文 LLM | 整段长上下文，相关句子位于中部 | Hanyang University（错，lost in the middle） |
| Vanilla RAG | 只检到 “演唱者是 Kathy Griffin” 的 chunk，缺少学校信息 | Seoul Arts College（错，关键信息不完整） |
| LongRAG | 抽取器从源段落取得 Griffin 在 Lee Strasberg Theatre and Film Institute 学习戏剧；过滤器保留支持性 chunk | Lee Strasberg Theatre and Film Institute（对） |

（Figure 1，p.1；附录 E，p.16；Tables 24–26，pp.31–33）

流程上，过滤器先读全部 7 个 chunk 生成一条推理线索（“I'll Say It → Griffin → 学校”），再逐个 chunk 判断是否 `<support>`；抽取器则把检到的 chunk 回扩成完整段落，补全同段落内“毕业学校”这句（§4.2–4.3）。

阅读者分析：该例说明 LongRAG 擅长“答案与桥接实体在同一源段落、但被切进不同 chunk”的情况；若第二跳证据所在段落根本没被检索到，回扩也无法补救，这正是 §7 所说的一次性检索依赖。

依据：Figure 1，PDF p.1；§4.2–4.3，pp.4–5；附录 E 与 Tables 24–26，pp.16、31–33；§7，p.9。
