# 具体用例

Fig.2（p.3）的例子：问题 “What's the rank of Bob in the football match?”，schema 含 players 与 matches 表。搜索路径为：
1. 列值识别（a1）：推理出需要过滤 player.name='Bob' 与 match.match_type='football'；
2. 列函数识别（a2）：判断不需要函数；
3. SQL 生成（a3）：生成 `SELECT T1.rank FROM players AS T1 JOIN matches AS T2 ON T1.id = T2.player_id WHERE T1.name = 'Bob' AND T2.match_type = 'football';`
4. 终止（a4）。

§4.1（p.5）另举两例说明动作动机：“How many people were born in 2024?” 需要 STRFTIME('%Y', people.date_of_birth)='2024' 与 COUNT 组合（列函数识别）；用户说 “America” 而库中存 “United States” 时，需要值检索（§4.3，p.6）。

阅读者分析：对本项目而言，这是标准结构化 NL2SQL 用例，答案可通过执行比对判定；若与语义算子查询对照，可作为“纯关系侧”的参照，但原文不涉及 LLM 在行级的语义判断。

依据：[arXiv:2502.17248v2（ICML 2025，PMLR 267），21 页](https://arxiv.org/abs/2502.17248)。
