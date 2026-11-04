# 具体用例

**用例（Figure 1–2，PDF pp.2–3）**：一篇三句短文档，首句提到 "Edmund Pope" 与 taste-01 事件，第二句有 convict-01 与 sentence-01 事件，末句为 "He denied any wrong-doing."

句级图把末句表示为 deny-01，Arg0 为 person（3rd、Singular），Arg1 为 do-02 wrong 的事情，aspect 为 Performance。文档级图再补上三类跨句信息：

- 共指：末句的 person 与首句的 Edmund Pope 是同一实体；
- 时间：第二句的定罪、判刑事件发生在首句 taste-01 之前；
- 模态：作者对 deny-01 的发生是完全肯定，而 Pope 本人否定 do-02（做错事）发生。

**低资源语言用例（例 1，PDF p.2）**：阿拉帕霍语单词 ne'toukutooxebei3i'（"然后他们把马拴上"）中，"马"并入动词词干；UMR 以 toukutooxebei-00 为谓词，另加 animal 节点作 :theme，以便与其他句中的马建立共指。

阅读者分析：对语义查询而言，这类图可以支持"谁否认了什么、说话人对事件真实性的态度、事件先后"等结构化问题；但论文本身没有演示任何查询或应用（阅读者分析）。
