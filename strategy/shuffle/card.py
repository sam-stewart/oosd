class Card:

    suits = {1 : 'Spades',
             2 : 'Clubs',
             3 : 'Hearts',
             4 : 'Diamonds',}

    def __init__(self, value, suit):

        self.suit = suit
        self.value = value

    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.value) + " of " + Card.suits[self.suit]
