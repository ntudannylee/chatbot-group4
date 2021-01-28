# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from flask import Config
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint, QnAMakerOptions
# from botbuilder.schema import ChannelAccount
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext, CardFactory
from botbuilder.schema import ChannelAccount, HeroCard, CardImage, CardAction
from websrestaurantrecom import webcrawl
from restaurant_recom import googlemaps_API, show_photo, googlemaps_search_location
from sql import DB_query
from linebot.models.sources import SourceUser

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
        # self.user_id = str(SourceUser.sender_id())

# define what we response
    async def on_message_activity(self, turn_context: TurnContext):
   
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0 and (turn_context.activity.text != response[0].answer):
            await turn_context.send_activity(MessageFactory.text(response[0].answer))
        else:
            if turn_context.activity.text == "wait":
                return await turn_context.send_activities([
                    Activity(
                        type=ActivityTypes.typing
                    ),
                    Activity(
                        type="delay",
                        value=3000
                    ),
                    Activity(
                        type=ActivityTypes.message,
                        text="Finished Typing"
                    )
                ])
            elif turn_context.activity.text == "test sql":
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
            
            
            # 書文的func
            elif "吃" in turn_context.activity.text: 

                msg = '請輸入您目前的地點或是附近的景點 🧐（例如：北車、公館）（小提示：點擊Line的+號可以傳地址上來呦!）'
       
                await turn_context.send_activity(msg)

            elif('_$' in turn_context.activity.text):
                money_status = 1
                # 判斷price_level
                if('_$$' in turn_context.activity.text):
                    money_status = 2
                elif('_$$$' in turn_context.activity.text):
                    money_status = 3
                    
                restaurants_dict = googlemaps_API(turn_context.activity.text, money_status)
                print('money_status:', money_status)
                # 沒有餐廳的狀況
                if(len(restaurants_dict) == 0):
                    message = "您附近沒有相對應的餐廳可以推薦呦，輸入『吃』來繼續👀"   

                elif(len(restaurants_dict) >= 5):
                    message = MessageFactory.carousel([
                            CardFactory.hero_card(HeroCard(title=restaurants_dict[0]['name'], text='推薦指數 : ' + str(restaurants_dict[0]['rating']), images=[CardImage(url=show_photo(restaurants_dict[0]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[0]['location_x']) + "," + str(restaurants_dict[0]['location_y']) +"&query_place_id="+str(restaurants_dict[0]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                            CardFactory.hero_card(HeroCard(title=restaurants_dict[1]['name'], text='推薦指數 : ' + str(restaurants_dict[1]['rating']), images=[CardImage(url=show_photo(restaurants_dict[1]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[1]['location_x']) + "," + str(restaurants_dict[1]['location_y']) +"&query_place_id="+str(restaurants_dict[1]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                            CardFactory.hero_card(HeroCard(title=restaurants_dict[2]['name'], text='推薦指數 : ' + str(restaurants_dict[2]['rating']), images=[CardImage(url=show_photo(restaurants_dict[2]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[2]['location_x']) + "," + str(restaurants_dict[2]['location_y']) +"&query_place_id="+str(restaurants_dict[2]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[2]['name']+"_評論")])),
                            CardFactory.hero_card(HeroCard(title=restaurants_dict[3]['name'], text='推薦指數 : ' + str(restaurants_dict[3]['rating']), images=[CardImage(url=show_photo(restaurants_dict[3]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[3]['location_x']) + "," + str(restaurants_dict[3]['location_y']) +"&query_place_id="+str(restaurants_dict[3]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[3]['name']+"_評論")])),
                            CardFactory.hero_card(HeroCard(title=restaurants_dict[4]['name'], text='推薦指數 : ' + str(restaurants_dict[4]['rating']), images=[CardImage(url=show_photo(restaurants_dict[4]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[4]['location_x']) + "," + str(restaurants_dict[4]['location_y']) +"&query_place_id="+str(restaurants_dict[4]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[4]['name']+"_評論")])),
                    ])
                # 資料少於五筆的情況
                else:
                    if len(restaurants_dict) == 4:
                        message = MessageFactory.carousel([
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[0]['name'], text='推薦指數 : ' + str(restaurants_dict[0]['rating']), images=[CardImage(url=show_photo(restaurants_dict[0]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[0]['location_x']) + "," + str(restaurants_dict[0]['location_y']) +"&query_place_id="+str(restaurants_dict[0]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[1]['name'], text='推薦指數 : ' + str(restaurants_dict[1]['rating']), images=[CardImage(url=show_photo(restaurants_dict[1]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[1]['location_x']) + "," + str(restaurants_dict[1]['location_y']) +"&query_place_id="+str(restaurants_dict[1]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[2]['name'], text='推薦指數 : ' + str(restaurants_dict[2]['rating']), images=[CardImage(url=show_photo(restaurants_dict[2]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[2]['location_x']) + "," + str(restaurants_dict[2]['location_y']) +"&query_place_id="+str(restaurants_dict[2]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[2]['name']+"_評論")])),
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[3]['name'], text='推薦指數 : ' + str(restaurants_dict[3]['rating']), images=[CardImage(url=show_photo(restaurants_dict[3]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[3]['location_x']) + "," + str(restaurants_dict[3]['location_y']) +"&query_place_id="+str(restaurants_dict[3]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[3]['name']+"_評論")])),
                        ])
                    if len(restaurants_dict) == 3:
                        message = MessageFactory.carousel([
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[0]['name'], text='推薦指數 : ' + str(restaurants_dict[0]['rating']), images=[CardImage(url=show_photo(restaurants_dict[0]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[0]['location_x']) + "," + str(restaurants_dict[0]['location_y']) +"&query_place_id="+str(restaurants_dict[0]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[1]['name'], text='推薦指數 : ' + str(restaurants_dict[1]['rating']), images=[CardImage(url=show_photo(restaurants_dict[1]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[1]['location_x']) + "," + str(restaurants_dict[1]['location_y']) +"&query_place_id="+str(restaurants_dict[1]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[2]['name'], text='推薦指數 : ' + str(restaurants_dict[2]['rating']), images=[CardImage(url=show_photo(restaurants_dict[2]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[2]['location_x']) + "," + str(restaurants_dict[2]['location_y']) +"&query_place_id="+str(restaurants_dict[2]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[2]['name']+"_評論")])),
                        ])
                    if len(restaurants_dict) == 2:
                        message = MessageFactory.carousel([
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[0]['name'], text='推薦指數 : ' + str(restaurants_dict[0]['rating']), images=[CardImage(url=show_photo(restaurants_dict[0]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[0]['location_x']) + "," + str(restaurants_dict[0]['location_y']) +"&query_place_id="+str(restaurants_dict[0]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[1]['name'], text='推薦指數 : ' + str(restaurants_dict[1]['rating']), images=[CardImage(url=show_photo(restaurants_dict[1]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[1]['location_x']) + "," + str(restaurants_dict[1]['location_y']) +"&query_place_id="+str(restaurants_dict[1]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                        ])
                    if len(restaurants_dict) == 1:
                        message = MessageFactory.carousel([
                                CardFactory.hero_card(HeroCard(title=restaurants_dict[0]['name'], text='推薦指數 : ' + str(restaurants_dict[0]['rating']), images=[CardImage(url=show_photo(restaurants_dict[0]['photo_reference']))], buttons=[CardAction(type="openUrl",title="地圖",value="https://www.google.com/maps/search/?api=1&query=" + str(restaurants_dict[0]['location_x']) + "," + str(restaurants_dict[0]['location_y']) +"&query_place_id="+str(restaurants_dict[0]['place_id'])), CardAction(type="imBack",title="點此看評論",value=restaurants_dict[0]['name']+"_評論")])),
                        ])
                    

                await turn_context.send_activity(message)

            else:              
                message = MessageFactory.carousel([
                        CardFactory.hero_card(
                          HeroCard(title='您的所在位置為：' + str(turn_context.activity.text)
                        , subtitle= '請選擇您的預算區間： 🤑'
                        , buttons=[CardAction(type="imBack",title="$$$",value=str(turn_context.activity.text) + "_$$$")
                        , CardAction(type="imBack",title="$$",value=str(turn_context.activity.text) + "_$$")
                        , CardAction(type="imBack",title="$",value=str(turn_context.activity.text) + "_$")]
                        ))
                
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
                await turn_context.send_activity("美食公道伯在此🧙‍♂️，請輸入『我要大吃特吃』以繼續")