import json
from boto3.dynamodb.conditions import Key, Attr
from flask import request

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
