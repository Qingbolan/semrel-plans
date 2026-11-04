# 评测与边界

指标（§VIII-A，PDF p.15）：EX（执行结果集一致；原文指出语义不同的 SQL 可能碰巧得到相同结果，产生假阳性/假阴性风险）、SM（字符串完全匹配）、CM（组件匹配）、EM（全部组件匹配）、VES（正确 SQL 相对于标准 SQL 的执行效率）、QVT（同一 SQL 的多种 NL 变体下的鲁棒性）。

工具（§VIII-B，PDF pp.15–16）：MT-TEQL 用 4 类 NL 变换和 8 类 schema 变换做变形测试；NL2SQL360 包括 Dataset、Model Zoo、Metrics、Dataset Filter、Evaluator、Analysis 六个组件，可按 SQL 特征等场景筛选子集评测。

错误分析（§VIII-C，PDF p.16）：第一层定位错误发生的 SQL 子句，第二层判断成因；用于 DIN-SQL 在 Spider 上的错误时，Others 类占 1.8%。

成本（Table III，PDF p.18，Spider）：RESDSQL 每条 SQL 1.91 s；ZeroNet 377 API tokens、3.72 s；DIN-SQL 3,579 tokens、10.34 s。

局限与开放问题（§X，PDF pp.17–18）：现有方法基于单一固定数据库，难以跨库检索和聚合；token 消耗高；缺乏可解释性与调试；对新领域适应差。作者提出 open-domain Text-to-SQL（数据库检索、异构 schema、答案聚合等 6 项挑战）、低成本方法（LLM+PLM 组合、EllieSQL 式路由）、可信性（解释、调试器、交互工具）和自适应训练数据合成。

阅读者分析：本综述没有对 LLM 方法做统一的重新评测，各方法在基准上的分数需查阅原论文。
