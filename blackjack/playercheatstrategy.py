import abc
from strategy import Strategy

class PlayerCheatStrategy(Strategy):

    """ Basic cheat strat, show the next card in deck """
    def hit(self):
        print("Next card: " + str(self.game_state.deck.cards[-1]))
        return raw_input("h to hit or s to stand: ") == 'h'

