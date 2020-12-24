import emoji
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
    2: 10
}

CARD_INFO = {
    'one_maki': {
        'CLDR': f'1{MAKI_CLDR}',
        'value': 1
    },
    'two_maki': {
        'CLDR': f'2{MAKI_CLDR}',
        'value': 2
    },
    'three_maki': {
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
        self._add_cards(TwoMaki(), 12)
        self._add_cards(ThreeMaki(), 8)
        self._add_cards(OneMaki(), 6)
        self._add_cards(Tempura(), CARD_INFO['tempura']['count'])
        self._add_cards(Sashimi(), CARD_INFO['sashimi']['count'])
        self._add_cards(Dumpling(), CARD_INFO['dumpling']['count'])
        self._add_cards(NigiriSquid(), CARD_INFO['nigiri_squid']['count'])
        self._add_cards(NigiriSalmon(), CARD_INFO['nigiri_salmon']['count'])
        self._add_cards(NigiriEgg(), CARD_INFO['nigiri_egg']['count'])
        self._add_cards(Wasabi(), CARD_INFO['wasabi']['count'])
        self._add_cards(Chopsticks(), CARD_INFO['chopsticks']['count'])
        self._add_cards(Pudding(), CARD_INFO['pudding']['count'])

    def _add_cards(self, card, count):
        for x in range(count):
            card = card
            self.cards.append(card)
    
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
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

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

class Card:
    def __init__(self, name, face_cldr):
        self.name = name
        self.face = face_cldr
    
    def get_face(self):
        return emoji.emojize(self.face)


class OneMaki(Card):
    def __init__(self):
        card_type = 'one_maki'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO[card_type]['value']


class TwoMaki(Card):
    def __init__(self):
        card_type = 'two_maki'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO[card_type]['value']


class ThreeMaki(Card):
    def __init__(self):
        card_type = 'three_maki'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO[card_type]['value']


class Tempura(Card):
    def __init__(self):
        card_type = 'tempura'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])


class Sashimi(Card):
    def __init__(self):
        card_type = 'sashimi'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])


class Dumpling(Card):
    def __init__(self):
        card_type = 'dumpling'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])


class NigiriSquid(Card):
    def __init__(self):
        card_type = 'nigiri_squid'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO['nigiri_squid']['value']


class NigiriSalmon(Card):
    def __init__(self):
        card_type = 'nigiri_salmon'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO['nigiri_salmon']['value']


class NigiriEgg(Card):
    def __init__(self):
        card_type = 'nigiri_egg'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])
        self.value = CARD_INFO['nigiri_egg']['value']


class Wasabi(Card):
    def __init__(self):
        card_type = 'wasabi'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])


class Chopsticks(Card):
    def __init__(self):
        card_type = 'chopsticks'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])


class Pudding(Card):
    def __init__(self):
        card_type = 'pudding'
        super().__init__(card_type, CARD_INFO[card_type]['CLDR'])