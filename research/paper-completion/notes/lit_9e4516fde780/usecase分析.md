# 具体用例

**FLARE 人体器官（Figure 6，PDF p.7）**：数据来自 MICCAI 2022 挑战赛，腹部器官已有标注。用户输入"Display only the digestive system, while making all other organs semi-transparent."。系统用开放词汇查询工具找出消化系统相关部件：肝、胰、胆囊、食管、胃、十二指肠，把它们的不透明度设为 1.0，其余器官设为半透明，并用自然语言说明做了哪些改动。

**backpack（Figure 8，p.7）**：用户先后用"the box""the storage container""the square-shaped object"指代同一对象，系统都能把它标成红色。作者以此说明系统能处理模糊指代。

**supernova（Figure 7，p.7）**：用户问绿色区域代表什么，系统通过感知识别出它是膨胀激波，添加图例并给出解释；随后通过 VPA 循环把光照方向从右下调整到左上。

阅读者分析：从数据系统角度看，这相当于"自然语言指令 → 语义对象检索（CLIP 相似度）→ 结构化命令"。§5 指出，若查询与场景无关，查询工具仍会返回最相似的部件；没有视觉能力的模型无法发现这种错配（p.9）。

依据：[arXiv:2507.12621v1（2025-07-16，IEEE TVCG 模板预印本，含附录），13 页](https://arxiv.org/pdf/2507.12621v1)，§4.1、§5、Figures 6–8，PDF pp.6–7、9。
