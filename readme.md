# sushi-go

- [App settings](https://api.slack.com/apps/A01HJTN6TDZ)
    - [Interactivity & Shortcuts](https://api.slack.com/apps/A01HJTN6TDZ/interactive-messages?)
    - [Slash commands](https://api.slack.com/apps/A01HJTN6TDZ/slash-commands?)
    - Endpoint: https://cb1083e57c96.ngrok.io/command

## button clicks

```bash
ImmutableMultiDict([('token', 'GW92hDeuxZtFtr6cFdoPgqKl'), ('team_id', 'T01HFA2HHMK'), ('team_domain', 'amandadev'), ('channel_id', 'C01HFA41AAZ'), ('channel_name', 'development'), ('user_id', 'U01H3KAPB71'), ('user_name', 'amanda.edades'), ('command', '/sushigo'), ('text', 'test'), ('api_app_id', 'A01HJTN6TDZ'), ('is_enterprise_install', 'false'), ('response_url', 'https://hooks.slack.com/commands/T01HFA2HHMK/1590563330886/iimiympQwliWNm6nNfsaJee0'), ('trigger_id', '1597546390051.1593342595733.bcbdf2c323dd3dbf71053523786cd63a')])
```

### payload

```bash
# keys
dict_keys(['type', 'actions', 'callback_id', 'team', 'channel', 'user', 'action_ts', 'message_ts', 'attachment_id', 'token', 'is_app_unfurl', 'enterprise', 'is_enterprise_install', 'original_message', 'response_url', 'trigger_id'])

# payload
{'type': 'interactive_message', 'actions': [{'name': 'add_player', 'type': 'button', 'value': 'add_player'}], 'callback_id': 'slack', 'team': {'id': 'T01HFA2HHMK', 'domain': 'amandadev'}, 'channel': {'id': 'C01HFA41AAZ', 'name': 'development'}, 'user': {'id': 'U01H3KAPB71', 'name': 'amanda.edades'}, 'action_ts': '1608796389.107554', 'message_ts': '1608791177.000100', 'attachment_id': '1', 'token': 'GW92hDeuxZtFtr6cFdoPgqKl', 'is_app_unfurl': False, 'enterprise': None, 'is_enterprise_install': False, 'original_message': {'bot_id': 'B01J8H5MTH6', 'type': 'message', 'text': '', 'user': 'U01HXAY0K2M', 'ts': '1608791177.000100', 'team': 'T01HFA2HHMK', 'bot_profile': {'id': 'B01J8H5MTH6', 'deleted': False, 'name': 'sushi-go', 'updated': 1608753495, 'app_id': 'A01HJTN6TDZ', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'team_id': 'T01HFA2HHMK'}, 'attachments': [{'callback_id': 'slack', 'text': '<@U01H3KAPB71> wants to start a game of Sushi Go! :sushi:', 'id': 1, 'actions': [{'id': '1', 'name': 'add_player', 'text': 'I want to play :raised_hand:', 'type': 'button', 'value': 'add_player', 'style': ''}], 'fallback': '<@U01H3KAPB71> wants to start a game of Sushi Go! :sushi:'}]}, 'response_url': 'https://hooks.slack.com/actions/T01HFA2HHMK/1621434051232/47Xw1m4vZ8JjryiN1hzNmS2J', 'trigger_id': '1603755601972.1593342595733.3deffb3e6d20b6c8d88907e4b7a3202b'}
```

## slash command