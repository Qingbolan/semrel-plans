# workload分析

**验证什么。** 领域整理能否用混合程序保持few-shot效果并少调用LLM；另独立验证工具型Agent是否更好发现相关表。两种证据不能互相冒用。

**数据、单位与gold。** §6表2为9数据集5任务：Amazon-Google/Abt-Buy商品对匹配（F1）；Buy/Restaurant人工遮盖属性补全（匹配准确率）；WikiNBA网页19属性抽取（token F1）；OS推文二分类（准确率）；Spider/OTT-QA/KaggleDBQA相关表发现（表集合F1）。gold来自原任务标签，表发现用参考SQL涉及表或OTT-QA标注。验证小模型用1,024条未标注样本加LLM伪标签，OS附录批量实验512条；未从本文核出每个主实验确切test条数，不能拿完整源数据规模代替。

**最有说服力用例（附录C原始工具轨迹重述）。** 用户问员工过去职位，目标找出可回答的表。使用前LLM-only只看BM25前20候选标题/schema；使用后Agent搜索employees/job/past，再查employees、jobs、job_history的schema，按返回内容继续选表。这里确有观察驱动的数据探索，不只是缓存分类结果。

**baseline及公平性。** 表发现：BM25、DrQA取top3（Spider/KaggleDBQA）或top1（OTT-QA），LLM-only看BM25前20；SEED可多次工具访问。匹配另对DITTO、MatchGPT；抽取对EVAPORATE-DIRECT/CODE+及DOM-LM等。监督模型训练量和LLM工具信息量不同，不能全部视作等预算。主成本LLM R是被LLM处理比例，不等于总token或训练总成本。

**效果范围。** 附录B.1表8：Spider F1为85.7，对LLM-only50.7；OTT-QA反降至67.8，对71.0；KaggleDBQA63.5，对56.1。§6的约90%调用比例下降来自实体匹配，不能宣称探索任务也下降90%。

来源：[本轮读v3，2024-04-24](https://arxiv.org/abs/2310.00749v3)。本分析为原文重述与比较边界判断，未复现实验。
