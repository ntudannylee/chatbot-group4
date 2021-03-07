### 2021 Microsoft x TSMC careerhack 決賽
### 主題：聊天機器人 - 美食公道伯

## 工具
- Microsoft Azure Service, including LUIS, SQL database, Application Insights.
- QnA Maker
- google map API
- Line messaging API
- 爬蟲相關工具

## 主題發想
![image](https://github.com/ntudannylee/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%871.jpeg)
![image](https://github.com/ntudannylee/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%873.jpeg)
![image](https://github.com/ntudannylee/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%874.jpeg)
![image](https://github.com/ntudannylee/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%875.jpeg)
![image](https://github.com/ntudannylee/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%876.jpeg)
![image](https://github.com/ntudannylee/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%877.jpeg)
![image](https://github.com/ntudannylee/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%878.jpeg)

 
## DEMO截圖
加入好友

<img src="https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E5%8A%A0%E5%85%A5%E5%A5%BD%E5%8F%8B.png" width="100" height="100">

四大功能，包括使用說明、個人化推薦、瀏覽紀錄、我的最愛

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E5%9B%9B%E5%80%8B%E5%8A%9F%E8%83%BD.png)

個人化推薦

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E5%80%8B%E4%BA%BA%E5%8C%96%E6%8E%A8%E8%96%A6.png)

使用方式：可輸入我想吃XX or 我在哪 or 我在XX想吃YY，系統都會推薦給您餐點

e.g. 我在公館

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E6%88%91%E5%9C%A8%E5%85%AC%E9%A4%A8.png)

e.g. 我想吃牛排

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E6%88%91%E6%83%B3%E5%90%83%E7%89%9B%E6%8E%92.png)

e.g. 我想在文山區喝咖啡

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E6%88%91%E6%83%B3%E5%9C%A8%E6%96%87%E5%B1%B1%E5%8D%80%E5%96%9D%E5%92%96%E5%95%A1.png)

點擊預算之後，系統就會發送美食字卡給使用者

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E6%88%91%E5%9C%A8%E5%85%AC%E9%A4%A8%EF%BC%84%EF%BC%84%EF%BC%84.png)

點擊地圖會導到google map應用程式app

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E5%9C%B0%E5%9C%96.png)

點擊評論會抓各大美食部落格的字卡給使用者

![image](https://github.com/ntudannylee/chatbot-group4/blob/master/demo_%E8%A9%95%E8%AB%96.png)

 
## 作法
- 透過Azure的自然語言模型LUIS來對使用者的輸入進行分析判斷，知道其intent後以擷取句子中的entity來進行相對應的推薦
- 透過QnA Maker建立知識庫，以及聊天機器人相對應的問與答支援
- 使用google map API查看餐廳的地理位置以及相對應的評分
- 透過BOT Framework模擬器跑模擬
- 利用beautifulsoup對部落格進行爬蟲
- 以Line作為channel跟使用者互動

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
