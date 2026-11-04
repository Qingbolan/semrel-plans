# BidCorpus 严格核验：Reject

本次原始依据：[论文 DOI](https://doi.org/10.1016/j.dib.2024.111202)、[下载的原论文全文 XML](../data/shared-environment-strict-bidcorpus/paper.xml)、[正文提取](../data/shared-environment-strict-bidcorpus/paper.txt)、[官方仓库](https://huggingface.co/datasets/tcepi/bidCorpus/tree/7dd1c1fc7fa8e4187bd25d6462be38c5947e3943)。这是当前目标的淘汰判定，不是否定该数据的分类研究用途。更像固定七标签语义分类，而非已验证的 HSCodeComp 式执行家族。

## 表 1：入场审计

| 数据湖 | E 组成与规模 | x / N | 固定 q / gold | C 定位 | D / E | G / H | Verdict |
|---|---|---|---|---|---|---|---|
| BidCorpus expert gold | 论文 Table 7 七项风险定义、Table 8 七项正则；完整冻结法律/专家手册未提供；引用的447页书不能算已下载E | 资格章节 text；实际1818唯一文本，train1454/test182/validation182 | 识别七类风险要求，7 Boolean；领域专家人工标注；不是官方违法裁决 | CSV无条款引用、依据span或E关联键；20条确定性开发抽样已保存，完整C闭合0/20，未声称读完20全文 | 作者§4.4明确文本模式可写正则；§4.6.1固定分类器有效。语义理解并不排除固定分类；K未测，7标签≠7执行家族 | gold与text须拆开；缺采购对象连接键、实体隔离。完整论文XML及全部expert CSV已下载；PDF403，完整11.5GB仓库未下载 | ❌ Reject：B/C/D/E/G/H未满足 |

专家数据1818条与weak/model各221417条、synthetic1818条必须分开。论文§4.4标注流程包含专家校验自动检出的风险、双专家与冲突裁定；不等于完全盲标设计。发布README标Apache-2.0，原论文CC BY-NC4.0，不能混为同一许可。

实数收据：[gold schema](../artifact/evidence/shared-environment-strict-bidcorpus/gold-schema-audit.json)、[source/hash](../artifact/evidence/shared-environment-strict-bidcorpus/source-progress.json)。七标签阳性数依次122、103、1118、40、330、284、40；356条全零。1818个唯一text哈希只证明无完全重复，不证明同机构/模板隔离。

## 表 2：Query × 数据湖

| Query | 数据湖数据1：资格章节 CSV | 数据湖数据2：共享规则 | 数据湖数据3：采购对象/关联 |
|---|---|---|---|
| q1 检出七类资格要求，输出7 Boolean；读取失败为ABSTAIN | train/test/validation.csv 的text；七列仅评分端 | Table7定义可一次整理；Table8是弱监督正则，不能当gold | 此任务不应擅自声称已判断要求是否合法 |
| q2 环境许可证要求在具体采购中是否不当？输出TRUE/FALSE/UNKNOWN | licenca_ambiental是风险标签，不能直接换成该q的gold | §4.3.1说药品、清洁服务、燃料可能允许相关限制；完整法律依据缺失 | gold CSV没有object、原notice ID或可验证join键；该q不可执行且无独立gold，不作为新增workload |

## 表 3：类 Python DAG

| 类Python的DAG | 具体数据/数值 | 普通或语义 / E依赖 | 决定gold的步骤 |
|---|---|---|---|
| rows = scan_csv(splits).project(text, public_id) | 1818行，移除7答案列 | 普通；不依赖E | 无 |
| rules = freeze(Table7) | 七项短定义，不是长法律环境 | 共享预处理 | 无 |
| flags = sem_map(rows, detect_required_documents, rules) | 每行7 Boolean；缺执行结果时ABSTAIN | 语义；同一固定分类步骤 | flags与专家7列比较 |
| selected = filter(flags.any()).project(id); count(selected) | gold any-positive=1462，仅评分端统计 | 普通聚合 | 下游标签清单/计数；未实跑预测 |

## 真实记录与表 4：方法推演

实际记录：train.csv **零基row1164**；text短引“certidao de cartorios de protestos”；专家certidao_protesto=1，其余六项=0。论文Table7定义是资格阶段要求负面protest证明。文本提到该类证明，支持标签类别；本次未验证完整法条、否定语义及是否合法。实际输入和gold见[sample20](../artifact/evidence/shared-environment-strict-bidcorpus/sample20.json)。

以下全是待检验执行预期，不是LOTUS/Agent实测。

| 预期关键语义算子直接交给LOTUS的结果 | 预期LOTUS执行过程 | 预期Data Agent结果 | 预期Agent执行过程（==环境探索==） | 预期operator结构 |
|---|---|---|---|---|
| q1预计识别certidao_protesto；准确率未知 | sem_map(text,七项定义)→7flags→filter；同定义供全部行 | 可能同一标签，无优势证据 | ==读取七项定义==→理解该记录要求→输出flags；为完整违法裁定查询不存在的法规不能补齐输入 | DetectQualificationRequirements(text,rules)→flags/status；固定七路语义判断即可表达，未证明需要家族库 |

| 比较臂 | 同一任务表下输入/预期风险 | 执行与摊销 |
|---|---|---|
| 静态，仅任务表 | text+七列解释；术语/否定可能误识别 | 一次分类；未测 |
| 静态+完整可得E | Table7/8短表可整体加入；不是获得完整法律 | 固定分类或正则候选+语义复核；没有已知理由必须逐行Agent |
| 逐记录Agent | 相同text与同一短表 | ==读定义、检查候选要求==→输出；可能重复读表 |
| 批Agent | 全批text与同一短表 | ==一次整理规则==→逐行分类、缓存同义表达；能否改善质量未知 |

ρ_E为共享七项定义读取；ρ_P为每行要求识别/否定检查；ρ_G为潜在同义表达族但未测；ρ_R为具体文本理解。无轨迹，不给虚构百分比。K未知，词面/语义触发不自动证明1≪K≪N。env-only整理很可能覆盖共享部分，这是候选被固定语义分类baseline击败的主要风险。

论文Table9 JurisBERT F1=92.93%属于作者交叉验证、非本次LOTUS结果；Table15合成同义改写只检验文本鲁棒性，不验证长E探索。需要采购对象来判断例外的明确说明来自§4.3.1，但expert CSV缺该输入及关联；不应把章节风险标签升级成最终法规合规gold。
