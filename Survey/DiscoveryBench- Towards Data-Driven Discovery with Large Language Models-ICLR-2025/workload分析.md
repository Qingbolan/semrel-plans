# Workload 分析

**要验证的问题。** 检验模型能否从数据发现并正确表述特定上下文下的变量关系，而不是只生成能运行的代码。

**数据、任务单位与gold。** DB-REAL264任务来自6个学科研究，复现原分析和数据；DB-SYNTH903任务、48领域，由生成过程控制关系。输入是文件、元数据、发现目标；gold是上下文/变量/关系组成的假设。HMS结合上下文二值语义匹配、变量F1和关系判定，含LLM语义judge；不等同因果真实性或任意发现均正确。

**具体use case：输入目标 → 使用前 → 使用后。** 原文图1：输入Catalonia植物引入与栖息地数据，问城市用地如何影响不同引入植物。使用前只拟合出可运行统计代码，仍可能把变量或关系方向说反；使用后目标评测要求人口/环境上下文、变量与方向都匹配。图1展示错误预测的分项评分，不是某系统纠正后成功的单例实验。

**Baseline与比较条件。** CodeGen、ReAct、DataVoyager配GPT-4o/GPT-4-preview/Llama3-70B；NoDataGuess不看数据诊断记忆；Reflexion(Oracle)收到gold HMS反馈、最多3试。后两者信息条件不同，正式版DB-REAL/GPT-4o中CodeGen20.9、ReAct24.4、Oracle24.6，不能把oracle使用的gold反馈忽略。

**证据边界。** 正式图4中ReAct在DB-REAL的GPT模型上优于CodeGen，但在DB-SYNTH对应模型上较低，说明交互收益依任务而变；正文§5.2“没有提升”的泛化表述不能覆盖全部单元格。给定文件下发现科学关系，不能直接证明开放数据源发现或跨记录复用。

来源：[阅读版本](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d70af566e69f1dfb687791ecf955e28-Paper-Conference.pdf)，§3–5、图1/3/4、评测附录；ICLR2025正式版。本文为原文工作负载分析，未复现实验。
