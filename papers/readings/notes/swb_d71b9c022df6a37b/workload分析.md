# workload

**语料**（§4，PDF pp.17–18，Table 2）：GUM v9，213 篇、12 个语体（访谈、新闻、旅行指南、how-to、学术、传记、小说、Reddit、对话、演讲、vlog、教材），共 203,879 token、26,352 EDU；作者注明发表时已扩展到 GUM v10（16 语体）+ GENTLE 测试集（8 语体），合计 246K token、24 语体、约 32K EDU，但本文统计与实验基于 v9。另对 RST-DT 测试集 38 篇（约 21K token）补标 DM、orphan 和次级边，不含非 DM 信号，且因版权仅发布标注不发布文本。

**规模统计**（Table 6，PDF p.24）：GUM 共 29,950 个关系、6,025 个 DM、895 个 orphan、1,008 条次级边（3.37%）；RST-DT 测试 2,580 关系、87 条次级边（3.37%）。语体差异：vlog 次级边 6.56% 最高，how-to 1.95% 最低。全部 GUM 关系中约 63% 有任何信号（PDF p.25）。人工核实的 lexical chain 1,280 个，覆盖 2,825 token（PDF p.22）。

**解析实验划分**（§5.3，PDF pp.33–34）：GUM v9 官方训练 165 篇、开发 24 篇（早停）、测试 24 篇；次级边训练样本不足 1K。

**一致性子集**：DM 识别/关联在 36 篇 GUM（32K token）与 RST-DT 38 篇上双标；次级边一致性先在 GUM dev 24 篇、后在另 12 篇上测；非 DM 信号在 12 篇测试文档人工校正、其中 4 篇双标（PDF pp.19–23）。

与图谱查询的关系：图谱中引用本文的派生任务“重建 GUM/eRST 话语树与次级关系”要求从文档 token 输出 EDU 区间、主树父边与次级边并抽取 attribution-positive、explanation-evidence、contingency-condition 等标签；这些标签确实属于本文 GUM 关系集（Table 10），但给定 EDU 与否、评分方式均为项目派生设定，并非本文直接评测（阅读者分析）。

依据：[Computational Linguistics 51(1), 2025，ACL Anthology 2025.cl-1.3，50 页](https://aclanthology.org/2025.cl-1.3)，§4–5，Tables 2、6、10，PDF pp.17–25、33–37。
