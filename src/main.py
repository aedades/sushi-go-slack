import os
import json
import logging
from deck import *
from flask import Flask, request, Response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask_dynamo import Dynamo

logging.basicConfig(level=logging.INFO)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
# https://api.slack.com/apps/A01HJTN6TDZ/oauth
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.environ.get('AWS_DEFAULT_REGION', 'us-west-2')

app = Flask(__name__)

app.config['DYNAMO_TABLES'] = [
    dict(
        TableName='users',
        KeySchema=[dict(AttributeName='username', KeyType='HASH')],
        AttributeDefinitions=[dict(AttributeName='username', AttributeType='S')],
        ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    ), dict(
        TableName='groups',
        KeySchema=[dict(AttributeName='name', KeyType='HASH')],
        AttributeDefinitions=[dict(AttributeName='name', AttributeType='S')],
        ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    )
]

dynamo = Dynamo(app)

# Temp hardcoded values
USER_ID = 'U01H3KAPB71'

client = WebClient(token=SLACK_BOT_TOKEN)


def parse_payload(payload):
    payload = json.loads(request.form.get('payload'))
    print(payload)
    print(payload.keys())
    print(payload['actions'])
    print(payload['user']['id'])
    print(payload['callback_id'])
    return payload


def post_slack_message(attachments, channel, text):
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


def start_game(channel, username):
    attachments = [{
        'text': f'<@{username}> wants to start a game of Sushi Go! :sushi:',
        'callback_id': 'add_player',
        'actions': [
            {
                'name': 'add_player',
                'text': 'I want to play :raised_hand:',
                'type': 'button',
                'value': 'add_player'
            }
        ]
    }]
    post_slack_message(attachments, channel, None)
    

def add_player(channel, user_id):
    print(f'TODO: Add user_id:{user_id} to game')
    text = f'<@{user_id}> joined the game :wave:'
    post_slack_message(None, channel, text)

    if get_num_players() > 1:
        prompt_start_game(channel, user_id)


def prompt_start_game(channel, user_id):
    attachments = [{
        'text': f'Start the game with {get_num_players()} players?',
        'callback_id': 'prompt_start_game',
        'actions': [
            {
                'name': 'prompt_start_game',
                'text': 'Itadakimasu! :bento: (Start game)',
                'type': 'button',
                'value': 'deal_cards'
            }
        ]
    }]
    post_slack_message(attachments, channel, None)


def get_num_players():
    # TODO: Check number of players
    return 2


def init_deck():
    deck = Deck()
    deck.shuffle()
    return deck


def deal_hands(deck):
    hands = deck.deal_hands(get_num_players())
    # TODO: Save hand in DB, 
    for hand in hands:
        prompt_player_pick(hand)
        print(hand)
    return hands


def prompt_player_pick(hand):
    # TODO: DM hand to player
    # TODO: Get player
    player_user_id = get_user_id()
    actions = []

    text = 'Choose a card to keep:'
    post_slack_message(None, player_user_id, text)

    for card in hand.cards:
        action = {
            'name': card.name,
            'text': card.face,
            'type': 'button',
            'value': card.name
        }
        actions.append(action)
        if len(actions) == 5:
            attachments = [{
                'text': '',
                'callback_id': 'choose_card',
                'actions': actions
            }]
            text = ''
            post_slack_message(attachments, player_user_id, text)
            actions = []

    attachments = [{
        'text': '',
        'callback_id': 'choose_card',
        'actions': actions
    }]
    post_slack_message(attachments, player_user_id, text)


# TODO: Get user_id from DB
def get_user_id():
    return USER_ID


@app.route('/command', methods=['POST'])
def command():
    # TODO: Verify request
    #if not request.form.get('token') == SLACK_WEBHOOK_SECRET:
    #    return '', 403

    channel_name = request.form.get('channel_name')
    username = request.form.get('user_name')
    command = request.form.get('command')
    text = request.form.get('text')
    action = request.form.get('action')
    data = request.data
    try:
        payload = parse_payload(request)
        callback_id = payload['callback_id']
        user_id = payload['user']['id']
        channel_id = payload['channel']['id']
    except:
        pass

    # TODO: Validate signature https://api.slack.com/authentication/verifying-requests-from-slack

    if command:
        if text == 'start':
            start_game(channel_name, username)
    elif callback_id:
        if callback_id == 'add_player':
            add_player(channel_id, user_id)
        elif callback_id == 'prompt_start_game':
            # TODO: Save player order for passing hands around
            deck = init_deck()
            hands = deal_hands(deck)
            # TODO: Assign hands to players
        elif callback_id == 'choose_card':
            pass
            # TODO: Remove card from hand & add to player's deck
    else:
        text = 'Hello from the app! :sushi:'
        post_slack_message(None, channel, text)
    return Response(), 200


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True)
