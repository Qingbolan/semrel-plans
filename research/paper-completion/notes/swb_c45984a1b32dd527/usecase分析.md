# 具体用例

**MuSR 谋杀谜题**：DeepSeek-V3 先在训练题上以 ReAct 方式解题，正确轨迹中的步骤被归类为“核对不在场证明”“检查时间线”等动作，再合成子程序。Figure 2 与附录 A.1.1 给出的 DeepSeek-V3 库包含 5 个子程序，例如：

- `investigate_evidence(narrative, focus)`：针对 focus（嫌疑人、凶器、地点等）分析手段、动机、机会、不在场证明一致性和物证，留意铁证式排除、矛盾证据和证人可靠性，返回按证据类别组织的文本。
- `initialize_suspect_analysis(narrative, focus)`：找出受害者和全部嫌疑人，提取初始线索，警惕叙事中的误导信息。

其余三个是 `determine_if_killer`、`evaluate_suspect_evidence`、`summarize_investigation_progress`。测试时智能体只提供 focus，叙事文本自动绑定，由一次 LLM 调用按规格执行，结果作为观察返回。DeepSeek-V3 上谋杀谜题准确率从 ReAct 的 45.0% 升至 75.0%。Gemini 2.5 Flash 独立归纳出另一套 5 个子程序（如 `investigate_means_and_weapon`、`formulate_killer_conclusion`），准确率从 78.0% 升至 86.0%。

依据：[arXiv:2606.02994v2，27 页](https://arxiv.org/pdf/2606.02994)，Figure 2、§3.3、Table 2、附录 A.1.1、A.2.1，PDF pp.2、5–6、12–14。
