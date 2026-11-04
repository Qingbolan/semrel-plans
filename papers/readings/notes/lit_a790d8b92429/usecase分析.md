# 具体用例

论文 Figure 1 / Examples 1–3 的用例：一张表含 Name、Admission Date、Address 三列。Admission Date 中混有 "Fri Jan 1st 10:36:28 2021" 与 "1996.07.10 AD at 15:08:56" 两种格式，Address 的写法也不统一。数据科学家只输入一句需求“日期列输出格式为 'MM/DD/YYYY HH:MM:SS'”。

CleanAgent 的 Column-type Annotator 判定 Admission Date 为 date 类型、Address 为 address 类型；Python Programmer 生成 `clean_date(df, column='Admission Date', output_format='MM/DD/YYYY HH:MM:SS')` 与 `clean_address(df, column='Address')`。

Code Executor 执行代码并返回 T′（如地址规范为 "1234 W. Main Hts., LA, 57033"）。

在 Web 界面（§6，Figure 3）中，用户上传 CSV → 点击开始 → 依次看到类型标注、生成代码、执行结果；若结果不满意，可再用自然语言追加需求重新运行。

在本项目语义算子视角下，这对应“按列的语义类型识别 + 确定性转换函数调用”，LLM 只负责类型判定与参数填写，逐单元格转换由库函数完成——与逐单元格调用 LLM 的语义映射相比成本结构不同。此为项目派生解读（阅读者分析）。

依据：[Qi, Miao & Wang，VLDB 2025 Workshop DATAI，4 页](https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/DATAI/DATAI25_8.pdf)，§1、§3、§6，Figures 1–3，p.1–4。
