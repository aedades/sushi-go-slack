import emoji
import pickle
import random

MAKI_CLDR = ':radio_button:'
TEMPURA_CLDR = ':fried_shrimp:'
SASHIMI_CLDR = ':fish:'
DUMPLING_CLDR = ':dumpling:'
NIGIRI_SQUID_CLDR= ':squid:'
NIGIRI_SALMON_CLDR = ':sushi:'
NIGIRI_EGG_CLDR = ':egg:'
WASABI_CLDR = ':hot_pepper:'
CHOPSTICKS_CLDR = ':chopsticks:'
PUDDING_CLDR = ':custard:'

HAND_SIZE = {
    1: 10,
    2: 10,
    3: 9,
    4: 8,
    5: 7
}

CARD_INFO = {
    'maki_one': {
        'CLDR': f'1{MAKI_CLDR}',
        'value': 1
    },
    'maki_two': {
        'CLDR': f'2{MAKI_CLDR}',
        'value': 2
    },
    'maki_three': {
        'CLDR': f'3{MAKI_CLDR}',
        'value': 3
    },
    'tempura': {
        'CLDR': TEMPURA_CLDR,
        'count': 14
    },
    'sashimi': {
        'CLDR': SASHIMI_CLDR,
        'count': 14
    },
    'dumpling': {
        'CLDR': DUMPLING_CLDR,
        'count': 14
    },
    'nigiri_squid': {
        'CLDR': NIGIRI_SQUID_CLDR,
        'count': 5,
        'value': 3
    },
    'nigiri_salmon': {
        'CLDR': NIGIRI_SALMON_CLDR,
        'count': 10,
        'value': 2
    },
    'nigiri_egg': {
        'CLDR': NIGIRI_EGG_CLDR,
        'count': 5,
        'value': 1
    },
    'wasabi': {
        'CLDR': WASABI_CLDR,
        'count': 6
    },
    'chopsticks': {
        'CLDR': CHOPSTICKS_CLDR,
        'count': 4
    },
    'pudding': {
        'CLDR': PUDDING_CLDR,
        'count': 10
    }
}


class Deck:
    def __init__(self):
        self.cards = []
        self._add_cards(MakiTwo, 12)
        self._add_cards(MakiThree, 8)
        self._add_cards(MakiOne, 6)
        self._add_cards(Tempura, CARD_INFO['tempura']['count'])
        self._add_cards(Sashimi, CARD_INFO['sashimi']['count'])
        self._add_cards(Dumpling, CARD_INFO['dumpling']['count'])
        self._add_cards(NigiriSquid, CARD_INFO['nigiri_squid']['count'])
        self._add_cards(NigiriSalmon, CARD_INFO['nigiri_salmon']['count'])
        self._add_cards(NigiriEgg, CARD_INFO['nigiri_egg']['count'])
        self._add_cards(Wasabi, CARD_INFO['wasabi']['count'])
        self._add_cards(Chopsticks, CARD_INFO['chopsticks']['count'])
        self._add_cards(Pudding, CARD_INFO['pudding']['count'])

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
    def __init__(self, name, card_num, face_cldr):
        self.name = f'{name}_{card_num}'
        self.face = face_cldr

    def Get_face(self):
         return emoji.emojize(self.face)


class Chopsticks(Card):
    def __init__(self, card_num):
        card_type = 'chopsticks'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])


class Dumpling(Card):
    def __init__(self, card_num):
        card_type = 'dumpling'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])

class MakiOne(Card):
    def __init__(self, card_num):
        card_type = 'maki_one'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO[card_type]['value']


class MakiTwo(Card):
    def __init__(self, card_num):
        card_type = 'maki_two'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO[card_type]['value']


class MakiThree(Card):
    def __init__(self, card_num):
        card_type = 'maki_three'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO[card_type]['value']


class NigiriEgg(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_egg'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO['nigiri_egg']['value']


class NigiriSalmon(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_salmon'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO['nigiri_salmon']['value']


class NigiriSquid(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_squid'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO['nigiri_squid']['value']


class Pudding(Card):
    def __init__(self, card_num):
        card_type = 'pudding'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])


class Sashimi(Card):
    def __init__(self, card_num):
        card_type = 'sashimi'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])


class Tempura(Card):
    def __init__(self, card_num):
        card_type = 'tempura'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])


class Wasabi(Card):
    def __init__(self, card_num):
        card_type = 'wasabi'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['CLDR'])


def init_deck():
    deck = Deck()
    deck.shuffle()
    return deck