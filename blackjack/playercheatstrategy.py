import abc
from strategy import Strategy

class PlayerCheatStrategy(Strategy):

    """ Basic cheat strat, show the next card in deck """
    def __init__(self, game_state):
        self.game_state = game_state

    def take_card(self, player, card):
        player.hand_of_cards.append(card)
        print("Next card: " + str(self.game_state.deck.cards[-1]))

