### 2021 Microsoft x TSMC careerhack 決賽
### 主題：聊天機器人
### 作品-美食公道伯

## 工具
- Microsoft Azure Service, including LUIS, SQL database, Application Insights.
- QnA Maker
- google map API
- Line messaging API
- 爬蟲相關工具

## 主題發想
等等要吃什麼？
附近有啥好吃的？
會不會踩到雷啊？
這三個問題是現代人對於美食需求的三大問題
 
## 作法
- 透過Azure的自然語言模型LUIS來對使用者的輸入進行分析判斷，知道其intent後以擷取句子中的entity來進行相對應的推薦
- 透過QnA Maker建立知識庫，以及聊天機器人相對應的問與答支援
- 透過BOT Framework模擬器跑模擬
- 以Line作為channel

## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)
