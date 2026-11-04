# benchmark分析

§4.1：Ubuntu、4颗XeonGold6148共80cores、2×4090、1TB RAM、6TB SSD、Python3.7；默认GPT4.1mini、Qwen3-Embedding-0.6B。成本单位是每文档每query的千token，延迟单位秒，不能标美元。7系统是Evaporate/PZ/LOTUS/DocETL/ZenDB/QUEST/UQE，含作者重实现及适配。

表3Finance extraction：PZ138.90ktoken/8.38s，LOTUS297.85/13.24，DocETL818.10/1509.08，ZenDB32.33/3.55，QUEST29.30/2.65，UQE124.02/5.83；Evaporate成本“-”不是零。WikiArt extraction UQE.92ktoken/.83s、QUEST1.20/.89s，说明短文分块未必划算。图2精度多数短数据约.85，Finance最佳约.52（图读近似，不伪造精确条形值）。

§4.6 Healthcare并发1/2/4/8：1.46/.74/.38/.20秒，F1均.53。modelcascade在困难Legal几乎总升级，反而增加费用；modelselection提升质量也可能花更多钱。图10聚类代替group属性抽取引入高相对误差，图11语义search减少join候选却误删匹配。结论应是数据条件下的折中，而非统一最佳系统。

本下载v1虽多处指向Appendix，文件在参考文献结束，没有附录模板/修改列表；详细query原文、系统commit和batch参数需作者artifact补证，不能从正文推造。

来源：[原论文](https://arxiv.org/abs/2510.27119v1)。本分析据所列版本全文核读，未复现实验。
