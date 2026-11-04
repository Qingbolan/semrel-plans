# Increment98 — WMT-MQM解析纠正、全量评分复现与长E排除

仍7/15。本轮结论：WMT2020 MQM具备真实批量与人工评分，但当前实证规范很短，不计严格长E湖。复用round97完整原论文与作者repo，来源：[原论文](https://aclanthology.org/2021.tacl-1.87/)、[作者仓库](https://github.com/google/wmt-mqm-human-evaluation)。

重要纠正：round97用csv默认引号语义解析TSV，正文引号导致部分物理行被错误合并。实际每个物理行严格9列，应使用csv.QUOTE_NONE。这是本地审计错误，不是上游数据破损。旧收据保留，本轮计数与结论取代旧计数。

正确规模：英德79024标注行、14180系统-段、1418源段、130文档、42540评审-段；中英124312标注行、20000系统-段、2000源段、155文档、60000评审-段。全部系统-段恰3评审。主文件去<v>后英德2900/中英7666段有target差异；no-postedits英德仅1、中英0。英德唯一差异Huoshan_Translate.832/reuters.276717/seg801是句首空格，两个版本正文其余完全相同，尚不自动统一偏移。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 根据文档上下文标注译文最多5个最严重错误 | 英德14180及中英20000系统-段，含人类译文系统 | 论文表1完整说明362词、表2类别163词，另严重度与权重规则 | 无编辑目标no-postedits；完整文档按源段连接需后续构造 | 每段3份人工错误标签，保留分歧；不是唯一裁决标签 |
| 生成段级质量分数并聚合 | 同原生人工/模型预测错误集合 | Major5/Minor1/Neutral0/Minor标点0.1/Nontranslation25 | 每评审先求和，再取负均值 | 34180段发布均分全量复算一致，误差阈值1e-6 |
| 复查Huoshan源段801输入版本 | 句首空格两种target | 与字符偏移规则有关 | 不靠strip后直接套旧跨度 | 一处输入格式边界，不能当语义判断错误 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `read_tsv(quoting=NONE).groupby(system,seg,rater)` | 英德42540/中英60000评审-段 | 每系统-段恰3评审；逐物理行9字段验证 |
| `errors.map(weight).sum_per_rater().negative_mean_per_segment()` | 14180＋20000＝34180段 | 主文件和no-postedits两版本全部与avg_seg_scores一致；0遗漏0分数差异 |
| `translations.sem_map(top5_mqm_errors,E,document_context).map(score)` | 尚未跑模型 | 上述评分复现只验证确定性评分器，非语义识别性能 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| eTranslation.737/seg1原生评审分布为Style/Awkward Minor、Mistranslation Major、Mistranslation Minor；实际模型输出未知 | 同文上下文＋短规则固定sem_map，再权重聚合 | 同任务，不能只挑与Agent一致的评审当gold | ==核对类别冲突优先级、最多5错及上下文规则==→输出错误集合 | `context→error_spans→category/severity→top5→score`；未学习 |
| 给定三份人工标注时得到−2.333333 | 惩罚1/5/1确定性平均 | 同−2.333333，无需Agent思考 | ==共享预处理确认权重==→确定性评分 | 评分属于固定节点，不把它称为Agent推理收益 |

长E判定依据：论文正文明确称Table1是complete annotator guidelines。其362词与类别表163词共525词，计数不含另行短严重度/评分段落。原泛MQM科学使用指南是框架适配参考，尚无证据证明完整文档是当前每个item必须理解的长环境。各文档上下文虽然必要，但不同document不是同一个E，不能把它们总长相加后声称一个长共享policy。因此当前停止将该来源作为长E待补资料路线；保留作短规范批处理对照候选，不计15个目标。

脚本artifact/evidence/shared-environment-audit-20260908-v98/audit.py及audit.json、target-conflict.json、norm-scope.json。无模型、无新下载、无作者代码/运行器改动，无公开快照。独立源文档计数130/155，不把十个系统的同源译文当完全独立自然文章。许可证等未因本轮评分一致而自动验证。
