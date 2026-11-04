# 具体用例

**电视频道查询**（附录 B Table 13，p.12）：问题为 “Find the package choice and series name of the TV channel that has high definition TV.”

- 普通 few-shot 输出在 SELECT 中多选了 `Hight_definition_TV` 列。
- ACT-SQL 下 LLM 先输出 “Let's think step by step.”，再逐步链接：
  1. 根据 “TV channel that has high definition TV”，可能用到 `[TV_Channel.Hight_definition_TV]`；
  2. 根据 “package choice and series name”，可能用到 `[TV_Channel.Package_Option]` 和 `[TV_Channel.series_name]`；
  3. 最后给出 `SELECT package_option, series_name FROM TV_Channel WHERE Hight_definition_TV = 'yes'`，与 gold 一致（§4.3，p.7）。

**数据库内容提示的作用**（Table 1，p.6）：问题 “What are the names of the singers who are not French citizens?” 在不附数据时生成 `Citizenship != 'French'`；附 3 行数据后，LLM 看到单元格值 “France”，生成正确条件。

**多轮改写失败**（Table 10，p.9）：“What are all the airlines? / Of these, which is Jetblue Airways? / What is the country corresponding it?” 中第二句未去掉指代，导致第三句丢失 “airline” 关键词。

依据：§4.2–4.4、Tables 1、10、13，PDF pp.6–9、12。
