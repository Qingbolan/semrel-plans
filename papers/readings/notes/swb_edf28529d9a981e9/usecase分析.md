# 具体用例

Figure 1（p.2）以 AAE 第 5 篇作文《Living and studying overseas》为例：首段的 major claim“留学者将从中获得许多技能”被标为 value；中间段各以一个 value claim 开头，后接若干 hypothetical-instance、common-ground、fact 等 premise；末段 major claim 再次为 value。

按 §5 的方法，这篇作文的段落级 semantic flow 例如 `(C:Value, HI, HI, …)`，合并连续重复后得到 change flow `(C:Value, HI)`；全文级 claim change flow 形如 `(M:Value, C:Value, …, M:Value)`。Table 4（p.7）显示全文级最常见的流正是 `(M:Value, C:Value, M:Value)`（0.09），中段最常见的 claim+premise 流为 `(C:Value, CG)`（0.08）。

阅读者分析：若把这类标注用于下游语义检索，可构造“找出以 policy 类 major claim 开头、中段用 statistics 支持 fact claim 的作文”这类过滤，但这是派生用法，原文未评测任何检索或查询任务。
