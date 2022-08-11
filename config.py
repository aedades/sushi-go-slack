import os
import logging
from store.store import *
from store.memory import *

PORT = "PORT"
SLACK_BOT_TOKEN = "SLACK_BOT_TOKEN"
SLACK_SIGNING_SECRET = "SLACK_SIGNING_SECRET"

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.environ.get('AWS_DEFAULT_REGION', 'us-west-2')

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

GENERAL_CHANNEL_ID = "C01HBK706S2"

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
# https://api.slack.com/apps/A01HJTN6TDZ/oauth
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')

if ENVIRONMENT == 'dev':
    MIN_NUM_PLAYERS = 1
else:
    MIN_NUM_PLAYERS = 2

logging.basicConfig(level=logging.INFO)

store_type = os.environ.get('STORE_TYPE', 'memory')

if store_type == 'memory':
    store = Memory()
# Fallback to memory store
else:
    store = Memory()

# Temp hardcoded values
USER_ID = 'U01H3KAPB71'
CHANNEL_ID = 'C01HFA41AAZ'
