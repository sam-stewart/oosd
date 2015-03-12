import abc
from strategy import Strategy

class NoStrategy(Strategy):

    def __init__(self, game_state):
        self.game_state = game_state

    def take_card(self, player, card):
        player.hand_of_cards.append(card)
