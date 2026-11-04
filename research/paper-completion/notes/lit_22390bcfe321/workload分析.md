# workload

**数据来源**（§3.1、§5，PDF pp.3、6–7）：97 个真实数据集——39 个蚂蚁集团真实业务应用 + 58 个公开数据集（46 Kaggle、2 UCI、2 Mendeley、8 个学术/政府源：UCSD Amazon 评论、BIRD、Natural Earth、2 份 NYC TLC、U.S. BTS、NCI GDC、OWID）。

**任务**：真实业务端由 5 个业务单元的 30 位专家用 600+ 人时整理 600 个任务，按技能覆盖贪心选出 102 个；公开数据端生成 242 个任务（8 位专家、960 人时注释）。合计 344 个任务、342 个数据文件、27.3GB、18 种文件格式、123.1M 行、35.0K 属性；真实业务部分 5 个领域、20.1GB、7 种格式、59.4M 行（PDF p.3）。总构建投入 1,560+ 人时。

**领域**（Table 2，PDF p.7）：真实业务 5 个（Financial、Loan Model、Loan Risk、Marketing、Strategy），公开 10 个（Agriculture、Ecommerce、Energy、Entertainment、Healthcare、Real Estate、Sports、Social Network、Tourism、Transportation）。每任务数据量差异很大：Loan Model 3,304.1MB、Ecommerce 2,602.4MB，Loan Risk/Financial 不足 100MB。

**未说明**：每个领域的任务数正文未单独给出；无训练/测试划分（纯评测集）。阅读者注意：摘要称“5 real-world B2B use cases”指 5 个业务领域；Figure 1b 中真实业务一行标注 155、公开数据一行标注 433，原文未解释 155 的含义（推测为该部分覆盖的技能数）。

依据：[arXiv:2607.01647v1，14 页](https://arxiv.org/abs/2607.01647)，§3.1、§5、§6.1、Table 2，PDF pp.1、3、6–8。
