from services.game_worker.sushigo.main import *
from test.helpers import *
import inspect

class TestDeck:
    def test_prompt_player_pick_signature(self):
        args = ['hand']
        args_spec = inspect.getfullargspec(prompt_player_pick)
        assert_method_signature(args, args_spec)
        