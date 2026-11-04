# 增量205：AnCora转换历史的结构变化证据

继续204，仍12/15，不增加合格来源。本轮复用原论文、24页语义规范及完整UD源数据，新增下载[UD tools](https://github.com/UniversalDependencies/tools)完整仓库（2099d07da45d24fdb80f673a895e3a08aaad3d73，208文件）与[Treex](https://github.com/ufal/treex)完整仓库（df815f19c4d8251f13d99b396bdf32fc4f188762，2563文件）。原件`data/shared-environment-audit-20260908-v205/`，全tracked文件hash及[audit.py/json](../artifact/evidence/shared-environment-audit-20260908-v205/)记录本轮证据。

实际找到UD历史两个提交：`3991588c75543cf4a9013d334942bdf17bc04fe3`于2022-12-06引入原AnCora的arg/tem字段；同日`5dc87949368f1d244fa3a97b4e77d7cd186081f5`修正字段投影。独立读取后者父提交及该提交的全部三个CoNLL-U文件，确认token键与form相同，但204句中410个位置的ArgTem变化：train324、dev50、test36。每个split的(arg,tem)多重集合完全相同，没有新增/删除标签对。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | gold及证据边界 |
|---|---|---|---|---|
| 验证语义标注迁移是否保留标签归属 | 2022修正前后全部三split | 原arg/tem引入和修正提交 | 完整原文token及24页语义规范 | 标签数不变，但410位置改变；不能只核分布 |
| 逐文档抽取谓词—论元关系 | 204当前1635文档/17662句 | 同版角色/事件/语态规则 | 原始谓词归属或有依据的投影实现，仍缺 | 当前135287位置/135742对不是已核验谓词边表 |

| 类python的DAG | 具体数值 | 本轮实际执行/拟执行 |
|---|---|---|
| `git_show(parent).join(git_show(commit),sent_id,token_id).compare(ArgTem)` | 410变化行、204句；token form一致 | 已执行，本轮结构审计 |
| `counter(before.split(',')) == counter(after.split(','))` | train109938、dev12821、test12984对，各自前后相等 | 已执行；历史版本计数，不与204当前HEAD混用 |
| `documents.sem_map(predicate_argument_roles,E).explode()` | 当前135742标签对仍需owner映射 | 未执行；不把UD HEAD直接当原语义谓词 |

具体历史例：修正前`Convenientemente`承载两个`argM:adv`，修正后该副词和随后的`ensartados`分词各承载一个。不是本研究重标注，也不是单纯去重。其他例子包括将时间角色从时间词移出一份至相邻分词，均保留在机器差异记录中。不能据一个例子断言全部剩余复合值无效，也不能无依据恢复原短语边界。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 在明确输入单位后输出正确角色及位置；未运行 | 固定检索语态/角色规则→sem_map→位置校验 | 相同目标；未运行 | ==查公开谓词和论元结构、相应角色规则==→判断→校验 | `ArgumentRoleMapper + OwnershipValidator`，以可靠构造为前置 |
| 上述副词/分词各有一份标签是修正版本目标；未运行 | 消费冻结版本契约，保留位置，不能只输出总count | 同目标；不允许从私有提交差异读取答案 | ==检查公开输入中的候选短语与规范==→逐项判断 | 不能把本次gold差异硬编码成operator |

==为可观察查阅。以上均未运行模型，固定检索/CodingAgent/E-only编译可使用同资源。原始构造缺失不应通过让Agent猜测来补齐。

本轮完整UD tools/Treex搜索未找到ArgTem字段实现；Treex的`HarmonizeAnCora.pm`执行句法依存转换，不能据此声称找到了2022语义投影器。这个结果只约束本次搜索到的源码，不证明全网无此实现。原始XML未取得；仍欠版本绑定、谓词归属、例句重叠、公开视图及独立评分。不以短共指子任务或仅角色频率聚合替代原目标来凑数。后续转查新独立来源，AnCora保留待源恢复。
