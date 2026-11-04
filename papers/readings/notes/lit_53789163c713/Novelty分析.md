# 贡献与评价

论文列出三点：(1) 定义“问题感知的数据准备”这一问题；(2) 多智能体框架 AutoPrep，Planner 使用 Chain-of-Clauses（CoC），Programmer 使用工具增强（从函数池选函数再推断参数）；(3) 在 TQA 数据集上评测。

CoC 的做法是先让 LLM 写一个带 UDF 的类 SQL Analysis Sketch，用 Binder 的语法解析器抽出子句并按执行顺序排序，再把每个子句与相关列的取值一起交给 LLM 生成逻辑操作，最后补一个只保留相关列的 Filter。逻辑/物理分离借鉴 DBMS，但物理实现按问题即时生成，而不是预先定义。

阅读者分析：真正新的部分是“把数据准备放在问答之前、以子句为单位对齐问题与列”。三种操作和函数池本身都很常规；Analyzer 用 NL2SQL，所以收益也包含了“让表能被 SQL 正确执行”的成分。扩展性只在一个新增 Transform 操作的实验中验证。

依据：§1 Contributions，PDF p.3；§4.2、Figure 5，PDF pp.6–7；§5.1–5.2，PDF pp.7–8；§6.5 Exp-6，PDF p.11。
