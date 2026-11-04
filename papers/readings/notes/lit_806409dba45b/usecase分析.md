# 具体用例

**论文用例：初学者友好的机器学习课程过滤（Figure 1–2，pp.2–4）。**

课程表含 course_id、title、subject、difficulty。查询为 sem_filter("beginner-friendly courses related to machine learning")。

- **解释式：** Row 1…Row N 各发给 LLM 一次，例如 C001 “ML Specialization” 保留、C002 “Advanced DL” 剔除、CNNN “Intro to ML” 保留。
- **编译式：** 编译提示（Figure 2）给出谓词、行模式 title/subject/difficulty，以及规则：函数名必须为 compiled_filter(row)、返回布尔值、只输出合法 Python、生成代码内不得调用 LLM。生成的函数用关键词模糊匹配判断 title+subject 是否与 ML/DL/AI 相关，并要求 difficulty == "beginner"，随后在全部行上本地执行（§1，pp.2–3）。

**SemBench 中的效果（Table 4）：** join 密集的 Q5–Q7 上，编译流水线准确率 0.90/1.00/1.00，原生为 0.50/0.70/0.65（表中 Q7 为 0.647）；LLM 调用合计 601→10，费用 0.195→0.058 美元。但 Q2、Q4、Q5、Q8 上编译总时间（编译时间）高于原生端到端时间，如 Q2 12.4s→48.5s。

**阅读者分析：** 编译在本例中“看到”的是模式和（join 时）样本行，而不是逐行内容，因此对于需要读取长文本的谓词，编译函数只能依赖关键词或已有结构化列；作者在 §5.5 承认需要开放世界知识或判断的算子编译效果差。
