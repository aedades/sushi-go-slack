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
    kwargs = {}
    _update_item(table, kwargs)


def get_user_item(table, item):
    kwargs = {
        'Key': {
            'user_id': item['user_id']
        }
    }
    item = _get_item(table, kwargs)
    return item


def _get_item(table, kwargs):
    response = table.get_item(**kwargs)
    item = response['Item']
    print(item)
    return item


def _update_item(table, kwargs):
    table.update_item(**kwargs)
