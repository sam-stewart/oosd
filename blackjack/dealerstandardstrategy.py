import abc
from strategy import Strategy

class DealerStandardStrategy(Strategy):
    """ Standard dealer strat, hit until score is at least 17 """
    def hit(self):
        if self.game_state.dealer.get_score() < 17:
            return True
        return False

