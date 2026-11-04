# 工作负载

| 数据集 | 内容 | 本文使用 |
|---|---|---|
| Spider | 200 个数据库、138 个领域；train 8,659、dev 1,034；按 SQL 难度分 easy/medium/hard/extra | dev 评测，train 作示例池；test 未公开，未评测 |
| Spider-Syn | 用同义词替换问题中与 schema 相关的词 | dev |
| Spider-DK | 加入 5 类领域知识的改写 | dev |
| Spider-Realistic | 去掉问题中对列名的显式提及 | dev |
| SParC | 4,298 个连贯问题序列，12k+ 问题 | dev |
| CoSQL | 10k+ 标注 SQL，模拟用户与专家的对话 | dev |

（§4.1，pp.5–6）论文没有给出 Spider-Syn/DK/Realistic 和 SParC/CoSQL dev 的具体条数。

**设置**：主要用 GPT-3.5-turbo，GPT-4 只评测 Spider 上 Create(EoT)、ns=nd=2 一组（§4.3，p.7）。温度 0；最大输出 token 普通设置 150、CoT 设置 750（§4.1，p.5）。零样本实验确定每表附 3 行数据最好，后续一律用 3 行（§4.2，p.6）。鲁棒性和多轮实验用 Create(EoT) 与 ns=nd=2（§4.3–4.4，pp.8）；多轮一节写作 “Create(CoT)”，阅读者推测为 Create(EoT) 的笔误（阅读者分析）。

依据：§4.1–4.4，PDF pp.5–8。
