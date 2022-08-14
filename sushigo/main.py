import os
import boto3
from config import *
from sushigo.deck import *
from flask import Flask, request, Response

flask_app = Flask(__name__)

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
    # post_slack_message(client, attachments, channel_id, None)

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
    # post_slack_message(client, attachments, channel_id, None)
    

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
    # post_slack_message(client, None, player_user_id, text)

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
            # post_slack_message(client, attachments, player_user_id, text)
            actions = []

    attachments = [{
        'text': '',
        'callback_id': 'choose_card',
        'actions': actions
    }]
    # post_slack_message(client, attachments, player_user_id, text)


@flask_app.route('/command', methods=['POST'])
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
            deck = Deck()
            deal_hands(channel_id, deck)
        elif callback_id == 'choose_card':
            pass
            # TODO: Remove card from hand & add to player's deck
    else:
        text = 'Hello from the app! :sushi:'
        # post_slack_message(client, None, channel_id, text)
    return Response(), 200


@flask_app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    flask_app.run(debug=True)
