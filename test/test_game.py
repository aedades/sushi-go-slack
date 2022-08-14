import pytest
from sushigo.game import *
from store.memory import *
from sushigo.deck import *

# game_state = None
PLAYER_IDS = ['1', '2', '3']
NUM_PLAYERS = len(PLAYER_IDS)

class TestGame():
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # Code that will run before your test
        # game_state = Game()
        store = Memory()
        self.game_state = Game(store)
        # yield
        # Code that will run after your test, for example:

    def test_init_game(self):
        # game_state = Game()
        assert self.game_state.game_started == False
        assert self.game_state.completed_rounds == 0
        assert self.game_state.current_round == 1
        assert self.game_state.round_complete == False

    def test_can_game_start(self):
        assert self.game_state._can_game_start() == False
        for user_id in PLAYER_IDS:
            self.game_state.add_player(user_id)
        assert self.game_state._can_game_start() == True

    def test_add_remove_player(self):
        assert list(self.game_state.get_players()) == []
        self.game_state.add_player('1')
        assert list(self.game_state.get_players()) == ['1']
        self.game_state.remove_player('1')
        assert list(self.game_state.get_players()) == []

    def test_get_players(self):
        for user_id in PLAYER_IDS:
            self.game_state.add_player(user_id)
        assert list(self.game_state.get_players()) == PLAYER_IDS

    def test_start_game(self):
        assert self.game_state.game_started == False

        for user_id in PLAYER_IDS:
            self.game_state.add_player(user_id)
        self.game_state.start_game()

        assert len(self.game_state.deck) == DECK_TOTAL_NUM_CARDS - (NUM_PLAYERS * HAND_SIZE[NUM_PLAYERS])
        assert len(self.game_state.hands) == NUM_PLAYERS
        assert self.game_state.game_started == True

    def test_start_game_not_enough_players(self):
        with pytest.raises(NotEnoughPlayersError):
            self.game_state.start_game()
        assert self.game_state.game_started == False