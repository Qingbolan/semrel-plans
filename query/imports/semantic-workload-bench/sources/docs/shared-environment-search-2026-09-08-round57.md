# 第57增量：CRAFT新版协议和示例隔离规模

本轮复用round56已完整下载并验证的原论文/作者仓库/47页指南，合格仍2/10。新增证据是新版边界规范和公开PMID排除后的实际规模，不是模型或独立确认结果。

作者CHANGES明确v3更新本体、扩展类和跨度规范；concept-annotation/README.md明确两项变化：一组指定词缀与词根之间可形成跨度边界；常规/斜体/上下标之间的格式变化也可形成边界。例如antichromatin的chromatin可标，BRAF与上标V600E可分界。精确原文保存于artifact/evidence/shared-environment-audit-20260908-v57/protocol-update.txt。因此应冻结47页原指南+本commit更新说明+本体/扩展规范，不能只用旧PDF。

仓库确实有对应文章的sections-and-typography人工标注，也有原NXML。若给定人工排版结构，必须明确是annotation-given上游；另一条路线是从公开NXML解析并核对偏移。不能只给扁平纯文本后把缺格式导致的错误当Agent优势。当前未构造这个适配。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 按当前CRAFT标准建立全文CHEBI概念索引 | 47页规范+指定commit跨度/扩展更新 | 冻结本体及公开扩展规则 | 排除指南明确引用文档后的51篇全文；必要字体结构仍需构造 | 8831提及，含30个不连续提及 |
| 开发例PMID14723793：Peptides linked ... from Acdp1 N- and C-terminals ... | 协调短语可共享成分，不连续跨度规则；最近概念匹配 | CHEBI_SO_EXT:N_terminus_or_N_terminal_region | 原文[19619:19621]为N-，[19628:19637]为terminals | 两段共同构成一个N末端提及，不把两段之间的and C-也吞入 |
| 同文另一处N- (肽序列) and C- (肽序列) terminuses | 语义成分选择与跨度组合 | N/C末端扩展概念 | N-[11000:11002]、C-[11034:11036]、共享terminuses[11054:11064] | 两个不同提及共享同一尾段，不能只输出平坦单跨度BIO标签 |

| 类python的DAG | 实际数值 |
|---|---|
| `docs=exclude_ids(cited_in_public_manual)` | 97减46=51篇，选择不依赖当前gold |
| `attach(public_typography_or_nxml)` | 原资源存在，尚未构造/验证公开格式输入 |
| `mentions=sem_map(docs, frozen_E)` | 原train剩32篇6139提及、dev4篇528、test15篇2164；总8831 |
| `index=groupby(doc_id).collect(concept_id, spans)` | 30不连续提及；属于51个源实体，不能说8831独立case |

| 预期关键语义算子直接交给LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| N-与共享terminals组成一条带两跨度的记录；模型未运行 | 固定规范检索→整段语义映射→跨度列表验证→集合聚合；同样允许本体检索和排版输入 | 同一目标，无优势假设 | ==查协调短语规则；定位共享尾段；查询末端概念定义；核对两个跨度与原文==→结构化记录 | 公开结构读取→协议索引→候选概念→跨度组合→扩展语义转换→输出检查；未学习或冻结 |

[作者当前README](https://github.com/lhunter-lab/CRAFT/blob/2abe82b8bb8089448b84937d5f61d8c218011322/concept-annotation/README.md)提供上述新版规则，原下载位置及哈希见round56。示例排除仅按指南明确PMID，未做全文近重复、论文示例与训练污染全审计；当前检查样例成为开发暴露。51文档的独立性和规模不足以直接支持大批量确认主张。所有多模块仍算同一来源湖。无模型/作者代码运行/工程测试，只有源数据审计；公共快照、执行、资源增益和成本未完成。
