import emoji
import pickle
import random
from sushigo.cards import *

HAND_SIZE = {
    1: 10,
    2: 10,
    3: 9,
    4: 8,
    5: 7
}

DECK_COUNTS = {
    'chopsticks': 4,
    'dumpling': 14,
    'maki_one': 6,
    'maki_two': 12,
    'maki_three': 8,
    'nigiri_egg': 5,
    'nigiri_salmon': 10,
    'nigiri_squid': 5,
    'pudding': 10,
    'sashimi': 14,
    'tempura': 14,
    'wasabi': 6,
}

class Deck:
    def __init__(self):
        self.cards = []
        self._add_cards(MakiTwo, 12)
        self._add_cards(MakiThree, 8)
        self._add_cards(MakiOne, 6)
        self._add_cards(Tempura, DECK_COUNTS['tempura'])
        self._add_cards(Sashimi, DECK_COUNTS['sashimi'])
        self._add_cards(Dumpling, DECK_COUNTS['dumpling'])
        self._add_cards(NigiriSquid, DECK_COUNTS['nigiri_squid'])
        self._add_cards(NigiriSalmon, DECK_COUNTS['nigiri_salmon'])
        self._add_cards(NigiriEgg, DECK_COUNTS['nigiri_egg'])
        self._add_cards(Wasabi, DECK_COUNTS['wasabi'])
        self._add_cards(Chopsticks, DECK_COUNTS['chopsticks'])
        self._add_cards(Pudding, DECK_COUNTS['pudding'])
        self.shuffle()

    def _add_cards(self, card, count):
        for x in range(count):
            card_obj = card(x)
            self.cards.append(card_obj)
    
    def deal_hands(self, number_of_players):
        hands = []
        for x in range(number_of_players):
            hands.append(Hand())
        self.shuffle()
        for x in range(HAND_SIZE[number_of_players]): # 10
            for hand in hands: # 2
                hand.add_card(self.cards.pop())
        return hands

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        column = 0
        string = ''
        for x in range(len(self.cards)):
            string += f'{self.cards[x].get_emoji()} '
            column += 1
            if column == 5:
                string+= '\n'
                column = 0
        return string


class Hand:
    def __init__(self):
        self.cards = {}

    def add_card(self, card):
        self.cards[card.name] = card

    def remove_card(self, card_name):
        return self.cards.pop(card_name)

    def pickle_hand(hand):
        return pickle.dumps(hand, 0).decode()

    def unpickle_hand(hand):
        return pickle.loads(hand.encode())

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        column = 0
        string = ''
        for card in self.cards.values():
            string += f'{card.Get_face()} '
            column += 1
            if column == 5:
                string+= '\n'
                column = 0
        return string
