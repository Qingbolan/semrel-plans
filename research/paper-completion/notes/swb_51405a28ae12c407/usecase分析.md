# 具体用例

Figure 3（协议 512，PDF p.5）是一份连接（ligation）反应协议：第一句引入 vial，之后各句省略 vial，最后一句用转喻 "ligation mixture" 指代它。标注者在模拟器中依次输入命令：把 "chill" 定为温度操作、把 vial 指派为其输入；模拟器检查缺失论元并只补全当前状态下合法的命令（Figure 2，PDF p.2）。最终 PEG 用 `succ` 串起各操作，并把 vial 作为每步的 `ARG0`。

研究者拿到 PEG 后，可把 swirl 映射到 Autoprotocol 的 mix（Agitate），并为 gently 指定具体转速、补上缺失的孵育温度（§1、§3，PDF pp.1、4）。

阅读者分析：在语义查询场景中，PEG 可支持"哪些协议在离心前对同一容器做过温度处理"一类跨句、按实体追踪的问题，但这属于派生用途，原文没有检索或问答评测。
