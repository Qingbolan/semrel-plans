# 第三十增量：PANORAMA 专利审查来源、长规则及准予标签核验

**新候选尚未计入，累计1/10。** 已取得原论文、完整作者仓库、全部8,143条结构化源记录及完整NOC4PC测试分片。真实审查结果可以追溯，但发现发布ALLOW标签把撤出本次审查的权利要求也视为准予；需要修复源构造而非直接使用现成三分类gold。

## 实际下载与核验

| 来源 | 本次下载与验证 |
|---|---|
| [NeurIPS2025原论文及附录](https://papers.neurips.cc/paper_files/paper/2025/file/4aab82c8d6b77c0b6b010145c1bfcdd3-Paper-Datasets_and_Benchmarks_Track.pdf) | 52页、4,055,875 bytes，已提取正文 |
| [完整作者仓库](https://github.com/LGAI-Research/PANORAMA) | commit `b4b84287128e9410f04abf108cb1f17196b2277a`，100个blob逐项Git SHA1核验通过，ZIP CRC通过并完整解压；未执行作者程序 |
| [作者数据](https://huggingface.co/datasets/LG-AI-Research/PANORAMA) | revision `5c40de5fb1de842d3a44ec4b9f5bb9c44d47a77d`；panorama.parquet完整167,031,631 bytes，NOC4PC/test.parquet完整13,402,692 bytes |
| [官方MPEP第2100章，Rev07.2022](https://www.uspto.gov/web/offices/pac/mpep/old/e9r07-2022/mpep-2100.pdf) | 524页、5,972,254 bytes，含专利性规则；此版本2023年2月出版，不能自动套用于全部2015–2024审查 |

未下载18.2GB整个HF湖，未声称完整专利说明书/图纸全部就绪。论文旧DxD-Lab基准链接目前API只列README，转而使用论文当前指向的LG作者数据，不使用第三方重打包。仓库名称PI4PC为Patentability Identification，最终论文为Paragraph Identification；本轮明确使用NOC4PC的实际schema。作者声明数据和代码CC-BY-NC-4.0，上游专利材料的具体再发布边界需另核。

下载收据及SHA256在`artifact/evidence/shared-environment-audit-20260908-v30/downloads.json`与`mpep-receipt.json`，原文件在data同名目录。脚本`audit_data.py`复用第2轮隔离Python/pyarrow，不改项目依赖。

## 实测结构及失败实例

- 原始表8,143行、8,143唯一申请。字段含initialClaims、finalClaims、CTNFBodyText、NOABodyText、parsed_CTNF、申请日期、firstInventorToFileIndicator等。**最终claims、NOA及CTNF分析不是预测输入**。
- 测试2,884条、164申请，无重复(application,claim)键，2,884均可连接原始申请。标签834个102、1,453个103、597个ALLOW；58条无prior art列表，455条无任何prior-art paragraphs，不自动等于这455条均无证据，仍可能有标题/摘要/claims。
- 论文§2.2.2说明GPT-4o解析真实CTNF，专家验证为抽样100申请、多评审；不能将全部解析字段称为逐项人工gold。
- 作者转换器`panorama/convert2bench_noc4pc.py`从`isReject=false`设ALLOW，并写统一理由。实测597条ALLOW理由完全相同，**不是597份真实专家准予解释**。
- 按文件顺序第一个ALLOW：申请15886404、claim10（便携腹腔镜的充气器置于外壳）。源CTNF开头明确该claim因未选定species F而withdrawn；结尾明确allowed清单为1–2、4–9、11、14，不含10。源解析却给claim10 `isReject=false,reasons=[]`，因此基准标ALLOW。该例不是模型推理错误，是构造把程序状态和实体结论合并。不能据一个例子估计全量错误率，也不能无证据否定全部原始湖。
- 本例filingDate=2018-02-01，但firstInventorToFileIndicator=N，CTNF明示pre-AIA。**按申请年直接选择AIA规则也不可靠**，需要有效申请及延续关系/源明示状态。CTNF所载2020程序记录也不能直接套本次2023出版手册。
- 转换器从审查员引用的段落编号过滤`prior_art_specifications.paragraphs`。所以现成NOC4PC是审查证据片段给定的任务，不能称Agent自行探索全部对比专利；公平比较须明确annotation-given条件，或另建完整公开说明书/图纸输入。

## 用户要求三表（候选构造审计，不列入合格湖）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 按固定版本审查规范，逐项判断权利要求应因§102/§103驳回还是可准予 | 已下载524页MPEP2100；实际适用版本需按审查时点锁定 | 2,884项/164申请的申请标题、摘要、初始claims | 对比专利及审查员预选段落；完整说明书/图纸尚未全取 | 发布834/1453/597三分类；需从原CTNF核验程序状态，不能直接作有效实体gold |
| 15886404 claim10：充气器位于腹腔镜外壳内 | 此案pre-AIA且有restriction/election程序；2100之外可能需800章 | 初始claim10依赖claim1，需要保留依赖链 | 不读当前CTNF分析或NOA作为预测输入 | 发布ALLOW，但真实本轮withdrawn；应保留WITHDRAWN程序状态，不当成False或准予 |
| 同申请claim18：腹腔镜组合充气器 | §103组合与动机规则 | 原申请claim18及依赖/上下文 | Schultz便携腹腔镜＋Sano充气器对比文献，图文证据需要完整 | 源CTNF给§103并解释为保证视野和操作空间而组合；本轮未作独立专利专家重审 |

| 类python的DAG | 具体数值 | 状态 |
|---|---|---|
| `scan(test).join(source,on=application)` | 2,884/2,884连接，164源申请 | 构造侧连接，不把source全列挂载到模型 |
| `resolve(exam_date, aia_status, claim_version, proceeding_status)` | 明确发现一个withdrawn→ALLOW错误 | 未完成全量，不能只删除已曝光例后宣称gold干净 |
| `sem_map(patentability, frozen_MPEP, initial_claims, prior_art)` | 待修复任务状态及规范版本 | 缺图/说明书与专家选段条件须披露 |
| `sem_filter(decision==ALLOW).project(application,claim).count()` | 发布参考597；有效准予数未知 | 不能用597评价正确合规数量 |
| `evaluate(private_source_verified_decisions)` | 未运行模型/评分 | 原始CTNF可支撑修复，但本轮尚未构造完成 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| claim18参考§103，实际未运行；claim10在当前实体三分类下无有效gold | 固定读取权利要求依赖、按相同规范解释特征、建立prior-art特征对应、检查单文献/组合及动机；共享规范编译和文献缓存 | 相同目标，不能预言更准；不可从提供的特征信息凭空知道后续withdrawn状态 | ==核对合法公开的申请版本与程序状态==→==定位§102/§103及适用AIA分支==→==核对全部claim限制与图文证据==→输出决定和证据；缺失可ABSTAIN | `PatentabilityOperator(E_version, aia_status, claim_dependency_graph, permitted_prior_art, anticipation_test, obviousness_test, evidence_gaps)`；程序状态应在冻结输入/任务边界处理，不学习“未驳回=准予” |

当前最有价值的下一步是对原始CTNF的allowed/withdrawn/objected/rejected状态做可追溯构造，并核对claim版本和审查日期，再决定是否下载完整对比专利包。所有专家分析和本轮开发例均私有诊断；不用于提取/确认集调参。没有模型调用、没有实验收益结论、工程测试新增0。

后续澄清：[第31轮](shared-environment-search-2026-09-08-round31.md)核对原论文提示，ALLOW只表示相对于给定对比文献的新颖性/非显而易见性，不是整体专利准予。§112驳回或形式异议不能单独证明ALLOW错误；withdrawn缺相应实体判断。第31轮另查得7项发布ALLOW与源明确§102/103语句冲突，不能据此估计全量错误率。
