# usecase

原文 Figure 7 与 §3.2（PDF pp.13–14）给出的具体用例：一段关于雨天的文本中，“but” 在主树中找不到对应关系（主树把 [23–27] 分析为 EVALUATION），于是作为 orphan DM 授权一条从 [27] 指向 [23–24] 的次级 CONCESSION 边；另一处“Arrogant people … know that they have no friends”，主树把 [141] 作为 [140] 的 ELABORATION，但 “know … that” 的转述认知结构授权一条次级 attribution-positive 边，并带有句法信号（know、that）与语义信号（归属来源 “Arrogant people”）。

§6 的应用示例（PDF pp.36–40）：对某政治人物的全部演讲做 eRST 解析并抽取所有 CONCESSION 关系供分析；利用 “if” 这一 DM 与 EXPLANATION-JUSTIFY 组合检索非条件性解释（“I have oregano if you want any”，Figure 12）；按信号过滤只保留显式标示的关系；统计 EVALUATION 的词汇信号（Table 11：good、very、feel…）。ANNIS 查询示例 (12)(13)（PDF pp.27–28）展示可组合 relname、POS 与 signal_type 的结构化检索。

阅读者分析：若项目把它用于“从文档中找出带证据的因果/让步关系”，应保留“主树 vs 次级边”的区别以及信号锚定 token，否则会漏掉 10% 以上的 result/concession 实例；自动解析下主树错误会级联放大，生产使用需谨慎。

依据：[Computational Linguistics 51(1), 2025，ACL Anthology 2025.cl-1.3，50 页](https://aclanthology.org/2025.cl-1.3)，§3.2、§4.3、§6，PDF pp.13–14、27–28、36–40。
