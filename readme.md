# sushi-go

## Bolt tutorial

<https://api.slack.com/start/building/bolt-python>

Set up:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Adding app credentials
# Found under OAuth & Permissions tab
export SLACK_BOT_TOKEN=xoxb-

# Found under Basic Information > App Credentials
export SLACK_SIGNING_SECRET=

# Run ngrok
ngrok http 3000
```

## Testing

```
python -m pytest -v
```

### Local testing

```
# Run ngrok
ngrok http 3000
```

Set the app's [event subscriptions request URL](https://api.slack.com/apps/A01HJTN6TDZ/event-subscriptions?) and [interactivity request URL](https://api.slack.com/apps/A01HJTN6TDZ/interactive-messages) to the `ngrok` endpoint (`/slack/events`).  For example, `https://9ea2-73-140-230-25.ngrok.io/slack/events`.

## Design

Classes:

- Card
- Card types:
  - Chopsticks
  - Dumpling
  - MakiOne
  - MakiTwo
  - MakiThree
  - Nigiri Egg
  - NigiriSalmon
  - NigiriSquid
  - Pudding
  - Sashimi
  - Tempura
  - Wasabi
- Deck
- Hand
- User


## Scratch

```
WARNING:slack_bolt.App:Unhandled request ({'type': 'block_actions', 'block_id': 'add_player', 'action_id': 'VLL3'})
---
[Suggestion] You can handle this type of event with the following listener function:

@app.action("VLL3")
def handle_some_action(ack, body, logger):
    ack()
    logger.info(body)

127.0.0.1 - - [12/Aug/2022 00:00:44] "POST /slack/events HTTP/1.1" 404 -

WARNING:slack_bolt.App:Unhandled request ({'type': 'block_actions', 'block_id': 'start_game', 'action_id': 'zwygK'})
```