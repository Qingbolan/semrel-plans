# 具体用例

源本体是 NCI Thesaurus，目标本体是 Disease Ontology（§4.4，PDF pp.9–11）。

**例 1（不需要调用 LLM）**：源实体 ncit:C99383 只有一个标签"autoimmune nervous system disorder"。目标候选按相似度依次为 DOID:438（autoimmune disease of the nervous system）、DOID:0060004、DOID:417、DOID:11465。DOID:438 的反向候选列表中，ncit:C99383 也排第一，两者互为首选，于是直接作为 HCB 对应接受。

**例 2（调用 LLM 两次）**：源实体 ncit:C3745（clear cell sarcoma of soft tissue）。前两个目标候选依次为 DOID:4880（kidney clear cell sarcoma，相似度 0.95621）和 DOID:4233（clear cell sarcoma）。第一个候选不是 HCB，询问 LLM 后被否定；第二个是双向对应但不是 HCB，询问 LLM 后得到确认，搜索停止。作者说先检索再提示的基线在这个例子里需要 5 次询问（p.9），MILA 只需 2 次。

阅读者分析：这个例子说明了 SBERT 的局限：kidney clear cell sarcoma 与源实体字面相似度最高，但语义并不等价，需要 LLM 来判断。这与作者所说的"区分语义相似与统计重叠"一致（§6，p.20）。

依据：[arXiv:2501.11441v2，25 页](https://arxiv.org/pdf/2501.11441v2)，§4.2、§4.4、Figures 2–4，PDF pp.7–11。
