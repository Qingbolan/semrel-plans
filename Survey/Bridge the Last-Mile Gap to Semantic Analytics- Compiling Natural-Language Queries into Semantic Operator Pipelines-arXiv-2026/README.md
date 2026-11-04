# Bridge the Last-Mile Gap to Semantic Analytics: Compiling Natural-Language Queries into Semantic Operator Pipelines

Palimpzest、LOTUS 等语义算子系统要求用户自己选算子、排顺序、写谓词并适配各后端 API。NL2Pipe（Dong、Li、Gurajada、Wang，夏威夷大学 / LinkedIn）把自然语言问题编译成可执行的语义算子流水线，分三阶段：Query-Data Linker 在数据中定位问题实体并发现问题里没出现的“桥接实体”；Planner 生成后端无关的动作计划；Code Generator 借离线自动生成的参考文档翻译成目标后端代码。

在 5 个多跳/多模态 QA 数据集 × 3 个后端上，NL2Pipe 在多数配置中质量最高，例如 Palimpzest-HybridQA 的 F1 为 68.6（次优 Hardcoded 47.5），平均编译费用约 $0.013/题（§4.1，Table 1）。

[原文](https://arxiv.org/abs/2606.04641v1)

版本：arXiv 2606.04641v1（2026-06-03，cs.DB），13 页；首页 PVLDB 卷页与 DOI 为占位字段。已通读 §1–5、Tables 1–7，数字已对照全文复核（2026-11）；未复现实验。
