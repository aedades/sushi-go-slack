import json
from store.store import *

class Memory(Store):
    def __init__(self):
        self.hands = {}
        self.users = {}

    # Return a list of user IDs
    def get_users(self):
        return self.users.keys()

    # Get a user's hand
    def get_hand(self, user_id):
        return self.hands[user_id]

    # Update user info for the given user
    def update_user(self, user_id, user_info):
        self.users[user_id] = user_info

    # Update hand info for the given hand
    def update_hand(self, hand_id, hand_info):
        self.hands[hand_id] = hand_info