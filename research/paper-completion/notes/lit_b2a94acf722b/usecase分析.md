# 具体用例

Figure 1 的例子：表中三名球员的 FA Cup 与 FL Trophy 次数分别为 Mark Phillips（1,0）、Liam Dickinson（1,1）、Blair Sturrock（0,1），问题是“哪位球员有一次 FA Cup 和一次 FL Trophy？”。初始链第 1 步错选了 Row 3，得到错误答案 Blair Sturrock。

Judge 判断推理状态为 Incorrect，并沿模板树 ROOT → Sub-table Error → Row Error 路由；Critic 指出第 1 步错在 Row 3 的 FA Cup 为 0，应选 Row 2；Refiner 从第 1 步重写，得到 Liam Dickinson。修正成功后，Curator 把这次经验提炼为新模板，必要时扩展树（如新增 Column Error 或 Final Query Error 分支）。

阅读者分析：这个例子的错误出现在“选行”这一筛选步骤，与语义过滤算子误判的结构相似；但论文只在单表问答上验证，未涉及多表或大规模表。

依据：[ACL 2025，pp.17432–17451，20 页](https://aclanthology.org/2025.acl-long.853/)，Figure 1、§3.2–3.4，PDF pp.2–5。
