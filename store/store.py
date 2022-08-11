class Store:
    def __init__(self):
        pass

    # Return a list of user IDs
    def get_users(self):
        pass

    def get_hand(self):
        pass

    # Update UserInfo for the given user
    def update_user(self, user_id, user_info):
        pass

    def update_hand(self):
        pass

class UserInfo:
    def __init__(self, hand_id, channel_id):
        self.hand_id = hand_id
        self.channel_id = channel_id

class HandInfo:
    def __init__(self, user_id, hand, channel_id, chose_card):
        self.current_user_id = user_id
        self.hand = hand
        self.channel_id = channel_id
        self.chose_card = chose_card