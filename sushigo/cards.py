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

CARD_INFO = {
    'chopsticks': {
        'emoji': CHOPSTICKS_EMOJI
    },
    'dumpling': {
        'emoji': DUMPLING_EMOJI
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
    'nigiri_egg': {
        'emoji': NIGIRI_EGG_EMOJI,
        'value': 1
    },
    'nigiri_salmon': {
        'emoji': NIGIRI_SALMON_EMOJI,
        'value': 2
    },
    'nigiri_squid': {
        'emoji': NIGIRI_SQUID_EMOJI,
        'value': 3
    },
    'pudding': {
        'emoji': PUDDING_EMOJI,
    },
    'sashimi': {
        'emoji': SASHIMI_EMOJI
    },
    'tempura': {
        'emoji': TEMPURA_EMOJI
    },
    'wasabi': {
        'emoji': WASABI_EMOJI,
    }
}

class Card:
    def __init__(self, name, card_num, emoji):
        self.name = f'{name}_{card_num}'
        self.emoji = emoji

    def get_emoji(self):
        return self.emoji


class Chopsticks(Card):
    def __init__(self, card_num):
        card_type = 'chopsticks'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])


class Dumpling(Card):
    def __init__(self, card_num):
        card_type = 'dumpling'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])

class MakiOne(Card):
    def __init__(self, card_num):
        card_type = 'maki_one'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])
        self.value = CARD_INFO[card_type]['value']


class MakiTwo(Card):
    def __init__(self, card_num):
        card_type = 'maki_two'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])
        self.value = CARD_INFO[card_type]['value']


class MakiThree(Card):
    def __init__(self, card_num):
        card_type = 'maki_three'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])
        self.value = CARD_INFO[card_type]['value']


class NigiriEgg(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_egg'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])
        self.value = CARD_INFO['nigiri_egg']['value']


class NigiriSalmon(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_salmon'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])
        self.value = CARD_INFO['nigiri_salmon']['value']


class NigiriSquid(Card):
    def __init__(self, card_num):
        card_type = 'nigiri_squid'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])
        self.value = CARD_INFO['nigiri_squid']['value']


class Pudding(Card):
    def __init__(self, card_num):
        card_type = 'pudding'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])


class Sashimi(Card):
    def __init__(self, card_num):
        card_type = 'sashimi'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])


class Tempura(Card):
    def __init__(self, card_num):
        card_type = 'tempura'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])


class Wasabi(Card):
    def __init__(self, card_num):
        card_type = 'wasabi'
        super().__init__(card_type, card_num, CARD_INFO[card_type]['emoji'])
