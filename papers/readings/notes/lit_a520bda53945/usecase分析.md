# 具体用例

Fig.5（p.7）的 DABStep 复杂查询：“2023 年第 10 天，Belles_cookbook_store 应支付的总费用（欧元）是多少？”系统将其拆为三个子任务：
1. 从 payments.csv 取该商户 day_of_year=10 的支付交易（CSVScan → Filter → Project），并计算是否境内交易；
2. 从 merchant_data.json 取商户静态属性（account_type、capture_delay、mcc），并由 1 月交易聚合出月交易量与欺诈率分档（JSONScan + 聚合 + InnerMerge）；
3. 从 fees.json 取费率规则（card_scheme、account_type、aci、intracountry 等组合，含 fixed_amount 与 rate）。
三个子任务结果物化为新数据集（TransactionBellesDay10、MerchantBellesDetails、FeeRules），再由规划智能体对原任务生成最终计划。正文还提到隐式知识难点，如“ACI 为 NULL 表示通配”（§7.2.2，p.10）。

Fig.2/4（pp.4、6）的玩具例子展示跨表与文本的语义连接：员工表（姓名/年龄/薪资/角色）与 Wikipedia 人物页通过 Name 关联，问题“求赢过 10 次以上 NBA 冠军者的总薪资”。

部署用例（§7.6，p.12）：国家电网——数百张表（数千列）与数万份文档上的负荷与营销分析，200 余个问题准确率 91%；邮储银行——300 个任务准确率 92%。这两组数字无可复核的数据或问题清单。

阅读者分析：对本项目而言，Wikipedia 子集的“多条件抽取”和“跨源语义连接”最接近语义算子查询；若派生查询，需注明是项目派生任务。

依据：[arXiv:2508.05002v2，13 页](https://arxiv.org/abs/2508.05002)，见文中所注章节与页码。
