# workload分析

§5：FEVER使用development split的1000 claims；BioDEX使用250医学文章及约24000反应标签；SciFact使用300 claims，先检索100 articles再rerank；HellaSwag-bench使用200合成摘要，20次trial、temperature0.7；主题分析647篇ArXiv文章、5个主题。

默认本地推理配置是4张80GB A100、Llama-3-70B、E5 embedding、vLLM inference batch size64。OpenAI对照使用64路线程并发；它不等于每个prompt装64条记录。BioDEX的250是评测记录数；K=5/10是输出排名指标；三者须分别记录（§5，pp.4177–4181）。

本文的批处理是一个查询对整个关系或join候选执行模型操作；没有定义把多条独立用户查询合成一个批提交。图1–3给出程序示例；完整可运行query需另对官方artifact做源码级提取，不能用本分析中文复述冒充原始英文query。

来源：[Semantic Operators and Their Optimization: Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)。
