# 具体用例

**ContractNLI 合同蕴含查询**（§7.2 p.10；§7.3 pp.10–11）。

```
contracts.sem_filter("Is this document a valid contract ... confidentiality obligations?")
  .sem_join(right_table=hypotheses, "Given the contract and hypothesis, does the contract entail the hypothesis?")
  .sem_map("Explain briefly why the contract entails the hypothesis, citing the relevant obligation or clause.")
```

1. 解析器在 CP 处把计划切为两个 stage：stage 1 对每份合同执行 sem_filter；stage 2 对每个（合同，假设）对执行蕴含判断与解释。
2. 一份合同通过 filter 后，Kalypso 执行 CP，为它生成 17 个子任务并放入 stage 2 的等待队列；合同前缀（平均 2,145 token）此时仍在 KV cache 中。
3. 调度器优先启动这些依赖任务，使 17 次蕴含判断与随后的解释生成都复用这段合同前缀，只需 prefill 假设和指令后缀；所有子任务完成后才释放父任务的预算（Algorithm 1 第 33、36–37 行）。
4. 若 stage 2 队列持续过长（饱和），预算向末阶段转移；若 stage 2 无活可干（饥饿），预算向 stage 1 转移，让更多合同进入流水线。

结果：Kalypso 1,062.4 s，Palimpzest 2,373.4 s（2.23×），相对 Lotus 4.57×；而且 Kalypso 在此负载上只用 oracle 模型，Lotus 对首个 filter 使用了代理模型级联（§7.3）。固定预算比例实验中，ContractNLI 在 1:9（首阶段 10%）时最好，自适应预算仍优于所有固定比例（Figure 10）。

阅读者分析：这个用例显示收益来源是“长左侧前缀 × 高扇出”；若每个子任务新增的内容很短或可复用前缀很小，额外内存的作用有限；原文对 BioDEX 指出右表反应平均仅 6.3 token，第二阶段增加内存效果较小（§7.3）。

依据：[arXiv 2607.23815v2](https://arxiv.org/abs/2607.23815)，§5.1、§5.3、§7.2–7.4、Figures 7、10，PDF pp.5–11。
