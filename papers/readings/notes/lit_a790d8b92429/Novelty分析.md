# 贡献与评价

作者列出四项贡献（§1）：(1) 开源库 Dataprep.Clean，类型专用函数简化格式标准化；(2) CleanAgent，将 Dataprep.Clean 与基于 AutoGen 风格的 LLM agent 结合实现自动化；(3) Web 应用与界面；(4) GitHub 开源代码与演示视频。

技术要点：统一 API 形式 `clean_type(df, column_name, target_format)`，目前 142 个函数各对应一种数据类型（§2）；四 agent 工作流中 Chat Manager 持有全部历史消息，执行出错时把错误信息写入记忆并重试整个流程直到成功（§3，Figure 2）。

创新主要是工程/系统层面——“给 LLM 一个高层声明式工具库以缩小代码生成空间”——而非新的算法或学习方法；列类型标注和代码生成都依赖提示 GPT-4o，论文没有给出提示内容、重试上限或失败处理的细节。作为 4 页工作坊论文，评测深度有限，应视为思路与系统演示（阅读者分析）。

依据：[Qi, Miao & Wang，VLDB 2025 Workshop DATAI，4 页](https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/DATAI/DATAI25_8.pdf)，§1–§3，p.1–3。
