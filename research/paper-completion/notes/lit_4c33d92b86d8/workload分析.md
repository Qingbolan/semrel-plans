# workload

**基准**：TAG（Biswal et al.）在 BIRD 基础上改写问题，使其需要世界知识或文本语义推理；覆盖 5 个 BIRD 领域（California Schools、Debit Card Specializing、Formula One、Codebase Community、European Football），每库最多 13 个关系，最大库 597.8 MB（§6.1.1，p.9）。TAG 原有 60 题（match-based、comparison、ranking 三类，有专家标注答案）+ 20 题聚合（对文本列做总结）。

**TAG+ 扩展**（p.9）：(1) 请三位数据库专家为每题写出分析型 ground-truth 查询，以便直接评测生成的查询；(2) 新增四种模式各 10 题，共 40 题：语义连接、语义分类、信息抽取、计算推理，并加入多跳、子查询和多次 LLM 调用。合计 80+40=120 题（§6.3.3 明确“Of the 120 benchmark queries”，p.11）。Table 3 的准确率为 120 题上的百分比（如 89.2% ≈ 107/120，阅读者换算）。

**子工作负载**：查询优化评测只针对被优化改写的 33 个计划（p.11）；smart-batching 评测为 10 个连接查询（Join1–Join10，Fig. 11，pp.11–12），其中 Join10 超过 1,000 次成对比较。

**数据规模单位**：论文给出的是库/关系数和库文件大小，没有按题报告输入行数；个别例子给出行数（Fig. 6 例中连接后 73→42 行；湾区县判断 57 次调用；F1 例 7×32 键对）。

**评测协议**：结果与 ground truth 相同视为正确；主观题（总结、排序“有前途的学校”）由 GPT-5 作为 LLM judge 判断（p.10）。没有训练/测试划分——方法为上下文学习，示例为 5 个人工挑选的问题-查询对（p.6），论文未说明这 5 个示例是否与 120 题重叠。

**与本项目查询的关系**：本 atlas 引用该论文的 40 条查询（sema-sql/tag-plus/1001–1040）取自作者仓库的 tag_plus_queries.csv，数量与论文所述新增 40 题一致（阅读者推断，逐题对应未核对）。
