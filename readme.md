# sushi-go

## Bolt tutorial


https://api.slack.com/start/building/bolt-python

Set up:

```bash
# Create virtual environment
python3 -m venv .venv

# aActivate
source .venv/bin/activate

# Adding app credentials
# Found under OAuth & Permissions tab
export SLACK_BOT_TOKEN=xoxb-

# Found under Basic Information > App Credentials
export SLACK_SIGNING_SECRET=

# Run ngrok
ngrok http 3000
```

## Local testing

```
# Run ngrok
ngrok http 3000
```

Set [event subscriptions request URL](https://api.slack.com/apps/A01HJTN6TDZ/event-subscriptions?) to `ngrok` endpoint (`/slack/events`).  For example, `https://9ea2-73-140-230-25.ngrok.io/slack/events`.
