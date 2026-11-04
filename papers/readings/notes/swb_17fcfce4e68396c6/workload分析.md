# workload

**原始语料**（§4.2、附录 A，PDF pp.14、43–44）：5,444 篇文档、694,110 tokens，来自 117 个网站域名。按体裁分为评论 4,196、论坛帖 1,124、博客 62、文章 62（Table A.2）。话题：在家上学、公立与私立学校、推迟入学（redshirting）、学校祈祷、单性别教育、融合教育（mainstreaming）。

**研究 1 数据**：990 篇评论/论坛帖随机子集，3 名标注者，多数投票后 524 篇（53%）为说服性（PDF p.15）。

**研究 2 金标准语料**（Tables 2–3，PDF p.21）：共标注 351 篇，剔除 11 篇后保留 340 篇。按体裁为评论 216、论坛帖 73、博客 46、文章 5；按话题从融合教育 21 篇到公立/私立 134 篇不等。共 84,673 tokens、3,899 句。

**类别分布**（Table 8，PDF p.35）：2,214 句（57%）不含成分；Premise-B 530、Backing-B 220、Claim-B 171、Rebuttal-B 61、Refutation-B 18。Rebuttal 与 Refutation 的 4 个类别合计仅约 3.4%，类别极不平衡。

**划分**（§5，PDF p.33）：三种设置，全数据 10 折交叉验证、每个话题内部 10 折交叉验证、留一话题的跨领域验证。原文没有固定的训练/测试划分。

阅读者分析：图谱中有以 persuasion 命名的派生任务目录（data/ukp-argumentation-derived），与本文研究 1 的说服性判定最接近；本次未逐条核对相关查询的具体内容。

依据：[Computational Linguistics 43(1):125–179, 2017（ACL Anthology J17-1004），55 页](https://aclanthology.org/J17-1004)。
