import abc
import random

class ShuffleStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def shuffle(self, deck):
        return

class RandomShuffleStrategy(ShuffleStrategy):
    
    def shuffle(self, deck):
        return random.shuffle(deck)


class AppendShuffleStrategy(ShuffleStrategy):

    def shuffle(self, deck):
        for x in range(0, len(deck)):
            deck.append(deck.pop(random.randint(0, len(deck) -1)))

class EvenOddShuffleStrategy(ShuffleStrategy):
    
    def shuffle(self, deck):
        for even_number in range(0, len(deck), 2):
            odd_number = random.choice(xrange(1, len(deck), 2))
            temp = deck[even_number]
            deck[even_number] = deck[odd_number]
            deck[odd_number] = temp

class ExchangeShuffleStrategy(ShuffleStrategy):

    def shuffle(self, deck):
        pass
