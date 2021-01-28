# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from flask import Config
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint, QnAMakerOptions
from botbuilder.ai.luis import LuisApplication, LuisRecognizer, LuisPredictionOptions
# from botbuilder.schema import ChannelAccount
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext, CardFactory, RecognizerResult
from botbuilder.schema import ChannelAccount, HeroCard, CardImage, CardAction, Activity, ActivityTypes
from websrestaurantrecom import webcrawl
from restaurant_recom import googlemaps_API, show_photo 
from sql import DB_query
from linebot.models.sources import SourceUser
from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(
        self, config: Config
        ):
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            ), QnAMakerOptions(
                score_threshold = 0.9
            )
        )

        luis_application = LuisApplication(
            config.LUIS_APP_ID,
            config.LUIS_API_KEY,
            "https://" + config.LUIS_API_HOST_NAME,
        )
        luis_options = LuisPredictionOptions(
            include_all_intents=True, include_instance_data=True
        )
        self.recognizer = LuisRecognizer(luis_application, luis_options, True)
        # self.user_id = str(SourceUser.sender_id())

# define what we response
    async def on_message_activity(self, turn_context: TurnContext):
        response = await self.qna_maker.get_answers(turn_context)
        recognizer_result = await self.recognizer.recognize(turn_context)
        intent = LuisRecognizer.top_intent(recognizer_result)
        if intent == "使用者地理位置":
            restaurants_dict = googlemaps_API(turn_context.activity.text)
            # 書文的func            
            message = MessageFactory.carousel([
                    CardFactory.hero_card(HeroCard(title=restaurants_dict[0]['name'], text='推薦指數 : ' + str(restaurants_dict[0]['rating']), images=[CardImage(url=show_photo(restaurants_dict[0]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[0]['location_x']) + "," + str(restaurants_dict[0]['location_y']) +"&query_place_id="+str(restaurants_dict[0]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                    CardFactory.hero_card(HeroCard(title=restaurants_dict[1]['name'], text='推薦指數 : ' + str(restaurants_dict[1]['rating']), images=[CardImage(url=show_photo(restaurants_dict[1]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[1]['location_x']) + "," + str(restaurants_dict[1]['location_y']) +"&query_place_id="+str(restaurants_dict[1]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                    CardFactory.hero_card(HeroCard(title=restaurants_dict[2]['name'], text='推薦指數 : ' + str(restaurants_dict[2]['rating']), images=[CardImage(url=show_photo(restaurants_dict[2]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[2]['location_x']) + "," + str(restaurants_dict[2]['location_y']) +"&query_place_id="+str(restaurants_dict[2]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[2]['name']+"_評論")])),
                    CardFactory.hero_card(HeroCard(title=restaurants_dict[3]['name'], text='推薦指數 : ' + str(restaurants_dict[3]['rating']), images=[CardImage(url=show_photo(restaurants_dict[3]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[3]['location_x']) + "," + str(restaurants_dict[3]['location_y']) +"&query_place_id="+str(restaurants_dict[3]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[3]['name']+"_評論")])),
                    CardFactory.hero_card(HeroCard(title=restaurants_dict[4]['name'], text='推薦指數 : ' + str(restaurants_dict[4]['rating']), images=[CardImage(url=show_photo(restaurants_dict[4]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[4]['location_x']) + "," + str(restaurants_dict[4]['location_y']) +"&query_place_id="+str(restaurants_dict[4]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[4]['name']+"_評論")])),
                ])
            await turn_context.send_activity(message)
        # elif intent == "使用者食物類別"：
        elif response and len(response) > 0 and (turn_context.activity.text != response[0].answer):
            await turn_context.send_activity(MessageFactory.text(response[0].answer))
        else:
            
            if turn_context.activity.text == "test sql":
                output = DB_query("Select ID from user_info")
                for i in range(0, len(output), 2):
                    await turn_context.send_activity(output[i] + ' ' + output[i+1])
            # elif turn_context.activity.text == "get my id":
            #     await turn_context.send_activity(self.user_id)
            elif "評論"in turn_context.activity.text:
                # 展宏的func
                re = webcrawl(turn_context.activity.text)
                # 佑誠的func

                message = MessageFactory.carousel([
                    CardFactory.hero_card(HeroCard(title=re["愛食記"][0], images=[CardImage(url=re["愛食記"][2])], buttons=[CardAction(type="openUrl",title="前往網頁",value=re["愛食記"][1])])),
                    CardFactory.hero_card(HeroCard(title=re["愛食記"][0], images=[CardImage(url=re["愛食記"][2])], buttons=[CardAction(type="openUrl",title="前往網頁",value=re["愛食記"][1])])),
                    CardFactory.hero_card(HeroCard(title=re["愛食記"][0], images=[CardImage(url=re["愛食記"][2])], buttons=[CardAction(type="openUrl",title="前往網頁",value=re["愛食記"][1])]))
                ])   
                await turn_context.send_activity(message)

# say helllo at the beginning
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")