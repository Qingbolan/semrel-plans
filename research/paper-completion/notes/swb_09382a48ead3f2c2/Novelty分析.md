# 贡献与评价

**原文列出的三项贡献**（§I，PDF p.2）：
1. LogiCode 框架：三模块 Code Prompt → Code Generation → Code Execution，把规则解析为逻辑表达式 L(r)，为每条规则选择 API A(r)，合成代码 c = ⋃{L(r), A(r)}（§III-C，式 1–3，PDF pp.4–5）；
2. LogiBench：结合 LLM 自动评估和专家人工评估的评测协议；
3. LOCO-Annotations 数据集，已在 GitHub 公开。

**评价（阅读者分析）**：
- 思路类似 ViperGPT 式"视觉程序生成"在工业检测上的应用，核心创新在任务迁移和标注数据，而非新的推理机制。
- find() 从 LOCO-Annotations 读取对象位置（Table I），§IV-D 也承认依赖像素级标注，作者把弱化这一依赖列为未来工作。因此 Table III 中 LogiCode 与 ST、EfficientAD 等无监督方法的比较条件不对等：后者没有使用对象分割或人工规则。原文也说"使用 LOCO-Annotations 可以利用额外数据"（§IV-C，PDF p.8）。
- 代码生成成功率约 0.59，推理准确率只在成功执行的代码上统计（§IV-C），主表准确率是否也只基于成功代码，原文没有说清。
- 规则由专家人工定义，没有报告规则编写成本，也没有测试规则缺失时的表现。
