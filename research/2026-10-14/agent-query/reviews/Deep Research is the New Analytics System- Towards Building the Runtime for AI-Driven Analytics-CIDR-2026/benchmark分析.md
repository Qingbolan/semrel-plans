# 基准评测

§4表1（KramaBench，一条query，各3次）：手工语义程序误差17.00%、$1.66、215.2秒；CodeAgent误差27.56%、$0.03、77.0秒；PZ compute误差0.02%、$1.17、583.0秒。原型提高准确性但增加延迟。

表2（Enron，一条query，各3次）：CodeAgent F1=50.53%、$0.08、37.0秒；CodeAgent+ F1=98.67%、$3.76、1999.9秒；PZ compute F1=98.67%、$0.87、546.2秒。相同F1下相对CodeAgent+费用/耗时下降76.8%/72.7%。CodeAgent及工具采用GPT-4o，原型允许优化器选较便宜模型。

只有邮件选取质量被计分，不能据此声称sender/subject/summary字段全部正确；没有对全部KramaBench运行，也没有独立复现实验。
