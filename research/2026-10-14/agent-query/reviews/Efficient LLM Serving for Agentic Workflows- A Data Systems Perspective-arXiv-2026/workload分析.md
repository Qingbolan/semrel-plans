# 工作负载与输入

§7.1：MapReduce、Debate用200道MMLU问题和100个TAT-QA context（每context6题）；Reflect用200个TAT-QA context（每个6题）；Iterative/Parallel用Amazon Reviews中200/100个item，每item60评论，分成6块、每块10条。

§7.2 Trading输入为100支股票、连续两天的公司简介、股价、社交帖文等。第一天预热，第二天评测；图7的batch size为8、16、32、64、80个query。数据环境是已采集金融资料和给定工作流/提示角色，不是实时下单环境。

模型批处理由引擎处理；“10条评论/块”是记录分块，“16个股票query”是工作流输入批次，二者必须分列。
