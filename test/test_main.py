from sushigo.main import *
import inspect

class TestDeck:
    def get_num_args(self, args_spec):
        return len(args_spec[0])

    def get_args(self, args_spec):
        return args_spec[0]

    def assert_method_signature(self, num_args, args, args_spec):
        assert self.get_num_args(args_spec) == num_args
        assert self.get_args(args_spec) == args

    def test_start_game(self):
        num_args = 2
        args = ['channel_id', 'username']
        args_spec = inspect.getfullargspec(start_game)
        self.assert_method_signature(num_args, args, args_spec)

    def test_prompt_start_game(self):
        num_args = 2
        args = ['channel_id', 'user_id']
        args_spec = inspect.getfullargspec(prompt_start_game)
        self.assert_method_signature(num_args, args, args_spec)

    def test_deal_hands(self):
        num_args = 2
        args = ['channel_id', 'deck']
        args_spec = inspect.getfullargspec(deal_hands)
        self.assert_method_signature(num_args, args, args_spec)

    def test_prompt_player_pick(self):
        num_args = 1
        args = ['hand']
        args_spec = inspect.getfullargspec(prompt_player_pick)
        self.assert_method_signature(num_args, args, args_spec)
        