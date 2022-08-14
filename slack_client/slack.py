from config import *
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClient:
    '''
    DynamoDB implementation of the Store Interface

    Attributes
    ----------
    client : slack_sdk.WebClient

    Methods
    -------
    get_user_name_by_id(logger, user_id)
        Return the user's name given a user_id
    '''
    def __init__(self):
        self.client = WebClient(token=SLACK_BOT_TOKEN)

    def get_user_name_by_id(self, logger, user_id):
        '''Return the user's name given a user_id'''
        response = self.client.api_call(
            api_method='users.info',
            params={'user': user_id}
        )
        logger.info(f'response: {response}')
        return response['user']['name']
