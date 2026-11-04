# 具体用例

**原文示例：按世纪画出画作中剑的最大数量**（§4.1 Query 2、Figure 4 右，pp.4–5）。输入是绘画元数据表（含创作日期 `inception`）和图像集合。GPT-4 生成的计划：

| 步骤 | 逻辑计划 | 物理算子与参数 |
|---|---|---|
| 1 | 按 `img_path` 连接元数据表与图像表 | SQL Join |
| 2 | 从每张图像提取剑的数量，新列 `num_swords` | VisualQA（"How many swords are depicted?"，int） |
| 3 | 从 `inception` 提取世纪，新列 `century` | Python（由描述生成代码） |
| 4 | 按世纪分组求剑数最大值 | SQL Aggregation |
| 5 | 画柱状图，x 为世纪，y 为最大剑数 | Plot（bar） |

**另一示例**（§4.1 Query 1，Figure 4 左）："每支球队单场最高得分是多少？"计划为两次连接后用 TextQA，问题模板为 `How many points did <name> score?`，执行时用表中球队名实例化，再按队名取 MAX。

**失败示例**（§4.3，p.6）："每支球队输了几场？"两个模型都没译对。ChatGPT-3.5 试图只用一条 SQL、忽略文本；GPT-4 知道要用文本，但没生成正确的抽取算子。作者给出的可行解是连接后用 TextQA 问 `Did <name> lose?` 再聚合。

阅读者分析：论文展示的是计划，没有逐张画核验 VisualQA 数剑是否准确，因此这些例子证明的是规划能力而非答案正确（阅读者分析）。

依据：[arXiv 2308.03424v1](https://arxiv.org/abs/2308.03424v1)，§4.1、§4.3、Figure 4，pp.4–6。
