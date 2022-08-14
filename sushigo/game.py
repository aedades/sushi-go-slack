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


    Methods
    -------
    add_player(user_id)
        Add a player to the current game (until the game is started)
    remove_player(user_id)
        Remove a player from the current game (until the game is started)
    get_players()
        Return a list of players in the current game

    get_hands()
        Return a list of hands in the current game

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

    def __init__(self, channel_id, store, game_started=False, completed_rounds=0, current_round=1, round_complete=False):
        self.channel_id = channel_id
        self.game_started = game_started
        self.completed_rounds = completed_rounds
        self.current_round = current_round
        self.round_complete = round_complete
        self.deck = Deck()
        self.store = store

    def add_player(self, user_id, channel_id):
        '''Add a player to the current game (until the game is started)'''
        self.store.update_user(self.channel_id, store.UserInfo(user_id, channel_id))

    def remove_player(self, user_id):
        '''Remove a player from the current game (until the game is started)'''
        self.store.remove_user(self.channel_id, user_id)

    def get_players(self):
        '''Return a list of players in the current game'''
        return self.store.get_users(self.channel_id)

    def get_hands(self):
        '''Return a list of hands in the current game'''
        return self.store.get_hands(self.channel_id)

    def start_game(self):
        '''Start the game'''
        players = self.get_players()
        # Check if more than the min number of players have joined the game
        if self._can_game_start():
            hands = self.deck.deal_hands(len(players))
            for i, hand in enumerate(hands):
                hand_info = HandInfo(hand.id, self.channel_id, players[i], hand)
                self.store.update_hand(self.channel_id, hand_info)
            self.game_started = True
        else:
            raise NotEnoughPlayersError(len(players))

    def complete_game(self):
        '''Determine game winner & end game'''

    def is_game_complete(self):
        '''Returns bool indicating whether the game is complete'''
        pass

    def start_round(self):
        '''Deal hands for the round and wait for players to pick cards'''
        self._deal_hands()

    def complete_round(self):
        '''Score player hands and save result in store'''
        pass

    def _can_game_start(self):
        '''Check if there are enough players to start a game'''
        if len(self.get_players()) > MIN_NUM_PLAYERS:
            return True
        else:
            return False

    def _deal_hands(self):
        '''Assign each hand to a player and save in the store'''
        hands = self.get_hands()
        for i, user_id in enumerate(self.get_players()):
            hand_id = hands[i]
            hand_info = HandInfo(hand_id, self.channel_id, user_id, self.store.get_hand(self.channel_id, hand_id))
            user_info = UserInfo(user_id, self.channel_id, hand_id, self.store.get_scores(self.channel_id, user_id))
            self.store.update_user(self.channel_id, user_info)
            self.store.update_hand(self.channel_id, hand_info)


class NotEnoughPlayersError(Exception):
    def __init__(self, number_of_players):
        message = f'Not enough players to start game!  Need at least {MIN_NUM_PLAYERS} (currently have: {number_of_players})'
        super().__init__(message)