class Store:
    '''
    Store Interface

    Methods
    -------
    get_game_info()
        Returns the GameInfo for the current game
    get_hand(hand_id)
        Returns the unpickled Hand
    get_users()
        Returns a list of users in the current game
    update_game_info()
        Update the stored GameInfo for the current game
    update_hand(hand_id, hand_info)
        Update the stored HandInfo for the given hand
    update_user(user_id, user_info)
        Update the stored UserInfo for the given user
    remove_user(user_id)
    '''

    def __init__(self):
        pass

    def get_game_info(self):
        pass

    def get_hand(self, hand_id):
        pass

    def get_users(self):
        pass

    def update_game_info(self):
        pass

    def update_hand(self, hand_id, hand_info):
        pass

    def update_user(self, user_id, user_info):
        pass

    def remove_user(self, user_id):
        pass


class GameInfo:
    '''
    Attributes
    ----------
    game_started : bool
        Flag indicating whether the game is already in-progress

    completed_rounds : int
        The number of completed rounds
    current_round : int
        The current round in play
    round_complete : bool
        Flag indicating whether the current round is complete
    '''
    def __init__(self, game_started=False, completed_rounds=0, current_round=1, round_complete=False):
        self.game_started = game_started
        self.completed_rounds = completed_rounds
        self.current_round = current_round
        self.round_complete = round_complete


class HandInfo:
    '''
    Attributes
    ----------
    hand_id : str
    channel_id : str
    chose_card : bool
        A flag indicating whether the user has chosen a card (and it has been
        added to the user's )
    current_user_id : str
        User ID of the user who currently "holds" this hand
    hand : pickled Hand
        Slack channel ID used to distinguish between multiple games
    '''

    def __init__(self, user_id, hand, channel_id, chose_card=False):
        self. hand_id
        self.channel_id = channel_id
        self.chose_card = chose_card
        self.current_user_id = user_id
        self.hand = hand


class UserInfo:
    '''
    Attributes
    ----------
    user_id : str
    hand_id : str
        ID of the hand the user currently "holds"
    channel_id : str
        Slack channel ID used to distinguish between multiple games
    scores : list of int
    '''

    def __init__(self, user_id, hand_id=None, channel_id=None, scores=[]):
        self.user_id = user_id
        self.hand_id = hand_id
        self.channel_id = channel_id
        self.scores = scores