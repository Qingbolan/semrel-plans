# 增量182：PCC标题约定与共指原生检查

复用181原件与hash，不新增湖，仍10/15。上一轮下载构成有效进展；本轮完成全部176文档原生遍历。

手册§10.5印刷178–179明确：标题单独形成EDU且始终不入正文树。因此175篇双根无需修正。maz-12666为标题segment1及两个span根33/40，仍需解释。176图无重复节点/parent循环，继承181无悬空引用结果。

MMAX176篇共33222个word节点，5272 primary markables、211 secondary markables、20 group markables、2233 sentence markables。共指关系本身有190个type=anaphoric但antecedent=empty，原因待查，不当作190个错误。

一项确切引用未闭合：maz-14172/primmark:markable_1000195指向groups:markable_1000196，目标group文件中不存在。四个跨度检查命中位于maz-00001和maz-17953；范围端点存在，但中间word IDs分别缺82/192及193。**这还不是跨度gold错误：若MMAX按序列端点解释范围，可以合法，需核对格式语义。** 不把整数ID连续性当成自然语言或标注要求。

全书显式文档ID匹配24项，其中22项存在于语料。另有maz-5297/maz-5279图题不一致，后者不在语料；不能猜测替换ID。完整名单在audit.json，尚未做无ID引用的文本相似/近重复检查。

手册共指§6.3确实包含非平凡任务约定：PM优先SM、PM/SM优先重新建组，即使距离更远；不连续表达的首/末部分与指代方向规则；通常连接最近提及并保留已有群组身份。这些是可供E-only程序编译的具体规则，不能自动证明轨迹提取更好。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 每篇重建RST正文树并汇总因果关系 | 176真实评论及标题/原生EDU | 手册RST章§10.5标题例外 | 原生EDU若公开则annotation-given | 5102原生边；175篇标题+正文双根，1篇多正文根待查 |
| 每篇解析名词指代，再汇总实体提及 | 同176篇，33222词节点 | 手册§5/6的表达类型、优先级、组指代约定 | 输入可给primary/secondary边界但不提供antecedent字段；届时任务显式given-markables | 5272 PM、211 SM、20组；完整原始标注本轮检查，不把实体字段全公开 |

| 类python的DAG | 具体数值/例子 | 当前验证边界 |
|---|---|---|
| `scan(docs).sem_map(parse_rst,E).validate(title_isolated).explode(edges).aggregate()` | 175/176满足两根计数；maz-12666三根 | 两根计数不是完整正文树正确性证明；单独标题由手册规定 |
| `scan(docs).sem_map(resolve_mentions,E).project(antecedent_edges).groupby(entity)` | maz-19372 word33“Sie”→secmark:markable_2，后者word14–17指那位贵族女士 | 直接前件是secondary，不应仅在primary候选找最近词；分组/空前件与评分契约未完成 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标为Sie→secondary markable_2，实际未知 | 固定sem_map读同样原文、边界及规范；固定检索/引用检查可用 | 同一目标，实际未知 | ==读取PM/SM与组优先级、检查跨层候选== → 输出前件 → 检查目标存在 | `AntecedentResolver(version, candidate_layers, preference_rules, discontinuity_policy, reference_validator, abstain)` |
| 目标保留标题独立，实际未知 | 预编译标题规则+固定RST语义调用 | 相同标题/正文契约 | ==定位§10.5并确定标题EDU== → 解析正文 → 图检查 | `RSTParser(title_policy, nuclearity_rules, relation_rules, graph_validator)` |

表中均为目标/待测过程，不是LLM输出。==表示可观察查阅步骤，不是私人思维链==。固定程序和E-only编译须获得同样资源，不能把确定格式检查包装成Agent推理优势。

证据：`artifact/evidence/shared-environment-audit-20260908-v182/audit.py`及`audit.json`。复现：仓库根目录运行`python3 artifact/evidence/shared-environment-audit-20260908-v182/audit.py`（将重写本轮审计JSON；解释注记见本卡）。原件来源与许可见[181卡](shared-environment-search-2026-09-08-round181.md)。没有新下载、原件修改、模型运行或独立评测。下一步核对MMAX范围/empty语义、章节示例去重和RST关系清单，之后才决定开发资格。
