# 具体用例

**句子 S1**（§1，PDF p.2）：“[Bush] intends to curb the increase in harmful gas emissions and is counting on the good will of [US industrialists].”

- 观点表达：intends、counting on、good will。
- 来源：Bush、US industrialists。
- 链接：Bush—intends，Bush—counting on，US industrialists—good will。

这说明一个来源可以链接多个观点。

**句子 S2**：“By questioning [the Imam]'s edict [the Islamic Republic of Iran] made [the people of the world] understand…”。questioning 的来源是 the Islamic Republic of Iran，二者并不相邻，最近实体启发式会出错。

**隐式来源**（§8，PDF p.9）：“Anti-Soviet hysteria was firmly oppressed.” 两个观点都没有显式来源，本系统会把它们丢掉。

阅读者分析：对项目而言，这是“片段抽取 + 片段间关系”的联合语义抽取任务，可映射为“抽取 (holder, opinion) 对”的语义抽取算子；若这样使用，应保留句内范围、一对多约束、重叠/精确两种匹配口径，以及 7% 隐式来源的召回上限（阅读者分析）。
