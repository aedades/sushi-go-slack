from config import *
from services.game_worker.store.store import *
from services.game_worker.sushigo.deck import *

class Game:
    '''
    Game-specific rules (i.e. rounds, scoring, win conditions)

    Attributes
    ----------
    channel_id : str
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
        Score player hands, save result in store, and pass passing hands to the next player
    '''

    def __init__(self, channel_id, store):
        self.channel_id = channel_id
        self.store = store

        game_info = GameInfo()
        self.store.update_game(channel_id, game_info)

    def add_player(self, user_id, channel_id):
        '''Add a player to the current game (until the game is started)'''
        self.store.update_user(self.channel_id, UserInfo(channel_id, user_id))

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
        game_info = self.store.get_game_info(self.channel_id)
        if self._can_game_start():
            # Deal hands
            hands = game_info.deck.deal_hands(len(players))
            # Assign hands to players
            for i, hand in enumerate(hands):
                hand_info = HandInfo(hand.id, self.channel_id, players[i], hand)
                self.store.update_hand(self.channel_id, hand_info)
            # Save game info
            new_game_info = GameInfo(game_info.deck, game_started=True)
            self.store.update_game(self.channel_id, new_game_info)
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
        '''Score player hands, save result in store, and pass passing hands to the next player'''
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
            hand_info = HandInfo(self.channel_id, user_id, self.store.get_hand_info(self.channel_id, hand_id).hand, hand_id)
            user_info = UserInfo(self.channel_id, user_id, passing_hand_id=hand_id, scores=self.store.get_scores(self.channel_id, user_id))
            self.store.update_user(self.channel_id, user_info)
            self.store.update_hand(self.channel_id, hand_info)


class NotEnoughPlayersError(Exception):
    def __init__(self, number_of_players):
        message = f'Not enough players to start game!  Need at least {MIN_NUM_PLAYERS} (currently have: {number_of_players})'
        super().__init__(message)