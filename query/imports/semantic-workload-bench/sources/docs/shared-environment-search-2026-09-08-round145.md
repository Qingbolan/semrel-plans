# 第145轮：OmniCompliance完整发布库与规则输入反事实核验

仍8/15。本来源不是新发现，首轮只核验GDPR一个文件；本轮补齐完整原论文/作者仓库并全库审计，不能重复计数。144有原始采购数据证据，属于进展。

下载[原论文](https://arxiv.org/abs/2603.13933)762018bytes，SHA256 `434cbe035120b41d1470c597db56a2170a530c6379301aac30e5bd4f3e333da6`；[完整作者仓库](https://github.com/HKUST-KnowComp/OmniCompliance-100K)commit `07c44ff5795229ce1f205acaf6018f7b4ce569d5`，ZIP26376602bytes、280members、CRC通过，SHA256 `55a71f1a3571525ca6af98120eb5458bd9ad190533125f5b1c479f90d6ef49dc`。原件在data/shared-environment-audit-20260908-v145/，下载及实际审计在artifact/evidence/shared-environment-audit-20260908-v145/。

实际完整工作树含74案例JSON文件，共77016行、11475个精确不同source_rule；不等于论文106009案例/12985规则。按全库相同source_rule分组，中位7行、最大33；规则正则词中位48、最大1318。COMPLIES35099、VIOLATES41877、字符串None37、COMPLATES3，非二分类标签不自动修复。76896个casefold名称、76964个精确background；这些是字符串去重计数，不是独立真实事件数量。

所有77016行均无reference_link字段。搜索Agent源码允许reference_link是URL或搜索描述，但发布案例未保留；不能把规则来源网址当逐案真实来源链闭合。案例是Agent搜索、摘要、筛选、标注的产物；论文§4.3人类验证的是rule-case关联度（无关/中度/直接适用），不等于逐案最终合规判断均经专家裁决。process_and_outcome是摘要字段，不是原始判决文件。没有核验每个真实事件和法规版本，不得写成已验证真实监管gold。

最关键的执行事实：benchmarking/case_eval_llm.py的_build_prompt(background,source_rule)和_construct_prompt(case)两条路径均未插入source_rule。后者虽然提示文字说background and rule，却只有background。通过AST抽出两段原函数、去掉类型注解后实际调用（不加载API客户端/密钥）：保持SAME_CASE、更换RULE_A/RULE_B，两个函数的完整prompt分别逐字不变，且均不含RULE_A。收据prompt-probe.json、脚本prompt_probe.py。这不是模型实验，也不证明作者历史论文所有运行路径相同；只证明锁定公开代码这两路径不满足显式E输入要求。未改上游代码，未将问题“修好”后冒称原baseline。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | gold及缺口 |
| --- | --- | --- | --- | --- |
| 判断隔离可疑文件的行为是否符合安全规则 | 发布首条Log4Shell/Cloudflare摘要，描述自动隔离可疑进程 | source_rule是自动隔离可疑文件的短规则，约一行 | relevant_rules列NIST SP800-83和公司政策名称，没有逐案原文链接 | 发布COMPLIES；事件细节未独立求证，不写成确定事实 |
| 同一完整政策下批量复核是否合规 | 全库77016摘要，74文件 | 11475种精确规则文本；不是74个已闭合完整政策环境 | 完整政策版本/适用关系/逐案证据仍需构造核验 | 每个精确规则最多33条；合并规则不能凭空增加每规则case数 |

| 类python的DAG | 具体数值 / 关键中间结果 | 下游边界 |
| --- | --- | --- |
| `cases.sem_map(classify_compliance, E).filter(label=='VIOLATES')` | 发布VIOLATES41877、COMPLIES35099、其他40 | 这是标签分布，不是模型输出或可直接采用的专家gold |
| `groupby(source_rule).apply(batch_classify)` | 11475组，中位7、最大33 | 短规则条件分类，不自动构成复杂共享E |
| `build_prompt(case,E_A)==build_prompt(case,E_B)` | 两作者函数实测均True | 当前执行没有E依赖；不能据此评价规则探索/编译收益 |

以下均未执行模型。样例结果只说明发布标签与方法设计，不承诺正确性。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 发布样例目标COMPLIES；实际输出未测 | 若明确给source_rule，固定短规则+摘要分类；锁定作者原prompt则只见摘要 | 相同目标，无根据声称更准 | ==读取短规则及核对案例证据来源==→发现原始来源链接缺失；不能通过private outcome替代证据 | `ComplianceClassifier(case,versioned_rule)->label,evidence/status`；规则只有一行时E-only编译是强对照 |
| 在相同case上更换E理应允许输出变化，具体要看案例 | LOTUS适配必须实际传E；当前作者函数忽略E | Agent也必须显式取得正确E，否则一样不可评测 | ==确认规则字段进入模型输入==→核对适用范围，不能只在日志记录E | 冻结输入契约先于轨迹学习；本轮只诊断未创建算子 |

不得把referenced/current gold规则直接挑出作为检索oracle而称完整环境探索；fixed RAG、Coding Agent、E-only编译与批Agent必须同资源。全库没有一套当前可直接推荐的长E+大量独立真实案+可信gold闭环；该路线保留为来源线索而不qualified。

下一行动：继续新的独立来源。全发布库数量、来源链接缺失、标签规范及prompt问题已具体核验，不反复下载同库。无模型/快照/正式评分/测试套件/commit；两函数局部原代码执行是工程诊断，不是历史研究复现。
