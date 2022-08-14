import os
from config import *
from sushigo.deck import *
from sushigo.slack_app import *
from slack_client.slack import *
from slack_bolt import App

slack = SlackClient()

# Initialize app
# HTTP server adapter is not recommended for production
app = App(
    token=os.environ.get(SLACK_BOT_TOKEN),
    signing_secret=os.environ.get(SLACK_SIGNING_SECRET)
)

if store_type == 'memory':
    store = Memory()
# Fallback to memory store
else:
    store = Memory()

# Add functionality here
# TODO: Add buttons to for various tests:
# [ ] initialize a game and DM a hand
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to your _App's Home_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "block_id": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              },
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Test deal hand"
                },
                "action_id": "deal_hand"
              }
            ]
          }
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")


@app.action({
  "block_id": "actions",
  "action_id": "deal_hand"
})
def test_deal_hand(ack, say, body, logger):
  try:
    ack()
    logger.info("deal_hand triggered")
    deck = Deck()
    logger.info(f'body: {body}')
    user = body['user']['name']

    say(channel=GENERAL_CHANNEL_ID, text=f'{user} wants to start a game!')
    say(channel=GENERAL_CHANNEL_ID, blocks=PROMPT_START_GAME_BLOCK, text=PROMPT_START_GAME_TEXT)

  except Exception as e:
    logger.error(f"Error handling deal_hand action: {e}")


# Start app
if __name__ == "__main__":
    app.start(port=int(os.environ.get(PORT, 3000)))
