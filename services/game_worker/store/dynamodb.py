import json
from store.store import *
from boto3.dynamodb.conditions import Key, Attr
from flask import request

class DynamoDB(Store):
    '''
    DynamoDB implementation of the Store Interface

    Methods
    -------
    get_users(user_id)
        Returns a list of users in the current game
    get_hand(hand_id)
        Returns the unpickled Hand
    update_user(user_id, user_info)
        Update the stored UserInfo for the given user
    update_hand(hand_id, hand_info)
        Update the stored HandInfo for the given hand
    '''
    def __init__(self):
        pass

# Old code in main
# Refactor & implement Store interface
'''
dynamodb = boto3.resource('dynamodb')
dynamodb_hands_table = dynamodb.Table(HANDS_TABLE_NAME)
dynamodb_users_table = dynamodb.Table(USERS_TABLE_NAME)

item = {
        'user_id': user_id,
        'deck': None,   # value 'true'
        'channel_id': channel_id
    }

update_user_item(dynamodb_users_table, item)

user_ids = scan_players(dynamodb_users_table, channel_id)

item = {
        'hand_id': hand_id,
        'cur_user_id': user_id,
        'hand': hand.pickle_hand(),
        'channel_id': channel_id,
        'chose_card': False
    }

update_hand_item(dynamodb_hands_table, item)
'''

# def pickle_hand(self):
#     '''Pickle the hand for storage'''
#     return pickle.dumps(self, 0).decode()

# def unpickle_hand(self):
#     '''Unpickle the hand retrieved from storage'''
#     return pickle.loads(self.encode())


def parse_payload(payload):
    payload = json.loads(request.form.get('payload'))
    print(payload)
    print(payload.keys())
    print(payload['actions'])
    print(payload['user']['id'])
    print(payload['callback_id'])
    return payload


def update_user_item(table, item):
    kwargs= {
        'Key': {
            'user_id': item['user_id']
        },
        'ExpressionAttributeValues': {
            ':d': item['deck'],
            ':c': item['channel_id']
        },
        'UpdateExpression': 'SET deck = :d, channel_id = :c'
    }
    _update_item(table, kwargs)


def update_hand_item(table, item):
    kwargs= {
        'Key': {
            'hand_id': str(item['hand_id'])
        },
        'ExpressionAttributeValues': {
            ':u': item['cur_user_id'],
            ':h': item['hand'],
            ':c': item['channel_id'],
            ':o': item['chose_card']
        },
        'UpdateExpression': 'SET cur_user_id = :u, hand = :h, channel_id = :c, chose_card = :o'
    }
    _update_item(table, kwargs)


def get_user_item(table, item):
    kwargs = {
        'Key': {
            'user_id': item['user_id']
        }
    }
    item = _get_item(table, kwargs)
    return item


def scan_players(table, channel_id):
    kwargs = {
        'FilterExpression': Attr('channel_id').eq(channel_id)
    }
    items = _scan(table, kwargs)
    players = [ item['user_id'] for item in items ]
    print(players)
    return players


def _get_item(table, kwargs):
    response = table.get_item(**kwargs)
    item = response['Item']
    print(item)
    return item


def _update_item(table, kwargs):
    table.update_item(**kwargs)


def _scan(table, kwargs):
    response = table.scan(**kwargs)
    items = response['Items']
    return items
