from math import pow
from shufflestrategy import RandomShuffleStrategy, AppendShuffleStrategy, EvenOddShuffleStrategy
from deck import Deck

strats_dict = {"Random class shuffle": Deck(RandomShuffleStrategy()),
          "Append shuffle" : Deck(AppendShuffleStrategy()),
          "Even odd shuffle strat" : Deck(EvenOddShuffleStrategy())}

def build_dict(deck):
    res_dict = {str(x):[0]*52 for x in deck.cards}
    for i in range(520):
        deck.shuffle()
        for i in range(len(deck.cards)):
            res_dict[str(deck.cards[i])][i] += 1
    return res_dict

def chi_square(res_dict):
    res = 0
    for li in res_dict.itervalues():
        for i in range(0, len(li)):
            res += pow((li[i] - 10), 2) / 10
    return res

for strat_name, deck in strats_dict.iteritems():
    print strat_name + ": " + str(chi_square(build_dict(deck)))
