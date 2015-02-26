import card
import random

class Deck:
    
    def __init__(self):
        self.cards = []
       
        for suit in range(1, 5):

            for val in range(2, 11):
                self.cards.append(card.Card(val,suit))

            for val in ['Ace', 'King', 'Queen', 'Jack']:
                self.cards.append(card.Card(val, suit))

    def get_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
                

