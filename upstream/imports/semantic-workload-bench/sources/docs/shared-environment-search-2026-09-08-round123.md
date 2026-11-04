# 第123轮：VetClaims新25案剩余22句来源差异均已定位

本轮只读复用完整作者源（120轮commitccb98b19525e及两原论文/六协议）。没有新下载，7/15不变。122轮获得新队列差异证据，属于进展。

## 来源定位

122轮2665句中，2609仅空白归一化可对回，另34句由显式排版归一化可解释，剩22句。本轮发现：

- 19句在排版归一化后去掉全部空白即可找到，包括页脚/律师字段粘连、日期行粘连、引文缺空格等。去空白只作诊断，不能作为默认语言输入的转换。
- 19139412数组位置30：标注写determiine，内嵌原文为determine。
- 19156394位置0：标注头部多两个§，内嵌原文没有。
- 19156394位置43：标注为ship's records，内嵌原文为ships' records。

三处经明确替换后的完整句子都在排版归一化原文中精确存在。本轮没有改写原始JSON、句子或gold；resolutions.json记录变更候选及验证。最初以原文行窗口做fuzzy候选，长段落导致两个低分错误候选；进一步用实际原文短语定位并逐句精确验证后才确认上述差异，不能把fuzzy候选当gold修复。

因此，新25案全部2665标注句现在都有解释清楚的文本来源关系，但不等于源字节一致，更不等于标签语义正确、许可清楚或环境有效性成立。三处文字差异的正式任务构造可保留作者句子作为输入并给原文上下文，同时单列来源差异；若改成原文句子，需要显式派生版本，不隐式迁移标签。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 提取支持事实认定的证据评价句 | 新25案2665作者标注句与内嵌全文 | 同一39页角色协议 | 当前共享19节点规则树 | 19156394位置43关于船舶记录因记录目的而具有较高证明力→ReasoningSentence；单复数撇号不同但已定位原文 |
| 检索抽象法律评价规则 | 同一批句子 | LegalRule/Finding/Evidence等边界协议 | 19139412位置30要求先判断证据来源是否适格 | LegalRuleSentence；标注拼写determiine与原文determine不同，不把修字过程算语义推理 |

| 类python的DAG | 具体数值 | 中间操作 | 下游gold |
| --- | --- | --- | --- |
| `rows.sem_map(role,E19,context).filter(role=='ReasoningSentence').project(row_id)` | 新25案2665输入；227源Reasoning | 保留原句或显式版本化转换；来源映射独立于分类 | 船舶记录例为Reasoning，227不是预测输出 |
| `rows.sem_map(role,E19,context).filter(role=='LegalRuleSentence').count()` | 334源LegalRule | 输入构造须声明34排版、19空白粘连、3文字差异的处理 | 334标签未重标，且无确认实验 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未运行；船舶记录句的正确目标ReasoningSentence | 同协议/E19/上下文语义分类→固定过滤；来源诊断不占用模型修复能力 | 未运行；应输出相同标签，不预设优势 | ==读取证据与证据评价区别== → ==核对当前句的归属和功能== → 输出角色 | `SentenceRole(author_sentence,source_context,E19,protocol_hash)`；构造侧来源映射对所有臂相同，private标签不可读 |

输入细节已有证据，但还未完成新E19与2018协议绑定、协议例子来源/近重复隔离、public/private构造及长环境必要性。不能将“全部句子可定位”晋级成符合全部要求。下一步应构造可审查的开发输入契约或核验规范绑定，而不是重复跑同样字符串检查。

产物：artifact/evidence/shared-environment-audit-20260908-v123/source_audit.py、source-audit.json、resolutions.json。可复跑`python3 artifact/evidence/shared-environment-audit-20260908-v123/source_audit.py`；三处明确定位验证见执行记录和resolutions.json。无新单元测试/模型调用/commit。gold暴露仅为开发，无独立确认。
