# 基准评测

§4.0.2主要模型gpt-5-mini，Codex对照gpt-5.1-codex-mini；后端执行统一gpt-5-mini。表1 Palimpzest-HybridQA：NL2Pipe EM/F1/LLM为59.3/68.6/73.3，mapping费$0.0156；Hardcoded为39.3/47.5/51.0，mapping费用不计。MMQA的NL2Pipe为51.7/57.1/63.3、$0.0134。

表4在100题比较中Palimpzest-HybridQA：Codex agent F1=52.9、$0.2521、mapping311.2秒；NL2Pipe F1=67.3、$0.0156、111.3秒。并非全部后端的完整总体值。离线参考文档每backend/dataset花费$0.40–0.70。

表7消融支持规划与参考文档的贡献，同时包含非单调结果。表6 Linker占编译耗时53%–61%。费用与延迟应分别记录mapping、execution、合计，不能将mapping单列称端到端成本。
