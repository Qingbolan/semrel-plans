# 具体用例

论文 Fig.4（BIRD-Dev QID 142）：问题“Which accounts placed orders for ‘household payment’ in Pisek?”，evidence 说明 k_symbol = 'SIPO' 表示 household payment。

直接链接与反向链接找到了 account、district 和 order.k_symbol，却漏掉真正需要的 trans.k_symbol；值链接通过把“household payment/SIPO”匹配到 trans 表中的值，召回该列，最终 SQL 为 trans JOIN account JOIN district 并以 T1.k_symbol 过滤（p.17）。

这说明一个典型场景：列名含义模糊、同名列分布在多表时，靠数据值本身来确定该用哪张表的列。流程中随后由 N-version 生成多条候选，经检查器链修复（例如加 GROUP BY、移除 SELECT *、空结果触发重新审视约束），再执行聚类投票。

阅读者分析：若项目把它用作自然语言到结构化查询的入口，需预先对文本列建值索引，并接受每题平均约 17.8 s、约 46K token（输入 23.21K + 输出 23.16K）的成本（Table 11）；这些数字是在 8×A100 本地部署 Qwen3-Coder-30B-A3B 下测得，不能直接外推到其他部署。

依据：[arXiv v3，PACMMOD Article 158，28 页](https://arxiv.org/abs/2510.17586)，Fig.4，p.17；Table 11，p.21；§4.1，p.15。
