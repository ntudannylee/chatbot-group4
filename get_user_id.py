class ConversationData:
    def __init__(
        self,
        timestamp: str = None,
        channel_id: str = None,
        prompted_for_user_name: bool = False,
    ):
        self.timestamp = timestamp
        self.channel_id = channel_id
        self.prompted_for_user_name = prompted_for_user_name



# import json

# from flask import Flask, request, abort

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,
# )

# # app = Flask(__name__)


# line_bot_api = LineBotApi('MfJeV1XmEPyhSFbKxhoE7YYqQhY3H94FJi+hx9OAfckSIcwZYa6J/3ZAPA1h2XwUQ47H1E2Uf8Fb1ODU/8o3E3XcK+uLfgbf0/ly9NX0BMTE1KgFH1U6rI0Dp3YWnkGsckwbTvbLrApUAUohUPZVWQdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('996d82ce5a05b038a3ab6861c732c868')

# # @app.route("/callback", methods=['POST'])
# # def callback():
# #     # get X-Line-Signature header value
# #     signature = request.headers['X-Line-Signature']

# #     # get request body as text
# #     body = request.get_data(as_text=True)

# #     app.logger.info("Request body: " + body)

# #     # handle webhook body
# #     try:
# #         handler.handle(body, signature)
# #     except InvalidSignatureError:
# #         abort(400)

# #     return 'OK'c


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     # get user id when reply
#     user_id = event.source.user_id
#     print("user_id =", user_id)

#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))

#     return user_id