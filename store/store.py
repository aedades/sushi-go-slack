class Store:
    '''
    Store Interface

    Methods
    -------
    get_users(user_id)
        Returns a list of users in the current game
    get_hand(hand_id)
        Returns the unpickled Hand
    update_user(user_id, user_info)
        Update the stored UserInfo for the given user
    update_hand(hand_id, hand_info)
        Update the stored HandInfo for the given hand
    '''
    def __init__(self):
        pass

    def get_users(self):
        pass

    def get_hand(self, hand_id):
        pass

    def update_user(self, user_id, user_info):
        pass

    def update_hand(self, hand_id, hand_info):
        pass

class UserInfo:
    '''
    Attributes
    ----------
    user_id : str
    hand_id : str
        ID of the hand the user currently "holds"
    channel_id : str
        Slack channel ID used to distinguish between multiple games
    '''
    def __init__(self, user_id, hand_id, channel_id):
        self.user_id = user_id
        self.hand_id = hand_id
        self.channel_id = channel_id

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
    def __init__(self, user_id, hand, channel_id, chose_card):
        self. hand_id
        self.channel_id = channel_id
        self.chose_card = chose_card
        self.current_user_id = user_id
        self.hand = hand
