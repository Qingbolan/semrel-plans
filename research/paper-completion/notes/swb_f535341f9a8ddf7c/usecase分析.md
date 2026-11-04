# 具体用例

**用例：把入排标准转成病历库查询**（Fig. 1，p.2；Rich semantic representation，p.6；Usage Notes，p.11；Fig. 4，p.13）

设想研究者在 Leaf 队列发现工具中输入一项试验的入选标准（原文 Usage Notes 称语料服务于未来版本的 Leaf，该流程尚未实现）。Fig. 1 的两条示例标准分别涉及 "preeclampsia"（第一条）和 "diseases that affect respiratory function"（第二条）；第一条的完整原句在图片中，正文未引用，本笔记不转述。

1. NER 与关系抽取模型输出 LCT 标注。"preeclampsia" 是 Condition + Condition-Name，可以直接归一化到 ICD-10 编码。"diseases" 只有 Condition，没有 Name，说明需要推理；"respiratory function" 被标为 `Stability[change]`，两者之间是 Caused-By 关系。
2. 下游算法据此推理出哮喘、COPD、肺气肿等会影响呼吸功能的疾病，生成按诊断编码筛选患者的 SQL。Fig. 1 右侧给出的是基于假想表结构的示例 SQL，文中说明 ICD-10 编码只是示例、并不完整。
3. Fig. 4 展示一份标注文档被转成有向无环图（DAG），作者称它可再编译成 SQL、FHIR 或 SPARQL。

**另一个推理案例**（p.6）："conditions contraindicating pioglitazone" 必须先回答"哪些疾病禁用吡格列酮"，前提是识别出 Contraindication 关系。

阅读者分析：这是"自然语言过滤条件 → 中间表示 → 结构化查询"的典型链路，涉及时间窗、数值比较、否定与外部知识推理。原文只提供中间表示的金标准，查询编译与执行正确性没有评测。

依据：Fig. 1、Fig. 4、Methods、Usage Notes，PDF pp.2、6、11、13。
