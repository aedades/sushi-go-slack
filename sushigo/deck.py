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
    '''
    Represents the game deck

    Attributes
    ----------
    cards : list of Cards

    Methods
    -------
    deal_hands(number_of_players)
        Return a list containing the given number of Hands
    '''
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
        self._shuffle()

    def _add_cards(self, card, count):
        '''Add x number of a give Card to the deck'''
        for x in range(count):
            card_obj = card(x)
            self.cards.append(card_obj)

    def _shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.cards)
    
    def deal_hands(self, number_of_players):
        '''Return a list containing the given number of Hands'''
        hands = []
        for x in range(number_of_players):
            hands.append(Hand())
        self.shuffle()
        for x in range(HAND_SIZE[number_of_players]): # 10
            for hand in hands: # 2
                hand.add_card(self.cards.pop())
        return hands

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
    '''
    Represents groups of Cards:
        1. Hands that are passed between players
        2. Hands that players keep
    Cards are removed from (1) and added to (2) over the course of the round

    Attributes
    ----------
    cards : dict
        Key: card_name
        Value: card

    Methods
    -------
    add_card(card)
        Add a card to the Hand
    remove_card(card_name)
        Remove a Card from the hand by name
    pickle_hand()
        Pickle the hand for storage
    update_hand(hand_id, hand_info)
        Unpickle the hand retrieved from storage
    '''
    def __init__(self):
        self.cards = {}

    def add_card(self, card):
        '''Add a Card to the hand'''
        self.cards[card.name] = card

    def remove_card(self, card_name):
        '''Remove a Card from the hand by name'''
        return self.cards.pop(card_name)

    def pickle_hand(self):
        '''Pickle the hand for storage'''
        return pickle.dumps(self, 0).decode()

    def unpickle_hand(self):
        '''Unpickle the hand retrieved from storage'''
        return pickle.loads(self.encode())

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
