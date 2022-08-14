import pytest
from services.game_worker.sushigo.game import *
from services.game_worker.store.memory import *
from services.game_worker.sushigo.deck import *

# game_state = None
PLAYER_IDS = ['1', '2', '3']
NUM_PLAYERS = len(PLAYER_IDS)
CHANNEL_ID = 'TEST_CHANNEL_ID'


class TestGame():
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # Code that will run before your test
        store = Memory()
        self.game_state = Game(CHANNEL_ID, store)
        # yield
        # Code that will run after your test, for example:

    def add_all_players(self, start_game=False):
        for user_id in PLAYER_IDS:
            self.game_state.add_player(user_id, CHANNEL_ID)
        if start_game:
            self.game_state.start_game()

    def get_game_info(self):
        return self.game_state.store.get_game_info(CHANNEL_ID)

    def test_init_game(self):
        game_info = self.game_state.store.get_game_info(CHANNEL_ID)
        assert isinstance(game_info.deck, Deck) == True
        assert game_info.game_started == False
        assert game_info.completed_rounds == 0
        assert game_info.current_round == 1
        assert game_info.round_complete == False

    def test_can_game_start(self):
        assert self.game_state._can_game_start() == False
        self.add_all_players()
        assert self.game_state._can_game_start() == True

    def test_add_remove_player(self):
        assert list(self.game_state.get_players()) == []
        self.game_state.add_player('1', CHANNEL_ID)
        assert list(self.game_state.get_players()) == ['1']
        self.game_state.remove_player('1')
        assert list(self.game_state.get_players()) == []

    def test_get_players(self):
        self.add_all_players()
        assert list(self.game_state.get_players()) == PLAYER_IDS

    def test_start_game(self):
        game_info = self.get_game_info()
        assert game_info.game_started == False
        assert len(self.game_state.get_players()) == 0
        assert len(game_info.deck) == DECK_TOTAL_NUM_CARDS
        assert len(self.game_state.get_hands()) == 0

        self.add_all_players(start_game=True)

        game_info = self.get_game_info()
        assert len(self.game_state.get_players()) == NUM_PLAYERS
        assert len(game_info.deck) == DECK_TOTAL_NUM_CARDS - (NUM_PLAYERS * HAND_SIZE[NUM_PLAYERS])
        assert len(self.game_state.get_hands()) == NUM_PLAYERS
        assert game_info.game_started == True

    def test_start_game_not_enough_players(self):
        with pytest.raises(NotEnoughPlayersError):
            self.game_state.start_game()
        game_info = self.get_game_info()
        assert game_info.game_started == False

    def test_start_round(self):
        self.add_all_players(start_game=True)

        self.game_state.start_round()
        for user_id in PLAYER_IDS:
            user_info = self.game_state.store.get_user(self.game_state.channel_id, user_id)
            assert user_info != None
            assert user_info.keep_hand_id != None
            assert user_info.passing_hand_id != None