# workload

**数据集**（§3，pp.4–5）：
- **HybridQA**：问题需要同时用 Wikipedia 表与段落（原作者消融：只用表 8.4、只用段落 19.5、两者 44.0）。评测在 dev 集，共 3,466 条（§5.1、§6，pp.6–7）。
- **OTT-QA**：HybridQA 的“去语境化”开放检索版本，需要在大语料（论文 Table 3 注明约 400k 表、5M 段落）上检索表和文本；BlendSQL 使用 Ma et al.（CORE）的 top-4 表检索结果，段落检索与阅读由 BlendSQL 内的 BM25（FTS5）查询完成（Table 3，p.7）。dev 集条数正文未给出。
- **FEVEROUS**：Wikipedia 句子与表格作为证据的事实核查，标签 supports/refutes/not enough info；沿用 Sui et al. 只评测含表格证据的声明，并丢弃 “not enough info” 标签（Table 4 脚注，pp.6–7），条数正文未给出。

**预处理**（§4.1，pp.5–6）：所有结构化与非结构化上下文放入 SQLite；documents 表建 FTS5 BM25 索引；端到端基线在 HybridQA 上因上下文过长，包含全部表格数据并把非结构化内容截断到 400 字符。

**示例与划分**（§4.2，p.6）：从各数据集训练集随机抽约 10 条并人工标注 BlendSQL；HybridQA 与 FEVEROUS 用 12 条，OTT-QA 用 9 条。所有结果报告在 dev 集。

**指标单位**：按题计算的语义 denotation accuracy（Cheng et al. 脚本），会把 “seven” 与 “7” 归一；HybridQA dev 中 101 个金答案含自然语言数字、697 个含阿拉伯数字（§4.3，p.6）。

**与本项目查询的关系**：本 atlas 引用该论文的 18 条查询来自作者仓库 benchmark/ 目录（1966_nba_draft、financials、national-parks、rugby 四个库），论文正文没有描述这些查询；它们不是论文中 HybridQA/OTT-QA/FEVEROUS 的评测题（阅读者核对：论文未提及这四个库）。
