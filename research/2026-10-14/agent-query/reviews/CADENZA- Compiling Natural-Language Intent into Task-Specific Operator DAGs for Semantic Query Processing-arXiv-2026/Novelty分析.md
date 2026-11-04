# 贡献与边界

贡献在于把一个语义算子内部的任务结果作为关系优化对象，并联动结构选择、按行实现路由和连续参数优化。语义替代采用经验验证，区别于有依赖条件约束的等价重写。本文不宣称一般语义正确性保证。

§1明确joint optimization across operators不在当前范围。§6.2缓存的是intent signature与data profile对应的物理计划；不是任意两条query之间自动共享所有中间数据，更不是共享答案。分布漂移仍需要重新采样调参。

评测需要保留条件：24小时timeout，部分E-Commerce结果用SF500外推；每个baseline平均值取其能执行的query交集；ThalamusDB设error=0、去掉token上限；部分join关闭Abacus；AFlow/DyFlow是作者扩展版。

原文也有待核实差异：Cars Q3正文§7.2写damaged，附录J写not damaged；Wildlife Q8的正文模态概述与附录J的图像/音频联合查询不一致。归档须保留版本，不用正文摘要覆盖原始query文件。
