from services.game_worker.store.store import *
from services.game_worker.store.memory import *
from services.game_worker.sushigo.deck import Hand
from test.helpers import *
import inspect
import pytest

# TODO: Test method signatures

class TestStore:
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # Code that will run before your test
        self.store = Memory()
        # yield
        # Code that will run after your test, for example:

    def test_get_game_info_signature(self):
        args = ['self', 'channel_id']
        args_spec = inspect.getfullargspec(self.store.get_game_info)
        assert_method_signature(args, args_spec)

    def test_get_hand_info_signature(self):
        args = ['self', 'channel_id', 'hand_id']
        args_spec = inspect.getfullargspec(self.store.get_hand_info)
        assert_method_signature(args, args_spec)

    def test_get_hands_signature(self):
        args = ['self', 'channel_id']
        args_spec = inspect.getfullargspec(self.store.get_hands)
        assert_method_signature(args, args_spec)

    def test_get_user_info_signature(self):
        args = ['self', 'channel_id', 'user_id']
        args_spec = inspect.getfullargspec(self.store.get_user_info)
        assert_method_signature(args, args_spec)

    def test_get_users_signature(self):
        args = ['self', 'channel_id']
        args_spec = inspect.getfullargspec(self.store.get_users)
        assert_method_signature(args, args_spec)

    def test_get_scores_signature(self):
        args = ['self', 'channel_id', 'user_id']
        args_spec = inspect.getfullargspec(self.store.get_scores)
        assert_method_signature(args, args_spec)

    def test_update_game_signature(self):
        args = ['self', 'channel_id', 'game_info']
        args_spec = inspect.getfullargspec(self.store.update_game)
        assert_method_signature(args, args_spec)

    def test_update_hand_signature(self):
        args = ['self', 'channel_id', 'hand_info']
        args_spec = inspect.getfullargspec(self.store.update_hand)
        assert_method_signature(args, args_spec)

    def test_update_user_signature(self):
        args = ['self', 'channel_id', 'user_info']
        args_spec = inspect.getfullargspec(self.store.update_user)
        assert_method_signature(args, args_spec)

    def test_remove_user_signature(self):
        args = ['self', 'channel_id', 'user_id']
        args_spec = inspect.getfullargspec(self.store.remove_user)
        assert_method_signature(args, args_spec)

    def test_memory_store(self):
        assert issubclass(Memory, Store) == True



class TestGameInfo:
    def test_init_game_info(self):
        game_info = GameInfo()
        assert isinstance(game_info.deck, Deck)
        assert game_info.game_started == False
        assert game_info.completed_rounds == 0
        assert game_info.current_round == 1
        assert game_info.round_complete == False


class TestHandInfo:
    def test_init_hand_info(self):
        channel_id = 'channel_id'
        current_user_id = 'current_user_id'
        hand = Hand()
        hand_info = HandInfo(channel_id, current_user_id, hand)
        assert hand_info.channel_id == channel_id
        assert isinstance(hand_info.hand_id, str)
        assert hand_info.chose_card == False
        assert hand_info.current_user_id == current_user_id
        assert isinstance(hand_info.hand, Hand)


class TestUserInfo:
    def test_init_user_info(self):
        user_id = 'user_id'
        channel_id = 'channel_id'
        user_info = UserInfo(channel_id, user_id)
        assert user_info.channel_id == channel_id
        assert user_info.user_id == user_id
        assert isinstance(user_info.keep_hand_id, str)
        assert user_info.passing_hand_id == None
        assert isinstance(user_info.scores, list)
