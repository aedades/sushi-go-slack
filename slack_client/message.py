from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def post_slack_message(client, attachments, channel, text):
    kwargs = {
        'channel': channel
    }
    if attachments != None:
        kwargs['attachments'] = attachments
    if text != None:
        kwargs['text'] = text
    try:
        response = client.chat_postMessage(**kwargs)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(e)
        assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'
