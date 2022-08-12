from sushigo.deck import *
import emoji

DECK_SIZE = 108
NUMBER_OF_PLAYERS = 2

class TestDeck:
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
        hands = deck.deal_hands(NUMBER_OF_PLAYERS)
        assert len(hands) == NUMBER_OF_PLAYERS
        assert len(deck) == DECK_SIZE - (NUMBER_OF_PLAYERS * HAND_SIZE[NUMBER_OF_PLAYERS])
        assert len(hands[0]) == HAND_SIZE[NUMBER_OF_PLAYERS]

    def test_hand_add_and_remove_card(self):
        deck = Deck()
        hands = deck.deal_hands(NUMBER_OF_PLAYERS)
        starting_hand_size = len(hands[0])
        card = list(hands[0].cards.keys())[0]
        removed_card = hands[0].remove_card(card)
        hands[1].add_card(removed_card)
        assert removed_card.name == card
        assert not card in hands[0].cards.keys()
        assert card in hands[1].cards.keys()
        assert len(hands[0]) == starting_hand_size - 1
        assert len(hands[1]) == starting_hand_size + 1
