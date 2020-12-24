from src.deck import *
import emoji

DECK_SIZE = 108

class TestDeck:
    def test_one_maki(self):
        maki = OneMaki()
        assert maki.name == 'one_maki'
        assert maki.face == f'1{MAKI_CLDR}'
        assert maki.value == 1

    def test_tempura(self):
        tempura = Tempura()
        assert tempura.face == TEMPURA_CLDR

    def test_sashimi(self):
        sashimi = Sashimi()
        assert sashimi.face == SASHIMI_CLDR

    def test_dumpling(self):
        dumpling = Dumpling()
        assert dumpling.face == DUMPLING_CLDR

    def test_nigiri_squid(self):
        nigiri_squid = NigiriSquid()
        assert nigiri_squid.face == NIGIRI_SQUID_CLDR

    def test_nigiri_salmon(self):
        nigiri_salmon = NigiriSalmon()
        assert nigiri_salmon.face == NIGIRI_SALMON_CLDR

    def test_nigiri_egg(self):
        nigiri_egg = NigiriEgg()
        assert nigiri_egg.face == NIGIRI_EGG_CLDR

    def test_wasabi(self):
        wasabi = Wasabi()
        assert wasabi.face == WASABI_CLDR

    def test_chopsticks(self):
        chopsticks = Chopsticks()
        assert chopsticks.face == CHOPSTICKS_CLDR
    
    def test_pudding(self):
        pudding = Pudding()
        assert pudding.face == PUDDING_CLDR

    def test_init_deck(self):
        deck = Deck()
        assert len(deck) == DECK_SIZE
    
    def test_shuffle_deck(self):
        deck = Deck()
        top_card = deck.cards[0]
        second_card = deck.cards[1]
        deck.shuffle()
        new_top_card = deck.cards[0]
        new_second_card = deck.cards[1]
        # top card could be a dupe, so check first two cards
        assert (top_card != new_top_card) or (second_card != new_second_card)
        assert len(deck) == DECK_SIZE
    
    def test_deal_hands(self):
        deck = Deck()
        hands = deck.deal_hands(2)
        assert len(hands) == 2
        assert len(deck) == DECK_SIZE - (len(hands[0]) + len(hands[1]))
        assert len(hands[0]) == 10
        assert len(hands[1]) == 10
        assert hands[0] != hands
