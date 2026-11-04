# 具体用例

**为 Joe Biden 生成摘要**（Figure 1，p.2；Figure 3，p.5）：

1. 以输入 “Generate a summary about Joe Biden.” 检索，生成首句 “Joe Biden (born November 20, 1942) is the 46th president of the United States.”，置信度足够，直接接受。
2. 临时下一句为 “Joe Biden attended the University of Pennsylvania, where he earned a law degree.”，其中 “the University of Pennsylvania”“a law degree” 概率低，触发检索。
3. 隐式查询把低置信部分遮盖为 “Joe Biden attended , where he earned .”；显式查询让 LM 生成 “What university did Joe Biden attend?” 和 “What degree did Joe Biden earn?”。
4. 检索后重新生成：“He graduated from the University of Delaware in 1965 with a Bachelor of Arts in history and political science.”
5. 后续句子中宣布参选日期 “August 18, 2019” 低置信，检索后改为 “April 25, 2019”。

这个例子同时说明作者提出遮盖/问题生成的原因：如果直接用含错误事实的句子当查询，可能检索到误导信息（§3.2.2，pp.4–5）。

阅读者分析：该例为示意图，论文没有给出这一案例的真实检索结果文本；对本项目而言，它对应“边生成边按需取证”的执行模式，需要逐句多次调用模型与检索器。

依据：§1、§3.2、Figures 1、3，PDF pp.2、4–5。
