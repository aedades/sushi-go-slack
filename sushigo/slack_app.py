def get_num_players():
    # TODO: Check number of players
    return 1

PROMPT_START_GAME_BLOCK = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f'Start the game with {get_num_players()} players?'
        }
    },
    {
    "type": "divider"
    },
    {
        "type": "actions",
        "block_id": "start_game",
        "elements": [
            {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Itadakimasu! :bento: (Start game)"
            }
            }
        ]
    }
]

PROMPT_START_GAME_TEXT = f'Irasshaimase!'
