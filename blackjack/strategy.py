import abc

class Strategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def take_card(self, player, card):
        return
