# usecase

原文 §3.2 用一篇讨论克隆技术的示例议论文说明：引言段中"cloning is an important technology for humankind"是主要主张，同句"it would be very useful for developing novel cures"是支持它的主张；正文段"cloning will be beneficial for many people who are in need of organ transplants"是主张，"Cloned organs will match perfectly to the blood group and tissue of patients"等是支持它的前提。解析器对这样一篇文章输出成分跨度、类型、段内树和支持/攻击标签，作者设想把它用于写作辅助，例如给出关于论证的反馈。

阅读者分析：若项目把这一任务用作批量语义抽取（例如"列出每篇文章中没有前提支撑的主张"），需要保留段内树约束、主要主张不参与联合推断以及攻击关系极少（219 条）等边界；这是项目派生用法，原文未评测。

依据：[Stab & Gurevych, Computational Linguistics 43(3):619–660, 2017，42 页](https://aclanthology.org/J17-3005.pdf)，§1、§3.2，PDF pp.2、9–10。
