def get_num_players():
    # TODO: Check number of players
    return 1

PROMPT_START_GAME_BLOCK = [
    {
        "type": "actions",
        "block_id": "add_player",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "I want to play! :hand: (Enter the game as a player)"
                }
            }
        ]
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
