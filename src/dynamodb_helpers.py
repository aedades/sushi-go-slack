def update_user_item(table, item):
    '''
    item = {
        'user_id': 'amanda',
        'deck': 'deck',
        'channel_id': 'development'
    }
    '''
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


def _update_item(table, kwargs):
    table.update_item(**kwargs)


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
