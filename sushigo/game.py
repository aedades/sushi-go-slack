from config import *
from store import *
from sushigo.deck import *

class Game:
    '''
    Game-specific rules (i.e. rounds, scoring, win conditions)

    Attributes
    ----------
    game_started : bool
        Flag indicating whether the game is already in-progress
    completed_rounds : int
        The number of completed rounds
    current_round : int
        The current round in play
    round_complete : bool
        Flag indicating whether the current round is complete

    deck : Deck
    store : Store
    hands : list of Hands


    Methods
    -------
    add_player(user_id)
        Add a player to the current game (until the game is started)
    remove_player(user_id)
        Remove a player from the current game (until the game is started)
    get_players()
        Return a list of players in the current game

    start_game(number_of_players)
        Start the game
    complete_game()
        Determine game winner & end game
    is_game_complete()
        Returns bool indicating whether the game is complete

    start_round()
        Deal hands for the round and wait for players to pick cards
    complete_round()
        Score player hands and save result in store
    '''

    def __init__(self, store, game_started=False, completed_rounds=0, current_round=1, round_complete=False):
        self.game_started = game_started
        self.completed_rounds = completed_rounds
        self.current_round = current_round
        self.round_complete = round_complete
        self.deck = Deck()
        self.hands = []
        self.store = store

    def _can_game_start(self):
        '''Check if there are enough players to start a game'''
        if len(self.get_players()) > MIN_NUM_PLAYERS:
            return True
        else:
            return False

    def add_player(self, user_id):
        '''Add a player to the current game (until the game is started)'''
        self.store.update_user(user_id, store.UserInfo)

    def remove_player(self, user_id):
        '''Remove a player from the current game (until the game is started)'''
        self.store.remove_user(user_id)

    def get_players(self):
        '''Return a list of players in the current game'''
        return self.store.get_users()

    def start_game(self):
        '''Start the game'''
        # Check if more than the min number of players have joined the game
        if self._can_game_start():
            self.hands = self.deck.deal_hands(len(self.get_players()))
            self.game_started = True
        else:
            raise NotEnoughPlayersError(len(self.get_players()))

    def complete_game(self):
        '''Determine game winner & end game'''

    def is_game_complete(self):
        '''Returns bool indicating whether the game is complete'''
        pass

    def start_round(self):
        '''Deal hands for the round and wait for players to pick cards'''
        # Assign hands
        pass

    def complete_round(self):
        '''Score player hands and save result in store'''
        pass


class NotEnoughPlayersError(Exception):
    def __init__(self, number_of_players):
        message = f'Not enough players to start game!  Need at least {MIN_NUM_PLAYERS} (currently have: {number_of_players})'
        super().__init__(message)