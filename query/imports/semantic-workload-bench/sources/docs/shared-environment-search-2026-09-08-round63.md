# 第63增量：NLM-Chem完整发布包与规范，历史MeSH环境待补齐

合格保持3/10。新增核查来源，不列为已满足全部条件的数据湖。它有真实全文、专家标注和明确受环境约束的归一化任务，但完整历史MeSH/SCR尚未冻结，公开输入构造和规范示例排除尚未完成。

[原论文](https://www.nature.com/articles/s41597-021-00875-1)已下载12页1229703bytes，SHA256 bb14a5a40d677dc8d87d36c007ddd2967876a49d625516d8b9b0efe05d4b8170。[作者Dryad完整发布](https://datadryad.org/dataset/doi:10.5061/dryad.3tx95x6dz)包含两个数据文件；其下载403，改从论文链接的[NIH官方目录](https://ftp.ncbi.nlm.nih.gov/pub/lu/NLMChem/)取得全部两个文件，未运行作者脚本：

- corpus.zip：2533277bytes，164条目CRC通过，SHA256 32f8a1633faacab749b41bf493380cd39bdd90215f811cb940db374502e08490。
- guidelines.docx：42154bytes，SHA256 d84f6cb25692043381c6a67614a9c0a64138d37ba130b4871ccd9f8065dd352c。按段落提取3043空白分词；Word缓存Pages=12，**未渲染验证实际分页**。

取得的是完整作者数据发布包，非681MB后续TaggerNormalizer系统包；未声称下载或复现全部模型软件。NIH两文件大小与Dryad登记一致，Dryad字节未取得，因此不声称跨镜像哈希相等。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 依NLM-Chem规范从每篇全文抽取化学实体并归一化至MeSH/SCR，汇总可检索的文档—化学概念索引 | 3043词规范；按最具体概念、类回退、多概念组合、药用蛋白例外等定义目标 | 历史MeSH/SCR词表及化学祖先树，**尚未冻结下载**；不可用当前词表冒充标注时期版本 | 150真实全文BioC，80train/20dev/50test；公开侧须仅保留必要文本与结构 | 38339 Chemical、1796 OTHER、78 NonStandardRef，共40213原标注；不能把这些当40213独立论文 |
| PMC5628336，测试集已查看开发例 | 蛋白一般排除，作为药物且有药名者可纳入；规范本身提及rituximab，不能当独立确认例 | 目标MeSH:D000069283，须由公开词表检索而非读当前gold | 文中把Rituximab列为immunotherapeutic并描述组合治疗；公开段落包含这些用法 | 两处Chemical：Rituximab offset5918 length9、rituximab offset6066 length9，均同一ID |

| 类python的DAG | 具体数值/当前状态 |
|---|---|
| `docs=scan(public_fulltext)` | 源150篇、10310段、4861074字符；尚未生成public-only快照 |
| `mentions=sem_map(doc,E.rules, E.mesh)` | 原train22254/dev5548/test12411条标注，包含三种类型；不是已执行预测 |
| `chemical=filter(mentions,type=='Chemical')` | 原Chemical38339；2061种完整identifier字段值，包含组合值与'-'，不是2061唯一原子MeSH概念 |
| `concepts=normalize_and_expand(chemical)` | '-'340条表示未分配标识，不等于执行失败；组合分隔含不同语义，不能未验证就无差别拆分 |
| `index=groupby(document,concept).collect(spans)` | 可评价实体跨度/归一化及文档索引；原始标注不是现实世界化学作用/安全性gold |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 例中两处rituximab应输出Chemical及D000069283；实际能否正确未知 | 完整规范+全文的固定sem_map；同资源MeSH候选检索、祖先树检查和固定上下文复核均应允许 | 相同目标，不预设准确率更高 | ==检查药用蛋白例外；从全文确认治疗用法；查冻结MeSH候选和祖先；核跨度==→类型/ID/证据 | 化学候选发现→语境排除/药用例外→最具体概念查找→无精确项时规范化类回退→组合表达解析→跨度校验→文档索引；只是预期，未从轨迹提取 |

全量字符审计发现PMC5600090/C372一处错误：标注water的段内起点48长度5切出thin-space+wate。保留原始数据，不自动平移或默默删除。所有150PMID均读出，与CHEMDNER已审查10000摘要的PMID交集0；原split无PMCID重叠。不证明与GENIA/CRAFT或训练数据无重叠，也未审计近重复。

共享环境的实质依赖是规范明确要求最具体MeSH/SCR归一化、祖先树资格和无精确条目的类回退。它比无条件NER更具体；但3043词规范本身没有满足30–100页示例，不能拿150篇长全文代替长E。需要核验完整当年词表及可用化学信息是否足以解释gold；现代词表新增条目会改变“最具体项/类回退”答案。原论文38339 Chemical与本次相符，文献报告的2064 MeSH assignments与本次2061 Chemical字段值仍须核对定义/版本。

文献称十位专业索引员、双人标注、多轮协作达成共识；没有自行重做专家复核。公开PMC文本许可逐文档保留，但本轮未完成整体再分发许可审计。新工程测试0，无模型/作者程序执行，无prompt/种子/推理预算/并发缓存，无确认split、学习轨迹、收益或成本测量。脚本/收据位于artifact/evidence/shared-environment-audit-20260908-v63，下载位于data同名v63。下一增量优先历史MeSH与原始规范版本及gold映射，不先放宽合格条件。
