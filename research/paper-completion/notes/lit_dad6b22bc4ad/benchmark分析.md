# 评测与边界

**基线**（§4.2）：Jupyter-AI、CoML（利用离线任务知识）、同一 LLM 的 PoT（Program-of-Thoughts）vanilla agent；QRData 另加 GPT-4 (PoT)。作者只比较单轮代码生成方法，排除 ReAct 等多轮带错误反馈的 agent。

**实验 1（DSEval，Table 1）**：通过率如下。

| 模型 | 方法 | LeetCode | SO | Exercise | Kaggle |
|---|---|---|---|---|---|
| Llama-3.1-70b | Jupyter-AI | 0.733 | 0.427 | 0.679 | 0.465 |
| Llama-3.1-70b | CoML | 0.683 | 0.794 | 0.783 | 0.577 |
| Llama-3.1-70b | PoT | 0.725 | 0.739 | 0.747 | 0.539 |
| Llama-3.1-70b | DSMentor | 0.792 | 0.837 | 0.752 | 0.577 |
| Claude-3.5-Sonnet | Jupyter-AI | 0.850 | 0.477 | 0.693 | 0.595 |
| Claude-3.5-Sonnet | CoML | 0.875 | 0.809 | 0.643 | 0.535 |
| Claude-3.5-Sonnet | PoT | 0.800 | 0.804 | 0.745 | 0.641 |
| Claude-3.5-Sonnet | DSMentor | 0.892 | 0.837 | 0.781 | 0.678 |

（表格列序由抽取文本还原，并用正文"Exercise +8.8%、Kaggle +8.3%、LeetCode +5.9%、SO +4.3%"核对一致。）

**实验 2（QRData，Table 2）**：

| 方法 | 总通过率 | 多选/数值 | 统计/因果 |
|---|---|---|---|
| GPT-4 (PoT) | 0.491 | 0.460/0.540 | 0.725/0.368 |
| Llama-3.1-70b (PoT) | 0.442 | 0.480/0.384 | 0.615/0.351 |
| Claude-3.5-Sonnet (PoT) | 0.471 | 0.495/0.436 | 0.646/0.379 |
| DSMentor-Llama | 0.508 | 0.566/0.419 | 0.676/0.419 |
| DSMentor-Claude | 0.543 | 0.602/0.452 | 0.707/0.456 |

因果题上 DSMentor-Claude 0.456 对 GPT-4 0.368（+8.8 个百分点）。

**实验 3（消融，Tables 3–7、Figure 4）**：见贡献与评价页；检索示例数增加时 Llama 在多轮数据集上常下降，Claude 通常上升。

**边界**：

- 摘要中的"提升 5.2%/8.8%"是绝对百分点差（阅读者分析）。
- Llama 版在 Exercise 上低于 CoML（0.752 对 0.783），在 Kaggle 上与 CoML 持平。
- 无方差、置信区间；无成本或延迟报告；记忆利用了测试题评测标签，与无反馈基线条件不同（阅读者分析）。
- 论文未写局限章节；结论只列出自适应课程、更强记忆机制、多智能体扩展等未来方向。

依据：[arXiv:2505.14163v1](https://arxiv.org/abs/2505.14163)，摘要 p.1；§4.2–4.4、Tables 1–7、Figure 4，PDF pp.6–11；§5，p.10。
