# 语义算子 Benchmark 与代码仓库核对

核对日期：2026-11-03。登记源 `config/benchmark-coverage.json`，构建生成 [收录核对表](../../../docs/benchmark-coverage.md)，并在 Paper 页面增加“收录核对”页签和代码仓库链接。

## 依据

- 论文身份：arXiv 摘要页的 `citation_title`、首次提交日期和摘要原文，保存在 `metadata.json`（含页面 SHA-256）。CoreSemDB 没有 arXiv 版本，依据 OpenReview 笔记 `ZtR4q390OK`（venue: COLM 2026）。
- 代码仓库：优先采用论文正文或摘要页给出的链接；commit 是 2026-11-03 `git ls-remote <repo> HEAD` 的结果。ThalamusDB、CAESURA、KathDB 的仓库是按系统名检索到的作者或机构仓库，论文中未给出链接，已在 `link_source` 标明。
- 查询规模：只引用 arXiv 或 OpenReview 摘要，以及 `Survey/` 中已有的七项分析。摘要没有给出规模的标为“摘要未给出”。
- 已收录数量：构建时按 `benchmark_id` / `scenario_id` 从 `query/queries.jsonl` 计算，不手写。

## 边界

- 本次没有下载论文全文，没有克隆仓库，也没有导入新的查询。
- “混合”列是对论文 workload 性质的判断，不是逐条审查；标 `?` 的需要读全文。
- SemBench 上游 HEAD（c4b2bcff）比图册固定的 commit（8c2cac89）新，尚未比对差异。
