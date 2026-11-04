# 具体用例

**场景**（阅读者用原文的准则示例拼成的典型情形，论文未给出单个完整案例）：一家独立研究站点要为一项哮喘试验预筛本站患者，站点没有可对接的 EHR，只能上传病历 PDF。

**流程**（按原文 Methods 与 Table 4–6 的准则示例组织）：

1. 系统把试验的入排标准文本拆成单条准则，例如入选“Participant has an asthma diagnosis according to the GINA guidelines”“Documented physician diagnosis of asthma for 12 months or more prior to Screening”、排除“Immunoglobulin or blood products within 4 weeks of Visit 1”；同时生成相关性准则（哮喘）和每条准则的检索指引。
2. 患者 PDF 拆页、去标识化、嵌入入库。
3. 先检索与“哮喘”最相关的一页，GPT-4o 判断患者是否值得评估；皮肤科患者在此被过滤。
4. 对每条准则按检索指引取若干页（真实部署评测为每条指引取前 3 页），交 o1 输出 met / unmet / unknown 及理由、原文引用（Fig. 2 为界面截图）。
5. 研究协调员逐条确认或修正，并决定“To screen”或“Not eligible”。

**成本与时间**：使用全部记录时每条准则平均 24.8 s、$0.15；每条指引只用前 3 页时为 19.0 s、$0.09。用户复核一名患者中位 5.5 分钟、平均约 9 分钟、四分位距 3–11 分钟。

阅读者分析：这是一个可映射为“文档集合上的逐行语义谓词 + 三值结果 + 人工复核”的工作流；患者级合格判断仍由人完成，论文没有评测自动汇总。

依据：Methods、Results（Inference efficiency、User review efficiency）、Fig. 2、Tables 4–6，PDF pp.2–7。
