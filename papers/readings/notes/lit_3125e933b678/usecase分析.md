# 具体用例

论文的运行示例是 CMT ↔ ConfOf 会议本体对齐，目标是为源实体 `http://cmt#ProgramCommitteeChair` 在 ConfOf 中找等价实体（§4.2，p.5）。

1. **检索**：元数据检索器判定它是源侧的 Class。句法检索器输出 "program committee chair"。词汇检索器以上下文 "conference" 提问，得到 LLM 生成的释义。语义检索器把 "ProgramCommitteeChair rdfs:subClassOf ProgramCommitteeMember" 口语化。实体元数据写入关系表 `ontology_matching`，三类文本嵌入后写入三张 vector(1536) 表（Table 2，p.6）。
2. **匹配**：在三张表中以相似度 ≥0.90、top_k=3 检索同类型、对侧实体。词汇表命中 Chair_PC；语义表命中 Member_PC、Scholar、Author；句法表没有命中。RRF 融合后，Chair_PC 与 Member_PC 并列 1.0。验证器对 Chair_PC 回答 yes，对 Member_PC 回答 no（理由是主席不等于普通成员），因此输出 `http://confOf#Chair_PC`（Table 3，p.7）。
3. **合并**：再从 Chair_PC 反向检索；只有反向的最佳匹配也是 ProgramCommitteeChair，这一对才会被接受（§4.2.2，p.7）。

这个例子展示了检索结果是相似度与元数据共同过滤的 SQL 查询，LLM 只负责生成释义和最终的是/否判断。若把它作为语义连接或实体匹配算子的参考，可沿用"嵌入阻断 + LLM 验证 + 双向一致"三段式（阅读者分析）。

依据：§4.2，Tables 2–3，pp.5–7。
