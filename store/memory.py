import json
from store.store import *

class Memory(Store):
    '''
    In-Memory implementation of the Store Interface

    Attributes
    ----------
    game_info : dict
        Key: channel_id
        Value: GameInfo
    hands : dict
        Key: channel_id
        Value: dict
            Key: hand_id
            Value: HandInfo
    users : dict
        Key: channel_id
        Value: dict
            Key: user_id
            Value: UserInfo
    round_complete : bool
        Flag indicating whether the current round is complete

    Methods
    -------
    get_game_info(channel_id)
        Returns the GameInfo for the current game
    get_hand(channel_id, hand_id)
        Returns the unpickled Hand
    get_hands(channel_id)
        Returns a list of hand_ids in the current game
    get_user(channel_id, user_id)
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

    def __init__(self, round_complete=False):
        self.game_info = {}
        self.hands = {}
        self.users = {}

    def get_game_info(self, channel_id):
        '''Returns the GameInfo for the current game'''
        return self.game_info[channel_id]

    def get_hand(self, channel_id, hand_id):
        '''Returns the unpickled Hand'''
        try:
            return self.hands[channel_id][hand_id]
        except KeyError:
            # No hands have been created for this round yet
            return []

    def get_hands(self, channel_id):
        '''Returns a list of hand_ids in the current game'''
        try:
            return list(self.hands[channel_id].keys())
        except KeyError:
            # No hands have been created for this round yet
            return []

    def get_user(self, channel_id, user_id):
        '''Returns the UserInfo stored for the given user'''
        return self.users[channel_id][user_id]

    def get_users(self, channel_id):
        '''Returns a list of user_ids in the current game'''
        try:
            return list(self.users[channel_id].keys())
        except KeyError:
            # No players have joined game yet
            return []

    def get_scores(self, channel_id, user_id):
        '''Returns list of scores for the given user'''
        return self.users[channel_id][user_id].scores

    def update_game_info(self, channel_id, game_info):
        '''Update the stored GameInfo for the current game'''
        self.game_info[channel_id] = game_info

    def update_user(self, channel_id, user_info):
        '''Update the stored UserInfo for the given user'''
        try:
            self.users[channel_id][user_info.user_id] = user_info
        except KeyError:
            # No players have joined game yet
            self.users[channel_id] = {}
            self.users[channel_id][user_info.user_id] = user_info

    def update_hand(self, channel_id, hand_info):
        '''Update the stored HandInfo for the given hand'''
        try:
            self.hands[channel_id][hand_info.hand_id] = hand_info
        except KeyError:
            # No hands have been created for game yet
            self.hands[channel_id] = {}
            self.hands[channel_id][hand_info.hand_id] = hand_info

    def remove_user(self, channel_id, user_id):
        '''Remove a user by user_id'''
        del self.users[channel_id][user_id]