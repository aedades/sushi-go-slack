from src.deck import *
import emoji

DECK_SIZE = 108
CARD_COUNT = 1
class TestDeck:
    def test_one_maki(self):
        maki = OneMaki(CARD_COUNT)
        assert maki.name == f'one_maki_{CARD_COUNT}'
        assert maki.face == f'1{MAKI_CLDR}'
        assert maki.value == 1

    def test_tempura(self):
        tempura = Tempura(CARD_COUNT)
        assert tempura.face == TEMPURA_CLDR

    def test_sashimi(self):
        sashimi = Sashimi(CARD_COUNT)
        assert sashimi.face == SASHIMI_CLDR

    def test_dumpling(self):
        dumpling = Dumpling(CARD_COUNT)
        assert dumpling.face == DUMPLING_CLDR

    def test_nigiri_squid(self):
        nigiri_squid = NigiriSquid(CARD_COUNT)
        assert nigiri_squid.face == NIGIRI_SQUID_CLDR

    def test_nigiri_salmon(self):
        nigiri_salmon = NigiriSalmon(CARD_COUNT)
        assert nigiri_salmon.face == NIGIRI_SALMON_CLDR

    def test_nigiri_egg(self):
        nigiri_egg = NigiriEgg(CARD_COUNT)
        assert nigiri_egg.face == NIGIRI_EGG_CLDR

    def test_wasabi(self):
        wasabi = Wasabi(CARD_COUNT)
        assert wasabi.face == WASABI_CLDR

    def test_chopsticks(self):
        chopsticks = Chopsticks(CARD_COUNT)
        assert chopsticks.face == CHOPSTICKS_CLDR
    
    def test_pudding(self):
        pudding = Pudding(CARD_COUNT)
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

    def test_deck_remove_card(self):
        deck = Deck()
        hands = deck.deal_hands(2)
        hand = hands[0]
        starting_hand_size = len(hand)
        card_to_remove = list(hand.cards.keys())[0]
        removed_card = hand.remove_card(card_to_remove)
        assert removed_card.name == card_to_remove
        assert not card_to_remove in hand.cards.keys()
        assert len(hand) == starting_hand_size - 1