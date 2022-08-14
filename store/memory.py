import json
from store.store import *

class Memory(Store):
    '''
    In-Memory implementation of the Store Interface

    Attributes
    ----------
    game_info : GameInfo
    hands : list of hand_ids
    users : list of user_ids
    round_complete : bool
        Flag indicating whether the current round is complete

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
        Remove a user by user_id
    '''

    def __init__(self, round_complete=False):
        self.game_info = GameInfo()
        self.hands = []
        self.users = {}
        self.round_complete = round_complete

    def get_game_info(self):
        '''Returns the GameInfo for the current game'''
        return self.game_info

    def get_users(self):
        '''Returns a list of users in the current game'''
        return self.users.keys()

    def get_hand(self, user_id):
        '''Returns the unpickled Hand'''
        return self.hands[user_id]

    def update_game_info(self):
        '''Update the stored GameInfo for the current game'''
        pass

    def update_user(self, user_id, user_info):
        '''Update the stored UserInfo for the given user'''
        self.users[user_id] = user_info

    def update_hand(self, hand_id, hand_info):
        '''Update the stored HandInfo for the given hand'''
        self.hands[hand_id] = hand_info

    def remove_user(self, user_id):
        '''Remove a user by user_id'''
        del self.users[user_id]