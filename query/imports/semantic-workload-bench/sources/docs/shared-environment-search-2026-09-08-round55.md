# 第55增量：CHEMDNER规范差异与下游gold闭合

合格仍2/10，本轮推进CHEMDNER来源/任务核验，不重复计一个湖。完整原论文和作者仓库已在round54下载；本轮复用原资产，未运行模型。

**规范差异已解释。** 25页包内版有数据选择章节；24页后版删除该章节。以`The focus for defining the chemical entities`开始的标注正文，去页码/空白并归一注册商标字符后，两版全文相同。不是两个不同标注标准。冻结随原数据版即可，不能说25页全是推理规则。

**下游接口已全量核验。** 非空提及文字按文档去重后，准确等于三份官方CDI gold：train15886、dev16095、test13690条。不是假设抽取输出可以聚合，已经按原文件实算集合等价。

发现4条test零长度MULTIPLE标注：23265513/T179:179、23360143/T55:55、23420583/A1519:1519、23454135/A58:58。round54的原文切片等值检查对空串也会通过，不能单独证明跨度有效；本轮明确补充非零检查。未修改源gold。后续可把这些源记录标为构造问题，不能静默给模型一个零长度目标。113个NO CLASS可保留位置提及gold，类型则需独立定义未分类状态；CDI无须强制七类。

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold |
|---|---|---|---|
| 依据化学提及协议建立逐文档索引 | 原25页protocol，含小肽/聚合物/词边界/配位结构等规则 | 原10000标题摘要 | 84355源标注行、45671官方文档-提及文字索引对 |
| PMID22732443具体例 | 小肽与长肽排除边界、化学名与蛋白名规则 | Ro25-6981、synthetic peptide Tat-GluA2(3Y)、AMPA receptors同时出现 | 原gold仅Ro25-6981/IDENTIFIER与AMPA/ABBREVIATION；不把Tat缺标直接判gold错误 |

| 类python的DAG | 实际数值 |
|---|---|
| `mentions=sem_map(title, abstract, protocol)` | 源标注84355，4条零长度需显式处理；未执行模型 |
| `index=set((doc_id,m.surface) for m in mentions if m.surface)` | train15886/dev16095/test13690 |
| `compare(index, official_CDI)` | 三split均集合完全相同，无缺失或额外 |

| 预期关键语义算子直接交给LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 例目标索引Ro25-6981和AMPA；实际输出未知 | 固定提取→非空/切片校验→逐文档去重；同资源检索允许 | 同一目标，无优势预设 | ==查长度与排除标准；当原文缺分子属性时查批准的独立结构资料；检查边界==→清单 | 规范索引→候选识别→属性查证→纳入/跨度判定→验证→去重；未提取冻结 |

该例暴露输入充分性问题：摘要只说synthetic peptide，没有氨基酸数量。独立研究[doi:10.1007/s12035-020-02246-0](https://link.springer.com/article/10.1007/s12035-020-02246-0)给出Tat-GluA2–3Y序列YGRKKRRQRRR-YKEGYNVYG，计20 aa，与原协议排除>15 aa一致。这是外部支持的解释，尚未证明与2012原例试剂身份完全一致；更不能推断全数据都具备必要的公共结构资料。后续要冻结可访问分子属性来源，固定流程和Agent同等可用。

脚本/收据在artifact/evidence/shared-environment-audit-20260908-v55。没有public/private快照、独立确认、模型比较或成本结果。许可仍需核验，不扩张论文许可到摘要。审计脚本是本地研究工具，未运行作者代码；新工程测试0。

辅助原论文已完整下载并pdftotext核实上述序列：20页4400995bytes，SHA256 fd59c31ac7ac9998c9854c8445d193bd9da96a0d62b26427484d33c6935b104c；位于data/shared-environment-audit-20260908-v55/peptide-source.pdf。尚未作为全批公共资源挂载。
