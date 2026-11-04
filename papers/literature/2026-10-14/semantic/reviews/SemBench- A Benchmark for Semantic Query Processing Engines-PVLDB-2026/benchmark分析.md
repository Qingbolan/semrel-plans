# benchmark分析

§5.1主实验EC2 g4dn.2xlarge（32GB RAM、8vCPU、T4 16GB，仅embedding用GPU），扩展实验双Xeon Gold5218/384GB Ubuntu。模型Gemini2.5Flash，适用系统temperature0；LOTUS1.1.3，Palimpzest0.8.2，ThalamusDB0.1.15，BigQuery2000slots。每实验5次。

表5在共同支持子集上，join均值：LOTUS质量.614/541.1s/$2.74，PZ.703/454.3s/$3.29，ThalamusDB.487/387.3s/$.14，BigQuery.601/69.4s/$1.02。便宜与更高质量并不一致；不可把最低费解释为最好。

MMQA Q7基础scale200导致40000次pair判断，PZ约35分钟、LOTUS约40分钟；scale400为160000次。E-Commerce Q8的图像pair累积可令内存达到约250/150/100GB（ThalamusDB/LOTUS/PZ）。规模实验总模型费$9935.80、约18天，不是单query费用。超时规则是1小时后该系统不跑更大scale，但本次不强制终止。以上结果是作者报告，未复现。

来源：[原论文](https://arxiv.org/abs/2511.01716v2)。本分析据所列版本全文核读，未复现实验。
