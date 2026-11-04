# 增量163：IBM Clais，真实批量应用存在，但公开claims链不完整

**本轮不纳入可行名单，仍8/15。** 这是新查证的研究来源，具体应用确实是政策规则编译后批量检查claims；公开可取得的只有规则抽取侧gold，不能把论文内部大数据库算作公开湖。

## 下载与来源核验

完整作者仓库[IBM/rules_extraction_from_healthcare_policy](https://github.com/IBM/rules_extraction_from_healthcare_policy)，commit `94c69e2d5e81a900781049af4abf23ef4b03423b`，113个tracked文件全部取得。两篇原论文均下载并pdftotext读取：

- [2024 Scientific Reports，Clais](https://www.nature.com/articles/s41598-024-62665-0.pdf)，8,635,540 bytes，SHA256 `db5f8403c64c1dbb721b6db90426253e1129f66c209d63cc300e56e840d1bda0`。
- [2021 Findings，原仓库引用的方法论文](https://aclanthology.org/2021.findings-acl.308.pdf)，1,031,103 bytes，SHA256 `3772e63fb1385323260effcf92f126c0b6788d5a896fcaebda8c60c56dc071d1`。

原件`data/shared-environment-audit-20260908-v163/`；逐文件大小/哈希、审计脚本和结果`artifact/evidence/shared-environment-audit-20260908-v163/`。PMC网页遇到验证码后改用出版社公开PDF成功，没有绕过认证。代码为Apache2.0，不将其延伸为MarketScan数据许可。

2024论文Data availability明确：带标签claims因MarketScan商业许可不公开，需要作者及数据权利方许可。未联系作者，未获取或构造替代claims。论文内部798,181,509总claims、44,913,580牙科claims、421,321阳性是**作者报告**，非本次下载计数。更关键的是标签由20个专家写的ground-truth程序生成，表示潜在不合规，不是逐case实际拒赔或专家最终裁决。不能把40余保险计划的混合数据库直接认定全部真实适用Iowa/Colorado相同政策。

## 原生公开规则实测

`benefit_rules_90.json`是90个唯一规则ID、单一policyId，318个条件、109个highlight片段（101种精确文本，中位22词）；`benefit_rules_51.json`是51个唯一ID、另一个policyId，269个条件、69个片段（52种文本，中位20词）。总141规则、587条件；类型总计Service Limitation112、Mutually Exclusive25、Non Coverage4，和论文一致。status都为VERIFIED只是源字段，不替代本研究科学验证。

每条含conditions、highlights、policyId、subtype等；highlights是gold挑选和标记的相关原文，不是独立未筛选文档。仓库还提供本体、实体词表、代码分组和PAS/Semgrex抽取notebook；没有完整claims及逐claim标签。本轮未完成完整历史政策PDF/章节绑定、当前发布本体与全部condition ID闭合审计，也没有证明本体长度或复杂度足够。政策抽取可作为中间任务候选，但目前只有两个源政策、gold-selected片段，不能升级为大量独立案例的合格湖。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 从政策原文生成可执行benefit-rule条件表 | 当前发布178个highlight条目，不是178独立病例 | 公开本体、服务代码组与lifting配置 | 两个policyId；历史全文未绑定 | 141规则587条件公开可下载；需将conditions隔离，gold-selected输入仅诊断 |
| 真实例：Colorado成年成员每保险年度牙科1000美元上限，急诊/义齿除外，转条件 | benefit_rules_51.json第0条highlight | 公开服务组；年度July1–June30、年龄下界21、maxAmount1000 | 原displayName带partial，不能冒称完整政策 | 原生8条件：起止日、服务、金额、单位、年龄、排除服务、时间数量 |
| 按政策筛出潜在不合规claims | 私有MarketScan claims，本次未取得 | 提取/人工复核规则 | 患者、provider、时间窗等关系 | 作者20程序标签未公开；不具可运行公开默认路径 |

| 类python的DAG | 具体数值 / 原生例 | 边界 |
| --- | --- | --- |
| `scan(policy_paragraphs).sem_map(extract_conditions,ontology)` | 目标141规则/587条件；当前仅178条gold-selected highlights | gold片段不冒充全文搜索输入 |
| `rules.sem_map(resolve_service_groups).compile()` | Colorado例含急诊与义齿两组排除，max1000、minAge21 | 群组本体映射可确定性执行，须审计字典闭合 |
| `claims.groupby(member,benefit_year).exclude(service_groups).sum(amount)` | 保险年度July1–June30 | 这是由原规则推导的程序结构，不是已下载病例或实测金额 |
| `aggregates.filter(violates_rule).collect(claim_id)` | 论文报告421321潜在阳性 | 本地输入/标签未取得，禁止输出假清单或假准确率 |

以下均为**未执行的方法预期**。不预报LOTUS/Agent谁准确，所有方法允许同一公开本体、查询工具、分支、循环和缓存。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| Colorado例对齐已发布8条件，实际匹配率未知 | 固定sem_map抽年龄/年度/上限/例外，再用相同词表解析代码组 | 相同8条件目标，不保证超越静态流程 | ==查询成年年龄编码、牙科服务组与两个例外组，核对保险年度==→结构化输出 | `PolicyText→TypedConditions→GroupResolver→RuleIR`；此例已开发暴露 |
| claims结果不可给出，数据未公开 | 一次编译规则后groupby/window/aggregate批执行 | 同样不可给出 | ==确认金额聚合范围、患者及年度键、例外是否先排除==→复用规则执行 | `RuleIR→KeyedWindow→Exclusion→Aggregation→ViolationFlag`；不是每行反复推理 |

这条来源的价值是明确真实工作流和对照设计：Clais已经研究“从政策本身抽可执行规则”。本研究必须比较E-only编译、固定程序、Coding Agent与轨迹提取；不能把“存在复杂政策”当“必须从执行经验学算子”的证明。论文中部分人工curation也需和自动方法分开计费。未执行任何模型/正式评分/真实claim实验，无独立确认结论。
