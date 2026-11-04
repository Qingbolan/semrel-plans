# 具体用例

**例 1（Figure 1，Doc #2823，文章评论，公立/私立学校领域，p.3）**：评论者写道 "I agree - Kids can do great in the public school system and parents DO need to be involved." 被标为 claim；"The public school system lets them deal with real life too…" 与 "There are still great teachers in the public schools…" 被标为 premise；中间的 "The more people leave, the worse its going to become." 未标为任何成分（O）。

**例 2（Figure 1，Doc #2224，论坛帖，单性别教育领域，p.3）**：作者的亲身经历 "I went to an all boys school" 与结尾 "Btw, I work at a co-ed school…" 被标为 backing；"would of much preferred gone to a co-ed" 为 claim；"It is closer to the 'real world' that way…" 为 premise。其余关于考试成绩和姐妹经历的句子未标注。

**系统输出示例（§5.1、Figure 2，pp.7–8）**：在 #4285 中，金标准把论证标为隐含 claim（支持私立学校）的省略式论证，而系统把第一个前提识别为显式 claim，作者认为这也可能是合理解读；在 #2180 中，系统识别出两个 premise 而非三个，但较长的 backing 有意义。

阅读者分析：用例说明论证成分边界和是否隐含 claim 都带有主观性；把此类标注作为语义抽取任务的金标准时，需要允许多种合理解读或使用宽松边界匹配。

依据：EMNLP 2015，§3、§5.1、Figures 1–2，PDF pp.3、7–8。
