# 具体用例

**场景**：从血管生成文献中抽取跨层级的因果陈述，例如"某药物抑制肿瘤血管生成"。

**表示方式**：

- "抑制"是 Negative regulation 事件：Cause 为药物实体（Drug or compound），Theme 为另一事件 Blood vessel development。
- 该事件以肿瘤（Pathological formation）为 Theme 或 At-Loc。
- 如果给药行为被提及，则另标一个 Planned process 事件，药物为 Instrument。

原文 Fig.4 正是这样一个连接不同层级实体的 Negative regulation 例子。Table 2 中的示例有 "Inhibition [of NO synthase by L-NAME]"、"[UFT] administration"、"[insulin] stimulates [VEGF expression]"。

**处理流程**：NERsuite 先识别实体，可选用 UMLS、Entrez Gene、OBO 词典特征。EventMine 再依次完成触发词识别、论元识别、多论元事件组装和修饰识别，每个模块都是一对多 SVM（§3.1–3.2）。

**下游用途**：作者计划把结果接入 MEDIE 等语义检索系统，支持"查找关于抑制器官生长的陈述"这类跨层级结构化查询（§5）。

依据：§3、§5、Table 2、Fig.4。
