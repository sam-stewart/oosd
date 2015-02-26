import deck
import player

class Dealer(player.Player):

    def __init__(self):
        player.Player.__init__(self)
        self.deck_of_cards = deck.Deck()
        self.deck_of_cards.shuffle()

    def deal_card(self, player):
        player.take_card(self.deck_of_cards.get_card())

    def take_card(self):
        self.hand_of_cards.append(self.deck_of_cards.get_card())
                
    def shuffle_deck(self):
        self.deck_of_cards.shuffle()

    def show_hand_hidden(self):
        i = len(self.hand_of_cards) - 1
        return "HIDDEN \t" + str(self.hand_of_cards[i])


