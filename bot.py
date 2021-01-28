# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from flask import Config
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint, QnAMakerOptions
# from botbuilder.schema import ChannelAccount
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext, CardFactory
from botbuilder.schema import ChannelAccount, HeroCard, CardImage, CardAction
from websrestaurantrecom import webcrawl
from sql import DB_query

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(self, config: Config):
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            ), QnAMakerOptions(
                score_threshold = 0.9
            )
        )

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
            else:
                re = webcrawl(turn_context.activity.text)
                message = MessageFactory.carousel([
                        CardFactory.hero_card(HeroCard(title=re["愛食記"][0], images=[CardImage(url=re["愛食記"][2])], buttons=[CardAction(type="openUrl",title="前往網頁",value=re["愛食記"][1])])),
                        CardFactory.hero_card(HeroCard(title=re["愛食記"][0], images=[CardImage(url=re["愛食記"][2])], buttons=[CardAction(type="openUrl",title="前往網頁",value=re["愛食記"][1])])),
                        CardFactory.hero_card(HeroCard(title=re["愛食記"][0], images=[CardImage(url=re["愛食記"][2])], buttons=[CardAction(type="openUrl",title="前往網頁",value=re["愛食記"][1])]))
                    ])#, buttons=[CardAction(title='button3')
                await turn_context.send_activity(message)

                # await (
                #     turn_context.send_activity(
                #         MessageFactory.content_url(url= re["愛食記"][2], content_type='image/jpg', text="There's the restaurants we find"))
                # )
                # await (
                #     turn_context.send_activity(
                #         MessageFactory.text(text= re["愛食記"][0])
                #     )
                # )

# say helllo at the beginning
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")