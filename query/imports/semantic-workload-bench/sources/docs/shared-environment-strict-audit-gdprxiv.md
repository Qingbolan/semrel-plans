# GDPRxiv：现成benchmark路线Reject，原始裁决仍可作为构造来源


本轮新增来源证据，尚未完成候选四表/20案核验，不加入Strong/Partial/Reject计数。

已下载[作者原论文](https://lawfulcomputing.org/papers/pets2023.pdf)，读取数据采集、系统边界、质量及评估时间范围。论文系统收集官方执法/指导等文档；评估时间2018-05-25至2022-11-24。论文明确系统提供相关文档，由使用者自行判断，不声称自动合规裁决。官方文档真实性不等于可直接获得无泄漏的案件预测样本。

[作者页面](https://gdprxiv.org)返回JavaScript应用壳，HTML652字节已保存。PoPETs页面抓取超时，使用作者PDF成功。公开[PyPI项目](https://pypi.org/project/gdprcrawlertest20/)指向GitHub GDPRxiv/crawler；实际完整clone返回128、Repository not found。不能说仓库已下载，也不能从此推断作者全部材料都不可访问。

当前缺口：原执法文件、共享法规与历史解释版本、逐案件公开事实/私有裁决分离、至少20完整映射、同任务N、可复用K、强固定对照、数据许可。模型和爬虫均未执行。下一步先追官方网页发布资产或源代码分发包，不启动大规模DPA爬取。

[获取收据](../artifact/evidence/shared-environment-strict-gdprxiv/source.json)。这只是待审来源，不冒充新benchmark。上一轮InsLogicBench有原件及构造证据变化，属于进展；本轮也增加了实际原件及明确仓库失败证据。

## 官网资产恢复

当前官网JS实际指向https://github.com/lawfulcomputing/GDPRxiv，旧GDPRxiv/crawler失败不能当现仓库不可获取。已下载PyPI完整sdist（202成员），只解包未执行。取得现仓库README/LICENSE和递归树，commit `c9e3988987bd9a2cafcb4b24653f561a54a3fce1`；API返回54832项且truncated=true，因此不是完整目录清单，更不是完整库下载。GitHub size4590072为API仓库大小字段，非本地数据字节计量。下一步按子树分页/分层读取，核查文档元数据与裁决字段。MIT源码许可证不自动授权全部监管原件。计数不变。

## 首案与元数据来源审查

已取得完整非递归root、llmtraining子树6项和pygdpr子树234项，均truncated=false；documents尚未完整枚举。样本固定为截断树中首个奥地利案件目录`023d538279432429c1901090ebe4749e`，不是随机样本，不估计总体比例。

| Query | 数据1：案件 | 数据2：元数据 | 数据3：环境 |
|---|---|---|---|
| 裁决预测（拟议） | en.txt，2023-06-26，DSB-D124.0073/23；开头已含多项裁决 | decision=unfounded、fine=0、articles=4,6,51,57,77 | 正文同时引用GDPR及DSG/RAO/DSt/VStG/AVG；只给GDPR不算已闭合 |
| 依据提取（另一任务） | 完整裁决文本 | articles是引用号，不证明每条均被违反 | 需要区分程序权限、定义与实体违法依据 |

`en.pdf`下载得到130字节LFS指针，不是PDF；其指针目标大小64698字节，尚未取到原件。英文文本是译文，尚未逐段与德文官方PDF核对。

仓库`llmtraining/metadata.py`明确用OpenAI（默认gpt-5-mini）提取decision/fine/controller/articles并写metadata.json；旧Metadata类仅保存标题、摘要、日期及URL。**这证明存在模型提取路径，不证明当前样本一定由该脚本生成，也不证明官方裁决由模型产生。** 需要commit历史/运行来源或独立重新人工核验才能使用现成字段作独立gold。脚本只阅读，未执行、未读取密钥。

| 类Python DAG | 性质/边界 |
|---|---|
| `facts = redact_outcome_and_analysis(ruling)` | 构造侧尚未实现；不能只删metadata便声称无泄漏 |
| `rules = retrieve(E, facts); y = sem_map(adjudicate, facts, rules)` | 拟议公开固定baseline；E尚缺其他法律 |
| `gold = independent_review(original_ruling)` | 私有评测构造要求，不是模型资源 |

| 方法 | 预期结果 | 执行过程 | operator候选 |
|---|---|---|---|
| LOTUS直接完整裁决 | 能读出unfounded，但这是答案抽取捷径 | 固定文本抽取 | 不证明环境必要 |
| LOTUS仅事实+完整E | 未实测且输入尚未构造 | 检索→语义裁决 | 固定RAG仍未排除 |
| 逐案Agent | 不能承诺恢复gold | ==检查多方请求、程序法及实体依据==→分项判断 | 多请求分解→规则适用→聚合，尚未提取 |
| 批Agent | 摊销未知 | ==索引法规与共同程序规则==→逐案处理 | ρE索引、ρP共同流程、ρG家族未测、ρR个案；K未知 |

单个metadata的unfounded压缩了首申诉无理由、补充请求驳回及代理他人请求驳回等不同结果，需冻结记录单位和聚合语义，不能自动当全案二分类。当前C完整0/20，未入场；本轮查清了字段与重大来源风险，继续保留待审。

## 元数据历史与最终入场判定

实际下载同一文件两个历史版本：`30db4a8159b6a606d9234a8a32b5603e0c684897`只有md5/releaseDate/title/url；`c08a7c5a3c00f0900298c6275be9b485e2c3461e`新增decision/fine/controller/articles，提交说明为“Created medata.py file for metadata.json extraction”。结合已读OpenAI提取脚本，当前字段不具备可直接宣称独立人工gold的来源证据；仍不把commit说明当逐条模型调用收据。官方RIS原PDF本轮HTTP503，未得到字节，不能用译文替代原件认证。

| 条件 | 结论 |
|---|---|
| A固定q | 可另行定义分项裁决任务，但发布单decision没有完整聚合契约 |
| B共享E | 裁决涉及GDPR及多国法律；统一冻结必要环境未构造 |
| C20定位/必要性 | 完整0/20；单案只审文件结构和标签来源 |
| D完整E静态不足 | 未证明；固定多阶段RAG仍是有效候选baseline |
| E执行家族 | K未知，法律条文号不能当K |
| F真实批 | 原件是真实法律材料；同q、同E、独立案件N尚未验证 |
| G可答/无泄漏 | 样本正文直接有答案；回顾性事实与分析未分离，多请求压缩 |
| H获取 | 原论文、源码sdist、部分原库文件与树已取得；完整库/官方原PDF/逐资产许可仍缺 |

**Reject仅指“已发布可直接实验的数据环境”入场主张。** 不否认官方裁决可经新构造和独立复核成为gold。若恢复此路线，需完整取源、明确国家/版本/请求单位、分离事实及裁决、独立核20案、测D/E；这些是尚未完成的研究，不能记成当前Partial或Strong。此前“待审”段落为过程记录，以本段为当前结论。


## 输出与信息不足边界补充

当前单decision字段没有跨请求聚合和信息不足契约。不能把unfounded当UNKNOWN或把缺资料填驳回。若另构造请求级裁决任务，应先冻结合法处置集合和证据不足定义；运行未完成记ABSTAIN，不把它计成官方处置。现未发布该执行契约。
