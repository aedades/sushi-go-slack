import json
from store.store import *

class Memory(Store):
    '''
    In-Memory implementation of the Store Interface

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
        self.hands = {}
        self.users = {}

    def get_users(self):
        '''Returns a list of users in the current game'''
        return self.users.keys()

    def get_hand(self, user_id):
        '''Returns the unpickled Hand'''
        return self.hands[user_id]

    # Update user info for the given user
    def update_user(self, user_id, user_info):
        '''Update the stored UserInfo for the given user'''
        self.users[user_id] = user_info

    # Update hand info for the given hand
    def update_hand(self, hand_id, hand_info):
        '''Update the stored HandInfo for the given hand'''
        self.hands[hand_id] = hand_info