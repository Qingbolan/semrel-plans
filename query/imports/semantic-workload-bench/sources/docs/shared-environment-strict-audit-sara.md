# SARA v1：简化税法推理控制，Reject

已下载并读取[原论文](https://ceur-ws.org/Vol-2645/paper5.pdf)的§2数据构造、§3求解器与实验部分，8页；下载[完整官方代码库](https://github.com/SgfdDttt/sara)和[JHU官方数据包](https://nlp.jhu.edu/law/sara/sara.tar.gz)。固定commit、哈希与数量见[来源收据](../artifact/evidence/shared-environment-strict-sara/source.json)。本卡仅审查v1，不把v2计作已下载。

## 表1：入场审计与十问

| 项 | 实际证据与判定 |
|---|---|
| A / q与输出 | 276条给定法条命题的蕴含判断；100条税额计算。不能把这两个输出任务合为376条同q。原数据没有UNKNOWN；实验若证据不足，应预先定义ABSTAIN而不修改gold。 |
| B / E规模 | 9份简化IRC纯文本，27,149 bytes、4,366空白分词。§1/2/63/68/151/152/3301/3306/7703；不是完整美国税法。论文删去细节及指向集合外的引用。 |
| C / gold与20条 | 作者按条文人工构造正反例，经法学教授审阅合理性；不是真实税务裁决。20条确定性抽样均有源section文件，见sample20收据；这只是文件级映射，完整必要性/充分性闭合0。 |
| D / 静态完整E | E只有4,366词，不能以放不进上下文论证Agent。论文手工Prolog规则+手工事实全对证明固定执行可行；不证明自动事实解析全对。没有同资源LOTUS对比。 |
| E / K与路由 | 原命题直接给出section，结构路由；亲属/时间/婚姻事实仍需语义解析。9节、276题均不是K。K及家族占比未知，不能证明目标中间形态。 |
| F / N与真实性 | 实际276二分类、100数值；原始split256train/120test=176+80/100+20。前者按法条构造，后者随机组合原案例再人工消歧，非真实天然批。硬性失败。 |
| G / 充分性与泄漏 | .pl文件将Text、Question、Facts、Test同置；Question末尾含gold，Facts是人工解析，Test含目标值。公开输入须剥离答案和事实程序，文件名pos/neg亦不可暴露。论文还明确部分常识未在法条定义，完整闭合未核。 |
| H / 下载许可 | 原论文、49文件完整库、122,704 bytes数据归档均取得。数据包LICENSE给出MIT式Dataset授权；代码库未找到独立LICENSE，不自动外推数据授权。 |
| Agent探索 / 可复用 | 可读取交叉引用、定义与税档，再解析日期/亲属关系；法条编译属E-only，事实解析每例重复，未证明必须在线探索。 |
| 是否超出RAG/条件分类 | 蕴含任务是规则条件判断；数值任务可采用语义解析+固定求解器。当前证据不能排除这种架构。更接近固定规则执行控制，不具备HSCodeComp式已证实语义家族。 |
| Verdict | **Reject**。真实天然批失败、共享E短、D/E未证；无需把缺少的20完整闭合伪称完成。 |

## 表2：Query × 数据湖

| Query | 数据湖数据1 | 数据湖数据2 | gold |
|---|---|---|---|
| 给定命题是否由事实与简化法条推出 | cases/s7703_a_2_pos.pl的Text及去答案Question | statutes/source/section7703及交叉引用 | Entailment（私有保存） |
| 指定人物指定年的税额 | cases/tax_case_1.pl的Text及去答案Question | 全9份source法条 | 0美元（私有保存） |

## 表3：类Python DAG

| 类Python的DAG | 普通/语义、E依赖、输出边界 |
|---|---|
| `records = scan_text_question(public_cases)` | 普通；不得载入Facts、Test、答案后缀或pos/neg ID |
| `rules = compile_rules(E)` | E-only语义编译，所有臂可用相同资源；手工Prolog是额外人工监督控制 |
| `facts = sem_map(records, schema)` | 语义：人物、日期、收入、关系；自动解析准确性未测 |
| `pred = solve(rules, facts, query)` | 固定逻辑/算术；预测蕴含或税额，非读取gold |
| `evaluate(pred, private_gold)` | 普通独立评分；本轮未执行 |

## 表4：四路推演（不是运行结果）

| 臂 | 预期关键算子结果 | 预期过程 | 可能operator结构 |
|---|---|---|---|
| LOTUS任务表only | 婚姻例可能凭常识答对；准确率未知，无法确认使用冻结规则 | Text+Question单次语义调用 | 条件文本判断 |
| LOTUS完整E | 4,366词可提供全E；没有实证理由预期必输Agent | 固定全E提示→事实解析/判断 | 固定语义解析+规则求解 |
| 逐例Data Agent | 正确目标为例中Entailment，但未执行，不能承诺输出 | ==读7703(a)(2)及税年定义==→核对2017离婚与2018税年→判断 | 时间/关系事实解析→固定谓词 |
| 批Data Agent | 未测质量和成本；可能摊销规则读取 | ==一次编译9节及交叉引用==→整批解析→执行 | 共享规则库+逐例事实表；不是已学到的家族库 |

ρ_E为法条加载/编译，ρ_P为事实解析与求解，ρ_G是否存在额外必要的家族共享计算未知，ρ_R为具体人物日期金额。所有比例、K及金额未测。最强固定对照为同资源自动事实解析+预编译规则，不能把手工gold事实提供给该对照后称公平自动执行。

## 实际打开的例子与抽样边界

s7703_a_2_pos：Alice与Bob在2012-04-05结婚，2017-09-16依法离婚。题目问2018年7703(a)(2)是否适用，官方构造gold为Entailment。源法条排除依法离婚/分居者的已婚身份。该局部例子支持条款应用，不是现实纳税人裁决。

tax_case_1：Alice在2019年监禁期间劳务收入1,200美元，获释后收入5,320美元，采用标准扣除；构造gold为0美元。没有逐条复核所有税额路径，因此不将其算作完整C通过。

[20条文件级映射](../artifact/evidence/shared-environment-strict-sara/sample20.json)从276条二分类按SHA256("sara-strict-v1"+NUL+文件名)取前20；只用于开发审计，不是新增确认集。归档包含AppleDouble隐藏资源文件，首次统计因将其误作UTF-8失败；随后按实际section名称和非隐藏.pl allowlist重算，未修改上游文件。未运行作者脚本、Prolog、模型或测试，不报告论文全对为本地复现。
