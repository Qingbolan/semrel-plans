# 增量164：MedProcNER三任务，原文/评分源码与镜像核验

仍8/15；本轮为待核验来源，不计合格。上一163为实质排除证据。本轮SHAC/PedSHAC先做可用性筛选，PedSHAC仓库README仍声明等待IRB/去标识后发布，未将病历算作可取得。转向MedProcNER真实公开病例报告。

## 已取得与未取得

[原始任务论文](https://ceur-ws.org/Vol-3497/paper-002.pdf)已下载1,837,004 bytes，SHA256 `15d56741c492d7ca6c4dd9bfd3cb4f686ad6cd00adf011b6ad45380123f57608`。完整[官方评分仓库](https://github.com/TeMU-BSC/medprocner_evaluation_library)commit `fa78d6df6e87d3c2a54b916edbcd1f865c571389`，10个tracked文件含6份toy TSV。原件data/shared-environment-audit-20260908-v164；收据与脚本artifact/evidence/shared-environment-audit-20260908-v164。

[官方规范页](https://temu.bsc.es/medprocner/annotation-guidelines/)说明30多页规范，Zenodo7817667文件和7817745 API各22秒读取超时；没有取得PDF，不将网页的页数说成本地实测。原始最新数据8224056也未下载。论文说明1000病例、16678句、350764tokens、14684操作mention（7179种文本），原train/test750/250；当时normalization训练只发布250文档，其余后续发布。这些为作者报告，不是镜像实测。

为继续核查，下载后续SynCABEL作者发布的[Aremaki/SPACCC镜像](https://huggingface.co/datasets/Aremaki/SPACCC/tree/dda7ad872c0e36c2fed9344bda46ad68496f21dd)全部original_data三分片和README，共2,417,357 bytes；仅该分区完整，不是整个HF仓库。revision `dda7ad872c0e36c2fed9344bda46ad68496f21dd`。它合并DisTEMIST/MedProcNER/SympTEMIST，不能算三湖，也不是原作者原始格式。SNOMED词表、processed/training派生分区未下载。

实测train675、validation75、test250文档；去掉es-前缀1000唯一ID。procedure分别4486/371/3618，共8475，明显少于论文14684。span逐段原文核对11处不符，错误ID/offset存收据，未改源。不能由行数1000就断言完整gold；需要审计转换是否丢弃未归一化/复合实体及原始版本差异。还需与CodiEsp等既有西班牙病例源做ID/文本重叠审计，不能默认独立湖。

## 评分边界实测

源码utils.calculate_fscore只迭代gold文档ID。用1个正确预测加1个额外文档预测调用原函数，micro P/R/F1仍1.0，说明额外文档不计FP。该探针仅验证函数边界，不是模型实验。任务normalization对“+”分隔多代码做集合比较；文档index按代码集合评分。将来本地契约须先拒绝extra/重复文档，不能直接把官方scorer通过称完整输出校验。本轮未改评分器。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 每篇病例提取操作mentions | 镜像1000真实病例报告文本；原始数据尚未取得 | 30多页规范待下载，现仅官方网页定义 | 固定offset/跨度契约 | 镜像8475procedure，11span不符；不是完整14684gold |
| 给每个mention映射SNOMED CT | 相同文本及预测跨度 | 历史词表/术语指南尚未取得 | 上下文、缩写与复合mention规则 | 镜像normalized字段；需与原始TSV核对 |
| 每篇文档生成procedure代码索引 | 预测实体代码 | 相同规范 | groupby文档去重代码 | 官方有index任务；镜像仅实体表，派生并集尚未与原index gold核验 |
| 具体toy例：Auscultación pulmonar | 文档S0004-06142005000700014-1的1023:1044跨度 | 官方task2_ref中该词组 | 本轮没取得该toy全文绑定 | 发布code449264008；toy非新确认样本 |

| 类python的DAG | 具体数值 / 实例 | 边界 |
| --- | --- | --- |
| `scan(reports).sem_map(detect_procedures,E)` | 镜像1000文档；procedure8475 | 不把private实体位置作为默认公开输入 |
| `mentions.sem_map(normalize,E,terminology)` | toy肺部听诊→449264008 | 未执行LLM，缺冻结术语资源 |
| `groupby(document_id).collect_unique(code)` | 原任务750train/250test；镜像675/75/250 | 需从原生index核验并集等价，不能先声称成立 |
| `score(native_gold,predictions)` | 额外文档探针仍F1=1.0 | 需独立ID完整性契约；不是质量优势证据 |

下表均未执行，固定程序与Agent允许同样资源、检索、代码表、循环和缓存。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| toy目标449264008，实际是否命中未知 | 固定识别跨度→同词表检索/排序→代码输出 | 相同目标 | ==核对肺部听诊是否属于规范procedure范围、查术语候选==→输出 | `SpanExtractor→TerminologyLookup→ContextResolver`，简单词典是否足够需对照 |
| 复杂/复合操作输出规范要求的跨度与代码集合 | 固定规范解析和代码候选校验 | 相同任务，不假设更准确 | ==检查复合实体、缩写和上下文依赖规则==→结构化结果 | `GuidelineRules→MentionResolver→CodeSet→DocumentIndex`；缺原始完整gold与E时不运行声称有效的实验 |

本轮已取得原论文、完整官方repo和可审计镜像，尚未取得长规范与完整原始gold，保留待核验。无模型/prompt/训练/种子/token费用预算/推理并发缓存/正式快照/独立确认/commit；使用既有pyarrow25读parquet，标准库调用官方评分函数做1个边界探针。
