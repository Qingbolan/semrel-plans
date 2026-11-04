# 具体用例

原文最具体的场景是数据目录自动丰富（Integration with Data Catalogs，PDF p.6）：当新表注册或模式显著变化时，事件触发剖析流程；对抽样数据脱敏后调用 GPT-4 生成列描述；经统计画像交叉核对、相似列一致性检查和置信度打分后，通过 Unity Catalog 原生 API 写入表/列元数据并保留版本与血缘；Apache Atlas 则需把自然语言描述映射到其类型和分类体系。

另一个具体例子是列名“amt”的歧义：可能是交易金额，也可能是修订日期，需要语义推断（PDF p.3）。Table 4 的“缩写误读”被标为常见失败模式，缓解方式为注入术语表（PDF p.5）。

阅读者分析：这些是设计描述而非经评测的案例，没有展示任何一条生成的列描述样例。若项目把“列语义描述生成”作为语义算子或元数据工作负载，可参考其目录触发与校验流程，但不能引用本文作为效果证据。

依据：Background、Implementation Challenges、Integration with Data Catalogs，PDF pp.3、5–6。
