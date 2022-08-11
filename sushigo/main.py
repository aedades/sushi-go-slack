import os
import logging
import boto3
from sushigo.deck import *
from store.store import *
from store.memory import *
from slack_client.message import *
from flask import Flask, request, Response

logging.basicConfig(level=logging.INFO)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
# https://api.slack.com/apps/A01HJTN6TDZ/oauth
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.environ.get('AWS_DEFAULT_REGION', 'us-west-2')

HANDS_TABLE_NAME = 'hands-sushi-go-dev'
USERS_TABLE_NAME = 'users-sushi-go-dev'
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

if ENVIRONMENT == 'dev':
    MIN_NUM_PLAYERS = 1
else:
    MIN_NUM_PLAYERS = 2

app = Flask(__name__)

store_type = os.environ.get('STORE_TYPE', 'memory')

if store_type == 'memory':
    store = Memory()
# Fallback to memory store
else:
    store = Memory()

# Temp hardcoded values
USER_ID = 'U01H3KAPB71'
CHANNEL_ID = 'C01HFA41AAZ'

client = WebClient(token=SLACK_BOT_TOKEN)


def start_game(channel_id, username):
    # TODO: Check if game already in progress (channel_id in table)
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
    print(attachments)
    print(channel_id)
    post_slack_message(client, attachments, channel_id, None)
    

def add_player(channel_id, user_id):
    # TODO: Check if game already in progress (channel_id in table)
    user_info = UserInfo(None, channel_id)
    store.update_user(user_id, user_info)
    text = f'<@{user_id}> joined the game :wave:'
    post_slack_message(client, None, channel_id, text)

    if get_num_players() >= MIN_NUM_PLAYERS:
        prompt_start_game(channel_id, user_id)


def prompt_start_game(channel_id, user_id):
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
    post_slack_message(client, attachments, channel_id, None)


def get_num_players():
    # TODO: Check number of players
    return 1
    

def deal_hands(channel_id, deck):
    hands = deck.deal_hands(get_num_players())
    # TODO: Assign hands to unique players
    # get players in current game
    user_ids = store.get_users()
    hand_id = 1
    user_id = user_ids[0]
    for hand in hands:
        # if just 1 player, assign all hands to that player
        if len(user_ids) == 1:
            user_id = user_ids[0]
        else:
            user_id = user_ids.pop()

        hand_info = HandInfo(None, user_id, hand.pickle_hand(), channel_id, False)
        store.update_hand(hand_id, hand_info)
        prompt_player_pick(hand)
        hand_id += 1
        print(hand)


def prompt_player_pick(hand):
    # TODO: DM hand to player
    # TODO: Get player
    player_user_id = get_user_id()
    actions = []

    text = 'Choose a card to keep:'
    post_slack_message(client, None, player_user_id, text)

    for card_name, card in hand.cards.items():
        action = {
            'name': card_name,
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
            post_slack_message(client, attachments, player_user_id, text)
            actions = []

    attachments = [{
        'text': '',
        'callback_id': 'choose_card',
        'actions': actions
    }]
    post_slack_message(client, attachments, player_user_id, text)


# TODO: Get user_id from DB
def get_user_id():
    return USER_ID


@app.route('/command', methods=['POST'])
def command():
    # TODO: Verify request
    #if not request.form.get('token') == SLACK_WEBHOOK_SECRET:
    #    return '', 403
    print(request.form)
    print(request.data)
    channel_id = request.form.get('channel_id')
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
    except Exception as e:
        print(e)

    # TODO: Validate signature https://api.slack.com/authentication/verifying-requests-from-slack

    if command:
        if text == 'start':
            start_game(channel_id, username)
    elif callback_id:
        if callback_id == 'add_player':
            add_player(channel_id, user_id)
        elif callback_id == 'prompt_start_game':
            deck = init_deck()
            deal_hands(channel_id, deck)
        elif callback_id == 'choose_card':
            pass
            # TODO: Remove card from hand & add to player's deck
    else:
        text = 'Hello from the app! :sushi:'
        post_slack_message(client, None, channel_id, text)
    return Response(), 200


@app.route('/')
def hello_world():
    return 'Hello world!'
    # TODO: Return how to play


if __name__ == '__main__':
    app.run(debug=True)
