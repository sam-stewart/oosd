import abc

class Strategy(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, game_state):
        self.game_state = game_state

    @abc.abstractmethod
    def hit(self):
        return
