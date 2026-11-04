# 海关裁定候选后续核验

状态：两条新线索，未纳入正式38候选计数，无新增Strong。

| 候选 | 已取得 | 待核验或获取失败 |
|---|---|---|
| HS-Bench: Right Code, Wrong Reasons | 原论文搜索索引摘录：2024年1月至2026年4月CROSS裁定，2282份原裁定提取1390产品，7284 grounding authorities，Kimi K2.6提取 | 两个OpenReview PDF地址及官方note API均403/验证页；未下载PDF、仓库或数据，不作为原文全文核验 |
| ATLAS | arXiv2509.18400原PDF及本地文本；读取§2.1–2.3 | HF官方dataset API401，无数据下载；未核验20条gold |

ATLAS论文称18731裁定、2992代码；列出的训练18254+验证200+测试200=18654，与18731差77，来源未解释前不修正数字。转换prompt把HTS、ruling number、URL及裁定全文给GPT-4o-mini，要求重写产品描述和解释。因此有真实裁定来源，但输入事实是否完整、重写是否引入裁定知识、解释是否忠实必须对原文逐条检查。不能把生成解释当作专家原文。

| Query | 数据湖1 | 数据湖2 | 数据湖3 |
|---|---|---|---|
| 按冻结版本HTS为产品分类（待形成正式契约） | 产品描述：数据未取得 | HTS全表/注释：必须锁版本 | 历史裁定：必须排除本例与近重复答案 |
| 类Python DAG | scan → classify → project(code) | 条款检索及版本检查 | 历史类比检索；具体输出数值未知 |

| LOTUS预期结果 | LOTUS过程 | Agent预期结果 | Agent过程 | operator结构 |
|---|---|---|---|---|
| 未知，未执行 | 完整相同资源上的固定检索/层级分类 | 未知，未执行 | ==核查商品属性、规则版本、条款排除项与案例适用性== → 输出或UNKNOWN | 待真实轨迹证明，不能预设动态家族 |

| 比较 | 当前证据 |
|---|---|
| 任务only / 完整E静态 / 逐案Agent / 共享批Agent | 均无本次匹配实验；ATLAS微调与通用模型结果不能替代固定E对照 |

后续优先取得HS-Bench官方资产；如无法取得，保留线索状态。ATLAS需恢复官方公开数据下载及原裁定映射后才能审核事实充分性。不得以访问失败推断全球无可用数据。

来源：https://openreview.net/pdf?id=VQbAzpWNEI；https://arxiv.org/abs/2509.18400；https://huggingface.co/datasets/flexifyai/cross_rulings_hts_dataset_for_tariffs 。
