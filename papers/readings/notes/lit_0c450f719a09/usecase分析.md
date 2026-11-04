# 具体用例

Figure 7 的多智能体编程例子：`WritePythonCode(task)` 产生 `code`，`WriteTestCode(task, code)` 产生 `test`，最后对 `code` 和 `test` 以 `perf=LATENCY` 调用 `get`。

Parrot 通过 `code` 变量识别两个请求的先后依赖，在服务端直接把第一个请求的输出送入第二个请求，不再经过客户端往返。两个最终变量被标为延迟敏感，并向上游传播。两个提示中的固定文本前缀会生成哈希，供与其他用户请求共享 KV cache。

阅读者分析：对本项目而言，map-reduce 文档摘要（大量并行 map 请求加一个 reduce）最接近语义算子批处理。Parrot 的启示是：把算子 DAG 和共享提示前缀暴露给服务层，可以把 map 阶段当作吞吐型 task group 调度；但论文只评估延迟/吞吐，不评估结果质量。

依据：[原文](https://www.usenix.org/system/files/osdi24-lin-chaofan.pdf)，§4.1、§5.1–5.2、Figures 7–9，PDF pp.6–8。
