from config import *
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClient:
    def __init__(self):
        self.client = WebClient(token=SLACK_BOT_TOKEN)

    def get_user_name_by_id(self, logger, user):
        response = self.client.api_call(
            api_method='users.info',
            params={'user': user}
        )
        logger.info(f'response: {response}')
        return response['user']['name']
