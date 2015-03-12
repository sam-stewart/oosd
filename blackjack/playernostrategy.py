import abc
from strategy import Strategy

class PlayerNoStrategy(Strategy):

    def hit(self):
        return raw_input("h to hit or s to stand: ") =='h'
