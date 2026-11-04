# 具体用例

原文 Figure 1 的语料例句：

- `I was booked for/DURATION 2 nights at/LOCUS this hotel in/TIME Oct 2007.`
- `I went to/GOAL ohm after/EXPLANATION;TIME reading some of/QUANTITY;WHOLE the reviews.`
- `... in_front_of/LOCUS my/SOCIALREL;GESTALT four year_old.`

第二句中 after 的功能是时间（TIME），但在场景中表达原因（EXPLANATION）；my 的功能是一般的所属（GESTALT），在场景中是社会关系（SOCIALREL）。这正是 construal 双槽位要捕捉的区别。

使用流程：给定一条评论句子，先识别哪些词或多词表达需要标注（例如 take_care_of 中的 of 不标，out_of 作为整体标注），再为每个目标预测 role 与 function。

阅读者分析：在语义关系抽取类任务中，SNACS 可作为介词/所有格层面的关系类型来源，例如区分“酒店里的位置”和“时间段”；但原文只评测词例级分类，没有评测下游关系抽取或问答。

依据：[ACL 2018 长文，pp.185–196，12 页](https://aclanthology.org/P18-1018)，Figure 1，PDF p.1；§3.3，PDF pp.3–4；§6.2，PDF p.7。
