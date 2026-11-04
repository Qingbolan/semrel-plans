# DeonticBench USCIS-AAO：现成共享环境路线 Reject

已下载[原论文](https://arxiv.org/abs/2604.04443)、[完整官方repo](https://github.com/guangyaodou/DeonticBench)和[官方USCIS全量数据](https://huggingface.co/datasets/gydou/DeonticBench)。repo 54 tracked文件，commit `3c168f943880fcbd3a3d717a516500312534273b`；HF revision `805fb0529d7ae295679c5c1730765ec07d2c20ac`。本轮只审核USCIS，不把全套6,232异质任务算同一q。USCIS whole parquet 817,973 bytes已实际解码；各原始AAO PDF、统一历史法源尚未下载，不能称完整原始案件湖已取得。HF数据CC-BY-4.0，其他来源权利不能自动继承。

原论文§2.3、D.1实际读取：来源为2022–2025年真实AAO非先例裁决，从6,483结构有效记录分层筛选242；源Accepted约20.1%，发布人为平衡为121/121。这里不是合成法律案件，但事实摘要经过GPT-5-mini抽取和人工修改；标签来自裁决处置，并非模型虚构gold。Accepted合并直接批准与发回重审，不能叫最终福利/移民申请获批。

## 表1：A–H

| 条件 | 本次证据 | 判断 |
|---|---|---|
| A固定q | 242例question完全相同，问accepted/dismissed | 成立，需保持合并remand的标签语义 |
| B共享E | statutes有221个不同字符串，最大完全相同组4例；为各案Law节选 | 未得到统一事前长E；字符串差异不等于规则实质不同 |
| C20定位 | 本轮读硬集实例与发布字段，完整20案原判/规则闭合0 | 未确认 |
| D静态不足 | 论文有CoT/Prolog比较；没有证明统一E预处理＋固定程序不足 | 未确认；局部给定法规推理不证明探索共享环境 |
| E家族 | 54例节选提及Dhanasar；仅引用计数 | 不是K，也不是54例完整同规则认证 |
| F批量 | 真来源242例、balanced子集；hard28是whole子集 | q总量数百，但同一充分长E批量未建立 |
| G输入充分 | 原Analysis含结论；发布facts为模型抽取后人工复核，论文承认边界与残余可靠性局限 | 不能把无显式最终答案当完整无泄漏证明；原始证据未冻结 |
| H来源 | 原论文、完整repo、全242行已下；非全部原始PDF | 部分闭合 |
| Verdict | 当前发布结构为case-specific法规＋事实，而非已验证共享长E | **Reject现成路线**；保留另行构造可能，不计Strong |

## 表2：Query × 具体文件

| Query | 数据湖数据1 | 数据湖数据2 | 私有gold |
|---|---|---|---|
| 固定q：本案上诉处置accepted/dismissed | `uscis-whole.parquet`：case_number/text/question，242行 | 同行statutes，221种文本；不是已取得统一法规库 | label：121 Accepted/121 Dismissed |
| q派生：是否最终获批 | 同上 | 同上 | 不成立：Accepted混入remand，现有label不足 |

字段reference_prolog包含实例事实与求解程序，属于参考答案资产，不能作为公开环境工具。hard与whole重叠，不能当独立训练测试。

真实已读样例：repo `data/uscis-aao/hard.json` 首行 `uscis_e2f62d25`，case_number25674629。申请人为泌尿肿瘤学医生研究者，主张EB-2 national-interest waiver；事实摘要提到临床研究、论文、审稿和专家推荐。法节选包含EB-2基础资格及Dhanasar三条件；源label Accepted。该标签本身无法区分最终批准/发回。引用的学术资料原件未提供，本轮不独立重判其贡献大小。

## 表3：DAG

| 类Python DAG | 具体数据 | 普通/语义 |
|---|---|---|
| `rows=scan(whole)` | 242条，121/121 | 普通 |
| `facts=sem_map(text)` | 医生研究者的资格、研究计划、影响材料 | 语义；不读取label/reference_prolog |
| `elements=sem_map(facts, statutes)` | 例中EB-2资格与Dhanasar条件 | 核心语义比较；statutes目前为逐案节选 |
| `disposition=sem_map(elements, procedural_facts)` | Accepted/Dismissed，不能忽略remand | 语义法律适用；本轮未执行 |
| `score(private_label, disposition)` | 独立保留源标签 | 普通评分，未执行 |

## 表4：四路推演，均无实测

| 臂 | 预期结果边界 | 过程 | operator结构 |
|---|---|---|---|
| LOTUS仅任务表 | gold目标Accepted；实际未知，可能靠预训练法律记忆 | 单次固定语义判断 | `facts→disposition` |
| LOTUS完整E | 统一完整E尚未取得；不能把短逐案节选称完整长E | 当前可测固定事实抽取＋所给法规判断；新统一E需另行冻结 | `extract→apply_rules→procedural_outcome` |
| 逐记录Agent | 同一目标，未证更好 | ==定位EB-2基础资格与Dhanasar条件==→核证据充分性→==辨别remand与最终批准==→标签 | 相关规则检索和固定要件判定可能足够 |
| 批Agent | 同一标签语义 | ==先冻结统一法源版本==→==按早期事实识别法律适用家族==→复用规则→逐例证据判断 | 仅假设，当前发布数据不证明共享环境探索 |

ρE为法源版本/索引，ρP为事实抽取和输出契约，ρG可能是签证类别/豁免等规则组，ρR为个案证明强度与程序事实。比例/K均未知；54次Dhanasar引用不能替代语义路由与轨迹。最强未排除基线是固定要件抽取＋给定法条适用。资料节选不足也不能算静态能力不足。

原件哈希与复算：[source.json](../artifact/evidence/shared-environment-strict-deonticbench/source.json)。本轮在专用audit-venv安装pyarrow21.0.0解码parquet，不改项目依赖；无模型运行、作者代码执行、原始PDF20例审查或新实验split。十问中的依据充分性、静态不足、K和区别于普通RAG仍不成立/未知，故不强行升级。


## 输出与信息不足边界补充

源q输出Accepted/Dismissed，Accepted含remand；不存在已核实第三类UNKNOWN gold。运行失败可记ABSTAIN，不把资料不足映射Dismissed。若评估证据不足或最终获批，应另建任务及独立标签，不能沿用当前二分类gold。
