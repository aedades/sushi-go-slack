import pytest
from services.game_worker.sushigo.deck import *

DECK_SIZE = 108
NUMBER_OF_PLAYERS = 2

class TestDeck:
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # Code that will run before your test
        self.deck = Deck()
        # yield
        # Code that will run after your test, for example:

    def deal_hands(self):
        return self.deck.deal_hands(NUMBER_OF_PLAYERS)

    def test_hand_size(self):
        assert HAND_SIZE == {
            1: 10,
            2: 10,
            3: 9,
            4: 8,
            5: 7
        }

    def test_deck_counts(self):
        assert DECK_COUNTS == {
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

    def test_deck_size(self):
        assert DECK_TOTAL_NUM_CARDS == DECK_SIZE

    def test_init_deck(self):
        assert len(self.deck) == DECK_TOTAL_NUM_CARDS
    
    def test_shuffle(self):
        top_card = self.deck.cards[0]
        second_card = self.deck.cards[1]
        self.deck._shuffle()
        new_top_card = self.deck.cards[0]
        new_second_card = self.deck.cards[1]
        # top card could be a dupe, so check first two cards
        assert (top_card != new_top_card) or (second_card != new_second_card)
        assert len(self.deck) == DECK_TOTAL_NUM_CARDS
    
    def test_deal_hands(self):
        hands = self.deal_hands()
        assert len(hands) == NUMBER_OF_PLAYERS
        assert len(self.deck) == DECK_TOTAL_NUM_CARDS - (NUMBER_OF_PLAYERS * HAND_SIZE[NUMBER_OF_PLAYERS])
        assert len(hands[0]) == HAND_SIZE[NUMBER_OF_PLAYERS]

    def test_init_hand(self):
        hands = self.deal_hands()
        assert hands[0].id != None
        assert isinstance(hands[0].id, str)
        assert isinstance(hands[0].cards, dict)

    def test_hand_add_and_remove_card(self):
        hands = self.deal_hands()
        starting_hand_size = len(hands[0])
        card = list(hands[0].cards.keys())[0]
        removed_card = hands[0].remove_card(card)
        hands[1].add_card(removed_card)
        assert removed_card.name == card
        assert not card in hands[0].cards.keys()
        assert card in hands[1].cards.keys()
        assert len(hands[0]) == starting_hand_size - 1
        assert len(hands[1]) == starting_hand_size + 1

    def test_hand_len(self):
        hands = self.deal_hands()
        assert len(hands[0]) == 10
