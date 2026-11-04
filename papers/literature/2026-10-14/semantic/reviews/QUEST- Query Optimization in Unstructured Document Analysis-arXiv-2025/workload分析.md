# workload分析

表1/§5.1：LCR从3000案例报告取100份，平均6247tokens，10属性、10查询；WikiText抓取200网页，10领域，平均1264tokens，20属性、25查询；SWDE取200网页，平均416tokens，16属性、15查询。主评测合计500文档50查询。

§5.4另构造60条双表join查询，以及3组各10条多表join查询。不能未经源artifact比对便把这些计数简单相加当作独立全部query ID。ground truth是LLM抽取后由10名研究生核验，查询随机选属性构造过滤再人工剔除不合理项。

默认采样约5%文档，证据聚类K=3（§4、§5.5）。5%是优化/证据采样比例，非batch size；文中没有统一的模型推理batch大小。文档可以分worker并行属于架构讨论，未做多查询联合批处理实验。

来源：[QUEST: Query Optimization in Unstructured Document Analysis](https://arxiv.org/abs/2507.06515v2)。
