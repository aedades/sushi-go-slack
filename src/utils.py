import pickle

def pickle_hand(hand):
    return pickle.dumps(hand, 0).decode()

def unpickle_hand(hand):
    return pickle.loads(hand.encode())