# 工作负载与输入

§4.0.1从MMQA、HybridQA、HotpotQA、ManyModalQA、TAT-QA各分层抽300题，共1500题，分别在三后端运行。Codex agent额外比较仅为六种backend/dataset组合、每组100题，不能混成全量评测。

MMQA与ManyModalQA输入可能包含表、文本和图片；HybridQA每题为Wikipedia表及关联文本；HotpotQA是多跳文本；TAT-QA为财务表格和段落。环境是已给定的数据上下文、schema/preview及后端API参考，未要求开放Web搜索。

300是评测题数，100是对照抽样题数，均不是记录batch size。文章没有逐题发布全部输入字段清单；本轮只记录论文明确的信息，未补造原始JSON。
