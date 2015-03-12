import abc
from strategy import Strategy

class DealerSoftHitStrategy(Strategy):

    """If dealer has soft hand equal to 17, force hit."""

    def hit(self):
        if self.game_state.dealer.get_score() < 17:
            return True
        elif (self.game_state.dealer.get_score() == 17 and
                self.game_state.dealer.hand_is_hard == False):
            return True
        return False
    
