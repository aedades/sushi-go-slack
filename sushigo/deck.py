import emoji
import pickle
import random

HAND_SIZE = {
    1: 10,
    2: 10,
    3: 9,
    4: 8,
    5: 7
}

MAKI_EMOJI = ':radio_button:'
TEMPURA_EMOJI = ':fried_shrimp:'
SASHIMI_EMOJI = ':fish:'
DUMPLING_EMOJI = ':dumpling:'
NIGIRI_SQUID_EMOJI= ':squid:'
NIGIRI_SALMON_EMOJI = ':sushi:'
NIGIRI_EGG_EMOJI = ':egg:'
WASABI_EMOJI = ':hot_pepper:'
CHOPSTICKS_EMOJI = ':chopsticks:'
PUDDING_EMOJI = ':custard:'

DECK_INFO = {
    'chopsticks': {
        'emoji': CHOPSTICKS_EMOJI,
        'count': 4
    },
    'maki_one': {
        'emoji': f'1{MAKI_EMOJI}',
        'value': 1
    },
    'maki_two': {
        'emoji': f'2{MAKI_EMOJI}',
        'value': 2
    },
    'maki_three': {
        'emoji': f'3{MAKI_EMOJI}',
        'value': 3
    },
    'tempura': {
        'emoji': TEMPURA_EMOJI,
        'count': 14
    },
    'sashimi': {
        'emoji': SASHIMI_EMOJI,
        'count': 14
    },
    'dumpling': {
        'emoji': DUMPLING_EMOJI,
        'count': 14
    },
    'nigiri_squid': {
        'emoji': NIGIRI_SQUID_EMOJI,
        'count': 5,
        'value': 3
    },
    'nigiri_salmon': {
        'emoji': NIGIRI_SALMON_EMOJI,
        'count': 10,
        'value': 2
    },
    'nigiri_egg': {
        'emoji': NIGIRI_EGG_EMOJI,
        'count': 5,
        'value': 1
    },
    'wasabi': {
        'emoji': WASABI_EMOJI,
        'count': 6
    },
    'pudding': {
        'emoji': PUDDING_EMOJI,
        'count': 10
    }
}

class Deck:
    def __init__(self):
        self.cards = []
        self._add_cards(MakiTwo, 12)
        self._add_cards(MakiThree, 8)
        self._add_cards(MakiOne, 6)
        self._add_cards(Tempura, DECK_INFO['tempura']['count'])
        self._add_cards(Sashimi, DECK_INFO['sashimi']['count'])
        self._add_cards(Dumpling, DECK_INFO['dumpling']['count'])
        self._add_cards(NigiriSquid, DECK_INFO['nigiri_squid']['count'])
        self._add_cards(NigiriSalmon, DECK_INFO['nigiri_salmon']['count'])
        self._add_cards(NigiriEgg, DECK_INFO['nigiri_egg']['count'])
        self._add_cards(Wasabi, DECK_INFO['wasabi']['count'])
        self._add_cards(Chopsticks, DECK_INFO['chopsticks']['count'])
        self._add_cards(Pudding, DECK_INFO['pudding']['count'])
        self.shuffle()

    def _add_cards(self, card, count):
        for x in range(count):
            card_obj = card(x)
            self.cards.append(card_obj)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hands(self, number_of_players):
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
            string += f'{self.cards[x].get_face()} '
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

class Card:
    def __init__(self, name, card_num, emoji):
        self.name = f'{name}_{card_num}'
        self.emoji = emoji


class Chopsticks(Card):
    def __init__(self, card_num):
        card_type = 'chopsticks'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])


class Dumpling(Card):
    def __init__(self, card_num):
        card_type = 'dumpling'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])

class MakiOne(Card):
    def __init__(self, card_num):
        card_type = 'maki_one'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])
        self.value = DECK_INFO[card_type]['value']


class MakiTwo(Card):
    def __init__(self, card_num):
        card_type = 'maki_two'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])
        self.value = DECK_INFO[card_type]['value']


class MakiThree(Card):
    def __init__(self, card_num):
        card_type = 'maki_three'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])
        self.value = DECK_INFO[card_type]['value']


class NigiriEgg(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_egg'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])
        self.value = DECK_INFO['nigiri_egg']['value']


class NigiriSalmon(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_salmon'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])
        self.value = DECK_INFO['nigiri_salmon']['value']


class NigiriSquid(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_squid'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])
        self.value = DECK_INFO['nigiri_squid']['value']


class Pudding(Card):
    def __init__(self, card_num):
        card_type = 'pudding'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])


class Sashimi(Card):
    def __init__(self, card_num):
        card_type = 'sashimi'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])


class Tempura(Card):
    def __init__(self, card_num):
        card_type = 'tempura'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])


class Wasabi(Card):
    def __init__(self, card_num):
        card_type = 'wasabi'
        super().__init__(card_type, card_num, DECK_INFO[card_type]['emoji'])
