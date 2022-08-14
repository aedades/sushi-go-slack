import uuid
from services.game_worker.sushigo.deck import Deck

class Store:
    '''
    Store Interface

    Methods
    -------
    get_game_info(channel_id)
        Returns the GameInfo for the current game
    get_hand_info(channel_id, hand_id)
        Returns the HandInfo for the given hand ID
    get_hands(channel_id)
        Returns a list of hand_ids in the current game
    get_user_info(channel_id, user_id)
        Returns the UserInfo stored for the given user
    get_users(channel_id)
        Returns a list of user_ids in the current game
    get_scores(chennel_id, user_id)
        Returns list of scores for the given user
    update_game_info(channel_id, game_info)
        Update the stored GameInfo for the current game
    update_hand(channel_id, hand_id, hand_info)
        Update the stored HandInfo for the given hand
    update_user(channel_id, user_id, user_info)
        Update the stored UserInfo for the given user
    remove_user(channel_id, user_id)
        Remove a user by user_id
    '''

    def __init__(self):
        pass

    def get_game_info(self, channel_id):
        pass

    def get_hand_info(self, channel_id, user_id):
        pass

    def get_hands(self, channel_id):
        pass

    def get_user(self, user_id):
        pass

    def get_users(self, channel_id):
        pass

    def get_scores(self, channel_id, user_id):
        pass

    def update_game_info(self, channel_id, game_info):
        pass

    def update_hand(self, hand_info):
        pass

    def update_user(self, user_info):
        pass

    def remove_user(self, user_id):
        pass


class GameInfo:
    '''
    Attributes
    ----------
    deck : Deck
    game_started : bool
        Flag indicating whether the game is already in-progress

    completed_rounds : int
        The number of completed rounds
    current_round : int
        The current round in play
    round_complete : bool
        Flag indicating whether the current round is complete
    '''
    def __init__(self, deck=Deck(), game_started=False, completed_rounds=0, current_round=1, round_complete=False):
        self.deck = deck
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
    hand : Hand
        Slack channel ID used to distinguish between multiple games
    '''

    def __init__(self, hand_id, channel_id, user_id, hand, chose_card=False):
        self.hand_id = str(uuid.uuid4())
        self.channel_id = channel_id
        self.chose_card = chose_card
        self.current_user_id = user_id
        self.hand = hand


class UserInfo:
    '''
    Attributes
    ----------
    user_id : str
    channel_id : str
        Slack channel ID used to distinguish between multiple games
    keep_hand_id : str
        ID of the player's hand
    passing_hand_id : str
        ID of the passing hand the player currently "holds"
    scores : list of int
    '''

    def __init__(self, user_id, channel_id, keep_hand_id=str(uuid.uuid4()), passing_hand_id=None, scores=[]):
        self.user_id = user_id
        self.channel_id = channel_id
        self.keep_hand_id = keep_hand_id
        self.passing_hand_id = passing_hand_id
        self.scores = scores