# C3PA 原件核验（进行中，未计为 Strong）

原论文：[EMNLP 2024](https://aclanthology.org/2024.emnlp-main.217/)，已下载13页PDF；[官方仓库](https://github.com/MaazBinMusa/C3PA_Dataset)固定d482b942542dc434d3052064504d64133b7f5ab6，804文件，完整ZIP31,810,590 bytes。来源和SHA见[收据](../artifact/evidence/shared-environment-strict-c3pa/source-progress.json)。

| 核验 | 论文 | 实际公开材料 | 影响 |
|---|---|---|---|
| 报告数量 | DB241、WS170，总411 | DB230、WS170，总400，均有HTML | 缺口集中DB，不用论文数代替下载数 |
| 标注行 | 48,947 | DB27,971、WS18,512，总46,483 | 多人标注行不是独立案例 |
| 标注类别 | 12披露要求 | 12类加Others506行 | Others不能默默并为合规或不合规 |
| 每政策标注员 | 恰好3人 | DB不同RANumb数2–6；WS1–3 | 原始字段与论文陈述需解释；零标注人员可能不留行，不直接推定缺人 |
| 共享规则 | §1798.130及培训 | 论文表1给12类映射；完整法规/培训材料尚未取得 | 长政策HTML是x，不是共享E |
| 许可 | 未取得明确数据许可 | 全库未找到license文件 | 公开可下载不等于许可完成 |

[400文件逐项计数与SHA](../artifact/evidence/shared-environment-strict-c3pa/annotation-integrity.json)。这些是原件完整性检查，不是C20充分性审查。

| Query | 数据1：政策HTML | 数据2：共享规范 | 私有gold |
|---|---|---|---|
| 提取回应12披露要求的片段和类别 | Htmls/DB与WS共400文件 | CCPA披露条文及标注约定（尚缺完整冻结材料） | Annotations对应数字CSV，RANumb/Text/Label |
| 企业是否违法 | HTML不能提供所有实际行为与适用门槛 | 完整法律与事实未闭合 | 原数据没有可直接使用的企业违法裁定，不能增造q |

| 类Python DAG | 当前可验证范围 |
|---|---|
| `scan(html) -> segment -> sem_map(span, mandate_definitions) -> aggregate` | 语义片段分类对应原标签；聚合缺失披露不自动等于违法 |
| `evaluate(pred, private_annotations)` | 多人分歧、聚合方式、空标签和span匹配需冻结，不能将所有行视为独立gold |

| 方法 | 预期过程（未执行） | 结果与operator边界 |
|---|---|---|
| LOTUS任务only | 提取片段→12类语义分类 | 未知；短类别定义或许已经足够，须验证E必要性 |
| LOTUS完整E/固定检索 | 冻结规则索引→固定分段→语义分类→合并 | `segment→classify→merge`是强固定候选；论文弱模型分数不证明其不足 |
| 逐记录Agent | ==检查CCPA条文、定义和跨段上下文==→抽取标签 | 不能用未公开专家培训作为特供知识；未实测 |
| 批Agent | ==共享条文索引与标签解释==→逐政策抽取 | 共享预处理属于rho_E；分段分类rho_P；rho_G、rho_R与K未知 |

原论文§5.2用BERT嵌入加12个logistic classifiers；§6用DistilBERT分类，均非同资源完整E/Agent比较。论文表5综合macro-F1为67%，该值不能证明动态探索必要，也不代表本次复现。当前任务结构更接近固定语义分类；尚没有支持Strong的D/E证据。20条规则闭合与版本审查尚未完成；不凭材料数量升级。


## 官方规则与20条局部审查

下载[2023年官方法规](https://cppa.ca.gov/regulations/pdf/20230329_final_regs_text.pdf)：66页515569bytes，SHA见[环境收据](../artifact/evidence/shared-environment-strict-c3pa/environment-source.json)。§7011在PDF12–16页规定隐私政策内容；此PDF保留修订标记，pdftotext混合旧新文字，不是已清洗的执行规则。不能以此替代确切标注培训环境。

固定20文件按SHA256(`c3pa-evidence-v1`+NUL+相对路径)排序，各取首个非Others行；已读全部20片段，[逐条局部审查](../artifact/evidence/shared-environment-strict-c3pa/sample20-local-review.json)。日期可与§7011(e)(4)、信息类别与(e)(1)(A)概念定位；选取首行导致日期/标题偏重，不估K。第14条DB138标Updated Privacy Policy但片段无日期；第13/20条是引言/标题，具体类别未给；这些仍需上下文和标注边界规则，未判源标签错误。没有完成20份全文的充分性/必要性核验，也没有排除固定类别提取程序。


## 当前入场结论：Reject（证据不满足，不证明任务不可能）

停止追加低价值完整性检查。独立真实标注存在，但C20必要性与充分性未闭合；D/E没有同资源强固定不足或语义执行家族证据；许可未确认。任务是固定12类提取，更接近GENIA/条件分类路线；66页法规不自动使原任务需要长环境。保留原件和20条局部审查，不把未知写成通过。此为第29项已审候选，总计0Strong/5Partial/24Reject。
