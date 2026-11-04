# HuBMAP ARMS：原件与任务语义审查

状态：进行中，未计为Strong或已完成入场候选。[原论文](https://arxiv.org/abs/2604.08552)与[完整官方仓库](https://github.com/musen-lab/metadata-standardization-agent)已下载，commit3a55839eca8b1a2a3a7524bd7081809e037e6804；来源SHA见[下载收据](../artifact/evidence/shared-environment-strict-hubmap/source-progress.json)。

| Query | 数据湖数据1 | 数据湖数据2 | gold |
|---|---|---|---|
| 按指定模板标准化旧元数据，无法确定留空 | data/<assay>/input/*.json共839 | data/schemas/*.json共12，17,468–42,660bytes/份，23–48字段 | 同名gold/*.json共839；专家曾查实验协议/厂商资料 |
| 严格校验模板约束 | 同一记录与模板 | datatype/pattern/permissible_values | 原专家保留部分旧值，原gold不等同严格有效性标签，不能直接增设此q |

每模板记录9–100，不把字段实例算记录。可研究共享12模板集合上的参数化q，但必须披露模板ID已给出，assay路由是结构触发，不是语义家族证明。库内模板已枚举许多可选术语；其快照与运行时BioPortal版本一致性待核。

| 类Python DAG | 含义 |
|---|---|
| `template=lookup(E,template_id)` | 已给ID的普通路由 |
| `mapping=sem_map(legacy_fields,template.descriptions)` | 字段语义对应 |
| `values=sem_map(mapping,template.allowed_values)` | 规范术语/枚举选择，可用固定循环与检索 |
| `format(values); preserve_or_abstain()` | 专家保留政策与模板约束冲突时如何输出须冻结 |

| 方法 | 预期过程 | 结果边界/预期operator |
|---|---|---|
| LOTUS任务only | 字段名/本体名→语义映射 | 论文baseline资源不足，不证明固定方法不足 |
| LOTUS完整E/固定工具 | 全模板描述/可选项→固定字段循环→术语检索 | `map_fields→resolve_values→format`强对照尚未排除；未实测 |
| 逐记录Agent | ==检索完整模板、按ontology/branch查询术语==→映射→日志 | 论文确有工具增益，但双方资源不同，不能作为D通过 |
| 批Agent | ==缓存模板、可选值和重复映射==→处理每条记录 | rho_E索引、rho_P字段遍历、rho_G未测、rho_R个例歧义；K未知 |

实际打开atacseq-bd435ed6aa55e9f57d783ce630d746bf.json：输入instrument_model=Novaseq6014、reagent_kit=NovaSeq6000，gold模型=NovaSeq 6000；只能说相邻字段提供可能线索，尚未核实专家依据。输入tissue_id=CALT0003-HT-3，gold parent_sample_id保留该旧值，而模板pattern要求HBM/SNT格式。输入cell_barcode有实际数值，gold barcode字段却为Not applicable；输入nucleus与gold single cell也需协议/定义解释，不能凭字段名断定谁错。

[全量结构检查](../artifact/evidence/shared-environment-strict-hubmap/schema-record-audit.json)：839文件名一一对应。按原JSON pattern直接应用Python fullmatch得到895字段不匹配；该数字只是静态格式诊断，须核查跨系统转义与校验语义，不是895个错误病例。论文明确保留不完全规范的有用原值，不能用严格格式目标替换专家输出目标。

C20、协议/厂商资料闭合、实体隔离、运行时E冻结和同资源D/E均未完成。没有运行模型、作者代码或评分。


## 20记录仪器字段核验

[冻结20记录及输入/gold哈希](../artifact/evidence/shared-environment-strict-hubmap/sample20-instrument-review.json)：全体839记录路径按SHA256(`hubmap20-v1`+NUL+相对路径)排序取20，固定检查acquisition_instrument_model。20个gold均在各自模板89项同一候选表内；7原值相同、3仅大小写/空格/标点归一、10需别名/具体型号解释。这不是20条完整记录C通过，也不是K测量。

完整读样本2和4输入：样本4的reagent_kit明确NovaSeq6000，可支持model从NovaSeq细化；样本2reagent_kit也只写NovaSeq，需要历史型号/协议等外部依据，不能凭词表包含6000就认定闭合。日期可提供线索，但需冻结产品历史证据。MIBIscope1→MIBIscope可能是实例号归一，尚未由公开定义证明。

已读官方tools.py：branch搜索无结果时枚举整个分支，且工具缓存模板与查询；返回候选label而非完整解释。该行为可以由固定程序表达，不能将缓存收益当rho_G。sampling.py默认seed=None，论文固定seed需实际运行收据而非默认值证明；未运行作者脚本。


协议访问补查：DOI能解析到Chromium Multiome ATAC_GEX(10x)页面，HTTP200、11163bytes；实际仅应用壳和结构化标题/描述，无步骤正文。元数据指向另一canonical v1路径；1970日期是无效版本证据，不能据此冻结历史。见[访问收据](../artifact/evidence/shared-environment-strict-hubmap/protocol-access.json)。未验证NovaSeq具体型号；完整E固定对照仍缺。
