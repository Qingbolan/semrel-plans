# 第141轮：STAC 原生图评分闭合与实际环境范围

仍8/15，不将本次工程评分通过当新增合格湖。上一轮140提供新数据证据，属于进展。本轮先检查临床试验新线索：TrialGPT早在13轮已核验synthetic患者及反向小组，未重复计数；PMC13035440页面访问返回验证码，未取得新公开病例/标签，不把搜索摘要当合格证据。随后完成STAC115已明确的评分缺口。

原论文、完整46页指南及完整语料已在111下载；完整Educe/IRIT-STAC/Attelo工作树已在115下载，commit/hash/URL详见对应卡片和下载收据。本轮复用已取得字节，不伪称新下载。原论文https://aclanthology.org/L16-1432/，作者规范https://www.irit.fr/STAC/stac-annotation-manual.pdf。当前实际输入为114 inspection-v2：944段/39局，给定10019 EDU与speaker/turn；1111 CDU及9732有向多标签关系是private原生gold。

本轮实现独立开发评分器NativeGraph/GraphEvaluator，放在artifact/evidence/shared-environment-audit-20260908-v141/score.py，未修改上游scorer、现行库CLI或旧冻结快照。CDU按递归直接成员结构匹配，不按任意c0名称；成员顺序不影响匹配，嵌套结构不压平；关系保留有向端点和标签三元组，允许同端点多标签。逐对话分别匹配，避免跨记录ID碰撞。完整图/CDU、问答清单、澄清清单均评分；ABSTAIN计全量分母，gold边计漏报，coverage与文档精确率为0。

check.py实际运行5类诊断：全944gold回填、全CDU重命名+成员反序、全ABSTAIN、删一条真实多标签边、嵌套与平面结构区分。另9个拒绝检查：遗漏/重复/额外record、CDU环/未知成员/重复成员、重复同标签边、未知标签、ABSTAIN携带图。全通过。gold回填9732关系/1111CDU匹配F1=1，是oracle评分诊断，绝不是模型表现。删record_0149 e35→e40的一个标签后9731TP、1FN；下游问答/澄清不变，说明整体图误差不必影响所选下游，不能以任意图误差宣称任务收益。

环境长度核验：46页合计12747正则词；直接定义当前关系与复合语段的§4在PDF14–22页、2374词（到23页§5前）。§5.1.4另含CDU操作语义，不能说§4就是全部必要信息；但也不能把分段标注、资源/偏好标注和Glozz界面操作全算作当前given-EDU解析必要环境。仍需冻结相关规范范围、检查足够性并比较完整E和短规则，不能通过评分器消除这一科学缺口。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 找出每段对话的问题及完整回应 | 944真实游戏对话，给定EDU/speaker/turn | 完整46页手册；当前关系核心§4为2374词 | record_0083: e0问wood换sheep；e1 yup；Nancy e2 sorry、e3 dont have wood | e0→e1问答，e0→CDU{e2,e3}问答；e2→e3 Explanation |
| 汇总需澄清的对话连接 | 同一输入复用图 | Clarification_question与Q_Elab区别及复合语段规范 | 不给人工受话者、CDU或边 | 全开发包378条Clarification_question；不是新数据湖 |

| 类python的DAG | 具体数值 / 关键中间输出 | 下游gold |
| --- | --- | --- |
| `dialogues.sem_map(parse_native_graph,E).explode(edges)` | 944段→gold1111CDU/9732边 | 原生有向多标签图，未进行CDU-head转换 |
| `.filter(type=='Question_answer_pair').project(question,response)` | 全包2359边；record0083有2条，完整回应含CDU | 结构化问答清单及数量2359 |
| `.filter(type=='Clarification_question').count()` | 全包378边 | 378是gold，不是模型预测 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确目标record0083含2条问答及1条Explanation；未执行 | 固定sem_map全文+规范→图结构校验→固定过滤/投影，允许缓存 | 同目标，未执行且不预设更准 | ==查§4.2复合回应规则==→核对Nancy同轮两个EDU→输出复合回应及关系→校验 | `NativeDiscourseParser(edus,speakers,turns,E)`产生cdus及typed_edges；递归结构，不写死CDU ID |
| 对record0149应保留e35→e40两个标签；未执行 | 使用多标签输出契约，不用单标签dict覆盖 | 同目标 | ==确认关系可共存及输出类型==→保留两条边 | typed-edge集合；这是正确输出设计，不能当单轨迹自动提取已完成 |

固定检索、Coding Agent、E-only编译与整批Agent都须享有相同资源；不能从多标签图复杂直接推断Agent必要。原生结构exact指标是本项目显式开发契约，不等同作者CDU转换后旧论文分数。

尚未：公开执行、独立确认、完整语义近重复审计、环境消融、模型对照/单轨迹提取。旧task.json中“无scorer”描述其冻结inspection版本，本轮未篡改快照，新增外部开发scorer不改变它的状态。不增加qualified计数；下一轮优先寻找新来源，STAC评分缺口已解决而长E价值仍待证。
