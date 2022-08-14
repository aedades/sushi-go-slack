from config import *
from services.game_worker.game.deck import *
from flask import Flask, request, Response

flask_app = Flask(__name__)

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
