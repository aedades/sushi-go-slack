class UserActions:
    '''
    User-specific actions (i.e. any game actions received from user interactions)

    Methods
    -------
    see_my_keep_hand(channel_id, user_id)
        Inspect the player's own keep hand
    see_all_user_hands(channel_id)
        Inspect all players' keep hands
    see_my_passing_hand(channel_id, user_id)
        Inspect the player's own passing hand
    see_game_info(channel_id)
        Inspect the game info for all games the player is a part of
    see_player_scores(channel_id)
        Inspect the scores for all players in the game

    pick_card(channel_id, user_id, card)
        Take a card from the hand and place it in the user's keep hand
    pass_hand(channel_id, user_id)
        Confirm card selection and indicate the passing hand is ready to pass
    '''